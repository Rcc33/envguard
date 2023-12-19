import threading
import time
import random
from MetaType import BaseType
from DataFrame import globalFrame


class AC(BaseType):

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
            print(self.room_name + '.AC.state: on')
            print("降温ing")
            globalFrame.loc(env, "ac_on", "Action", self.room_name, 'AC', self.room_name + '.AC.state: on', source)
            # with globalFrame.df_lock:
            #     globalFrame.df.loc[len(globalFrame.df)] = ["ac_on", "Action", self.room_name, 'AC', time.strftime(
            #         "%Y-%m-%d %H:%M:%S", time.localtime(globalFrame.start_time)), self.room_name + '.AC.state: on', source]
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
            self.room_state["Temperature"].ext_action_decrease(self.room_state["Temperature"], env)
        else:
            self.lock.release()
        time.sleep(random.uniform(0.6*5, 0.6*10))
        self.lock.acquire()
        if self.on == 1:
            self.lock.release()
            self.room_state["Humidity"].ext_action_decrease(self.room_state["Humidity"], env)
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
            print(self.room_name + '.AC.state: off')
            globalFrame.loc(env, "ac_off", 'Action', self.room_name, 'AC', self.room_name + '.AC.state: off', source)
            # with globalFrame.df_lock:
            #     globalFrame.df.loc[len(globalFrame.df)] = ["ac_off", 'Action', self.room_name, 'AC', time.strftime(
            #         "%Y-%m-%d %H:%M:%S", time.localtime(globalFrame.start_time)), self.room_name + '.AC.state: off', source]
            self.on = 0
        self.lock.release()
