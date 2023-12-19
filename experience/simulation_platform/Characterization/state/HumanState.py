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
        self.count_lock.acquire()
        v = self.getCount(self)
        self.setCount(self, v - 1)
        self.count_lock.release()
        if self.getCount(self) == 0:
            Time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(globalFrame.start_time))
            with self.lock:
                if self._enable_decrease(self):
                    url = getIP() + "/set_state_value/" + self.room + "/HumanState/0"
                    response = requests.post(url)
                    if response.status_code == 200:
                        print("请求成功")
                        print(self.room + '.HumanState.state: false')
                        globalFrame.loc(env, "human_undetected", 'Event', self.room, 'HumanState', self.room + '.HumanState.state: 0', 'Environment Change', Time, self.space)
                    else:
                        print("请求失败")

    def ext_action_increase(self,env):
        self.count_lock.acquire()
        v = self.getCount(self)
        self.setCount(self, v + 1)
        self.count_lock.release()
        Time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(globalFrame.start_time))
        if self.getCount(self) == 1:
            with self.lock:
                if self._enable_increase(self):
                    url = getIP() + "/set_state_value/" + self.room + "/HumanState/1"
                    response = requests.post(url)
                    if response.status_code == 200:
                        print("请求成功")
                        print(self.room + '.HumanState.state: true')
                        globalFrame.loc(env, "human_detected", 'Event', self.room, 'HumanState', self.room + '.HumanState.state: 1', 'Environment Change', Time, self.space)
                    else:
                        print("请求失败")
            
    def ap_value(self):
        url = getIP() + "/room_state_info/" + self.room + "/HumanState"
        value = requests.get(url).json()
        return str(value["value"])
    
    def getCount(self):
        return self.count
    
    def setCount(self, value):
        self.count = value