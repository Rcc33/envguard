import threading
import time
import random
import datetime
from Environment import env
from DataFrame import globalFrame


Context = env["space_dict"]["Context"]
Lab = env["space_dict"]["Lab"]
MeetingRoomOne = env["space_dict"]["MeetingRoomOne"]
MeetingRoomTwo = env["space_dict"]["MeetingRoomTwo"]
TeaRoom = env["space_dict"]["TeaRoom"]
Corridor = env["space_dict"]["Corridor"]

random_device_list = [
    [Lab["device_dict"]["Curtain"].action_on, Lab["device_dict"]["Curtain"]],
    [Lab["device_dict"]["Curtain"].action_off, Lab["device_dict"]["Curtain"]],
    [Lab["device_dict"]["Door"].action_on, Lab["device_dict"]["Door"]],
    [Lab["device_dict"]["AC"].action_on, Lab["device_dict"]["AC"]],
    # [Lab["device_dict"]["Heater"].action_on, Lab["device_dict"]["Heater"]],
    [Lab["device_dict"]["Humidifier"].action_on, Lab["device_dict"]["Humidifier"]],
    [Lab["device_dict"]["Printer"].action_on, Lab["device_dict"]["Printer"]],
    [Lab["device_dict"]["AirPurifier"].action_on, Lab["device_dict"]["AirPurifier"]],
    [Lab["device_dict"]["Window"].action_on, Lab["device_dict"]["Window"]],
    [Lab["device_dict"]["Light"].action_on, Lab["device_dict"]["Light"]],
    [Lab["device_dict"]["AC"].action_off, Lab["device_dict"]["AC"]],
    # [Lab["device_dict"]["Heater"].action_off, Lab["device_dict"]["Heater"]],
    [Lab["device_dict"]["Humidifier"].action_off, Lab["device_dict"]["Humidifier"]],
    [Lab["device_dict"]["AirPurifier"].action_off, Lab["device_dict"]["AirPurifier"]],
    [Lab["device_dict"]["Window"].action_off, Lab["device_dict"]["Window"]],
    # [Lab["device_dict"]["Light"].action_off, Lab["device_dict"]["Light"]],
    [Lab["device_dict"]["Door"].action_off, Lab["device_dict"]["Door"]]]

def SignIn():
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(globalFrame.start_time)))
    Corridor["device_dict"]["Door"].action_on(Corridor["device_dict"]["Door"], env, 'offline')
    time.sleep(random.uniform(0.02, 0.04))
    Corridor["env_state"]["HumanState"].ext_action_increase(Corridor["env_state"]["HumanState"], env, )
    time.sleep(random.uniform(0.01, 0.02))
    Corridor["device_dict"]["Door"].action_off(Corridor["device_dict"]["Door"], env, 'offline')
    # t1 = threading.Thread(target=Corridor["device_dict"]["Speaker"].action_on,args=(Corridor["device_dict"]["Speaker"],))
    # t1.start()
    # print("到 Corridor -> Lab, sleep 10-20s...")
    time.sleep(random.uniform(0.10, 0.20))
    Lab["device_dict"]["Door"].action_on(Lab["device_dict"]["Door"], env, 'offline')
    time.sleep(random.uniform(0.02, 0.04))
    Corridor["env_state"]["HumanState"].ext_action_decrease(Corridor["env_state"]["HumanState"], env, )
    Lab["env_state"]["HumanState"].ext_action_increase(Lab["env_state"]["HumanState"], env, )
    Lab["device_dict"]["Door"].action_off(Lab["device_dict"]["Door"], env,  'offline')
    # t1.join()

def SignOut():
    Lab["device_dict"]["Door"].action_on(Lab["device_dict"]["Door"], env,  'offline')
    time.sleep(random.uniform(0.02, 0.04))
    Lab["env_state"]["HumanState"].ext_action_decrease(Lab["env_state"]["HumanState"], env, )
    Corridor["env_state"]["HumanState"].ext_action_increase(Corridor["env_state"]["HumanState"], env, )
    Lab["device_dict"]["Door"].action_off(Lab["device_dict"]["Door"], env,  'offline')
    print("签退 Lab -> Corridor, sleep 10-20s...")
    time.sleep(random.uniform(0.10, 0.20))
    Corridor["device_dict"]["Door"].action_on(Corridor["device_dict"]["Door"], env, 'offline')
    time.sleep(random.uniform(0.02, 0.04))
    Corridor["env_state"]["HumanState"].ext_action_decrease(Corridor["env_state"]["HumanState"], env, )
    time.sleep(random.uniform(0.01, 0.02))
    Corridor["device_dict"]["Door"].action_off(Corridor["device_dict"]["Door"], env, 'offline')


def CatchWater():
    Lab["device_dict"]["Door"].action_on(Lab["device_dict"]["Door"], env,  'offline')
    time.sleep(random.uniform(0.02, 0.04))
    Lab["env_state"]["HumanState"].ext_action_decrease(Lab["env_state"]["HumanState"], env, )
    Corridor["env_state"]["HumanState"].ext_action_increase(Corridor["env_state"]["HumanState"], env, )
    Lab["device_dict"]["Door"].action_off(Lab["device_dict"]["Door"], env,  'offline')
    print("Lab -> TeaRoom, sleep 10-30s...")
    time.sleep(random.uniform(0.10, 0.30))
    TeaRoom["device_dict"]["Door"].action_on(TeaRoom["device_dict"]["Door"], env,  'offline')
    time.sleep(random.uniform(0.02, 0.04))
    Corridor["env_state"]["HumanState"].ext_action_decrease(Corridor["env_state"]["HumanState"], env, )
    TeaRoom["env_state"]["HumanState"].ext_action_increase(TeaRoom["env_state"]["HumanState"], env, )
    TeaRoom["device_dict"]["Door"].action_off(TeaRoom["device_dict"]["Door"], env,  'offline')
    print("TeaRoom -> WaterDispenser, sleep 5-10s...")
    time.sleep(random.uniform(0.05, 0.10))
    TeaRoom["device_dict"]["WaterDispenser"].action_on(TeaRoom["device_dict"]["WaterDispenser"], env,  'offline')
    print("接水, sleep 20-60s...")
    if random.randint(1, 7) == 1:
        time.sleep(random.uniform(0.08, 0.60))
        TeaRoom["device_dict"]["Door"].action_on(TeaRoom["device_dict"]["Door"], env,  'offline')
        time.sleep(random.uniform(0.02, 0.04))
        TeaRoom["env_state"]["HumanState"].ext_action_decrease(TeaRoom["env_state"]["HumanState"], env, )
        Corridor["env_state"]["HumanState"].ext_action_increase(Corridor["env_state"]["HumanState"], env, )
        TeaRoom["device_dict"]["Door"].action_off(TeaRoom["device_dict"]["Door"], env,  'offline')
        time.sleep(random.uniform(0.02, 0.04))
        TeaRoom["device_dict"]["Door"].action_on(TeaRoom["device_dict"]["Door"], env,  'offline')
        time.sleep(random.uniform(0.01, 0.03))
        Corridor["env_state"]["HumanState"].ext_action_decrease(Corridor["env_state"]["HumanState"], env, )
        TeaRoom["env_state"]["HumanState"].ext_action_increase(TeaRoom["env_state"]["HumanState"], env, )
        TeaRoom["device_dict"]["Door"].action_off(TeaRoom["device_dict"]["Door"], env,  'offline')
        time.sleep(random.uniform(0.07, 1.09))
    else:      
        time.sleep(random.uniform(0.20, 0.60*3))
    TeaRoom["device_dict"]["WaterDispenser"].action_off(TeaRoom["device_dict"]["WaterDispenser"], env,  'offline')
    print("WaterDispenser -> TeaRoom, sleep 5-10s...")
    time.sleep(random.uniform(0.05, 0.10))
    TeaRoom["device_dict"]["Door"].action_on(TeaRoom["device_dict"]["Door"], env,  'offline')
    time.sleep(random.uniform(0.02, 0.04))
    TeaRoom["env_state"]["HumanState"].ext_action_decrease(TeaRoom["env_state"]["HumanState"], env, )
    Corridor["env_state"]["HumanState"].ext_action_increase(Corridor["env_state"]["HumanState"], env, )
    TeaRoom["device_dict"]["Door"].action_off(TeaRoom["device_dict"]["Door"], env,  'offline')
    print("TeaRoom -> Lab, sleep 10-30s...")
    time.sleep(random.uniform(0.10, 0.30))
    Lab["device_dict"]["Door"].action_on(Lab["device_dict"]["Door"], env,  'offline')
    time.sleep(random.uniform(0.02, 0.04))
    Corridor["env_state"]["HumanState"].ext_action_decrease(Corridor["env_state"]["HumanState"], env, )
    Lab["env_state"]["HumanState"].ext_action_increase(Lab["env_state"]["HumanState"], env, )
    Lab["device_dict"]["Door"].action_off(Lab["device_dict"]["Door"], env,  'offline')


def Meeting(room):
    if room == "MeetingRoomOne":
        # go to meetingroom one
        Lab["device_dict"]["Door"].action_on(Lab["device_dict"]["Door"], env,  'offline')
        time.sleep(random.uniform(0.02, 0.04))
        Lab["env_state"]["HumanState"].ext_action_decrease(Lab["env_state"]["HumanState"], env, )
        Corridor["env_state"]["HumanState"].ext_action_increase(Corridor["env_state"]["HumanState"], env, )
        Lab["device_dict"]["Door"].action_off(Lab["device_dict"]["Door"], env,  'offline')
        print("Lab -> TeaRoom, sleep 20-40s...")
        time.sleep(random.uniform(0.20, 0.40))
        TeaRoom["device_dict"]["Door"].action_on(TeaRoom["device_dict"]["Door"], env,  'offline')
        time.sleep(random.uniform(0.02, 0.04))
        Corridor["env_state"]["HumanState"].ext_action_decrease(Corridor["env_state"]["HumanState"], env, )
        TeaRoom["env_state"]["HumanState"].ext_action_increase(TeaRoom["env_state"]["HumanState"], env, )
        TeaRoom["device_dict"]["Door"].action_off(TeaRoom["device_dict"]["Door"], env,  'offline')
        print("TeaRoom -> MeetingRoomOne, sleep 5-10s...")
        time.sleep(random.uniform(0.05, 0.10))
        MeetingRoomOne["device_dict"]["Door"].action_on(MeetingRoomOne["device_dict"]["Door"], env,  'offline')
        time.sleep(random.uniform(0.02, 0.04))
        TeaRoom["env_state"]["HumanState"].ext_action_decrease(TeaRoom["env_state"]["HumanState"], env, )
        MeetingRoomOne["env_state"]["HumanState"].ext_action_increase(MeetingRoomOne["env_state"]["HumanState"], env, )
        MeetingRoomOne["device_dict"]["Door"].action_off(MeetingRoomOne["device_dict"]["Door"], env, 'offline')
        if random.randint(0, 1) == 1: 
            MeetingRoomOne["device_dict"]["TV"].action_on(MeetingRoomOne["device_dict"]["TV"], env,  'offline')
        if random.randint(0, 1) == 1: 
            MeetingRoomOne["device_dict"]["AC"].action_on(MeetingRoomOne["device_dict"]["AC"], env,  'offline')
        if random.randint(0, 1) == 1: 
            MeetingRoomOne["device_dict"]["Curtain"].action_on(MeetingRoomOne["device_dict"]["Curtain"], env,  'offline')
        if random.randint(0, 1) == 1: 
            MeetingRoomOne["device_dict"]["AirPurifier"].action_on(MeetingRoomOne["device_dict"]["AirPurifier"], env,  'offline')
        # if random.randint(0, 1) == 1: 
        #     MeetingRoomOne["device_dict"]["Humidifier"].action_on(MeetingRoomOne["device_dict"]["Humidifier"], env,  'offline')
        MeetingRoomOne["device_dict"]["Light"].action_on(MeetingRoomOne["device_dict"]["Light"], env,  'offline')
        print("开会, sleep 600-3600s...")
        time.sleep(random.uniform(15*0.6, 90*0.6))
        if random.randint(1, 100) < 95: 
            MeetingRoomOne["device_dict"]["TV"].action_off(MeetingRoomOne["device_dict"]["TV"], env,  'offline')
        if random.randint(1, 100) < 95: 
            MeetingRoomOne["device_dict"]["AC"].action_off(MeetingRoomOne["device_dict"]["AC"], env,  'offline')
        if random.randint(1, 100) < 95: 
            MeetingRoomOne["device_dict"]["Curtain"].action_off(MeetingRoomOne["device_dict"]["Curtain"], env,  'offline')
        if random.randint(1, 100) < 95: 
            MeetingRoomOne["device_dict"]["AirPurifier"].action_off(MeetingRoomOne["device_dict"]["AirPurifier"], env,  'offline')
        if random.randint(1, 100) < 50: 
            MeetingRoomOne["device_dict"]["Humidifier"].action_off(MeetingRoomOne["device_dict"]["Humidifier"], env,  'offline')  
        if random.randint(1, 100) < 20: 
            MeetingRoomOne["device_dict"]["Light"].action_off(MeetingRoomOne["device_dict"]["Light"], env,  'offline')
        MeetingRoomOne["device_dict"]["Door"].action_on(MeetingRoomOne["device_dict"]["Door"], env,  'offline')
        time.sleep(random.uniform(0.02, 0.04))
        MeetingRoomOne["env_state"]["HumanState"].ext_action_decrease(MeetingRoomOne["env_state"]["HumanState"], env, )
        TeaRoom["env_state"]["HumanState"].ext_action_increase(TeaRoom["env_state"]["HumanState"], env, )
        MeetingRoomOne["device_dict"]["Door"].action_off(MeetingRoomOne["device_dict"]["Door"], env,  'offline')
        print("MeetingRoomOne -> TeaRoom, sleep 5-10s...")
        time.sleep(random.uniform(0.05, 0.10))
        TeaRoom["device_dict"]["Door"].action_on(TeaRoom["device_dict"]["Door"], env,  'offline')
        time.sleep(random.uniform(0.02, 0.04))
        TeaRoom["env_state"]["HumanState"].ext_action_decrease(TeaRoom["env_state"]["HumanState"], env, )
        Corridor["env_state"]["HumanState"].ext_action_increase(Corridor["env_state"]["HumanState"], env, )
        TeaRoom["device_dict"]["Door"].action_off(TeaRoom["device_dict"]["Door"], env,  'offline')
        print("TeaRoom -> Lab, sleep 20-40s...")
        time.sleep(random.uniform(0.20, 0.40))
        Lab["device_dict"]["Door"].action_on(Lab["device_dict"]["Door"], env,  'offline')
        time.sleep(random.uniform(0.02, 0.04))
        Corridor["env_state"]["HumanState"].ext_action_decrease(Corridor["env_state"]["HumanState"], env, )
        Lab["env_state"]["HumanState"].ext_action_increase(Lab["env_state"]["HumanState"], env, )
        Lab["device_dict"]["Door"].action_off(Lab["device_dict"]["Door"], env,  'offline')
    elif room == "MeetingRoomTwo":
        # go to meetingroom two
        Lab["device_dict"]["Door"].action_on(Lab["device_dict"]["Door"], env, 'offline')
        time.sleep(random.uniform(0.02, 0.04))
        Lab["env_state"]["HumanState"].ext_action_decrease(Lab["env_state"]["HumanState"], env, )
        Corridor["env_state"]["HumanState"].ext_action_increase(Corridor["env_state"]["HumanState"], env, )
        Lab["device_dict"]["Door"].action_off(Lab["device_dict"]["Door"], env, 'offline')
        print("Lab -> MeetingRoomTwo, sleep 20-40s...")
        time.sleep(random.uniform(0.20, 0.40))
        MeetingRoomTwo["device_dict"]["Door"].action_on(MeetingRoomTwo["device_dict"]["Door"], env, 'offline')
        time.sleep(random.uniform(0.02, 0.04))
        Corridor["env_state"]["HumanState"].ext_action_decrease(Corridor["env_state"]["HumanState"], env, )
        MeetingRoomTwo["env_state"]["HumanState"].ext_action_increase(MeetingRoomTwo["env_state"]["HumanState"], env, )
        MeetingRoomTwo["device_dict"]["Door"].action_off(MeetingRoomTwo["device_dict"]["Door"], env, 'offline')
        if random.randint(0, 1) == 1: 
            MeetingRoomTwo["device_dict"]["TV"].action_on(MeetingRoomTwo["device_dict"]["TV"], env,  'offline')
        if random.randint(0, 1) == 1: 
            MeetingRoomTwo["device_dict"]["AC"].action_on(MeetingRoomTwo["device_dict"]["AC"], env,  'offline')
        if random.randint(0, 1) == 1: 
            MeetingRoomTwo["device_dict"]["Curtain"].action_on(MeetingRoomTwo["device_dict"]["Curtain"], env,  'offline')
        if random.randint(0, 1) == 1: 
            MeetingRoomTwo["device_dict"]["AirPurifier"].action_on(MeetingRoomTwo["device_dict"]["AirPurifier"], env,  'offline')
        # if random.randint(0, 1) == 1: 
        #     MeetingRoomTwo["device_dict"]["Humidifier"].action_on(MeetingRoomTwo["device_dict"]["Humidifier"], env,  'offline')
        MeetingRoomTwo["device_dict"]["Light"].action_on(MeetingRoomTwo["device_dict"]["Light"], env,  'offline')
        print("开会, sleep 600-3600s...")
        time.sleep(random.uniform(10*0.6, 60*0.6))
        if random.randint(1, 100) < 95: 
            MeetingRoomTwo["device_dict"]["TV"].action_off(MeetingRoomTwo["device_dict"]["TV"], env,  'offline')
        if random.randint(1, 100) < 95: 
            MeetingRoomTwo["device_dict"]["AC"].action_off(MeetingRoomTwo["device_dict"]["AC"], env,  'offline')
        if random.randint(1, 100) < 95: 
            MeetingRoomTwo["device_dict"]["Curtain"].action_off(MeetingRoomTwo["device_dict"]["Curtain"], env,  'offline')
        if random.randint(1, 100) < 95: 
            MeetingRoomTwo["device_dict"]["AirPurifier"].action_off(MeetingRoomTwo["device_dict"]["AirPurifier"], env,  'offline')
        if random.randint(1, 100) < 50: 
            MeetingRoomTwo["device_dict"]["Humidifier"].action_off(MeetingRoomTwo["device_dict"]["Humidifier"], env,  'offline')  
        if random.randint(1, 100) < 20: 
            MeetingRoomTwo["device_dict"]["Light"].action_off(MeetingRoomTwo["device_dict"]["Light"], env,  'offline')
        MeetingRoomTwo["device_dict"]["Door"].action_on(MeetingRoomTwo["device_dict"]["Door"], env, 'offline')
        time.sleep(random.uniform(0.02, 0.04))
        MeetingRoomTwo["env_state"]["HumanState"].ext_action_decrease(MeetingRoomTwo["env_state"]["HumanState"], env, )
        Corridor["env_state"]["HumanState"].ext_action_increase(Corridor["env_state"]["HumanState"], env, )
        MeetingRoomTwo["device_dict"]["Door"].action_off(MeetingRoomTwo["device_dict"]["Door"], env, 'offline')
        print("MeetingRoomTwo -> Lab, sleep 20-40s...")
        time.sleep(random.uniform(0.20, 0.40))
        Lab["device_dict"]["Door"].action_on(Lab["device_dict"]["Door"], env, 'offline')
        time.sleep(random.uniform(0.02, 0.04))
        Corridor["env_state"]["HumanState"].ext_action_decrease(Corridor["env_state"]["HumanState"], env, )
        Lab["env_state"]["HumanState"].ext_action_increase(Lab["env_state"]["HumanState"], env, )
        Lab["device_dict"]["Door"].action_off(Lab["device_dict"]["Door"], env, 'offline')


def GoRestRoom():
    Lab["device_dict"]["Door"].action_on(Lab["device_dict"]["Door"], env, 'offline')
    time.sleep(random.uniform(0.02, 0.04))
    Lab["env_state"]["HumanState"].ext_action_decrease(Lab["env_state"]["HumanState"], env, )
    Corridor["env_state"]["HumanState"].ext_action_increase(Corridor["env_state"]["HumanState"], env, )
    Lab["device_dict"]["Door"].action_off(Lab["device_dict"]["Door"], env, 'offline')
    print("Lab -> Corridor, sleep 20-40s...")
    time.sleep(random.uniform(0.20, 0.40))
    Corridor["env_state"]["HumanState"].ext_action_decrease(Corridor["env_state"]["HumanState"], env, )
    print("上厕所, sleep 180-600s...")
    time.sleep(random.uniform(1.8, 10*0.6))
    Corridor["env_state"]["HumanState"].ext_action_increase(Corridor["env_state"]["HumanState"], env, )
    print("Corridor -> Lab, sleep 20-40s...")
    time.sleep(random.uniform(0.20, 0.40))
    Lab["device_dict"]["Door"].action_on(Lab["device_dict"]["Door"], env, 'offline')
    time.sleep(random.uniform(0.02, 0.04))
    Corridor["env_state"]["HumanState"].ext_action_decrease(Corridor["env_state"]["HumanState"], env, )
    Lab["env_state"]["HumanState"].ext_action_increase(Lab["env_state"]["HumanState"], env, )
    Lab["device_dict"]["Door"].action_off(Lab["device_dict"]["Door"], env, 'offline')


def HaveLunch():
    Lab["device_dict"]["Door"].action_on(Lab["device_dict"]["Door"], env, 'offline')
    time.sleep(random.uniform(0.02, 0.04))
    Lab["env_state"]["HumanState"].ext_action_decrease(Lab["env_state"]["HumanState"], env, )
    Corridor["env_state"]["HumanState"].ext_action_increase(Corridor["env_state"]["HumanState"], env, )
    Lab["device_dict"]["Door"].action_off(Lab["device_dict"]["Door"], env, 'offline')
    print("Lab -> TeaRoom, sleep 20-40s...")
    time.sleep(random.uniform(0.20, 0.40))
    TeaRoom["device_dict"]["Door"].action_on(TeaRoom["device_dict"]["Door"], env, 'offline')
    time.sleep(random.uniform(0.02, 0.04))
    Corridor["env_state"]["HumanState"].ext_action_decrease(Corridor["env_state"]["HumanState"], env, )
    TeaRoom["env_state"]["HumanState"].ext_action_increase(TeaRoom["env_state"]["HumanState"], env, )
    TeaRoom["device_dict"]["Door"].action_off(TeaRoom["device_dict"]["Door"], env, 'offline')
    if random.randint(0, 1) == 1: 
        TeaRoom["device_dict"]["Curtain"].action_on(TeaRoom["device_dict"]["Curtain"], env,  'offline')
    if random.randint(0, 1) == 1: 
        TeaRoom["device_dict"]["Window"].action_on(TeaRoom["device_dict"]["Window"], env,  'offline')
    if random.randint(0, 1) == 1: 
        TeaRoom["device_dict"]["AirPurifier"].action_on(TeaRoom["device_dict"]["AirPurifier"], env,  'offline')
    if random.randint(0, 1) == 1: 
        TeaRoom["device_dict"]["Humidifier"].action_on(TeaRoom["device_dict"]["Humidifier"], env,  'offline')
    TeaRoom["device_dict"]["Light"].action_on(TeaRoom["device_dict"]["Light"], env,  'offline')
    TeaRoom["device_dict"]["MicrowaveOven"].action_on(TeaRoom["device_dict"]["MicrowaveOven"], env, 'offline')
    print("吃饭, sleep 600-1200s...")
    if random.randint(1, 100) < 50: 
        TeaRoom["device_dict"]["Light"].action_off(TeaRoom["device_dict"]["Light"], env,  'offline')
    if random.randint(1, 100) < 80: 
        TeaRoom["device_dict"]["Window"].action_off(TeaRoom["device_dict"]["Window"], env,  'offline')
    if random.randint(1, 100) < 95: 
        TeaRoom["device_dict"]["Curtain"].action_off(TeaRoom["device_dict"]["Curtain"], env,  'offline')
    if random.randint(1, 100) < 95: 
        TeaRoom["device_dict"]["AirPurifier"].action_off(TeaRoom["device_dict"]["AirPurifier"], env,  'offline')
    if random.randint(1, 100) < 95: 
        TeaRoom["device_dict"]["Humidifier"].action_off(TeaRoom["device_dict"]["Humidifier"], env,  'offline')  
    time.sleep(random.uniform(10*0.6, 20*0.6))
    TeaRoom["device_dict"]["Door"].action_on(TeaRoom["device_dict"]["Door"], env, 'offline')
    time.sleep(random.uniform(0.02, 0.04))
    TeaRoom["env_state"]["HumanState"].ext_action_decrease(TeaRoom["env_state"]["HumanState"], env, )
    Corridor["env_state"]["HumanState"].ext_action_increase(Corridor["env_state"]["HumanState"], env, )
    TeaRoom["device_dict"]["Door"].action_off(TeaRoom["device_dict"]["Door"], env, 'offline')
    print("TeaRoom -> Lab, sleep 20-40s...")
    time.sleep(random.uniform(0.20, 0.40))
    Lab["device_dict"]["Door"].action_on(Lab["device_dict"]["Door"], env, 'offline')
    time.sleep(random.uniform(0.02, 0.04))
    Corridor["env_state"]["HumanState"].ext_action_decrease(Corridor["env_state"]["HumanState"], env, )
    Lab["env_state"]["HumanState"].ext_action_increase(Lab["env_state"]["HumanState"], env, )
    Lab["device_dict"]["Door"].action_off(Lab["device_dict"]["Door"], env, 'offline')


def CheckIn():
    print("签到 Corridor -> Lab, sleep 10-20s...")
    t1 = threading.Thread(target=Corridor["device_dict"]["Speaker"].action_on, args=(Corridor["device_dict"]["Speaker"], env, 'app',))
    t1.start()
    time.sleep(random.uniform(0.10, 0.20))
    t2 = threading.Thread(target=Lab["device_dict"]["Printer"].action_on, args=(Lab["device_dict"]["Printer"], env, 'app',))
    t2.start()

    t1.join()
    t2.join()


def Reservation(start_time, room):
    time.sleep(start_time - 20*0.6)
    t1 = threading.Thread(target=env["space_dict"][room]["device_dict"]["AirPurifier"].action_on,
                          args=(env["space_dict"][room]["device_dict"]["AirPurifier"], env, 'app',))
    t1.start()
    time.sleep(random.uniform(0.5, 0.10))
    t2 = threading.Thread(target=env["space_dict"][room]["device_dict"]["AC"].action_on,
                          args=(env["space_dict"][room]["device_dict"]["AC"], env, 'app',))
    t2.start()

    time.sleep(start_time - 10*0.6)
    t3 = threading.Thread(target=Lab["device_dict"]["Printer"].action_on, args=(Lab["device_dict"]["Printer"], env, 'app',))
    t3.start()
    time.sleep(random.uniform(0.5, 0.10))
    t4 = threading.Thread(target=env["space_dict"][room]["device_dict"]["Curtain"].action_on,
                          args=(env["space_dict"][room]["device_dict"]["Curtain"], env, 'app',))
    t4.start()
    
    t1.join()
    t2.join()
    t3.join()
    t4.join()

 
random_event_list = [CatchWater, GoRestRoom, HaveLunch, Reservation]


def test():
    
    t1 = threading.Thread(target=Lab["device_dict"]["AC"].action_on, args=(Lab["device_dict"]["AC"], env, 'offline',))
    t1.start()
    t1.join()
    t2 = threading.Thread(target=Lab["device_dict"]["Heater"].action_on, args=(Lab["device_dict"]["Heater"], env, 'offline',))
    t2.start()
    t2.join()
    

def personOne():
    time.sleep(random.uniform(0.6*60*8.5, 0.6*60*9.2))
    print("人员一到...")
    sign_in = threading.Thread(target=SignIn)
    sign_in.start()
    sign_in.join()
    time.sleep(random.uniform(0.03, 0.05))
    check_in = threading.Thread(target=CheckIn)
    check_in.start()
    check_in.join()
    time.sleep(random.uniform(0.03, 0.05))
    t1 = threading.Thread(target=Lab["device_dict"]["Humidifier"].action_on, args=(Lab["device_dict"]["Humidifier"], env, 'offline',))
    t1.start()
    time.sleep(random.uniform(0.6, 5*0.6))
    random_device = random.randint(0, len(random_device_list)-1)
    t2 = threading.Thread(target=random_device_list[random_device][0], args=(random_device_list[random_device][1], env, 'offline',))
    t2.start()
    time.sleep(random.uniform(0.6, 5*0.6))
    random_device = random.randint(0, len(random_device_list)-1)
    t3 = threading.Thread(target=random_device_list[random_device][0], args=(random_device_list[random_device][1], env, 'offline',))
    t3.start()
    print("人员一工作ing...")
    time.sleep(random.uniform(60*0.6, 80*0.6))
    random_device = random.randint(0, len(random_device_list)-1)
    t4 = threading.Thread(target=random_device_list[random_device][0], args=(random_device_list[random_device][1], env, 'offline',))
    t4.start()
    print("人员一继续工作ing...")
    time.sleep(random.uniform(60*0.6, 90*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    print("人员一继续工作ing...")
    time.sleep(random.uniform(10*0.6, 20*0.6))
    if random.randint(0, 1) == 0:
        have_lunch = threading.Thread(target=HaveLunch)
        have_lunch.start()
        have_lunch.join()
        print("人员一午休ing...")
        time.sleep(random.uniform(90*0.6, 120*0.6))
    else:
        sign_out = threading.Thread(target=SignOut)
        sign_out.start()
        sign_out.join()
        t = random.uniform(10*0.6, 120*0.6)
        time.sleep(t)
        sign_in = threading.Thread(target=SignIn)
        sign_in.start()
        sign_in.join()
        if t < 65*0.6:
            time.sleep(random.uniform((70-t)*0.6, (110-t)*0.6))
    time.sleep(random.uniform(1*0.6, 3*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    print("人员一继续工作ing...")
    time.sleep(random.uniform(90*0.6, 120*0.6))
    meeting = threading.Thread(target=Meeting, args=("MeetingRoomOne",))
    meeting.start()
    meeting.join()
    print("人员一继续工作ing...")
    time.sleep(random.uniform(50*0.6, 90*0.6))
    if random.randint(0, 1) == 0:
        sign_out = threading.Thread(target=SignOut)
        sign_out.start()
        sign_out.join()
        time.sleep(random.uniform(5*0.6, 20*0.6))
        sign_in = threading.Thread(target=SignIn)
        sign_in.start()
        sign_in.join()
    time.sleep(random.uniform(5*0.6, 20*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    print("人员一继续工作ing...")
    time.sleep(random.uniform(100*0.6, 130*0.6))
    t5 = threading.Thread(target=Lab["device_dict"]["AC"].action_off, args=(Lab["device_dict"]["AC"], env, 'offline',))
    t5.start()
    print("人员一签退...")
    print(datetime.datetime.fromtimestamp(globalFrame.start_time))
    sign_out = threading.Thread(target=SignOut)
    sign_out.start()
    sign_out.join()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()


def personTwo():
    pool = []
    time.sleep(random.uniform(0.6*60*8.8, 0.6*60*9))
    print("人员二到...")
    sign_in = threading.Thread(target=SignIn)
    sign_in.start()
    sign_in.join()
    time.sleep(random.uniform(0.03, 0.05))
    check_in = threading.Thread(target=CheckIn)
    check_in.start()
    check_in.join()
    time.sleep(random.uniform(0.6, 0.6*2))
    random_device = random.randint(0, len(random_device_list)-1)
    t1 = threading.Thread(target=random_device_list[random_device][0], args=(random_device_list[random_device][1], env, 'offline',))
    t1.start()
    print("人员二工作ing...")
    time.sleep(random.uniform(30*0.6, 60*0.6))
    t2 = threading.Thread(target=Lab["device_dict"]["Printer"].action_on, args=(Lab["device_dict"]["Printer"], env, 'offline',))
    t2.start()
    print("人员二继续工作ing...")
    time.sleep(random.uniform(60*0.6, 90*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    room = ['MeetingRoomOne', 'MeetingRoomTwo']
    if event_index == 3:
        start_time = random.uniform(40*0.6, 90*0.6)
        random_event = threading.Thread(target=random_event_list[event_index], args=(start_time, room[random.randint(0, 1)],))
        random_event.start()
        pool.append(random_event)
        if random.randint(0, 50) < 40: 
            time.sleep(start_time - 10*0.6)
            meeting = threading.Thread(target=Meeting, args=(room,))
            meeting.start()
            meeting.join()
    else:
        time.sleep(random.uniform(60*0.6, 120*0.6))
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    print("人员二午休ing...")
    time.sleep(random.uniform(1*0.6, 3*0.6))
    if random.randint(0, 2) == 0:
        have_lunch = threading.Thread(target=HaveLunch)
        have_lunch.start()
        have_lunch.join()
        print("人员一午休ing...")
        time.sleep(random.uniform(60*0.6, 90*0.6))
    else:
        sign_out = threading.Thread(target=SignOut)
        sign_out.start()
        sign_out.join()
        t = random.uniform(10*0.6, 90*0.6)
        time.sleep(t)
        sign_in = threading.Thread(target=SignIn)
        sign_in.start()
        sign_in.join()
        if t < 55*0.6:
            time.sleep(random.uniform((60-t)*0.6, (90-t)*0.6))
    time.sleep(random.uniform(1*0.6, 3*0.6))
    random_device = random.randint(0, len(random_device_list)-1)
    t3 = threading.Thread(target=random_device_list[random_device][0], args=(random_device_list[random_device][1], env, 'offline',))
    t3.start()
    print("人员二继续工作ing...")
    time.sleep(random.uniform(30*0.6, 60*0.6))
    catch_water = threading.Thread(target=CatchWater)
    catch_water.start()
    catch_water.join()
    time.sleep(random.uniform(0.6, 0.6*2))
    meeting = threading.Thread(target=Meeting, args=("MeetingRoomOne",))
    meeting.start()
    meeting.join()
    print("人员二继续工作ing...")
    time.sleep(random.uniform(120*0.6, 150*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    print("人员二继续工作ing...")
    time.sleep(random.uniform(90*0.6, 120*0.6))
    random_device = random.randint(0, len(random_device_list)-1)
    t4 = threading.Thread(target=random_device_list[random_device][0], args=(random_device_list[random_device][1], env, 'offline',))
    t4.start()
    time.sleep(random.uniform(0.6*30, 0.6*45))
    t5 = threading.Thread(target=Lab["device_dict"]["Window"].action_off, args=(Lab["device_dict"]["Window"], env, 'offline',))
    t5.start()
    print("人员二签退...")
    print(datetime.datetime.fromtimestamp(globalFrame.start_time))
    sign_out = threading.Thread(target=SignOut)
    sign_out.start()
    sign_out.join()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    
    for item in pool:
        item.join()


def personThree():
    pool = []
    time.sleep(random.uniform(0.6*60*8, 0.6*60*9))
    print("人员三到...")
    sign_in = threading.Thread(target=SignIn)
    sign_in.start()
    sign_in.join()
    time.sleep(random.uniform(0.03, 0.05))
    check_in = threading.Thread(target=CheckIn)
    check_in.start()
    check_in.join()
    time.sleep(random.uniform(0.6, 0.6*2))
    random_device = random.randint(0, len(random_device_list)-1)
    t1 = threading.Thread(target=random_device_list[random_device][0], args=(random_device_list[random_device][1], env, 'offline',))
    t1.start()
    print("人员三工作ing...")
    time.sleep(random.uniform(90*0.6, 110*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    print("人员三继续工作ing...")
    time.sleep(random.uniform(30*0.6, 60*0.6))
    rest_room = threading.Thread(target=GoRestRoom)
    rest_room.start()
    rest_room.join()
    print("人员三继续工作ing...")
    time.sleep(random.uniform(80*0.6, 100*0.6))
    have_lunch = threading.Thread(target=HaveLunch)
    have_lunch.start()
    have_lunch.join()
    print("人员三午休ing...")
    time.sleep(random.uniform(80*0.6, 100*0.6))
    random_device = random.randint(0, len(random_device_list)-1)
    t2 = threading.Thread(target=random_device_list[random_device][0], args=(random_device_list[random_device][1], env, 'offline',))
    t2.start()
    time.sleep(random.uniform(15*0.6, 30*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    room = ['MeetingRoomOne', 'MeetingRoomTwo']
    if event_index == 3:
        start_time = random.uniform(40*0.6, 90*0.6)
        random_event = threading.Thread(target=random_event_list[event_index], args=(start_time, room[random.randint(0, 1)],))
        random_event.start()
        pool.append(random_event)
        if random.randint(0, 50) < 40: 
            time.sleep(start_time - 10*0.6)
            meeting = threading.Thread(target=Meeting, args=(room,))
            meeting.start()
            meeting.join()
    else:
        time.sleep(random.uniform(40*0.6, 100*0.6))
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    print("人员三继续工作ing...")
    time.sleep(random.uniform(120*0.6, 150*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(5*0.6, 15*0.6))
    if random.randint(0, 1) == 0:
        sign_out = threading.Thread(target=SignOut)
        sign_out.start()
        sign_out.join()
        t = random.uniform(20*0.6, 50*0.6)
        time.sleep(t)
        sign_in = threading.Thread(target=SignIn)
        sign_in.start()
        sign_in.join()
        time.sleep(random.uniform(5*0.6, 15*0.6))
    else:
        print("人员三继续工作ing...")
        time.sleep(random.uniform(30*0.6, 60*0.6))
    random_device = random.randint(0, len(random_device_list)-1)
    t3 = threading.Thread(target=random_device_list[random_device][0], args=(random_device_list[random_device][1], env, 'offline',))
    t3.start()
    time.sleep(random.uniform(0.6, 0.6*2))
    t4 = threading.Thread(target=Lab["device_dict"]["Printer"].action_on, args=(Lab["device_dict"]["Printer"], env, 'offline',))
    t4.start()
    print("人员三继续工作ing...")
    time.sleep(random.uniform(15*0.6, 30*0.6))
    print("人员三签退...")
    print(datetime.datetime.fromtimestamp(globalFrame.start_time))
    sign_out = threading.Thread(target=SignOut)
    sign_out.start()
    sign_out.join()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    for item in pool:
        item.join()


def personFour():
    pool = []
    time.sleep(random.uniform(0.6*60*8.3, 0.6*60*9.1))
    print("人员四到...")
    sign_in = threading.Thread(target=SignIn)
    sign_in.start()
    sign_in.join()
    time.sleep(random.uniform(0.03, 0.05))
    check_in = threading.Thread(target=CheckIn)
    check_in.start()
    check_in.join()
    time.sleep(random.uniform(0.6, 0.6*2))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    print("人员四工作ing...")
    time.sleep(random.uniform(90*0.6, 150*0.6))
    random_device = random.randint(0, len(random_device_list)-1)
    t1 = threading.Thread(target=random_device_list[random_device][0], args=(random_device_list[random_device][1], env, 'offline',))
    t1.start()
    time.sleep(random.uniform(0.6, 0.6*2))
    event_index = random.randint(0, len(random_event_list)-1)
    room = ['MeetingRoomOne', 'MeetingRoomTwo']
    if event_index == 3:
        start_time = random.uniform(40*0.6, 90*0.6)
        random_event = threading.Thread(target=random_event_list[event_index], args=(start_time, room[random.randint(0, 1)],))
        random_event.start()
        pool.append(random_event)
        if random.randint(0, 50) < 40: 
            time.sleep(start_time - 10*0.6)
            meeting = threading.Thread(target=Meeting, args=(room,))
            meeting.start()
            meeting.join()
    else:
        time.sleep(random.uniform(50*0.6, 110*0.6))
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    print("人员四继续工作ing...")
    time.sleep(random.uniform(40*0.6, 70*0.6))
    random_device = random.randint(0, len(random_device_list)-1)
    t2 = threading.Thread(target=random_device_list[random_device][0], args=(random_device_list[random_device][1], env, 'offline',))
    t2.start()
    print("人员四午休ing...")
    time.sleep(random.uniform(5*0.6, 15*0.6))
    if random.randint(0, 1) == 0:
        sign_out = threading.Thread(target=SignOut)
        sign_out.start()
        sign_out.join()
        t = random.uniform(20*0.6, 50*0.6)
        time.sleep(t)
        sign_in = threading.Thread(target=SignIn)
        sign_in.start()
        sign_in.join()
        time.sleep(random.uniform(30*0.6, 40*0.6))
    else:
        time.sleep(random.uniform(50*0.6, 100*0.6))
    random_device = random.randint(0, len(random_device_list)-1)
    t3 = threading.Thread(target=random_device_list[random_device][0], args=(random_device_list[random_device][1], env, 'offline',))
    t3.start()
    print("人员四继续工作ing...")
    time.sleep(random.uniform(30*0.6, 60*0.6))
    random_device = random.randint(0, len(random_device_list)-1)
    t4 = threading.Thread(target=random_device_list[random_device][0], args=(random_device_list[random_device][1], env, 'offline',))
    t4.start()
    print("人员四继续工作ing...")
    time.sleep(random.uniform(120*0.6, 180*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(5*0.6, 15*0.6))
    if random.randint(0, 1) == 0:
        sign_out = threading.Thread(target=SignOut)
        sign_out.start()
        sign_out.join()
        t = random.uniform(20*0.6, 40*0.6)
        time.sleep(t)
        sign_in = threading.Thread(target=SignIn)
        sign_in.start()
        sign_in.join()
        time.sleep(random.uniform(5*0.6, 15*0.6))
    else:
        time.sleep(random.uniform(30*0.6, 60*0.6))
    time.sleep(random.uniform(0.6, 0.6*2))
    t5 = threading.Thread(target=Lab["device_dict"]["Light"].action_on, args=(Lab["device_dict"]["Light"], env, 'offline',))
    t5.start()
    print("人员四继续工作ing...")
    time.sleep(random.uniform(40*0.6, 60*0.6))
    random_device = random.randint(0, len(random_device_list)-1)
    t6 = threading.Thread(target=random_device_list[random_device][0], args=(random_device_list[random_device][1], env, 'offline',))
    t6.start()
    print("人员四签退...")
    print(datetime.datetime.fromtimestamp(globalFrame.start_time))
    sign_out = threading.Thread(target=SignOut)
    sign_out.start()
    sign_out.join()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    for item in pool:
        item.join()


def personFive():
    pool = []
    time.sleep(random.uniform(0.6*60*8.5, 0.6*60*8.9))
    print("人员五到...")
    sign_in = threading.Thread(target=SignIn)
    sign_in.start()
    sign_in.join()
    time.sleep(random.uniform(0.03, 0.05))
    check_in = threading.Thread(target=CheckIn)
    check_in.start()
    check_in.join()
    time.sleep(random.uniform(0.6*5, 0.6*15))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(0.6*2, 0.6*15))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    print("人员五工作ing...")
    time.sleep(random.uniform(60*0.6, 90*0.6))
    random_device = random.randint(0, len(random_device_list)-1)
    t1 = threading.Thread(target=random_device_list[random_device][0], args=(random_device_list[random_device][1], env, 'offline',))
    t1.start()
    time.sleep(random.uniform(0.6*8, 0.6*15))
    meeting = threading.Thread(target=Meeting, args=("MeetingRoomOne",))
    meeting.start()
    meeting.join()
    print("人员五午休ing...")
    time.sleep(random.uniform(5*0.6, 15*0.6))
    if random.randint(0, 1) == 0:
        sign_out = threading.Thread(target=SignOut)
        sign_out.start()
        sign_out.join()
        t = random.uniform(20*0.6, 50*0.6)
        time.sleep(t)
        sign_in = threading.Thread(target=SignIn)
        sign_in.start()
        sign_in.join()
        time.sleep(random.uniform(60*0.6, 80*0.6))
    else:
        t_window = threading.Thread(target=Lab["device_dict"]["Window"].action_on, args=(Lab["device_dict"]["Window"], env, 'offline',))
        t_window.start()
        pool.append(t_window)
        time.sleep(random.uniform(90*0.6, 110*0.6))
    t2 = threading.Thread(target=Lab["device_dict"]["Printer"].action_on, args=(Lab["device_dict"]["Printer"], env, 'offline',))
    t2.start()
    print("人员五继续工作ing...")
    time.sleep(random.uniform(90*0.6, 110*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(0.6*3, 0.6*15))
    random_device = random.randint(0, len(random_device_list)-1)
    t3 = threading.Thread(target=random_device_list[random_device][0], args=(random_device_list[random_device][1], env, 'offline',))
    t3.start()
    print("人员五继续工作ing...")
    time.sleep(random.uniform(90*0.6, 100*0.6))
    t4 = threading.Thread(target=Lab["device_dict"]["Curtain"].action_off, args=(Lab["device_dict"]["Curtain"], env, 'offline',))
    t4.start()
    print("人员五继续工作ing...")
    time.sleep(random.uniform(60*0.6, 80*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(0.6*8, 0.6*15))
    meeting = threading.Thread(target=Meeting, args=("MeetingRoomTwo",))
    meeting.start()
    meeting.join()
    time.sleep(random.uniform(0.6*8, 0.6*15))
    event_index = random.randint(0, len(random_event_list)-1)
    room = ['MeetingRoomOne', 'MeetingRoomTwo']
    if event_index == 3:
        start_time = random.uniform(40*0.6, 90*0.6)
        random_event = threading.Thread(target=random_event_list[event_index], args=(start_time, room[random.randint(0, 1)],))
        random_event.start()
        pool.append(random_event)
        if random.randint(0, 50) < 40: 
            time.sleep(start_time - 10*0.6)
            meeting = threading.Thread(target=Meeting, args=(room,))
            meeting.start()
            meeting.join()
    else:
        time.sleep(random.uniform(40*0.6, 70*0.6))
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    print("人员五继续工作ing...")
    time.sleep(random.uniform(40*0.6, 50*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(0.6*8, 0.6*15))
    print("人员五签退...")
    print(datetime.datetime.fromtimestamp(globalFrame.start_time))
    sign_out = threading.Thread(target=SignOut)
    sign_out.start()
    sign_out.join()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    for item in pool:
        item.join()


def personSix():
    pool = []
    time.sleep(random.uniform(0.6*60*8.6, 0.6*60*9.1))
    print("人员六到...")
    sign_in = threading.Thread(target=SignIn)
    sign_in.start()
    sign_in.join()
    time.sleep(random.uniform(0.03, 0.05))
    check_in = threading.Thread(target=CheckIn)
    check_in.start()
    check_in.join()
    time.sleep(random.uniform(0.6, 0.6*15))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    print("人员六工作ing...")
    time.sleep(random.uniform(60*0.6, 90*0.6))
    random_device = random.randint(0, len(random_device_list)-1)
    t1 = threading.Thread(target=Lab["device_dict"]["Humidifier"].action_on, args=(Lab["device_dict"]["Humidifier"], env, 'offline',))
    t1.start()
    time.sleep(random.uniform(90*0.6, 120*0.6))
    meeting = threading.Thread(target=Meeting, args=("MeetingRoomTwo",))
    meeting.start()
    meeting.join()
    print("人员六午休ing...")
    time.sleep(random.uniform(90*0.6, 120*0.6))
    t2 = threading.Thread(target=Lab["device_dict"]["AC"].action_on, args=(Lab["device_dict"]["AC"], env, 'offline',))
    t2.start()
    print("人员六继续工作ing...")
    time.sleep(random.uniform(30*0.6, 60*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    room = ['MeetingRoomOne', 'MeetingRoomTwo']
    if event_index == 3:
        start_time = random.uniform(40*0.6, 90*0.6)
        random_event = threading.Thread(target=random_event_list[event_index], args=(start_time, room[random.randint(0, 1)],))
        random_event.start()
        pool.append(random_event)
        if random.randint(0, 50) < 40: 
            time.sleep(start_time - 10*0.6)
            meeting = threading.Thread(target=Meeting, args=(room,))
            meeting.start()
            meeting.join()
    else:
        time.sleep(random.uniform(60*0.6, 110*0.6))
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(0.6, 0.6*15))
    random_device = random.randint(0, len(random_device_list)-1)
    t3 = threading.Thread(target=random_device_list[random_device][0], args=(random_device_list[random_device][1], env, 'offline',))
    t3.start()
    print("人员六继续工作ing...")
    time.sleep(random.uniform(5*0.6, 15*0.6))
    if random.randint(0, 1) == 0:
        sign_out = threading.Thread(target=SignOut)
        sign_out.start()
        sign_out.join()
        t = random.uniform(20*0.6, 50*0.6)
        time.sleep(t)
        sign_in = threading.Thread(target=SignIn)
        sign_in.start()
        sign_in.join()
    else:
        time.sleep(random.uniform(20*0.6, 40*0.6))
    random_device = random.randint(0, len(random_device_list)-1)
    t4 = threading.Thread(target=random_device_list[random_device][0], args=(random_device_list[random_device][1], env, 'offline',))
    t4.start()
    time.sleep(random.uniform(0.6, 0.6*15))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    print("人员六继续工作ing...")
    time.sleep(random.uniform(120*0.6, 150*0.6))
    print("人员六签退...")
    print(datetime.datetime.fromtimestamp(globalFrame.start_time))
    sign_out = threading.Thread(target=SignOut)
    sign_out.start()
    sign_out.join()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    for item in pool:
        item.join()


def personSeven():
    time.sleep(random.uniform(0.6*60*8, 0.6*60*9))
    print("人员七到...")
    sign_in = threading.Thread(target=SignIn)
    sign_in.start()
    sign_in.join()
    time.sleep(random.uniform(0.03, 0.05))
    check_in = threading.Thread(target=CheckIn)
    check_in.start()
    check_in.join()
    time.sleep(random.uniform(0.6, 0.6*15))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    print("人员七工作ing...")
    time.sleep(random.uniform(60*0.6, 120*0.6))
    random_device = random.randint(0, len(random_device_list)-1)
    t1 = threading.Thread(target=random_device_list[random_device][0], args=(random_device_list[random_device][1], env, 'offline',))
    t1.start()
    time.sleep(random.uniform(60*0.6, 120*0.6))
    meeting = threading.Thread(target=Meeting, args=("MeetingRoomOne",))
    meeting.start()
    meeting.join()

    time.sleep(random.uniform(60*0.6, 120*0.6))
    random_device = random.randint(0, len(random_device_list)-1)
    t2 = threading.Thread(target=random_device_list[random_device][0], args=(random_device_list[random_device][1], env, 'offline',))
    t2.start()
    print("人员七午休ing...")
    time.sleep(random.uniform(5*0.6, 15*0.6))
    if random.randint(0, 1) == 0:
        sign_out = threading.Thread(target=SignOut)
        sign_out.start()
        sign_out.join()
        t = random.uniform(20*0.6, 50*0.6)
        time.sleep(t)
        sign_in = threading.Thread(target=SignIn)
        sign_in.start()
        sign_in.join()
        time.sleep(random.uniform(50*0.6, 60*0.6))
    else:
        time.sleep(random.uniform(90*0.6, 120*0.6))
    t3 = threading.Thread(target=Lab["device_dict"]["Door"].action_off, args=(Lab["device_dict"]["Door"], env, 'offline',))
    t3.start()
    print("人员七继续工作ing...")
    time.sleep(random.uniform(30*0.6, 60*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(0.6, 0.6*15))
    random_device = random.randint(0, len(random_device_list)-1)
    t4 = threading.Thread(target=random_device_list[random_device][0], args=(random_device_list[random_device][1], env, 'offline',))
    t4.start()
    print("人员七继续工作ing...")
    time.sleep(random.uniform(50*0.6, 100*0.6))
    random_device = random.randint(0, len(random_device_list)-1)
    t5 = threading.Thread(target=random_device_list[random_device][0], args=(random_device_list[random_device][1], env, 'offline',))
    t5.start()
    time.sleep(random.uniform(0.6, 0.6*15))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    print("人员七继续工作ing...")
    time.sleep(random.uniform(5*0.6, 15*0.6))
    if random.randint(0, 1) == 0:
        sign_out = threading.Thread(target=SignOut)
        sign_out.start()
        sign_out.join()
        t = random.uniform(20*0.6, 50*0.6)
        time.sleep(t)
        sign_in = threading.Thread(target=SignIn)
        sign_in.start()
        sign_in.join()
        time.sleep(random.uniform(30*0.6, 45*0.6))
    else:
        time.sleep(random.uniform(60*0.6, 90*0.6))
    print("人员七签退...")
    print(datetime.datetime.fromtimestamp(globalFrame.start_time))
    sign_out = threading.Thread(target=SignOut)
    sign_out.start()
    sign_out.join()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()


def personEight():
    pool = []
    time.sleep(random.uniform(0.6*60*8, 0.6*60*8.9))
    print("人员八到...")
    sign_in = threading.Thread(target=SignIn)
    sign_in.start()
    sign_in.join()
    time.sleep(random.uniform(0.03, 0.05))
    check_in = threading.Thread(target=CheckIn)
    check_in.start()
    check_in.join()
    print("人员八工作ing...")
    time.sleep(random.uniform(60*0.6, 90*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(15*0.6, 30*0.6))
    water = threading.Thread(target=CatchWater)
    water.start()
    water.join()
    print("人员八午休ing...")
    time.sleep(random.uniform(90*0.6, 120*0.6))
    random_device = random.randint(0, len(random_device_list)-1)
    t1 = threading.Thread(target=random_device_list[random_device][0], args=(random_device_list[random_device][1], env, 'offline',))
    t1.start()
    print("人员八继续工作ing...")
    time.sleep(random.uniform(40*0.6, 60*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    room = ['MeetingRoomOne', 'MeetingRoomTwo']
    if event_index == 3:
        start_time = random.uniform(40*0.6, 90*0.6)
        random_event = threading.Thread(target=random_event_list[event_index], args=(start_time, room[random.randint(0, 1)],))
        random_event.start()
        pool.append(random_event)
        if random.randint(0, 50) < 40: 
            time.sleep(start_time - 10*0.6)
            meeting = threading.Thread(target=Meeting, args=(room,))
            meeting.start()
            meeting.join()
    else:
        time.sleep(random.uniform(80*0.6, 100*0.6))
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(0.6, 0.6*15))
    random_device = random.randint(0, len(random_device_list)-1)
    t2 = threading.Thread(target=random_device_list[random_device][0], args=(random_device_list[random_device][1], env, 'offline',))
    t2.start()
    print("人员八继续工作ing...")
    time.sleep(random.uniform(5*0.6, 15*0.6))
    if random.randint(0, 1) == 0:
        sign_out = threading.Thread(target=SignOut)
        sign_out.start()
        sign_out.join()
        t = random.uniform(20*0.6, 50*0.6)
        time.sleep(t)
        sign_in = threading.Thread(target=SignIn)
        sign_in.start()
        sign_in.join()
        time.sleep(random.uniform(30*0.6, 40*0.6))
    else:
        time.sleep(random.uniform(50*0.6, 100*0.6))
    restRoom = threading.Thread(target=GoRestRoom)
    restRoom.start()
    restRoom.join()
    time.sleep(random.uniform(10*0.6, 30*0.6))
    random_device = random.randint(0, len(random_device_list)-1)
    t3 = threading.Thread(target=random_device_list[random_device][0], args=(random_device_list[random_device][1], env, 'offline',))
    t3.start()
    time.sleep(random.uniform(0.6, 0.6*15))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    print("人员八继续工作ing...")
    time.sleep(random.uniform(160*0.6, 180*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    print("人员八签退...")
    print(datetime.datetime.fromtimestamp(globalFrame.start_time))
    sign_out = threading.Thread(target=SignOut)
    sign_out.start()
    sign_out.join()

    t1.join()
    t2.join()
    t3.join()
    for item in pool:
        item.join()


def personNine():
    pool = []
    time.sleep(random.uniform(0.6*60*8.5, 0.6*60*9.2))
    print("人员九到...")
    sign_in = threading.Thread(target=SignIn)
    sign_in.start()
    sign_in.join()
    time.sleep(random.uniform(0.03, 0.05))
    check_in = threading.Thread(target=CheckIn)
    check_in.start()
    check_in.join()
    print("人员九工作ing...")
    time.sleep(random.uniform(30*0.6, 60*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(90*0.6, 120*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    room = ['MeetingRoomOne', 'MeetingRoomTwo']
    if event_index == 3:
        start_time = random.uniform(40*0.6, 90*0.6)
        random_event = threading.Thread(target=random_event_list[event_index], args=(start_time, room[random.randint(0, 1)],))
        random_event.start()
        pool.append(random_event)
        if random.randint(0, 50) < 40: 
            time.sleep(start_time - 10*0.6)
            meeting = threading.Thread(target=Meeting, args=(room,))
            meeting.start()
            meeting.join()
    else:
        time.sleep(random.uniform(40*0.6, 90*0.6))
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    print("人员九午休ing...")
    time.sleep(random.uniform(5*0.6, 15*0.6))
    if random.randint(0, 1) == 0:
        sign_out = threading.Thread(target=SignOut)
        sign_out.start()
        sign_out.join()
        t = random.uniform(20*0.6, 50*0.6)
        time.sleep(t)
        sign_in = threading.Thread(target=SignIn)
        sign_in.start()
        sign_in.join()
        time.sleep(random.uniform(60*0.6, 70*0.6))
    else:
        time.sleep(random.uniform(90*0.6, 120*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    print("人员九继续工作ing...")
    time.sleep(random.uniform(30*0.6, 60*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    room = ['MeetingRoomOne', 'MeetingRoomTwo']
    if event_index == 3:
        start_time = random.uniform(40*0.6, 90*0.6)
        random_event = threading.Thread(target=random_event_list[event_index], args=(start_time, room[random.randint(0, 1)],))
        random_event.start()
        pool.append(random_event)
        if random.randint(0, 50) < 40: 
            time.sleep(start_time - 10*0.6)
            meeting = threading.Thread(target=Meeting, args=(room,))
            meeting.start()
            meeting.join()
    else:
        time.sleep(random.uniform(40*0.6, 90*0.6))
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(0.6, 0.6*15))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    print("人员九继续工作ing...")
    time.sleep(random.uniform(70*0.6, 100*0.6))
    random_device = random.randint(0, len(random_device_list)-1)
    t1 = threading.Thread(target=random_device_list[random_device][0], args=(random_device_list[random_device][1], env, 'offline',))
    t1.start()
    print("人员九继续工作ing...")
    time.sleep(random.uniform(60*0.6, 90*0.6))
    print("人员九签退...")
    print(datetime.datetime.fromtimestamp(globalFrame.start_time))
    sign_out = threading.Thread(target=SignOut)
    sign_out.start()
    sign_out.join()

    t1.join()
    for item in pool:
        item.join()


def personTen():
    pool = []
    time.sleep(random.uniform(0.6*60*8.6, 0.6*60*8.9))
    print("人员十到...")
    sign_in = threading.Thread(target=SignIn)
    sign_in.start()
    sign_in.join()
    time.sleep(random.uniform(0.03, 0.05))
    check_in = threading.Thread(target=CheckIn)
    check_in.start()
    check_in.join()
    print("人员十工作ing...")
    time.sleep(random.uniform(60*0.6, 120*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(60*0.6, 120*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    print("人员十午休ing...")
    time.sleep(random.uniform(5*0.6, 15*0.6))
    if random.randint(0, 1) == 0:
        sign_out = threading.Thread(target=SignOut)
        sign_out.start()
        sign_out.join()
        t = random.uniform(20*0.6, 50*0.6)
        time.sleep(t)
        sign_in = threading.Thread(target=SignIn)
        sign_in.start()
        sign_in.join()
        time.sleep(random.uniform(20*0.6, 30*0.6))
    else:
        time.sleep(random.uniform(40*0.6, 90*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    room = ['MeetingRoomOne', 'MeetingRoomTwo']
    if event_index == 3:
        start_time = random.uniform(40*0.6, 90*0.6)
        random_event = threading.Thread(target=random_event_list[event_index], args=(start_time, room[random.randint(0, 1)],))
        random_event.start()
        pool.append(random_event)
        if random.randint(0, 50) < 40: 
            time.sleep(start_time - 10*0.6)
            meeting = threading.Thread(target=Meeting, args=(room,))
            meeting.start()
            meeting.join()
    else:
        time.sleep(random.uniform(40*0.6, 60*0.6))
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    print("人员十继续工作ing...")
    time.sleep(random.uniform(60*0.6, 75*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(0.6, 0.6*15))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    print("人员十继续工作ing...")
    time.sleep(random.uniform(50*0.6, 100*0.6))
    random_device = random.randint(0, len(random_device_list)-1)
    t1 = threading.Thread(target=random_device_list[random_device][0], args=(random_device_list[random_device][1], env, 'offline',))
    t1.start()
    print("人员十继续工作ing...")
    time.sleep(random.uniform(150*0.6, 160*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    print("人员十签退...")
    print(datetime.datetime.fromtimestamp(globalFrame.start_time))
    sign_out = threading.Thread(target=SignOut)
    sign_out.start()
    sign_out.join()

    t1.join()
    for item in pool:
        item.join()


def environmentNormal():
    pool = []
    
    time.sleep(random.uniform(0.6*30, 0.6*60*1))
    if random.randint(0, 1) == 1:
        t0 = threading.Thread(target=Context["env_state"]["Weather"].ext_action_change, args=(Context["env_state"]["Weather"], 'sunny', env, ))
        t0.start()
        pool.append(t0)
    # 01.00-02.00
    time.sleep(random.uniform(0.6*30, 0.6*60*1))
    t1 = threading.Thread(target=Context["env_state"]["Temperature"].ext_action_decrease, args=(Context["env_state"]["Temperature"], env, ))
    t1.start()
    pool.append(t1)
    # 06.00
    time.sleep(random.uniform(0.6*60*5, 0.6*60*5.2))
    t2 = threading.Thread(target=Context["env_state"]["Brightness"].ext_action_increase, args=(Context["env_state"]["Brightness"], env, ))
    t2.start()
    pool.append(t2)

    # 9.30-10.00
    time.sleep(random.uniform(0.6*60*3.5, 0.6*60*4))
    t3 = threading.Thread(target=Context["env_state"]["Brightness"].ext_action_increase, args=(Context["env_state"]["Brightness"], env, ))
    t3.start()
    pool.append(t3)

    # 10.00-10.30
    time.sleep(random.uniform(0.6*60*0.5, 0.6*60*0.6))
    t4 = threading.Thread(target=Context["env_state"]["Humidity"].ext_action_decrease, args=(Context["env_state"]["Humidity"], env, ))
    t4.start()
    pool.append(t4)
    
    time.sleep(random.uniform(0.6*60*0.5, 0.6*60*0.6))
    t1 = threading.Thread(target=Context["env_state"]["Temperature"].ext_action_increase, args=(Context["env_state"]["Temperature"], env, ))
    t1.start()
    pool.append(t1)

    # 13.00-13.30
    time.sleep(random.uniform(0.6*60*2.5, 0.6*60*2.9))
    if random.randint(0, 1) == 1:
        t5 = threading.Thread(target=Context["env_state"]["Weather"].ext_action_change, args=(Context["env_state"]["Weather"], "cloudy", env, ))
        t5.start()
        pool.append(t5)

    # 14.00-14.30
    time.sleep(random.uniform(0.6*60*1, 0.6*60*1.5))
    t6 = threading.Thread(target=Context["env_state"]["Temperature"].ext_action_increase, args=(Context["env_state"]["Temperature"], env, ))
    t6.start()
    pool.append(t6)

    # 17.00
    time.sleep(random.uniform(0.6*60*3, 0.6*60*3.2))
    t7 = threading.Thread(target=Context["env_state"]["Weather"].ext_action_change, args=(Context["env_state"]["Weather"], 'sunny', env, ))
    t7.start()
    pool.append(t7)

    time.sleep(random.uniform(0.6*60*0.5, 0.6*60*0.8))
    t8 = threading.Thread(target=Context["env_state"]["Brightness"].ext_action_decrease, args=(Context["env_state"]["Brightness"], env, ))
    t8.start()
    pool.append(t8)

    # 18.00
    time.sleep(random.uniform(0.6*60*0.5, 0.6*60*1))
    t9 = threading.Thread(target=Context["env_state"]["Humidity"].ext_action_increase, args=(Context["env_state"]["Humidity"], env, ))
    t9.start()
    pool.append(t9)

    time.sleep(random.uniform(0.6*60*0.2, 0.6*60*0.3))
    t10 = threading.Thread(target=Context["env_state"]["Temperature"].ext_action_decrease, args=(Context["env_state"]["Temperature"], env, ))
    t10.start()
    pool.append(t10)

    # 20.00
    time.sleep(random.uniform(0.6*60*2, 0.6*60*3))
    t11 = threading.Thread(target=Context["env_state"]["Temperature"].ext_action_decrease, args=(Context["env_state"]["Temperature"], env, ))
    t11.start()
    pool.append(t11)
    
    time.sleep(random.uniform(0.6*5, 0.6*10))
    if random.randint(0, 1) == 1:
        t12 = threading.Thread(target=Context["env_state"]["Weather"].ext_action_change, args=(Context["env_state"]["Weather"], "cloudy", env, ))
        t12.start()
        pool.append(t12)

    time.sleep(random.uniform(0.6*60*0.2, 0.6*60*0.5))
    t13 = threading.Thread(target=Context["env_state"]["Brightness"].ext_action_decrease, args=(Context["env_state"]["Brightness"], env, ))
    t13.start()
    pool.append(t13)

    for item in pool:
        item.join()


def environmentRaining():
    pool = []
    # 1-1.30
    time.sleep(random.uniform(0.6*60*1, 0.6*60*1.5))
    if random.randint(0, 1) == 1:
        t0 = threading.Thread(target=Context["env_state"]["Weather"].ext_action_change, args=(Context["env_state"]["Weather"], "raining", env, ))
        t0.start()
        pool.append(t0)
        time.sleep(random.uniform(0.6*60*0.2, 0.6*60*0.3))
        t_window = threading.Thread(target=Lab["device_dict"]["Window"].action_on, args=(Lab["device_dict"]["Window"], env, 'offline',))
        t_window.start()
        pool.append(t_window)
    else:
        time.sleep(random.uniform(0.6*60*0.2, 0.6*60*0.3))
    
    # 02.00-02.30
    time.sleep(random.uniform(0.6*60*0.8, 0.6*60*0.9))
    t1 = threading.Thread(target=Context["env_state"]["Weather"].ext_action_change, args=(Context["env_state"]["Weather"], "cloudy", env, ))
    t1.start()
    pool.append(t1)
    
    time.sleep(random.uniform(0.6*60*0.5, 0.6*60*0.6))
    t1 = threading.Thread(target=Context["env_state"]["Temperature"].ext_action_decrease, args=(Context["env_state"]["Temperature"], env, ))
    t1.start()
    pool.append(t1)

    # 04.00-05.00
    time.sleep(random.uniform(0.6*60*1.5, 0.6*60*1.9))
    t2 = threading.Thread(target=Context["env_state"]["Weather"].ext_action_change, args=(Context["env_state"]["Weather"], "sunny", env, ))
    t2.start()
    pool.append(t2)

    # 6.30-7.36
    time.sleep(random.uniform(0.6*60*2.5, 0.6*60*2.6))
    t3 = threading.Thread(target=Context["env_state"]["Brightness"].ext_action_increase, args=(Context["env_state"]["Brightness"], env, ))
    t3.start()
    pool.append(t3)

    # 9.00-10.12
    time.sleep(random.uniform(0.6*60*2.5, 0.6*60*2.6))
    t4 = threading.Thread(target=Context["env_state"]["Brightness"].ext_action_increase, args=(Context["env_state"]["Brightness"], env, ))
    t4.start()
    pool.append(t4)

    # 09.42-11.12
    time.sleep(random.uniform(0.6*60*0.7, 0.6*60*1))
    t5 = threading.Thread(target=Context["env_state"]["Weather"].ext_action_change, args=(Context["env_state"]["Weather"], "cloudy", env, ))
    t5.start()
    pool.append(t5)

    # 10.42-12.18
    time.sleep(random.uniform(0.6*60*1, 0.6*60*1.1))
    t6 = threading.Thread(target=Context["env_state"]["Temperature"].ext_action_increase, args=(Context["env_state"]["Temperature"], env, ))
    t6.start()
    pool.append(t6)

    # 11.42-13.24
    time.sleep(random.uniform(0.6*60*1, 0.6*60*1.1))
    t7 = threading.Thread(target=Context["env_state"]["Weather"].ext_action_change, args=(Context["env_state"]["Weather"], "raining", env, ))
    t7.start()
    pool.append(t7)
    if random.randint(1, 3) == 1:
        time.sleep(random.uniform(0.6*60*0.2, 0.6*60*0.3))
        t_window = threading.Thread(target=Lab["device_dict"]["Window"].action_on, args=(Lab["device_dict"]["Window"], env, 'offline',))
        t_window.start()
        pool.append(t_window)
    else:
        time.sleep(random.uniform(0.6*60*0.2, 0.6*60*0.3))

    # 12.12-14.00
    time.sleep(random.uniform(0.6*60*0.3, 0.6*20))
    t8 = threading.Thread(target=Context["env_state"]["Humidity"].ext_action_decrease, args=(Context["env_state"]["Humidity"], env, ))
    t8.start()
    pool.append(t8)
    
    time.sleep(random.uniform(0.6*60*0.5, 0.6*60*0.6))
    t1 = threading.Thread(target=Context["env_state"]["Temperature"].ext_action_increase, args=(Context["env_state"]["Temperature"], env, ))
    t1.start()
    pool.append(t1)

    # 15.42-17.30
    time.sleep(0.6*60*3)
    t9 = threading.Thread(target=Context["env_state"]["Weather"].ext_action_change, args=(Context["env_state"]["Weather"], "cloudy", env, ))
    t9.start()
    pool.append(t9)

    # 18.00-20.00
    time.sleep(random.uniform(0.6*60*2.3, 0.6*60*2.5))
    t10 = threading.Thread(target=Context["env_state"]["Brightness"].ext_action_decrease, args=(Context["env_state"]["Brightness"], env, ))
    t10.start()
    pool.append(t10)

    # 18.30-20.36
    time.sleep(random.uniform(0.6*60*0.5, 0.6*60*0.6))
    t11 = threading.Thread(target=Context["env_state"]["Temperature"].ext_action_decrease, args=(Context["env_state"]["Temperature"], env, ))
    t11.start()
    pool.append(t11)

    # 19.42-21.48
    time.sleep(0.6*60*1.2)
    t12 = threading.Thread(target=Context["env_state"]["Humidity"].ext_action_increase, args=(Context["env_state"]["Humidity"], env, ))
    t12.start()
    pool.append(t12)
    
    time.sleep(random.uniform(0.6*60*0.5, 0.6*60*0.6))
    t11 = threading.Thread(target=Context["env_state"]["Temperature"].ext_action_decrease, args=(Context["env_state"]["Temperature"], env, ))
    t11.start()
    pool.append(t11)

    # 20.42-22.54
    time.sleep(random.uniform(0.6*60*0.5, 0.6*60*0.6))
    t13 = threading.Thread(target=Context["env_state"]["Brightness"].ext_action_decrease, args=(Context["env_state"]["Brightness"], env, ))
    t13.start()
    pool.append(t13)
    
    
    time.sleep(random.uniform(0.6*10, 0.6*35))
    if random.randint(0, 1) == 1:
        t0 = threading.Thread(target=Context["env_state"]["Weather"].ext_action_change, args=(Context["env_state"]["Weather"], "raining", env, ))
        t0.start()
        pool.append(t0)

    for item in pool:
        item.join()


def weekendPersonOne():
    time.sleep(random.uniform(0.6*60*10, 0.6*60*12))
    print("到...")
    sign_in = threading.Thread(target=SignIn)
    sign_in.start()
    sign_in.join()
    print("工作ing...")
    time.sleep(random.uniform(60*0.6, 90*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(30*0.6, 50*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    print("午休ing...")
    time.sleep(random.uniform(5*0.6, 15*0.6))
    if random.randint(0, 1) == 0:
        sign_out = threading.Thread(target=SignOut)
        sign_out.start()
        sign_out.join()
        t = random.uniform(20*0.6, 50*0.6)
        time.sleep(t)
        sign_in = threading.Thread(target=SignIn)
        sign_in.start()
        sign_in.join()
        time.sleep(random.uniform(20*0.6, 40*0.6))
    else:
        time.sleep(random.uniform(60*0.6, 80*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(0.6*15, 0.6*45))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    print("继续工作ing...")
    time.sleep(random.uniform(50*0.6, 100*0.6))
    random_device = random.randint(0, len(random_device_list)-1)
    t1 = threading.Thread(target=random_device_list[random_device][0], args=(random_device_list[random_device][1], env, 'offline',))
    t1.start()
    print("签退...")
    print(datetime.datetime.fromtimestamp(globalFrame.start_time))
    sign_out = threading.Thread(target=SignOut)
    sign_out.start()
    sign_out.join()

    t1.join()


def weekendPersonTwo():
    time.sleep(random.uniform(0.6*60*10, 0.6*60*14))
    print("到...")
    sign_in = threading.Thread(target=SignIn)
    sign_in.start()
    sign_in.join()
    print("工作ing...")
    time.sleep(random.uniform(60*0.6, 90*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(30*0.6, 50*0.6))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    time.sleep(random.uniform(5*0.6, 15*0.6))
    if random.randint(0, 1) == 0:
        sign_out = threading.Thread(target=SignOut)
        sign_out.start()
        sign_out.join()
        t = random.uniform(20*0.6, 50*0.6)
        time.sleep(t)
        sign_in = threading.Thread(target=SignIn)
        sign_in.start()
        sign_in.join()
        time.sleep(random.uniform(5*0.6, 10*0.6))
    else:
        time.sleep(random.uniform(30*0.6, 50*0.6))
    time.sleep(random.uniform(10*0.6, 15*0.6))
    random_device = random.randint(0, len(random_device_list)-1)
    t1 = threading.Thread(target=random_device_list[random_device][0], args=(random_device_list[random_device][1], env, 'offline',))
    t1.start()
    time.sleep(random.uniform(0.6*15, 0.6*45))
    event_index = random.randint(0, len(random_event_list)-1)
    if event_index != 3:
        random_event = threading.Thread(target=random_event_list[event_index])
        random_event.start()
        random_event.join()
    print("继续工作ing...")
    time.sleep(random.uniform(5*0.6, 15*0.6))
    random_device = random.randint(0, len(random_device_list)-1)
    t2 = threading.Thread(target=random_device_list[random_device][0], args=(random_device_list[random_device][1], env, 'offline',))
    t2.start()
    print("签退...")
    print(datetime.datetime.fromtimestamp(globalFrame.start_time))
    sign_out = threading.Thread(target=SignOut)
    sign_out.start()
    sign_out.join()

    t1.join()
    t2.join()
