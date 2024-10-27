import threading
from Characterization.MetaType import BaseType
from util.DataFrame import globalFrame
import time
import requests
from config import getIP

class HumanState(BaseType):
    def __init__(self, room, space):
        super().__init__()
        self.space = space
        self.room = room
        if(room == "BedroomOne"):
            self.count = 1
        elif(room == "BedroomTwo"):
            self.count = 2
        else:
            self.count = 0
        self.count_lock = threading.Lock()
        self.lock = threading.Lock()

    def _enable_decrease(self):
        v = self.ap_value(self)
        print("enable_decrease " + v)
        if v == '0':
            return 0
        else:
            return 1

    def _enable_increase(self):
        v = self.ap_value(self)
        if v == '1':
            return 0
        else:
            return 1

    def ext_action_decrease(self,env):
        with self.lock:
            if self._enable_decrease(self):
                self.count_lock.acquire()
                v = self.count
                self.count = v - 1
                self.count_lock.release()
                if v == 1:
                    Time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(globalFrame.start_time))
                    url = getIP() + "/set_state_value/" + self.room + "/HumanState/0"
                    response = requests.post(url)
                    if response.status_code == 200:
                        globalFrame.loc(env, "human_undetected", 'Event', self.room, 'HumanState', self.room + '.HumanState.state: 0', 'None', Time, self.space)
                    else:
                        print("请求失败")

    def ext_action_increase(self,env):
        with self.lock:
            if self._enable_increase(self):
                self.count_lock.acquire()
                self.count = self.count + 1
                self.count_lock.release()
                Time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(globalFrame.start_time))
                url = getIP() + "/set_state_value/" + self.room + "/HumanState/1"
                response = requests.post(url)
                if response.status_code == 200:
                    globalFrame.loc(env, "human_detected", 'Event', self.room, 'HumanState', self.room + '.HumanState.state: 1', 'None', Time, self.space)
                else:
                    print("请求失败")
            
    def ap_value(self):
        url = getIP() + "/room_state_info/" + self.room + "/HumanState"
        value = requests.get(url).json()
        return str(value["value"])
