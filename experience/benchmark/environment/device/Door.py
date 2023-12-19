import time
import threading
import random
from DataFrame import globalFrame
from MetaType import BaseType


class Door(BaseType):
    def __init__(self, adjacent, room_state, room_name):
        super().__init__()
        self.adjacent = adjacent
        self.room_state = room_state
        self.room_name = room_name
        self.lock = threading.Lock()
        self.on = 0

    def enable_on(self):
        if self.on == 1:
            return 0
        else:
            return 1

    def effect(self, env):
        self.lock.acquire()
        if self.on == 0:
            self.lock.release()
            return
        else:
            self.lock.release()
            time.sleep(random.uniform(0.6*5, 0.6*10))
            self.lock.acquire()
            if self.on == 1:
                self.lock.release()
                self.adjacent["Temperature"].lock.acquire()
                self.room_state["Temperature"].lock.acquire()
                if self.adjacent["Temperature"].value - self.room_state["Temperature"].value >= 2:
                    self.adjacent["Temperature"].lock.release()
                    self.room_state["Temperature"].lock.release()
                    self.room_state["Temperature"].ext_action_increase(self.room_state["Temperature"],env)
                    self.adjacent["Temperature"].ext_action_decrease(self.adjacent["Temperature"],env)
                elif self.room_state["Temperature"].value - self.adjacent["Temperature"].value >= 2:
                    self.adjacent["Temperature"].lock.release()
                    self.room_state["Temperature"].lock.release()
                    self.room_state["Temperature"].ext_action_decrease(self.room_state["Temperature"],env)
                    self.adjacent["Temperature"].ext_action_increase(self.adjacent["Temperature"],env)
                else:
                    self.adjacent["Temperature"].lock.release()
                    self.room_state["Temperature"].lock.release()
            else:
                self.lock.release()

            # self.adjacent["Humidity"].lock.acquire()
            # self.room_state["Humidity"].lock.acquire()
            # if self.adjacent["Humidity"].value - self.room_state["Humidity"].value >= 2:
            #     self.adjacent["Humidity"].lock.release()
            #     self.room_state["Humidity"].lock.release()
            #     self.room_state["Humidity"].ext_action_increase(self.room_state["Humidity"])
            #     self.adjacent["Humidity"].ext_action_decrease(self.adjacent["Humidity"])
            # elif self.room_state["Humidity"].value - self.adjacent["Humidity"].value >= 2:
            #     self.adjacent["Humidity"].lock.release()
            #     self.room_state["Humidity"].lock.release()
            #     self.room_state["Humidity"].ext_action_decrease(self.room_state["Humidity"])
            #     self.adjacent["Humidity"].ext_action_increase(self.adjacent["Humidity"])
            # else:
            #     self.adjacent["Humidity"].lock.release()
            #     self.room_state["Humidity"].lock.release()

    def action_on(self, env, source):
        self.lock.acquire()
        if self.enable_on(self):
            # 判断pre-conditions，产生相应的effects
            print(self.room_name + '.Door.state: on')
            # print("开门 环境状态变化ing")
            globalFrame.loc(env, "door_on", 'Action', self.room_name, 'Door', self.room_name + '.Door.state: on', source)
            # with globalFrame.df_lock:
            #     globalFrame.df.loc[len(globalFrame.df)] = ["door_on", 'Action', self.room_name, 'Door', time.strftime(
            #         "%Y-%m-%d %H:%M:%S", time.localtime(globalFrame.start_time)), self.room_name + '.Door.state: on', source]
            self.on = 1
            self.lock.release()
            # time.sleep(0.01)
            # t1 = threading.Thread(target=self.effect, args=(self, env,))
            # t1.start()
            # globalFrame.thread_list.append(t1)
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
            print(self.room_name + '.Door.state: off')
            globalFrame.loc(env, "door_off", 'Action', self.room_name, 'Door', self.room_name + '.Door.state: off', source)
            # with globalFrame.df_lock:
            #     globalFrame.df.loc[len(globalFrame.df)] = ["door_off", 'Action', self.room_name, 'Door', time.strftime(
            #         "%Y-%m-%d %H:%M:%S", time.localtime(globalFrame.start_time)), self.room_name + '.Door.state: off', source]
            self.on = 0
        self.lock.release()
