import threading
import time
from DeviceController.DeviceController import *
    

def labInnerEffect(env, Name, Location, PayloadData, thread_list):
    t1 = threading.Thread(target=labEffect, args=(env, Name, Location, PayloadData, thread_list, ))
    t1.start()
    thread_list.append(t1)

def labEffect(env, Name, Location, PayloadData, thread_list):   
    if Name == "human_detected":
        env["space_dict"][Location]["env_state"]["HumanState"].count_lock.acquire() 
        env["space_dict"][Location]["env_state"]["HumanState"].count = env["space_dict"][Location]["env_state"]["HumanState"].count + 1
        if env["space_dict"][Location]["env_state"]["HumanState"].count == 10:
            env["space_dict"][Location]["env_state"]["HumanState"].count_lock.release()
            t1 = threading.Thread(target=AirQualityEffect, args=(env, Location,))
            t1.start()
            thread_list.append(t1)
        else:
            env["space_dict"][Location]["env_state"]["HumanState"].count_lock.release()

def AirQualityEffect(env, Location, thread_list):
        time.sleep(0.6*20)
        env["space_dict"][Location]["env_state"]["HumanState"].count_lock.acquire()
        if env["space_dict"][Location]["env_state"]["HumanState"].count >= 10:
            env["space_dict"][Location]["env_state"]["HumanState"].count_lock.release()
            t1 = threading.Thread(target=stateDecrease, args=(thread_list, Location, "AirQuality", env, ))
            t1.start()
            thread_list.append(t1)
        else:
            env["space_dict"][Location]["env_state"]["HumanState"].count_lock.release()