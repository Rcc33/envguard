import threading
import time
import pandas as pd
from regulation.tap import tap


class DataFrame():
    def __init__(self):
        super().__init__()
        self.df_lock = threading.Lock()
        self.flag = True
        self.thread_list = []
        self.df = pd.DataFrame(columns=('Name', 'Type', 'Location', 'Object', 'Timestamp', 'Payload Data', 'Source'))
        self.start_time = time.mktime(time.strptime("2023-09-04 00:00:01", "%Y-%m-%d %H:%M:%S"))

    def changeTime(self):
        while self.flag:
            self.start_time += 1
            time.sleep(0.01)

    def loc(self, env, Name, Type, Location, Object, PayloadData, source):
        self.df_lock.acquire()
        self.df.loc[len(self.df)] = [Name, Type, Location, Object, time.strftime(
            "%Y-%m-%d %H:%M:%S", time.localtime(self.start_time)), PayloadData, source]
        self.df_lock.release()
        thread = threading.Thread(target=tap, args=(env, Name, Location, PayloadData, self.thread_list,))
        thread.start()
        self.thread_list.append(thread)
        # tap(env, Name, Location, PayloadData)


globalFrame = DataFrame()
