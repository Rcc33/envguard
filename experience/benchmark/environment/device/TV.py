from DataFrame import globalFrame
from MetaType import BaseType
import threading
import time
import random


class TV(BaseType):
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
            globalFrame.loc(env, "tv_on", 'Action', self.room_name, 'TV', self.room_name + '.TV.state: on', source)
            # with globalFrame.df_lock:
            #     globalFrame.df.loc[len(globalFrame.df)] = ["tv_on",'Action', self.room_name, 'TV', time.strftime(
            #         "%Y-%m-%d %H:%M:%S", time.localtime(globalFrame.start_time)), self.room_name + '.TV.state: on', source]
            self.on = 1
            self.lock.release()
            print(self.room_name + '.TV.state: on')
            t1 = threading.Thread(target=self.effect, args=(self, env,))
            t1.start()
            globalFrame.thread_list.append(t1)
        else:
            self.lock.release()

    def effect(self, env):
        time.sleep(random.uniform(0.6*3, 0.6*5))
        self.lock.acquire()
        if self.on == 1:
            self.lock.release()
            self.room_state["Noise"].ext_action_increase(self.room_state["Noise"], env)
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
            globalFrame.loc(env, "tv_off", 'Action', self.room_name, 'TV', self.room_name + '.TV.state: off', source)
            # with globalFrame.df_lock:
            #     globalFrame.df.loc[len(globalFrame.df)] = ["tv_off",'Action', self.room_name, 'TV', time.strftime(
            #         "%Y-%m-%d %H:%M:%S", time.localtime(globalFrame.start_time)), self.room_name + '.TV.state: off', source]
            self.on = 0
            self.lock.release()
            print(self.room_name + '.TV.state: off')
            t1 = threading.Thread(target=self.effect_off, args=(self, env,))
            t1.start()
            globalFrame.thread_list.append(t1)
        else:
            self.lock.release()

    def effect_off(self,env):
        time.sleep(random.uniform(0.6*3, 0.6*5))
        self.lock.acquire()
        if self.on == 0:
            self.lock.release()
            self.room_state["Noise"].ext_action_decrease(self.room_state["Noise"], env)
        else:
            self.lock.release()    