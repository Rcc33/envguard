import random
import time
import pandas as pd
import threading
from DeviceController.DeviceController import *

def homeTap(env, Name, Location, PayloadData, thread_list):
    if Name == 'human_detected':
        if (Location in ['LivingRoom']):
            t1 = threading.Thread(target=deviceOn, args=(Location, "Light", env, 'app',))
            t1.start()
            thread_list.append(t1)
    if Name == 'humidity_down':
        if (Location in ['BedroomOne', 'BedroomTwo', 'LivingRoom']) and PayloadData.split(': ')[1] == 'low':
            t1 = threading.Thread(target=deviceOn, args=(Location, "Humidifier", env, 'app',))
            t1.start()
            thread_list.append(t1)
    if Name == 'washing_machine_off':
        t1 = threading.Thread(target=deviceOn, args=("LivingRoom", "Speaker", env, 'app',))
        t1.start()
        thread_list.append(t1)
    