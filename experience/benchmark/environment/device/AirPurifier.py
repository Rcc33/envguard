import threading
import time
import random
from DataFrame import globalFrame
from MetaType import BaseType


class AirPurifier(BaseType):
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
            print(self.room_name + '.AirPurifier.state: on')
            print("空气净化")
            self.on = 1
            self.lock.release()
            globalFrame.loc(env, "air_purifier_on", 'Action', self.room_name, 'AirPurifier', self.room_name + '.AirPurifier.state: on', source)
            # with globalFrame.df_lock:
            #     globalFrame.df.loc[len(globalFrame.df)] = ["air_purifier_on", 'Action', self.room_name, 'AirPurifier', time.strftime(
            #         "%Y-%m-%d %H:%M:%S", time.localtime(globalFrame.start_time)), self.room_name + '.AirPurifier.state: on', source]
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
            # threading.Thread(target=self.room_state["AirQuality"].ext_action_increase, args=(self.room_state["AirQuality"], env,)).start()
            self.room_state["AirQuality"].ext_action_increase(self.room_state["AirQuality"], env)
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
            print(self.room_name + '.AirPurifier.state: off')
            globalFrame.loc(env, "air_purifier_off", 'Action', self.room_name, 'AirPurifier', self.room_name + '.AirPurifier.state: off', source)
            # with globalFrame.df_lock:
            #     globalFrame.df.loc[len(globalFrame.df)] = ["air_purifier_off", 'Action', self.room_name, 'AirPurifier', time.strftime(
            #         "%Y-%m-%d %H:%M:%S", time.localtime(globalFrame.start_time)), self.room_name + '.AirPurifier.state: off', source]
            self.on = 0
        self.lock.release()
