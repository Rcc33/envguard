import threading
from MetaType import BaseType
from DataFrame import globalFrame
import time


class HumanState(BaseType):
    def __init__(self, room):
        super().__init__()
        self.room = room
        self.count = 0
        self.count_lock = threading.Lock()
        self.lock = threading.Lock()
        self.value = 0

    def enable_decrease(self):
        if self.value == 0:
            return 0
        else:
            return 1

    def enable_increase(self):
        if self.value == 1:
            return 0
        else:
            return 1

    def ext_action_decrease(self,env):
        self.count_lock.acquire()
        if self.count > 0:
            self.count = self.count - 1
            if self.count == 0:
                self.count_lock.release()
                with self.lock:
                    if self.enable_decrease(self):
                        self.value = 0
                        print(self.room + '.HumanState.state: false')
                        globalFrame.loc(env, "human_undetected", 'Event', self.room, 'HumanState', self.room + '.HumanState.state: false', 'Environment Change')
                        
                        # with globalFrame.df_lock:
                        #     globalFrame.df.loc[len(globalFrame.df)] = ["human_undetected", 'Event', self.room, 'HumanState', time.strftime(
                        #         "%Y-%m-%d %H:%M:%S", time.localtime(globalFrame.start_time)), self.room + '.HumanState.state: false', 'Environment Change']
            else:
                self.count_lock.release()
        else:
            self.count_lock.release()

    def ext_action_increase(self,env):
        self.count_lock.acquire()
        self.count = self.count + 1
        if self.count == 10:
            t1 = threading.Thread(target=self.AirQuality, args=(self, env,))
            t1.start()
            globalFrame.thread_list.append(t1)
        if self.count == 1:
            self.count_lock.release()
            with self.lock:
                if self.enable_increase(self):
                    self.value = 1
                    print(self.room + '.HumanState.state: true')
                    globalFrame.loc(env, "human_detected", 'Event', self.room, 'HumanState', self.room + '.HumanState.state: true', 'Environment Change')
        else:
            self.count_lock.release()
    def get(self):
        return self.value

    def AirQuality(self, env):
        time.sleep(0.6*20)
        if self.count > 10:
            t1 = threading.Thread(target=env["space_dict"][self.room]['env_state']['AirQuality'].ext_action_decrease,
                                        args=(env["space_dict"][self.room]['env_state']['AirQuality'], env, ))
            t1.start()
            globalFrame.thread_list.append(t1)