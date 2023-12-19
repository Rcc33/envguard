from Characterization.Environment import env
import threading
import time
import random
from util.DataFrame import globalFrame
from DeviceController.DeviceController import *

def SignIn():   
  deviceOn("Corridor", "Door", env, 'User Activity')
  time.sleep(random.uniform(0.02, 0.04))
  stateIncrease(globalFrame.thread_list,"Corridor", "HumanState", env)
  time.sleep(random.uniform(0.01, 0.02)) 
  deviceOff("Corridor", "Door", env, 'User Activity')
  time.sleep(random.uniform(0.10, 0.20))
  deviceOn("Lab", "Door", env, 'User Activity')
  time.sleep(random.uniform(0.02, 0.04))
  stateDecrease(globalFrame.thread_list,"Corridor", "HumanState", env)
  stateIncrease(globalFrame.thread_list,"Lab", "HumanState", env)
  deviceOff("Lab", "Door", env, 'User Activity')

def SignOut():
	deviceOn("Lab", "Door", env, 'User Activity') 
	time.sleep(random.uniform(0.02, 0.04))
	stateDecrease(globalFrame.thread_list,"Lab", "HumanState", env)
	stateIncrease(globalFrame.thread_list,"Corridor", "HumanState", env)
	deviceOff("Lab", "Door", env, 'User Activity')
	print("签退 Lab -> Corridor, sleep 10-20s...")
	time.sleep(random.uniform(0.10, 0.20))
	deviceOn("Corridor", "Door", env, 'User Activity')
	time.sleep(random.uniform(0.02, 0.04))
	stateDecrease(globalFrame.thread_list,"Corridor", "HumanState", env)
	time.sleep(random.uniform(0.01, 0.02))
	deviceOff("Corridor", "Door", env, 'User Activity')

def CatchWater():
	deviceOn("Lab", "Door", env, 'User Activity') 
	time.sleep(random.uniform(0.02, 0.04))
	stateDecrease(globalFrame.thread_list,"Lab", "HumanState", env)
	stateIncrease(globalFrame.thread_list,"Corridor", "HumanState", env)
	deviceOff("Lab", "Door", env, 'User Activity') 
	print("Lab -> TeaRoom, sleep 10-30s...")
	time.sleep(random.uniform(0.10, 0.30))
	deviceOn("TeaRoom", "Door", env, 'User Activity') 
	time.sleep(random.uniform(0.02, 0.04))
	stateDecrease(globalFrame.thread_list,"Corridor", "HumanState", env)
	stateIncrease(globalFrame.thread_list,"TeaRoom", "HumanState", env)
	deviceOff("TeaRoom", "Door", env, 'User Activity') 
	print("TeaRoom -> WaterDispenser, sleep 5-10s...")
	time.sleep(random.uniform(0.05, 0.10))
	deviceOn("TeaRoom", "WaterDispenser", env, 'User Activity') 
	print("接水, sleep 20-60s...")
	if random.randint(1, 7) == 1:
		time.sleep(random.uniform(0.08, 0.60))
		deviceOn("TeaRoom", "Door", env, 'User Activity') 
		time.sleep(random.uniform(0.02, 0.04))
		stateDecrease(globalFrame.thread_list,"TeaRoom", "HumanState", env)
		stateIncrease(globalFrame.thread_list,"Corridor", "HumanState", env)
		deviceOff("TeaRoom", "Door", env, 'User Activity') 
		time.sleep(random.uniform(0.02, 0.04))
		deviceOn("TeaRoom", "Door", env, 'User Activity') 
		time.sleep(random.uniform(0.01, 0.03))
		stateDecrease(globalFrame.thread_list,"Corridor", "HumanState", env)
		stateIncrease(globalFrame.thread_list,"TeaRoom", "HumanState", env)
		deviceOff("TeaRoom", "Door", env, 'User Activity') 
		time.sleep(random.uniform(0.07, 1.09))
	else:      
		time.sleep(random.uniform(0.20, 0.60*3))
	deviceOff("TeaRoom", "WaterDispenser", env, 'User Activity') 
	print("WaterDispenser -> TeaRoom, sleep 5-10s...")
	time.sleep(random.uniform(0.05, 0.10))
	deviceOn("TeaRoom", "Door", env, 'User Activity') 
	time.sleep(random.uniform(0.02, 0.04))
	stateDecrease(globalFrame.thread_list,"TeaRoom", "HumanState", env)
	stateIncrease(globalFrame.thread_list,"Corridor", "HumanState", env)
	deviceOff("TeaRoom", "Door", env, 'User Activity') 
	print("TeaRoom -> Lab, sleep 10-30s...")
	time.sleep(random.uniform(0.10, 0.30))
	deviceOn("Lab", "Door", env, 'User Activity') 
	time.sleep(random.uniform(0.02, 0.04))
	stateDecrease(globalFrame.thread_list,"Corridor", "HumanState", env)
	stateIncrease(globalFrame.thread_list,"Lab", "HumanState", env)
	deviceOff("Lab", "Door", env, 'User Activity') 

def Meeting(room):
	if room == "MeetingRoomOne":
		# go to meetingroom one
		deviceOn("Lab", "Door", env, 'User Activity') 
		time.sleep(random.uniform(0.02, 0.04))
		stateDecrease(globalFrame.thread_list,"Lab", "HumanState", env)
		stateIncrease(globalFrame.thread_list,"Corridor", "HumanState", env)
		deviceOff("Lab", "Door", env, 'User Activity') 
		print("Lab -> TeaRoom, sleep 20-40s...")
		time.sleep(random.uniform(0.20, 0.40))
		deviceOn("TeaRoom", "Door", env, 'User Activity') 
		time.sleep(random.uniform(0.02, 0.04))
		stateDecrease(globalFrame.thread_list,"Corridor", "HumanState", env)
		stateIncrease(globalFrame.thread_list,"TeaRoom", "HumanState", env)
		deviceOff("TeaRoom", "Door", env, 'User Activity') 
		print("TeaRoom -> MeetingRoomOne, sleep 5-10s...")
		time.sleep(random.uniform(0.05, 0.10))
		deviceOn("MeetingRoomOne", "Door", env, 'User Activity') 
		time.sleep(random.uniform(0.02, 0.04))
		stateDecrease(globalFrame.thread_list,"TeaRoom", "HumanState", env)
		stateIncrease(globalFrame.thread_list,"MeetingRoomOne", "HumanState", env)
		deviceOff("MeetingRoomOne", "Door", env, 'User Activity') 
		if random.randint(0, 1) == 1: 
			deviceOn("MeetingRoomOne", "TV", env, 'User Activity') 
		if random.randint(0, 1) == 1: 
			deviceOn("MeetingRoomOne", "AC", env, 'User Activity') 
		if random.randint(0, 1) == 1: 
			deviceOn("MeetingRoomOne", "Curtain", env, 'User Activity') 
		if random.randint(0, 1) == 1: 
			deviceOn("MeetingRoomOne", "AirPurifier", env, 'User Activity') 
		# if random.randint(0, 1) == 1: 
		#     MeetingRoomOne["device_dict"]["Humidifier"].action_on(MeetingRoomOne["device_dict"]["Humidifier"], env,  'User Activity')
		deviceOn("MeetingRoomOne", "Light", env, 'User Activity') 
		print("开会, sleep 600-3600s...")
		time.sleep(random.uniform(15*0.6, 90*0.6))
		if random.randint(1, 100) < 95: 
			deviceOff("MeetingRoomOne", "TV", env, 'User Activity') 
		if random.randint(1, 100) < 95: 
			deviceOff("MeetingRoomOne", "AC", env, 'User Activity') 
		if random.randint(1, 100) < 95: 
			deviceOff("MeetingRoomOne", "Curtain", env, 'User Activity') 
		if random.randint(1, 100) < 95: 
			deviceOff("MeetingRoomOne", "AirPurifier", env, 'User Activity') 
		if random.randint(1, 100) < 50: 
			deviceOff("MeetingRoomOne", "Humidifier", env, 'User Activity') 
		if random.randint(1, 100) < 20: 
			deviceOff("MeetingRoomOne", "Light", env, 'User Activity') 
		deviceOn("MeetingRoomOne", "Door", env, 'User Activity') 
		time.sleep(random.uniform(0.02, 0.04))
		stateDecrease(globalFrame.thread_list,"MeetingRoomOne", "HumanState", env)
		stateIncrease(globalFrame.thread_list,"TeaRoom", "HumanState", env)
		deviceOff("MeetingRoomOne", "Door", env, 'User Activity') 
		print("MeetingRoomOne -> TeaRoom, sleep 5-10s...")
		time.sleep(random.uniform(0.05, 0.10))
		deviceOn("TeaRoom", "Door", env, 'User Activity') 
		time.sleep(random.uniform(0.02, 0.04))
		stateDecrease(globalFrame.thread_list,"TeaRoom", "HumanState", env)
		stateIncrease(globalFrame.thread_list,"Corridor", "HumanState", env)
		deviceOff("TeaRoom", "Door", env, 'User Activity') 
		print("TeaRoom -> Lab, sleep 20-40s...")
		time.sleep(random.uniform(0.20, 0.40))
		deviceOn("Lab", "Door", env, 'User Activity') 
		time.sleep(random.uniform(0.02, 0.04))
		stateDecrease(globalFrame.thread_list,"Corridor", "HumanState", env)
		stateIncrease(globalFrame.thread_list,"Lab", "HumanState", env)
		deviceOff("Lab", "Door", env, 'User Activity') 	
	elif room == "MeetingRoomTwo":
		# go to meetingroom two
		deviceOn("Lab", "Door", env, 'User Activity') 
		time.sleep(random.uniform(0.02, 0.04))
		stateDecrease(globalFrame.thread_list,"Lab", "HumanState", env)
		stateIncrease(globalFrame.thread_list,"Corridor", "HumanState", env)
		deviceOff("Lab", "Door", env, 'User Activity') 
		print("Lab -> MeetingRoomTwo, sleep 20-40s...")
		time.sleep(random.uniform(0.20, 0.40))
		deviceOn("MeetingRoomTwo", "Door", env, 'User Activity') 
		time.sleep(random.uniform(0.02, 0.04))
		stateDecrease(globalFrame.thread_list,"Corridor", "HumanState", env)
		stateIncrease(globalFrame.thread_list,"MeetingRoomTwo", "HumanState", env)
		deviceOff("MeetingRoomTwo", "Door", env, 'User Activity') 
		if random.randint(0, 1) == 1: 
			deviceOn("MeetingRoomTwo", "TV", env, 'User Activity') 
		if random.randint(0, 1) == 1: 
			deviceOn("MeetingRoomTwo", "AC", env, 'User Activity') 
		if random.randint(0, 1) == 1: 
			deviceOn("MeetingRoomTwo", "Curtain", env, 'User Activity') 
		if random.randint(0, 1) == 1: 
			deviceOn("MeetingRoomTwo", "AirPurifier", env, 'User Activity') 
		# if random.randint(0, 1) == 1: 
		#     MeetingRoomTwo["device_dict"]["Humidifier"].action_on(MeetingRoomTwo["device_dict"]["Humidifier"], env,  'User Activity')
		deviceOn("MeetingRoomTwo", "Light", env, 'User Activity') 
		print("开会, sleep 600-3600s...")
		time.sleep(random.uniform(10*0.6, 60*0.6))
		if random.randint(1, 100) < 95: 
			deviceOff("MeetingRoomTwo", "TV", env, 'User Activity') 
		if random.randint(1, 100) < 95: 
			deviceOff("MeetingRoomTwo", "AC", env, 'User Activity') 
		if random.randint(1, 100) < 95: 
			deviceOff("MeetingRoomTwo", "Curtain", env, 'User Activity') 
		if random.randint(1, 100) < 95: 
			deviceOff("MeetingRoomTwo", "AirPurifier", env, 'User Activity') 
		if random.randint(1, 100) < 50: 
			deviceOff("MeetingRoomTwo", "Humidifier", env, 'User Activity') 
		if random.randint(1, 100) < 20: 
			deviceOff("MeetingRoomTwo", "Light", env, 'User Activity') 
		deviceOn("MeetingRoomTwo", "Door", env, 'User Activity') 
		time.sleep(random.uniform(0.02, 0.04))
		stateDecrease(globalFrame.thread_list,"MeetingRoomTwo", "HumanState", env)
		stateIncrease(globalFrame.thread_list,"Corridor", "HumanState", env)
		deviceOff("MeetingRoomTwo", "Door", env, 'User Activity') 		
		print("MeetingRoomTwo -> Lab, sleep 20-40s...")
		time.sleep(random.uniform(0.20, 0.40))
		deviceOn("Lab", "Door", env, 'User Activity') 
		time.sleep(random.uniform(0.02, 0.04))
		stateDecrease(globalFrame.thread_list,"Corridor", "HumanState", env)
		stateIncrease(globalFrame.thread_list,"Lab", "HumanState", env)
		deviceOff("Lab", "Door", env, 'User Activity')

def GoRestRoom():
	deviceOn("Lab", "Door", env, 'User Activity') 
	time.sleep(random.uniform(0.02, 0.04))
	stateDecrease(globalFrame.thread_list,"Lab", "HumanState", env)
	stateIncrease(globalFrame.thread_list,"Corridor", "HumanState", env)
	deviceOff("Lab", "Door", env, 'User Activity') 
	print("Lab -> Corridor, sleep 20-40s...")
	time.sleep(random.uniform(0.20, 0.40))
	stateDecrease(globalFrame.thread_list,"Corridor", "HumanState", env)
	print("上厕所, sleep 180-600s...")
	time.sleep(random.uniform(1.8, 10*0.6))
	stateIncrease(globalFrame.thread_list,"Corridor", "HumanState", env)
	print("Corridor -> Lab, sleep 20-40s...")
	time.sleep(random.uniform(0.20, 0.40))
	deviceOn("Lab", "Door", env, 'User Activity') 
	time.sleep(random.uniform(0.02, 0.04))
	stateDecrease(globalFrame.thread_list,"Corridor", "HumanState", env)
	stateIncrease(globalFrame.thread_list,"Lab", "HumanState", env)
	deviceOff("Lab", "Door", env, 'User Activity') 

def HaveLunch():
	deviceOn("Lab", "Door", env, 'User Activity') 
	time.sleep(random.uniform(0.02, 0.04))
	stateDecrease(globalFrame.thread_list,"Lab", "HumanState", env)
	stateIncrease(globalFrame.thread_list,"Corridor", "HumanState", env)
	deviceOff("Lab", "Door", env, 'User Activity') 
	print("Lab -> TeaRoom, sleep 20-40s...")
	time.sleep(random.uniform(0.20, 0.40))
	deviceOn("TeaRoom", "Door", env, 'User Activity') 
	time.sleep(random.uniform(0.02, 0.04))
	stateDecrease(globalFrame.thread_list,"Corridor", "HumanState", env)
	stateIncrease(globalFrame.thread_list,"TeaRoom", "HumanState", env)
	deviceOff("TeaRoom", "Door", env, 'User Activity') 
	if random.randint(0, 1) == 1: 
		deviceOn("TeaRoom", "Curtain", env, 'User Activity') 
	if random.randint(0, 1) == 1: 
		deviceOn("TeaRoom", "Window", env, 'User Activity') 
	if random.randint(0, 1) == 1: 
		deviceOn("TeaRoom", "AirPurifier", env, 'User Activity') 
	if random.randint(0, 1) == 1: 
		deviceOn("TeaRoom", "Humidifier", env, 'User Activity') 
	deviceOn("TeaRoom", "Light", env, 'User Activity') 
	deviceOn("TeaRoom", "MicrowaveOven", env, 'User Activity') 
	print("吃饭, sleep 600-1200s...")
	if random.randint(1, 100) < 70: 
		deviceOff("TeaRoom", "Light", env, 'User Activity') 
	if random.randint(1, 100) < 80: 
		deviceOff("TeaRoom", "Window", env, 'User Activity') 
	if random.randint(1, 100) < 95: 
		deviceOff("TeaRoom", "Curtain", env, 'User Activity') 
	if random.randint(1, 100) < 95: 
		deviceOff("TeaRoom", "AirPurifier", env, 'User Activity') 
	if random.randint(1, 100) < 95: 
		deviceOff("TeaRoom", "Humidifier", env, 'User Activity') 
	time.sleep(random.uniform(10*0.6, 20*0.6))
	deviceOn("TeaRoom", "Door", env, 'User Activity') 
	time.sleep(random.uniform(0.02, 0.04))
	stateDecrease(globalFrame.thread_list,"TeaRoom", "HumanState", env)
	stateIncrease(globalFrame.thread_list,"Corridor", "HumanState", env)
	deviceOff("TeaRoom", "Door", env, 'User Activity') 
	print("TeaRoom -> Lab, sleep 20-40s...")
	time.sleep(random.uniform(0.20, 0.40))
	deviceOn("Lab", "Door", env, 'User Activity') 
	time.sleep(random.uniform(0.02, 0.04))
	stateDecrease(globalFrame.thread_list,"Corridor", "HumanState", env)
	stateIncrease(globalFrame.thread_list,"Lab", "HumanState", env)
	deviceOff("Lab", "Door", env, 'User Activity') 

def CheckIn():
	print("签到 Corridor -> Lab, sleep 10-20s...")
	t1 = threading.Thread(target=deviceOn, args=("Corridor", "Speaker", env, 'Application',))
	t1.start()
	time.sleep(random.uniform(0.10, 0.20))
	t2 = threading.Thread(target=deviceOn, args=("Lab", "Printer", env, 'Application',))
	t2.start()

	t1.join()
	t2.join()

def Reservation(start_time, room):
	time.sleep(start_time - 20*0.6)
	t1 = threading.Thread(target=deviceOn, args=(room, "AirPurifier", env, 'Application',))
	t1.start()
	time.sleep(random.uniform(0.5, 0.10))
	t2 = threading.Thread(target=deviceOn, args=(room, "AC", env, 'Application',))
	t2.start()

	time.sleep(start_time - 10*0.6)
	t3 = threading.Thread(target=deviceOn, args=("Lab", "Printer", env, 'Application',))
	t3.start()
	time.sleep(random.uniform(0.5, 0.10))
	t4 = threading.Thread(target=deviceOn, args=(room, "Curtain", env, 'Application',))
	t4.start()
	
	t1.join()
	t2.join()
	t3.join()
	t4.join()

 