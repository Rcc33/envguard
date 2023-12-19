import threading
from Characterization.MetaType import BaseType
from util.DataFrame import globalFrame
import time
import requests
from config import getIP

class Noise(BaseType):
    def __init__(self, room,space):
        super().__init__()
        self.space = space
        self.room = room
        self.lock = threading.Lock()

    def _enable_decrease(self):
        if self.ap_value(self) == '-1':
            return 0
        else:
            return 1

    def _enable_increase(self):
        if self.ap_value(self) == '1':
            return 0
        else:
            return 1

    def ext_action_decrease(self, env):
        Time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(globalFrame.start_time))
        with self.lock:
            if self._enable_decrease(self):
                value = str(int(self.ap_value(self)) - 1)
                url = getIP() + "/set_state_value/" + self.room + "/Noise/" + value
                response = requests.post(url)
                if response.status_code == 200:
                    print("请求成功")
                    globalFrame.loc(env, "noise_down", 'Event', self.room, 'Noise', self.room + '.Noise.state: ' + value, 'Environment Change', Time, self.space)
                else:
                    print("请求失败")
                
    def ext_action_increase(self, env):
        Time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(globalFrame.start_time))
        with self.lock:
            if self._enable_increase(self):
                value = str(int(self.ap_value(self)) + 1)
                url = getIP() + "/set_state_value/" + self.room + "/Noise/" + value
                response = requests.post(url)
                if response.status_code == 200:
                    print("请求成功")
                    globalFrame.loc(env, "noise_up", 'Event', self.room, 'Noise', self.room + '.Noise.state: ' + value, 'Environment Change', Time, self.space)
                else:
                    print("请求失败")
                
    def ap_value(self):
        url = getIP() + "/room_state_info/" + self.room + "/Noise"
        value = requests.get(url).json()
        return str(value["value"])