import threading
from MetaType import BaseType
from DataFrame import globalFrame
import time


class Brightness(BaseType):

    def __init__(self, room):
        super().__init__()
        self.value = 0
        self.room = room
        self.lock = threading.Lock()

    def enable_decrease(self):
        if self.value == -1:
            return 0
        else:
            return 1

    def enable_increase(self):
        if self.value == 1:
            return 0
        else:
            return 1

    def ext_action_decrease(self, env):
        with self.lock:
            if self.enable_decrease(self):
                self.value = self.value - 1
                match self.value:
                    case -1:
                        print(self.room + '.Brightness.state: low')
                        globalFrame.loc(env, "brightness_down", 'Event', self.room, 'Brightness', self.room + '.Brightness.state: low', 'Environment Change')
                        # with globalFrame.df_lock:
                        #     globalFrame.df.loc[len(globalFrame.df)] = ["brightness_decrease", 'Event', self.room, 'Brightness', time.strftime(
                        #         "%Y-%m-%d %H:%M:%S", time.localtime(globalFrame.start_time)), self.room + '.Brightness.state: low', 'Environment Change']
                    case 0:
                        print(self.room + '.Brightness.state: middle')
                        globalFrame.loc(env, "brightness_down", 'Event', self.room, 'Brightness', self.room + '.Brightness.state: middle', 'Environment Change')
                        # with globalFrame.df_lock:
                        #     globalFrame.df.loc[len(globalFrame.df)] = ["brightness_decrease", 'Event', self.room, 'Brightness', time.strftime(
                        #         "%Y-%m-%d %H:%M:%S", time.localtime(globalFrame.start_time)), self.room + '.Brightness.state: middle', 'Environment Change']
        if self.room == "Context":
            for room in env["space_dict"]:
                item = env["space_dict"][room]
                if room != "Corridor" and room != "Context":
                    Curtain = item["device_dict"]["Curtain"]
                    Light = item["device_dict"]["Light"]
                    Curtain.lock.acquire()
                    Light.lock.acquire()
                    if Curtain and Curtain.on == 1 and Light and Light.on == 0:
                        Curtain.lock.release()
                        Light.lock.release()
                        item["env_state"]["Brightness"].ext_action_decrease(item["env_state"]["Brightness"], env)
                    else:
                        Curtain.lock.release()
                        Light.lock.release()

    def ext_action_increase(self, env):
        with self.lock:
            if self.enable_increase(self):
                self.value = self.value + 1
                match self.value:
                    case 0:
                        print(self.room + '.Brightness.state: middle')
                        globalFrame.loc(env, "brightness_up", 'Event', self.room, 'Brightness', self.room + '.Brightness.state: middle', 'Environment Change')
                        # with globalFrame.df_lock:
                        #     globalFrame.df.loc[len(globalFrame.df)] = ["brightness_increase", 'Event', self.room, 'Brightness', time.strftime(
                        #         "%Y-%m-%d %H:%M:%S", time.localtime(globalFrame.start_time)), self.room + '.Brightness.state: middle', 'Environment Change']
                    case 1:
                        print(self.room + '.Brightness.state: high')
                        globalFrame.loc(env, "brightness_up", 'Event', self.room, 'Brightness', self.room + '.Brightness.state: high', 'Environment Change')
                        # with globalFrame.df_lock:
                        #     globalFrame.df.loc[len(globalFrame.df)] = ["brightness_increase", 'Event', self.room, 'Brightness', time.strftime(
                        #         "%Y-%m-%d %H:%M:%S", time.localtime(globalFrame.start_time)), self.room + '.Brightness.state: high', 'Environment Change']
        if self.room == "Context":
            for room in env["space_dict"]:
                item = env["space_dict"][room]
                if room != "Corridor" and room != "Context":
                    Curtain = item["device_dict"]["Curtain"]
                    Light = item["device_dict"]["Light"]
                    Curtain.lock.acquire()
                    Light.lock.acquire()
                    if Curtain and Curtain.on == 1 and Light and Light.on == 0:
                        Curtain.lock.release()
                        Light.lock.release()
                        item["env_state"]["Brightness"].ext_action_increase(item["env_state"]["Brightness"], env)
                    else:
                        Curtain.lock.release()
                        Light.lock.release()
