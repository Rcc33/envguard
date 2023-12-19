import time
from MetaType import BaseType
from DataFrame import globalFrame
import threading
import random


class WaterDispenser(BaseType):
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
            print(self.room_name + '.WaterDispenser.state: on')
            globalFrame.loc(env, "water_dispenser_on", 'Action', self.room_name, 'WaterDispenser', self.room_name + '.WaterDispenser.state: on', source)
            # with globalFrame.df_lock:
            #     globalFrame.df.loc[len(globalFrame.df)] = ["water_dispenser_on", 'Action', self.room_name, 'WaterDispenser', time.strftime(
            #         "%Y-%m-%d %H:%M:%S", time.localtime(globalFrame.start_time)), self.room_name + '.WaterDispenser.state: on', source]
            self.on = 1
        self.lock.release()

    def enable_off(self):
        if self.on == 0:
            return 0
        else:
            return 1

    def action_off(self, env, source):
        self.lock.acquire()
        if self.enable_off(self):
            print(self.room_name + '.WaterDispenser.state: off')
            globalFrame.loc(env, "water_dispenser_off", 'Action', self.room_name, 'WaterDispenser', self.room_name + '.WaterDispenser.state: off', source)
            # with globalFrame.df_lock:
            #     globalFrame.df.loc[len(globalFrame.df)] = ["water_dispenser_off", 'Action', self.room_name, 'WaterDispenser', time.strftime(
            #         "%Y-%m-%d %H:%M:%S", time.localtime(globalFrame.start_time)), self.room_name + '.WaterDispenser.state: off', source]
            self.on = 0
        self.lock.release()
