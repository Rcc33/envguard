import time
from util.DataFrame import globalFrame
from Characterization.MetaType import BaseType
import threading
import random
import requests
from util.parse.parse import parse
from config import getIP

class Window(BaseType):
    def __init__(self, room_name, space):
        super().__init__()
        self.space = space
        self.room_name = room_name
        self.lock = threading.Lock()

    def _enable_on(self):
        if self.ap_on(self) == '1':
            return 0
        else:
            return 1

    def action_on(self, env, source): 
        self.lock.acquire()
        if self._enable_on(self):
            # 判断pre-conditions，产生相应的effects
            url = getIP() + "/set_device_value/" + self.room_name + "/Window001/1"
            response = requests.post(url)
            if response.status_code == 200:
                print("请求成功")
                self.lock.release()   
                print(self.room_name + '.Window.state: on')
                Time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(globalFrame.start_time))
                globalFrame.loc(env, "window_on", 'Action', self.room_name, 'Window', self.room_name + '.Window.state: 1', source, Time, self.space)        
                t1 = threading.Thread(target=self._effect, args=(self, env, '1', 'action_on',))
                t1.start()
                globalFrame.thread_list.append(t1)
            else:
                print("请求失败")
        else:
            self.lock.release()

    def _effect(self, env, expect_value, action_name):
        url = getIP() + "/effect_and_pre/" + self.room_name + "/Window001/" + action_name
        effect_and_pre = requests.get(url).json()
        time.sleep(random.uniform(0.6*5, 0.6*10))
        self.lock.acquire()
        if self.ap_on(self) == expect_value:
            self.lock.release()
            for effect in effect_and_pre:
                (func, state) = parse(effect, effect_and_pre, env)
                if func:
                    func(state, env)
        else:
            self.lock.release() 

    def _enable_off(self):
        if self.ap_on(self) == '0':
            return 0
        else:
            return 1

    def action_off(self, env, source): 
        self.lock.acquire()
        if self._enable_off(self):
            url = getIP() + "/set_device_value/" + self.room_name + "/Window001/0"
            response = requests.post(url)
            if response.status_code == 200:
                print("请求成功")
                self.lock.release()
                print(self.room_name + '.Window.state: off')
                Time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(globalFrame.start_time))
                globalFrame.loc(env, "window_off", 'Action', self.room_name, 'Window', self.room_name + '.Window.state: 0', source, Time, self.space)
                t1 = threading.Thread(target=self._effect, args=(self, env, '0', 'action_off',))
                t1.start()
                globalFrame.thread_list.append(t1)
            else:
                print("请求失败")
        else:
            self.lock.release()
            
    def ap_on(self):
        url = getIP() + "/room_device_info/" + self.room_name + "/Window001"
        value = requests.get(url).json()
        return str(value["state"])