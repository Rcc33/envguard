import threading
from MetaType import BaseType
from DataFrame import globalFrame
import time


class AirQuality(BaseType):
    def __init__(self, room):
        super().__init__()
        self.room = room
        self.lock = threading.Lock()
        self.value = 0

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
                        print(self.room + '.AirQuality.state: low')
                        globalFrame.loc(env, "air_quality_down", 'Event', self.room, 'AirQuality', self.room + '.AirQuality.state: low', 'Environment Change')
                        # with globalFrame.df_lock:
                        #     globalFrame.df.loc[len(globalFrame.df)] = ["air_quality_decrease", 'Event', self.room, 'AirQuality', time.strftime(
                        #         "%Y-%m-%d %H:%M:%S", time.localtime(globalFrame.start_time)), self.room + '.AirQuality.state: low', 'Environment Change']
                    case 0:
                        print(self.room + '.AirQuality.state: middle')
                        globalFrame.loc(env, "air_quality_down", 'Event', self.room, 'AirQuality', self.room + '.AirQuality.state: middle', 'Environment Change')
                        # with globalFrame.df_lock:
                        #     globalFrame.df.loc[len(globalFrame.df)] = ["air_quality_decrease", 'Event', self.room, 'AirQuality', time.strftime(
                        #         "%Y-%m-%d %H:%M:%S", time.localtime(globalFrame.start_time)), self.room + '.AirQuality.state: middle', 'Environment Change']

    def ext_action_increase(self, env):
        with self.lock:
            if self.enable_increase(self):
                self.value = self.value + 1
                match self.value:
                    case 0:
                        print(self.room + '.AirQuality.state: middle')
                        globalFrame.loc(env, "air_quality_up", 'Event', self.room, 'AirQuality', self.room + '.AirQuality.state: middle', 'Environment Change')
                        # with globalFrame.df_lock:
                        #     globalFrame.df.loc[len(globalFrame.df)] = ["air_quality_increase", 'Event', self.room, 'AirQuality', time.strftime(
                        #         "%Y-%m-%d %H:%M:%S", time.localtime(globalFrame.start_time)), self.room + '.AirQuality.state: middle', 'Environment Change']
                    case 1:
                        print(self.room + '.AirQuality.state: high')
                        globalFrame.loc(env, "air_quality_up", 'Event', self.room, 'AirQuality', self.room + '.AirQuality.state: high', 'Environment Change')
                        # with globalFrame.df_lock:
                        #     globalFrame.df.loc[len(globalFrame.df)] = ["air_quality_increase", 'Event', self.room, 'AirQuality', time.strftime(
                        #         "%Y-%m-%d %H:%M:%S", time.localtime(globalFrame.start_time)), self.room + '.AirQuality.state: high', 'Environment Change']
