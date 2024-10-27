import time
from Characterization.MetaType import BaseType
from DeviceController.DeviceController import *
from util.DataFrame import globalFrame
import threading
import random
import requests
from util.parse.parse import parse
from config import getIP


class MicrowaveOven(BaseType):
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
            url = getIP() + "/set_device_value/" + self.room_name + "/MicrowaveOven001/1"
            response = requests.post(url)
            if response.status_code == 200:
                self.lock.release()
                Time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(globalFrame.start_time))
                globalFrame.loc(env, "microwave_oven_on", 'Action', self.room_name, 'MicrowaveOven', self.room_name + '.MicrowaveOven.state: 1', source, Time, self.space)
                t1 = threading.Thread(target=self._effect, args=(self, env, '1', 'action_on', source,))
                t1.start()
                globalFrame.thread_list.append(t1)  
            else:
                print("请求失败")
        else:
            self.lock.release()

    def _effect(self, env, expect_value, action_name, source):
        url = getIP() + "/effect_and_pre/" + self.room_name + "/MicrowaveOven001/" + action_name
        effect_and_pre = requests.get(url).json()
        time.sleep(random.uniform(0.05, 0.10))
        self.lock.acquire()
        if self.ap_on(self) == expect_value:
            self.lock.release()
            for effect in effect_and_pre:
                (func, state) = parse(effect, effect_and_pre, env)
                if func:
                    func(state, env)
        else:
            self.lock.release()

        # 设置人随机离开
        if random.randint(1, 3) == 1:
            t = threading.Thread(target=self.person_leave, args=(self, env,))
            t.start()
            globalFrame.thread_list.append(t)  
        
        if expect_value == '1':
            time.sleep(random.uniform(0.6*1, 0.6*5))
            self.action_off(self, env, source)
    
    def person_leave(self, env):
        time.sleep(random.uniform(0.3, 1.5))
        env['space_dict']['TeaRoom']["device_dict"]["Door"].action_on(env['space_dict']['TeaRoom']["device_dict"]["Door"], env,  'offline')
        time.sleep(random.uniform(0.02, 0.04))
        stateDecrease(globalFrame.thread_list,"TeaRoom", "HumanState", env)
        stateIncrease(globalFrame.thread_list,"Corridor", "HumanState", env)
        env['space_dict']['TeaRoom']["device_dict"]["Door"].action_off(env['space_dict']['TeaRoom']["device_dict"]["Door"], env,  'offline')
        time.sleep(random.uniform(0.15, 0.45))
        env['space_dict']['TeaRoom']["device_dict"]["Door"].action_on(env['space_dict']['TeaRoom']["device_dict"]["Door"], env,  'offline')
        time.sleep(random.uniform(0.01, 0.03))
        stateDecrease(globalFrame.thread_list,"Corridor", "HumanState", env)
        stateIncrease(globalFrame.thread_list,"TeaRoom", "HumanState", env)
        env['space_dict']['TeaRoom']["device_dict"]["Door"].action_off(env['space_dict']['TeaRoom']["device_dict"]["Door"], env,  'offline')
        time.sleep(random.uniform(0.2, 1.3))

    def _enable_off(self):
        if self.ap_on(self) == '0':
            return 0
        else:
            return 1

    def action_off(self, env, source): 
        self.lock.acquire()
        if self._enable_off(self):
            url = getIP() + "/set_device_value/" + self.room_name + "/MicrowaveOven001/0"
            response = requests.post(url)
            if response.status_code == 200:
                self.lock.release()
                Time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(globalFrame.start_time))
                globalFrame.loc(env, "microwave_oven_off", 'Action', self.room_name, 'MicrowaveOven', self.room_name + '.MicrowaveOven.state: 0', source, Time, self.space)
                t1 = threading.Thread(target=self._effect, args=(self, env, '0', 'action_off', source,))
                t1.start()
                globalFrame.thread_list.append(t1)
            else:
                print("请求失败")
        else:
            self.lock.release()
            
    def ap_on(self):
        url = getIP() + "/room_device_info/" + self.room_name + "/MicrowaveOven001"
        value = requests.get(url).json()
        return str(value["state"])