import threading
from DeviceController.DeviceController import *

def labOuterEffect(env, Name, Location, PayloadData, thread_list):
    t1 = threading.Thread(target=labEffect, args=(env, Name, Location, PayloadData, thread_list, ))
    t1.start()
    thread_list.append(t1)

def labEffect(env, Name, Location, PayloadData, thread_list):
    if Location == "Context" and Name == "brightness_up":
        for room in env["space_dict"]:
            item = env["space_dict"][room]
            if room != "Corridor" and room != "Context" and "Curtain" in item["device_dict"]:
                Curtain = item["device_dict"]["Curtain"]
                Light = item["device_dict"]["Light"]
                Curtain.lock.acquire()
                Light.lock.acquire()
                if Curtain and getDeviceState(room, "Curtain", env) == '1' and Light and getDeviceState(room, "Light", env) == '0':
                    Curtain.lock.release()
                    Light.lock.release()
                    t1 = threading.Thread(target=stateIncrease, args=(thread_list,room, "Brightness", env, ))
                    t1.start()
                    thread_list.append(t1)
                else:
                    Curtain.lock.release()
                    Light.lock.release()
                    
    if Location == "Context" and Name == "brightness_down":
        for room in env["space_dict"]:
            item = env["space_dict"][room]
            if room != "Corridor" and room != "Context" and "Curtain" in item["device_dict"]:
                Curtain = item["device_dict"]["Curtain"]
                Light = item["device_dict"]["Light"]
                Curtain.lock.acquire()
                Light.lock.acquire()
                if Curtain and getDeviceState(room, "Curtain", env) == '1' and Light and getDeviceState(room, "Light", env) == '0':
                    Curtain.lock.release()
                    Light.lock.release()
                    t1 = threading.Thread(target=stateDecrease, args=(thread_list,room, "Brightness", env, ))
                    t1.start()
                    thread_list.append(t1)
                else:
                    Curtain.lock.release()
                    Light.lock.release()
