import time
from DataFrame import globalFrame
from MetaType import BaseType
import threading
import random


class Window(BaseType):
    def __init__(self, state, room_state, room_name):
        super().__init__()
        self.state = state
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
            globalFrame.loc(env, "window_on", 'Action', self.room_name, 'Window', self.room_name + '.Window.state: on', source)
            # with globalFrame.df_lock:
            #     globalFrame.df.loc[len(globalFrame.df)] = ["window_on",'Action', self.room_name, 'Window', time.strftime(
            #         "%Y-%m-%d %H:%M:%S", time.localtime(globalFrame.start_time)), self.room_name + '.Window.state: on', source]
            self.on = 1
            self.lock.release()
            print(self.room_name + '.Window.state: on')
            print("开窗 环境状态变化ing")
            t1 = threading.Thread(target=self.effect, args=(self, env,))
            t1.start()
            globalFrame.thread_list.append(t1)
        else:
            self.lock.release()

    def effect(self, env):
        time.sleep(random.uniform(0.6*5, 0.6*8))
        AirPurifier = env["space_dict"][self.room_name]["device_dict"]["AirPurifier"]
        Humidifier = env["space_dict"][self.room_name]["device_dict"]["Humidifier"]
        if self.room_name != 'TeaRoom':
            AC = env["space_dict"][self.room_name]["device_dict"]["AC"]
            Heater = env["space_dict"][self.room_name]["device_dict"]["Heater"]
            self.lock.acquire()
            if self.on == 1:
                self.lock.release()
                AC.lock.acquire()
                Heater.lock.acquire()
                if AC.on == 0 and Heater == 0:
                    AC.lock.release()
                    Heater.lock.release()
                    self.state["Temperature"].lock.acquire()
                    self.room_state["Temperature"].lock.acquire()
                    if self.state["Temperature"].value > self.room_state["Temperature"].value:
                        self.state["Temperature"].lock.release()
                        self.room_state["Temperature"].lock.release()
                        self.room_state["Temperature"].ext_action_increase(self.room_state["Temperature"], env)
                    elif self.state["Temperature"].value < self.room_state["Temperature"].value:
                        self.state["Temperature"].lock.release()
                        self.room_state["Temperature"].lock.release()
                        self.room_state["Temperature"].ext_action_decrease(self.room_state["Temperature"], env)
                    else:
                        self.state["Temperature"].lock.release()
                        self.room_state["Temperature"].lock.release()
                else:
                    AC.lock.release()
                    Heater.lock.release()
                    
                Humidifier.lock.acquire()
                if Humidifier.on == 0:
                    Humidifier.lock.release()
                    self.state["Humidity"].lock.acquire()
                    self.room_state["Humidity"].lock.acquire()
                    if self.state["Humidity"].value > self.room_state["Humidity"].value:
                        self.state["Humidity"].lock.release()
                        self.room_state["Humidity"].lock.release()
                        self.room_state["Humidity"].ext_action_increase(self.room_state["Humidity"], env)
                    elif self.state["Humidity"].value < self.room_state["Humidity"].value:
                        self.state["Humidity"].lock.release()
                        self.room_state["Humidity"].lock.release()
                        self.room_state["Humidity"].ext_action_decrease(self.room_state["Humidity"], env)
                    else:
                        self.state["Humidity"].lock.release()
                        self.room_state["Humidity"].lock.release()
                else:
                    Humidifier.lock.release()
                
                AirPurifier.lock.acquire()
                if AirPurifier.on == 0:
                    AirPurifier.lock.release()
                    self.state["AirQuality"].lock.acquire()
                    self.room_state["AirQuality"].lock.acquire()
                    if self.state["AirQuality"].value > self.room_state["AirQuality"].value:
                        self.state["AirQuality"].lock.release()
                        self.room_state["AirQuality"].lock.release()
                        self.room_state["AirQuality"].ext_action_increase(self.room_state["AirQuality"], env)
                    elif self.state["AirQuality"].value < self.room_state["AirQuality"].value:
                        self.state["AirQuality"].lock.release()
                        self.room_state["AirQuality"].lock.release()
                        self.room_state["AirQuality"].ext_action_decrease(self.room_state["AirQuality"], env)
                    else:
                        self.state["AirQuality"].lock.release()
                        self.room_state["AirQuality"].lock.release()
                else:
                    AirPurifier.lock.release()
            else:
                self.lock.release()
        else:
            self.lock.acquire()
            if self.on == 1:
                self.lock.release()
                self.state["Temperature"].lock.acquire()
                self.room_state["Temperature"].lock.acquire()
                if self.state["Temperature"].value > self.room_state["Temperature"].value:
                    self.state["Temperature"].lock.release()
                    self.room_state["Temperature"].lock.release()
                    self.room_state["Temperature"].ext_action_increase(self.room_state["Temperature"], env)
                elif self.state["Temperature"].value < self.room_state["Temperature"].value:
                    self.state["Temperature"].lock.release()
                    self.room_state["Temperature"].lock.release()
                    self.room_state["Temperature"].ext_action_decrease(self.room_state["Temperature"], env)
                else:
                    self.state["Temperature"].lock.release()
                    self.room_state["Temperature"].lock.release()
                    
                Humidifier.lock.acquire()
                if Humidifier.on == 0:
                    Humidifier.lock.release()
                    self.state["Humidity"].lock.acquire()
                    self.room_state["Humidity"].lock.acquire()
                    if self.state["Humidity"].value > self.room_state["Humidity"].value:
                        self.state["Humidity"].lock.release()
                        self.room_state["Humidity"].lock.release()
                        self.room_state["Humidity"].ext_action_increase(self.room_state["Humidity"], env)
                    elif self.state["Humidity"].value < self.room_state["Humidity"].value:
                        self.state["Humidity"].lock.release()
                        self.room_state["Humidity"].lock.release()
                        self.room_state["Humidity"].ext_action_decrease(self.room_state["Humidity"], env)
                    else:
                        self.state["Humidity"].lock.release()
                        self.room_state["Humidity"].lock.release()
                else:
                    Humidifier.lock.release()
                
                AirPurifier.lock.acquire()
                if AirPurifier.on == 0:
                    AirPurifier.lock.release()
                    self.state["AirQuality"].lock.acquire()
                    self.room_state["AirQuality"].lock.acquire()
                    if self.state["AirQuality"].value > self.room_state["AirQuality"].value:
                        self.state["AirQuality"].lock.release()
                        self.room_state["AirQuality"].lock.release()
                        self.room_state["AirQuality"].ext_action_increase(self.room_state["AirQuality"], env)
                    elif self.state["AirQuality"].value < self.room_state["AirQuality"].value:
                        self.state["AirQuality"].lock.release()
                        self.room_state["AirQuality"].lock.release()
                        self.room_state["AirQuality"].ext_action_decrease(self.room_state["AirQuality"], env)
                    else:
                        self.state["AirQuality"].lock.release()
                        self.room_state["AirQuality"].lock.release()
                else:
                    AirPurifier.lock.release()
            else:
                self.lock.release()

    def enable_off(self):
        if self.on == 0:
            return 0
        else:
            return 1

    def action_off(self, env, source):
        self.lock.acquire()
        if self.enable_off(self):
            print(self.room_name + '.Window.state: off')
            globalFrame.loc(env, "window_off", 'Action', self.room_name, 'Window', self.room_name + '.Window.state: off', source)
            # with globalFrame.df_lock:
            #     globalFrame.df.loc[len(globalFrame.df)] = ["window_off",'Action', self.room_name, 'Window', time.strftime(
            #         "%Y-%m-%d %H:%M:%S", time.localtime(globalFrame.start_time)), self.room_name + '.Window.state: off', source]
            self.on = 0
        self.lock.release()
