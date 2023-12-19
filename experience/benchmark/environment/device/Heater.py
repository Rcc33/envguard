import time
from MetaType import BaseType
from DataFrame import globalFrame
import threading
import random


class Heater(BaseType):
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
            print(self.room_name + '.Heater.state: on')
            print("加热ing")
            globalFrame.loc(env, "heater_on", 'Action', self.room_name, 'Heater', self.room_name + '.Heater.state: on', source)
            # with globalFrame.df_lock:
            #     globalFrame.df.loc[len(globalFrame.df)] = ["heater_on", 'Action', self.room_name, 'Heater', time.strftime(
            #         "%Y-%m-%d %H:%M:%S", time.localtime(globalFrame.start_time)), self.room_name + '.Heater.state: on', source]
            self.on = 1
            self.lock.release()
            t1 = threading.Thread(target=self.effect, args=(self, env,))
            t1.start()
            globalFrame.thread_list.append(t1)
        else:
            self.lock.release()

    def effect(self, env):
        time.sleep(random.uniform(0.6*5, 0.6*10))
        self.lock.acquire()
        if self.on == 1:
            self.lock.release()
            self.room_state["Temperature"].ext_action_increase(self.room_state["Temperature"], env)
        else:
            self.lock.release()

    def enable_off(self):
        if self.on == 0:
            return 0
        else:
            return 1

    def action_off(self, env, source):
        self.lock.acquire()
        if self.enable_off(self):
            print(self.room_name + '.Heater.state: off')
            globalFrame.loc(env, "heater_off", 'Action', self.room_name, 'Heater', self.room_name + '.Heater.state: off', source)
            # with globalFrame.df_lock:
            #     globalFrame.df.loc[len(globalFrame.df)] = ["heater_off", 'Action', self.room_name, 'Heater', time.strftime(
            #         "%Y-%m-%d %H:%M:%S", time.localtime(globalFrame.start_time)), self.room_name + '.Heater.state: off', source]
            self.on = 0
        self.lock.release()
