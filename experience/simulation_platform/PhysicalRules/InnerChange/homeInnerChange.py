import threading
import time

from DeviceController.DeviceController import *

def homeInnerEffect(env, Name, Location, PayloadData, thread_list):
    t1 = threading.Thread(target=homeEffect, args=(env, Name, Location, PayloadData, thread_list, ))
    t1.start()
    thread_list.append(t1)

def homeEffect(env, Name, Location, PayloadData, thread_list):   
    print()