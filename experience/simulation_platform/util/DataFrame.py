import threading
import time
import pandas as pd
from AutomatedApplication.tap.labTap import labTap
from AutomatedApplication.tap.homeTap import homeTap
from AutomatedApplication.tap.simulationTap import simulationTap
from PhysicalRules.InnerChange.homeInnerChange import *
from PhysicalRules.InnerChange.labInnerChange import *
from PhysicalRules.InnerChange.simulationInnerChange import *
from PhysicalRules.OuterChange.homeOuterChange import *
from PhysicalRules.OuterChange.labOuterChange import *
from PhysicalRules.OuterChange.simulationOuterChange import *


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

    def loc(self, env, Name, Type, Location, Object, PayloadData, source, Time,space):
        self.df_lock.acquire()
        self.df.loc[len(self.df)] = [Name, Type, Location, Object, Time, PayloadData, source]
        self.df_lock.release()        
        if (space == "Lab"):
            thread = threading.Thread(target=labTap, args=(env, Name, Location, PayloadData, self.thread_list,))
            innerEffectThread = threading.Thread(target=labInnerEffect, args=(env, Name, Location, PayloadData, self.thread_list,))
            outerEffectThread = threading.Thread(target=labOuterEffect, args=(env, Name, Location, PayloadData, self.thread_list,))
        elif (space == "Home"):
            thread = threading.Thread(target=homeTap, args=(env, Name, Location, PayloadData, self.thread_list,))
            innerEffectThread = threading.Thread(target=homeInnerEffect, args=(env, Name, Location, PayloadData, self.thread_list,))
            outerEffectThread = threading.Thread(target=homeOuterEffect, args=(env, Name, Location, PayloadData, self.thread_list,))
        elif (space == "Simulation"):
            thread = threading.Thread(target=simulationTap, args=(env, Name, Location, PayloadData, self.thread_list,))
            innerEffectThread = threading.Thread(target=simulationInnerEffect, args=(env, Name, Location, PayloadData, self.thread_list,))
            outerEffectThread = threading.Thread(target=simulationOuterEffect, args=(env, Name, Location, PayloadData, self.thread_list,))
        thread.start()
        self.thread_list.append(thread)
        innerEffectThread.start()
        self.thread_list.append(innerEffectThread)
        outerEffectThread.start()
        self.thread_list.append(outerEffectThread)
            

globalFrame = DataFrame()
