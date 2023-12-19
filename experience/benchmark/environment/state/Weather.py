import threading
import time
from MetaType import BaseType
from DataFrame import globalFrame


class Weather(BaseType):
    def __init__(self, room):
        super().__init__()
        self.room = room
        self.lock = threading.Lock()
        self.value = 'sunny'

    def enable_change(self, value):
        if self.value == value:
            return 0
        else:
            return 1

    def ext_action_change(self, value, env):
        with self.lock:
            if self.enable_change(self, value):
                self.value = value
                print(self.room + '.Weather.state: ' + self.value)
                globalFrame.loc(env, "weather_change", 'Event', self.room, 'Weather', self.room + '.Weather.state: ' + self.value, 'Environment Change')
                # with globalFrame.df_lock:
                #     globalFrame.df.loc[len(globalFrame.df)] = ["weather_change", 'Event', self.room, 'Weather', time.strftime(
                #         "%Y-%m-%d %H:%M:%S", time.localtime(globalFrame.start_time)), self.room + '.Weather.state: ' + self.value, 'Environment Change']
