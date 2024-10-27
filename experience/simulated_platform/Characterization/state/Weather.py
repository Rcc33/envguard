import threading
import time
from Characterization.MetaType import BaseType
from util.DataFrame import globalFrame
import requests
from config import getIP

class Weather(BaseType):
    def __init__(self, room,space):
        super().__init__()
        self.space = space
        self.room = room
        self.lock = threading.Lock()

    def _enable_change(self, value):
        if self.ap_value(self) == value:
            return 0
        else:
            return 1

    def ext_action_change(self, value, env):
        Time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(globalFrame.start_time))
        with self.lock:
            if self._enable_change(self, value):
                url = getIP() + "/set_state_value/" + self.room + "/Weather/" + value
                response = requests.post(url)
                if response.status_code == 200:
                    globalFrame.loc(env, "weather_change", 'Event', self.room, 'Weather', self.room + '.Weather.state: ' + value, 'None', Time, self.space)
                else:
                    print("请求失败")
                
    def ap_value(self):
        url = getIP() + "/room_state_info/" + self.room + "/Weather"
        value = requests.get(url).json()
        return str(value["value"])