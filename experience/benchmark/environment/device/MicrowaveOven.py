import time
from MetaType import BaseType
from DataFrame import globalFrame
import threading
import random


class MicrowaveOven(BaseType):
    def __init__(self, room_state, room_name):
        super().__init__()
        self.room_state = room_state
        self.room_name = room_name
        self.lock = threading.Lock()
        self.on = 0

    def enable_on(self):
        if self.on == 1:
            return 0
        else:
            return 1

    def action_on(self, env, source):
        self.lock.acquire()
        if self.enable_on(self):
            # 判断pre-conditions，产生相应的effects
            globalFrame.loc(env, "microwave_oven_on", 'Action', self.room_name, 'MicrowaveOven', self.room_name + '.MicrowaveOven.state: on', source)
            # with globalFrame.df_lock:
            #     globalFrame.df.loc[len(globalFrame.df)] = ["microwave_oven_on", 'Action', self.room_name, 'MicrowaveOven', time.strftime(
            #         "%Y-%m-%d %H:%M:%S", time.localtime(globalFrame.start_time)), self.room_name + '.MicrowaveOven.state: on', source]
            print(self.room_name + '.MicrowaveOven.state: on')
            print("加热食物ing")
            self.on = 1
            self.lock.release()
            t1 = threading.Thread(target=self.effect, args=(self, env, source,))
            t1.start()
            globalFrame.thread_list.append(t1)     
        else:
            self.lock.release()

    def effect(self, env, source):
        if random.randint(1, 7) == 1:
            time.sleep(random.uniform(0.3, 1.5))
            env['space_dict']['TeaRoom']["device_dict"]["Door"].action_on(env['space_dict']['TeaRoom']["device_dict"]["Door"], env,  'offline')
            time.sleep(random.uniform(0.02, 0.04))
            env['space_dict']['TeaRoom']["env_state"]["HumanState"].ext_action_decrease(env['space_dict']['TeaRoom']["env_state"]["HumanState"], env, )
            env['space_dict']['Corridor']["env_state"]["HumanState"].ext_action_increase(env['space_dict']['Corridor']["env_state"]["HumanState"], env, )
            env['space_dict']['TeaRoom']["device_dict"]["Door"].action_off(env['space_dict']['TeaRoom']["device_dict"]["Door"], env,  'offline')
            time.sleep(random.uniform(0.07, 0.13))
            env['space_dict']['TeaRoom']["device_dict"]["Door"].action_on(env['space_dict']['TeaRoom']["device_dict"]["Door"], env,  'offline')
            time.sleep(random.uniform(0.01, 0.03))
            env['space_dict']['Corridor']["env_state"]["HumanState"].ext_action_decrease(env['space_dict']['Corridor']["env_state"]["HumanState"], env, )
            env['space_dict']['TeaRoom']["env_state"]["HumanState"].ext_action_increase(env['space_dict']['TeaRoom']["env_state"]["HumanState"], env, )
            env['space_dict']['TeaRoom']["device_dict"]["Door"].action_off(env['space_dict']['TeaRoom']["device_dict"]["Door"], env,  'offline')
            time.sleep(random.uniform(0.2, 1.3))
            self.action_off(self, env, source)
        else:      
            time.sleep(random.uniform(0.6*1, 0.6*5))
            self.action_off(self, env, source)

    def enable_off(self):
        if self.on == 0:
            return 0
        else:
            return 1

    def action_off(self, env, source):
        self.lock.acquire()
        if self.enable_off(self):
            print(self.room_name + '.MicrowaveOven.state: off')
            globalFrame.loc(env, "microwave_oven_off", 'Action', self.room_name, 'MicrowaveOven',
                            self.room_name + '.MicrowaveOven.state: off', source)
            # with globalFrame.df_lock:
            #     globalFrame.df.loc[len(globalFrame.df)] = ["microwave_oven_off", 'Action', self.room_name, 'MicrowaveOven', time.strftime(
            #         "%Y-%m-%d %H:%M:%S", time.localtime(globalFrame.start_time)), self.room_name + '.MicrowaveOven.state: off', source]
            self.on = 0
        self.lock.release()
