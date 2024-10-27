from Characterization.Environment import env
import threading
import time
import random
from util.DataFrame import globalFrame
from DeviceController.DeviceController import *

def SignIn():   
  deviceOn("Corridor", "Door", env, 'offline')
  time.sleep(random.uniform(0.02, 0.04))
  stateIncrease(globalFrame.thread_list,"Corridor", "HumanState", env)
  time.sleep(random.uniform(0.01, 0.02)) 
  deviceOff("Corridor", "Door", env, 'offline')
  time.sleep(random.uniform(0.10, 0.20))
  deviceOn("Lab", "Door", env, 'offline')
  time.sleep(random.uniform(0.02, 0.04))
  stateDecrease(globalFrame.thread_list,"Corridor", "HumanState", env)
  stateIncrease(globalFrame.thread_list,"Lab", "HumanState", env)
  deviceOff("Lab", "Door", env, 'offline')

def SignOut():
  deviceOn("Lab", "Door", env, 'offline') 
  time.sleep(random.uniform(0.02, 0.04))
  stateDecrease(globalFrame.thread_list,"Lab", "HumanState", env)
  stateIncrease(globalFrame.thread_list,"Corridor", "HumanState", env)
  deviceOff("Lab", "Door", env, 'offline')
  print("签退 Lab -> Corridor, sleep 10-20s...")
  time.sleep(random.uniform(0.10, 0.20))
  deviceOn("Corridor", "Door", env, 'offline')
  time.sleep(random.uniform(0.02, 0.04))
  stateDecrease(globalFrame.thread_list,"Corridor", "HumanState", env)
  time.sleep(random.uniform(0.01, 0.02))
  deviceOff("Corridor", "Door", env, 'offline')

def CatchWater():
  deviceOn("Lab", "Door", env, 'offline') 
  time.sleep(random.uniform(0.02, 0.04))
  stateDecrease(globalFrame.thread_list,"Lab", "HumanState", env)
  stateIncrease(globalFrame.thread_list,"Corridor", "HumanState", env)
  deviceOff("Lab", "Door", env, 'offline') 
  time.sleep(random.uniform(0.10, 0.30))
  deviceOn("TeaRoom", "Door", env, 'offline') 
  time.sleep(random.uniform(0.02, 0.04))
  stateDecrease(globalFrame.thread_list,"Corridor", "HumanState", env)
  stateIncrease(globalFrame.thread_list,"TeaRoom", "HumanState", env)
  deviceOff("TeaRoom", "Door", env, 'offline') 
  time.sleep(random.uniform(0.05, 0.10))
  deviceOn("TeaRoom", "WaterDispenser", env, 'offline') 
  print("接水, sleep 30-210s...")
  if random.randint(1, 3) == 2:
    time.sleep(random.uniform(0.02, 0.04))
    deviceOn("TeaRoom", "Door", env, 'offline') 
    time.sleep(random.uniform(0.02, 0.04))
    stateDecrease(globalFrame.thread_list,"TeaRoom", "HumanState", env)
    stateIncrease(globalFrame.thread_list,"Corridor", "HumanState", env)
    deviceOff("TeaRoom", "Door", env, 'offline') 
    time.sleep(random.uniform(0.4, 1.8))
    deviceOn("TeaRoom", "Door", env, 'offline') 
    time.sleep(random.uniform(0.01, 0.03))
    stateDecrease(globalFrame.thread_list,"Corridor", "HumanState", env)
    stateIncrease(globalFrame.thread_list,"TeaRoom", "HumanState", env)
    deviceOff("TeaRoom", "Door", env, 'offline') 
    time.sleep(random.uniform(0.5, 0.6 * 2))
  else:      
    time.sleep(random.uniform(0.8, 0.6 * 3))
  deviceOff("TeaRoom", "WaterDispenser", env, 'offline') 
  time.sleep(random.uniform(0.05, 0.10))
  deviceOn("TeaRoom", "Door", env, 'offline') 
  time.sleep(random.uniform(0.02, 0.04))
  stateDecrease(globalFrame.thread_list,"TeaRoom", "HumanState", env)
  stateIncrease(globalFrame.thread_list,"Corridor", "HumanState", env)
  deviceOff("TeaRoom", "Door", env, 'offline') 
  time.sleep(random.uniform(0.10, 0.30))
  deviceOn("Lab", "Door", env, 'offline') 
  time.sleep(random.uniform(0.02, 0.04))
  stateDecrease(globalFrame.thread_list,"Corridor", "HumanState", env)
  stateIncrease(globalFrame.thread_list,"Lab", "HumanState", env)
  deviceOff("Lab", "Door", env, 'offline') 

def Meeting(room):
  if room == "MeetingRoomOne":
    # go to meetingroom one
    deviceOn("Lab", "Door", env, 'offline') 
    time.sleep(random.uniform(0.02, 0.04))
    stateDecrease(globalFrame.thread_list,"Lab", "HumanState", env)
    stateIncrease(globalFrame.thread_list,"Corridor", "HumanState", env)
    deviceOff("Lab", "Door", env, 'offline') 
    time.sleep(random.uniform(0.20, 0.40))
    deviceOn("TeaRoom", "Door", env, 'offline') 
    time.sleep(random.uniform(0.02, 0.04))
    stateDecrease(globalFrame.thread_list,"Corridor", "HumanState", env)
    stateIncrease(globalFrame.thread_list,"TeaRoom", "HumanState", env)
    deviceOff("TeaRoom", "Door", env, 'offline') 
    time.sleep(random.uniform(0.05, 0.10))
    deviceOn("MeetingRoomOne", "Door", env, 'offline') 
    time.sleep(random.uniform(0.02, 0.04))
    stateDecrease(globalFrame.thread_list,"TeaRoom", "HumanState", env)
    stateIncrease(globalFrame.thread_list,"MeetingRoomOne", "HumanState", env)
    deviceOff("MeetingRoomOne", "Door", env, 'offline') 
    if random.randint(0, 1) == 1: 
      deviceOn("MeetingRoomOne", "TV", env, 'offline') 
    if random.randint(0, 1) == 1: 
      deviceOn("MeetingRoomOne", "Heater", env, 'offline') 
    if random.randint(0, 1) == 1: 
      deviceOn("MeetingRoomOne", "Curtain", env, 'offline') 
    if random.randint(0, 1) == 1: 
      deviceOn("MeetingRoomOne", "AirPurifier", env, 'offline') 
    if random.randint(0, 1) == 1: 
      deviceOn("MeetingRoomOne", "Humidifier", env, 'offline') 
    deviceOn("MeetingRoomOne", "Light", env, 'offline') 
    print("开会, sleep 600-3600s...")
    time.sleep(random.uniform(15*0.6, 90*0.6))
    if random.randint(1, 100) < 95: 
      deviceOff("MeetingRoomOne", "TV", env, 'offline') 
    if random.randint(1, 100) < 95: 
      deviceOff("MeetingRoomOne", "Heater", env, 'offline') 
    if random.randint(1, 100) < 95: 
      deviceOff("MeetingRoomOne", "Curtain", env, 'offline') 
    if random.randint(1, 100) < 95: 
      deviceOff("MeetingRoomOne", "AirPurifier", env, 'offline') 
    if random.randint(1, 100) < 45: 
      deviceOff("MeetingRoomOne", "Humidifier", env, 'offline') 
    if random.randint(1, 100) < 40: 
      deviceOff("MeetingRoomOne", "Light", env, 'offline') 
    deviceOn("MeetingRoomOne", "Door", env, 'offline') 
    time.sleep(random.uniform(0.02, 0.04))
    stateDecrease(globalFrame.thread_list,"MeetingRoomOne", "HumanState", env)
    stateIncrease(globalFrame.thread_list,"TeaRoom", "HumanState", env)
    deviceOff("MeetingRoomOne", "Door", env, 'offline') 
    time.sleep(random.uniform(0.05, 0.10))
    deviceOn("TeaRoom", "Door", env, 'offline') 
    time.sleep(random.uniform(0.02, 0.04))
    stateDecrease(globalFrame.thread_list,"TeaRoom", "HumanState", env)
    stateIncrease(globalFrame.thread_list,"Corridor", "HumanState", env)
    deviceOff("TeaRoom", "Door", env, 'offline') 
    time.sleep(random.uniform(0.20, 0.40))
    deviceOn("Lab", "Door", env, 'offline') 
    time.sleep(random.uniform(0.02, 0.04))
    stateDecrease(globalFrame.thread_list,"Corridor", "HumanState", env)
    stateIncrease(globalFrame.thread_list,"Lab", "HumanState", env)
    deviceOff("Lab", "Door", env, 'offline') 	
  elif room == "MeetingRoomTwo":
    # go to meetingroom two
    deviceOn("Lab", "Door", env, 'offline') 
    time.sleep(random.uniform(0.02, 0.04))
    stateDecrease(globalFrame.thread_list,"Lab", "HumanState", env)
    stateIncrease(globalFrame.thread_list,"Corridor", "HumanState", env)
    deviceOff("Lab", "Door", env, 'offline') 
    time.sleep(random.uniform(0.20, 0.40))
    deviceOn("MeetingRoomTwo", "Door", env, 'offline') 
    time.sleep(random.uniform(0.02, 0.04))
    if random.randint(0, 100) < 60: 
      deviceOn("MeetingRoomTwo", "Light", env, 'offline') 
    stateDecrease(globalFrame.thread_list,"Corridor", "HumanState", env)
    stateIncrease(globalFrame.thread_list,"MeetingRoomTwo", "HumanState", env)
    deviceOff("MeetingRoomTwo", "Door", env, 'offline') 
    if random.randint(0, 1) == 1: 
      deviceOn("MeetingRoomTwo", "TV", env, 'offline') 
    if random.randint(0, 1) == 1: 
      deviceOn("MeetingRoomTwo", "AC", env, 'offline') 
    if random.randint(0, 1) == 1: 
      deviceOn("MeetingRoomTwo", "Curtain", env, 'offline') 
    if random.randint(0, 1) == 1: 
      deviceOn("MeetingRoomTwo", "AirPurifier", env, 'offline') 
    if random.randint(0, 100) < 70: 
      deviceOn("MeetingRoomTwo", "Humidifier", env, 'offline') 
    print("开会, sleep 600-3600s...")
    time.sleep(random.uniform(10*0.6, 60*0.6))
    if random.randint(1, 100) < 95: 
      deviceOff("MeetingRoomTwo", "TV", env, 'offline') 
    if random.randint(1, 100) < 95: 
      deviceOff("MeetingRoomTwo", "AC", env, 'offline') 
    if random.randint(1, 100) < 95: 
      deviceOff("MeetingRoomTwo", "Curtain", env, 'offline') 
    if random.randint(1, 100) < 95: 
      deviceOff("MeetingRoomTwo", "AirPurifier", env, 'offline') 
    if random.randint(1, 100) < 40: 
      deviceOff("MeetingRoomTwo", "Humidifier", env, 'offline') 
    if random.randint(1, 100) < 35: 
      deviceOff("MeetingRoomTwo", "Light", env, 'offline') 
    deviceOn("MeetingRoomTwo", "Door", env, 'offline') 
    time.sleep(random.uniform(0.02, 0.04))
    stateDecrease(globalFrame.thread_list,"MeetingRoomTwo", "HumanState", env)
    stateIncrease(globalFrame.thread_list,"Corridor", "HumanState", env)
    deviceOff("MeetingRoomTwo", "Door", env, 'offline') 		
    time.sleep(random.uniform(0.20, 0.40))
    deviceOn("Lab", "Door", env, 'offline') 
    time.sleep(random.uniform(0.02, 0.04))
    stateDecrease(globalFrame.thread_list,"Corridor", "HumanState", env)
    stateIncrease(globalFrame.thread_list,"Lab", "HumanState", env)
    deviceOff("Lab", "Door", env, 'offline')

def GoRestRoom():
  deviceOn("Lab", "Door", env, 'offline') 
  time.sleep(random.uniform(0.02, 0.04))
  stateDecrease(globalFrame.thread_list,"Lab", "HumanState", env)
  stateIncrease(globalFrame.thread_list,"Corridor", "HumanState", env)
  deviceOff("Lab", "Door", env, 'offline') 
  time.sleep(random.uniform(0.20, 0.40))
  stateDecrease(globalFrame.thread_list,"Corridor", "HumanState", env)
  print("上厕所, sleep 180-600s...")
  time.sleep(random.uniform(1.8, 10*0.6))
  stateIncrease(globalFrame.thread_list,"Corridor", "HumanState", env)
  time.sleep(random.uniform(0.20, 0.40))
  deviceOn("Lab", "Door", env, 'offline') 
  time.sleep(random.uniform(0.02, 0.04))
  stateDecrease(globalFrame.thread_list,"Corridor", "HumanState", env)
  stateIncrease(globalFrame.thread_list,"Lab", "HumanState", env)
  deviceOff("Lab", "Door", env, 'offline') 

def HaveLunch():
  deviceOn("Lab", "Door", env, 'offline') 
  time.sleep(random.uniform(0.02, 0.04))
  stateDecrease(globalFrame.thread_list,"Lab", "HumanState", env)
  stateIncrease(globalFrame.thread_list,"Corridor", "HumanState", env)
  deviceOff("Lab", "Door", env, 'offline') 
  ("Lab -> TeaRoom, sleep 20-40s...")
  time.sleep(random.uniform(0.20, 0.40))
  deviceOn("TeaRoom", "Door", env, 'offline') 
  time.sleep(random.uniform(0.02, 0.04))
  stateDecrease(globalFrame.thread_list,"Corridor", "HumanState", env)
  stateIncrease(globalFrame.thread_list,"TeaRoom", "HumanState", env)
  deviceOff("TeaRoom", "Door", env, 'offline') 
  if random.randint(0, 1) == 1: 
    deviceOn("TeaRoom", "Curtain", env, 'offline') 
  if random.randint(0, 1) == 1: 
    deviceOn("TeaRoom", "Window", env, 'offline') 
  if random.randint(0, 1) == 1: 
    deviceOn("TeaRoom", "AirPurifier", env, 'offline') 
  if random.randint(0, 1) == 1: 
    deviceOn("TeaRoom", "Humidifier", env, 'offline') 
  deviceOn("TeaRoom", "Light", env, 'offline') 
  deviceOn("TeaRoom", "MicrowaveOven", env, 'offline') 
  print("吃饭, sleep 600-1200s...")
  if random.randint(1, 100) < 70: 
    deviceOff("TeaRoom", "Light", env, 'offline') 
  if random.randint(1, 100) < 80: 
    deviceOff("TeaRoom", "Window", env, 'offline') 
  if random.randint(1, 100) < 95: 
    deviceOff("TeaRoom", "Curtain", env, 'offline') 
  if random.randint(1, 100) < 95: 
    deviceOff("TeaRoom", "AirPurifier", env, 'offline') 
  if random.randint(1, 100) < 60: 
    deviceOff("TeaRoom", "Humidifier", env, 'offline') 
  time.sleep(random.uniform(10*0.6, 20*0.6))
  deviceOn("TeaRoom", "Door", env, 'offline') 
  time.sleep(random.uniform(0.02, 0.04))
  stateDecrease(globalFrame.thread_list,"TeaRoom", "HumanState", env)
  stateIncrease(globalFrame.thread_list,"Corridor", "HumanState", env)
  deviceOff("TeaRoom", "Door", env, 'offline') 
  time.sleep(random.uniform(0.20, 0.40))
  deviceOn("Lab", "Door", env, 'offline') 
  time.sleep(random.uniform(0.02, 0.04))
  stateDecrease(globalFrame.thread_list,"Corridor", "HumanState", env)
  stateIncrease(globalFrame.thread_list,"Lab", "HumanState", env)
  deviceOff("Lab", "Door", env, 'offline') 

def CheckIn():
  print("签到 Corridor -> Lab, sleep 10-20s...")
  t1 = threading.Thread(target=deviceOn, args=("Corridor", "Speaker", env, 'app',))
  t1.start()
  time.sleep(random.uniform(0.10, 0.20))
  t2 = threading.Thread(target=deviceOn, args=("Lab", "Printer", env, 'app',))
  t2.start()

  t1.join()
  t2.join()

def Reservation(start_time, room):
  time.sleep(start_time - 20*0.6)
  t1 = threading.Thread(target=deviceOn, args=(room, "AirPurifier", env, 'app',))
  t1.start()
  time.sleep(random.uniform(0.5, 0.10))
  t2 = threading.Thread(target=deviceOn, args=(room, "AC", env, 'app',))
  t2.start()

  time.sleep(start_time - 10*0.6)
  t3 = threading.Thread(target=deviceOn, args=("Lab", "Printer", env, 'app',))
  t3.start()
  time.sleep(random.uniform(0.5, 0.10))
  t4 = threading.Thread(target=deviceOn, args=(room, "Curtain", env, 'app',))
  t4.start()
  
  t1.join()
  t2.join()
  t3.join()
  t4.join()

 