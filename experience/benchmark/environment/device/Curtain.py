from DataFrame import globalFrame
from MetaType import BaseType
import time
import random
import threading


class Curtain(BaseType):
    def __init__(self, state, room_state, room_name):
        super().__init__()
        self.state = state
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
            print(self.room_name + '.Curtain.state: on')
            globalFrame.loc(env, "curtain_on", 'Action', self.room_name, 'Curtain', self.room_name + '.Curtain.state: on', source)
            # with globalFrame.df_lock:
            #     globalFrame.df.loc[len(globalFrame.df)] = ["curtain_on", 'Action', self.room_name, 'Curtain', time.strftime(
            #         "%Y-%m-%d %H:%M:%S", time.localtime(globalFrame.start_time)), self.room_name + '.Curtain.state: on', source]
            self.on = 1
            self.lock.release()
            t1 = threading.Thread(target=self.effect, args=(self, env,))
            t1.start()
            globalFrame.thread_list.append(t1)
        else:
            self.lock.release()

    def effect(self, env):
        # 房间内开灯时，窗帘对亮度没有影响
        Light = env["space_dict"][self.room_name]["device_dict"]["Light"]
        Light.lock.acquire()
        if Light.on == 0:
            Light.lock.release()
            self.state["Brightness"].lock.acquire()
            self.room_state["Brightness"].lock.acquire()
            if self.state["Brightness"].value > self.room_state["Brightness"].value:
                self.state["Brightness"].lock.release()
                self.room_state["Brightness"].lock.release()
                time.sleep(random.uniform(0.6*0.5, 0.6*1))
                self.room_state["Brightness"].ext_action_increase(self.room_state["Brightness"], env)
            else:
                self.state["Brightness"].lock.release()
                self.room_state["Brightness"].lock.release()
        else:
            Light.lock.release()

    def enable_off(self):
        if self.on == 0:
            return 0
        else:
            return 1

    def action_off(self, env, source):
        self.lock.acquire()
        if self.enable_off(self):
            print(self.room_name + '.Curtain.state: off')
            globalFrame.loc(env, "curtain_off", 'Action', self.room_name, 'Curtain', self.room_name + '.Curtain.state: off', source)
            # with globalFrame.df_lock:
            #     globalFrame.df.loc[len(globalFrame.df)] = ["curtain_off", 'Action', self.room_name, 'Curtain', time.strftime(
            #         "%Y-%m-%d %H:%M:%S", time.localtime(globalFrame.start_time)), self.room_name + '.Curtain.state: off', source]
            self.on = 0
            self.lock.release()
            t1 = threading.Thread(target=self.effect_off, args=(self, env,))
            t1.start()
            globalFrame.thread_list.append(t1)
        else:
            self.lock.release()

    def effect_off(self, env):
        Light = env["space_dict"][self.room_name]["device_dict"]["Light"]
        Light.lock.acquire()
        if Light.on == 0:
            Light.lock.release()
            time.sleep(random.uniform(0.6*0.5, 0.6*1))
            self.state["Brightness"].lock.acquire()
            self.room_state["Brightness"].lock.acquire()
            if self.state["Brightness"].value > self.room_state["Brightness"].value:
                self.state["Brightness"].lock.release()
                self.room_state["Brightness"].lock.release()
                self.room_state["Brightness"].ext_action_decrease(self.room_state["Brightness"], env)
            else:
                self.state["Brightness"].lock.release()
                self.room_state["Brightness"].lock.release()
        else:
            Light.lock.release()
