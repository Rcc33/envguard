from DataFrame import globalFrame
from MetaType import BaseType
import time
import random
import threading


class Light(BaseType):
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
            self.on = 1
            self.lock.release()
            print(self.room_name + '.Light.state: on')
            # with self.room_state["Brightness"].lock:
            #     self.room_state["Brightness"].value = 1
            globalFrame.loc(env, "light_on", 'Action', self.room_name, 'Light', self.room_name + '.Light.state: on', source)
            # with globalFrame.df_lock:
            #     globalFrame.df.loc[len(globalFrame.df)] = ["light_on", 'Action', self.room_name, 'Light', time.strftime(
            #         "%Y-%m-%d %H:%M:%S", time.localtime(globalFrame.start_time)), self.room_name + '.Light.state: on', source]
            t1 = threading.Thread(target=self.effect, args=(self, env,))
            t1.start()
            globalFrame.thread_list.append(t1)
        else:
            self.lock.release()
    
    def effect(self,env):
        time.sleep(random.uniform(0.6*0.5, 0.6*1))
        self.room_state["Brightness"].ext_action_increase(self.room_state["Brightness"], env)
        self.room_state["Brightness"].ext_action_increase(self.room_state["Brightness"], env)
    
    def enable_off(self):
        if self.on == 0:
            return 0
        else:
            return 1

    def action_off(self, env, source):
        self.lock.acquire()
        if self.enable_off(self):
            globalFrame.loc(env, "light_off", 'Action', self.room_name, 'Light', self.room_name + '.Light.state: off', source)
            # with globalFrame.df_lock:
            #     globalFrame.df.loc[len(globalFrame.df)] = ["light_off", 'Action', self.room_name, 'Light', time.strftime(
            #         "%Y-%m-%d %H:%M:%S", time.localtime(globalFrame.start_time)), self.room_name + '.Light.state: off', source]
            self.on = 0
            self.lock.release()
            print(self.room_name + '.Light.state: off')
            t1 = threading.Thread(target=self.effect_off, args=(self, env,))
            t1.start()
            globalFrame.thread_list.append(t1)
        else:
            self.lock.release()

    def effect_off(self,env):
        time.sleep(random.uniform(0.6*0.5, 0.6*1))
        self.room_state["Brightness"].ext_action_decrease(self.room_state["Brightness"], env)