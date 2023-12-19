import threading
import time

from DeviceController.DeviceController import *
    
def simulationInnerEffect(env, Name, Location, PayloadData, thread_list):
    t1 = threading.Thread(target=simulationEffect, args=(env, Name, Location, PayloadData, thread_list, ))
    t1.start()
    thread_list.append(t1)

def simulationEffect(env, Name, Location, PayloadData, thread_list):   
    print()