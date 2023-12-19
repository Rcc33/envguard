from DeviceController.DeviceController import *
from Characterization.Environment import env
import threading
import time
import random
from util.DataFrame import globalFrame

# 30min
def Washing():
  pool = []
  t3 = threading.Thread(target=deviceOn, args=("Bathroom", "Door", env, 'User Activity',))
  t3.start()
  pool.append(t3)
  time.sleep(random.uniform(0.03, 0.05))
  stateDecrease(globalFrame.thread_list,"LivingRoom", "HumanState", env)
  stateIncrease(globalFrame.thread_list,"Bathroom", "HumanState", env)
  time.sleep(random.uniform(0.03, 0.05))
  t4 = threading.Thread(target=deviceOff, args=("Bathroom", "Door", env, 'User Activity',))
  t4.start()  
  pool.append(t4)
  time.sleep(random.uniform(0.03, 0.05))
  t5 = threading.Thread(target=deviceOn, args=("Bathroom", "Light", env, 'User Activity',))
  t5.start()
  pool.append(t5)
  time.sleep(random.uniform(0.6*10, 0.6*13))
  if(random.randint(0, 5) == 1): 
    t = threading.Thread(target=deviceOn, args=("Bathroom", "WaterHeater", env, 'User Activity',))
    t.start()  
    pool.append(t)
    time.sleep(random.uniform(0.6*15, 0.6*16))
  if(random.randint(0, 5) == 1): 
    t = threading.Thread(target=deviceOn, args=("Bathroom", "TowelDryer", env, 'User Activity',))
    t.start()  
    pool.append(t)
  time.sleep(random.uniform(0.03, 0.05))
  t6 = threading.Thread(target=deviceOff, args=("Bathroom", "Light", env, 'User Activity',))
  t6.start()
  pool.append(t6)
  time.sleep(random.uniform(0.03, 0.05))
  t7 = threading.Thread(target=deviceOn, args=("Bathroom", "Door", env, 'User Activity',))
  t7.start()  
  pool.append(t7)
  time.sleep(random.uniform(0.03, 0.05))
  if(random.randint(0, 4) == 1): 
    t = threading.Thread(target=deviceOff, args=("Bathroom", "TowelDryer", env, 'User Activity',))
    t.start()  
    pool.append(t)
  time.sleep(random.uniform(0.03, 0.05))
  stateDecrease(globalFrame.thread_list,"Bathroom", "HumanState", env)
  stateIncrease(globalFrame.thread_list,"LivingRoom", "HumanState", env)
  time.sleep(random.uniform(0.03, 0.05))
  t8 = threading.Thread(target=deviceOff, args=("Bathroom", "Door", env, 'User Activity',))
  t8.start()
  pool.append(t8)
  
  for item in pool:
    item.join()
    
# 15min
def Cook():
  pool = []
  t1 = threading.Thread(target=deviceOn, args=("Kitchen", "Door", env, 'User Activity',))
  t1.start()
  pool.append(t1)
  time.sleep(random.uniform(0.03, 0.05))
  stateDecrease(globalFrame.thread_list,"LivingRoom", "HumanState", env)
  stateIncrease(globalFrame.thread_list,"Kitchen", "HumanState", env)
  time.sleep(random.uniform(0.03, 0.05))
  t4 = threading.Thread(target=deviceOff, args=("Kitchen", "Door", env, 'User Activity',))
  t4.start()  
  pool.append(t4)
  time.sleep(random.uniform(0.6*2, 0.6*3.2))
  if(random.randint(0, 3) == 1):
    t5 = threading.Thread(target=deviceOn, args=("Kitchen", "Fridge", env, 'User Activity',))
    t5.start()  
    pool.append(t5)
    time.sleep(random.uniform(0.3, 0.6*5))
    t6 = threading.Thread(target=deviceOff, args=("Kitchen", "Fridge", env, 'User Activity',))
    t6.start()  
    pool.append(t6)
    time.sleep(random.uniform(0.1, 0.15))
  if(random.randint(0, 3) == 1): 
    t = threading.Thread(target=deviceOn, args=("Kitchen", "WaterDispenser", env, 'User Activity',))
    t.start()  
    pool.append(t)
  time.sleep(random.uniform(0.6*8, 0.6*12))
  if(random.randint(0, 2) == 1):
    t = threading.Thread(target=deviceOn, args=("Kitchen", "CookerHood", env, 'User Activity',))
    t.start()  
    pool.append(t)
    time.sleep(random.uniform(0.6*10, 0.6*12))
    t = threading.Thread(target=deviceOff, args=("Kitchen", "CookerHood", env, 'User Activity',))
    t.start()  
    pool.append(t)
  else:
    stateDecrease(globalFrame.thread_list,"Kitchen", "AirQuality", env)
    time.sleep(random.uniform(0.6*8, 0.6*12))
  t7 = threading.Thread(target=deviceOn, args=("Kitchen", "Door", env, 'User Activity',))
  t7.start()  
  pool.append(t7)
  time.sleep(random.uniform(0.03, 0.05))
  stateDecrease(globalFrame.thread_list,"Kitchen", "HumanState", env)
  stateIncrease(globalFrame.thread_list,"LivingRoom", "HumanState", env)
  
  for item in pool:
    item.join()

# 10min
def changeClothes():
  pool = []
  t3 = threading.Thread(target=deviceOn, args=("Cloakroom", "Door", env, 'User Activity',))
  t3.start()
  pool.append(t3)
  time.sleep(random.uniform(0.03, 0.05))
  stateDecrease(globalFrame.thread_list,"LivingRoom", "HumanState", env)
  stateIncrease(globalFrame.thread_list,"Cloakroom", "HumanState", env)
  time.sleep(random.uniform(0.03, 0.05))
  t4 = threading.Thread(target=deviceOff, args=("Cloakroom", "Door", env, 'User Activity',))
  t4.start()  
  pool.append(t4)
  time.sleep(random.uniform(0.03, 0.05))
  t5 = threading.Thread(target=deviceOn, args=("Cloakroom", "Light", env, 'User Activity',))
  t5.start()
  pool.append(t5)
  time.sleep(random.uniform(0.6*5, 0.6*8))
  t6 = threading.Thread(target=deviceOff, args=("Cloakroom", "Light", env, 'User Activity',))
  t6.start()
  pool.append(t6)
  time.sleep(random.uniform(0.03, 0.05))
  t7 = threading.Thread(target=deviceOn, args=("Cloakroom", "Door", env, 'User Activity',))
  t7.start()  
  pool.append(t7)
  time.sleep(random.uniform(0.03, 0.05))
  stateDecrease(globalFrame.thread_list,"Cloakroom", "HumanState", env)
  stateIncrease(globalFrame.thread_list,"LivingRoom", "HumanState", env)
  time.sleep(random.uniform(0.03, 0.05))
  t8 = threading.Thread(target=deviceOff, args=("Cloakroom", "Door", env, 'User Activity',))
  t8.start()
  pool.append(t8)
  
  for item in pool:
    item.join()


def washClothes():
  pool = []
  t1 = threading.Thread(target=deviceOn, args=("Balcony", "Door", env, 'User Activity',))
  t1.start()
  pool.append(t1)
  time.sleep(random.uniform(0.03, 0.05))
  stateDecrease(globalFrame.thread_list,"BedroomTwo", "HumanState", env)
  stateIncrease(globalFrame.thread_list,"Balcony", "HumanState", env)
  time.sleep(random.uniform(0.03, 0.05))
  if(random.randint(0, 3) == 1): 
    t = threading.Thread(target=deviceOff, args=("Balcony", "Door", env, 'User Activity',))
    t.start()  
    pool.append(t)
  time.sleep(random.uniform(0.03, 0.05))
  if(random.randint(0, 3) == 1): 
    t = threading.Thread(target=deviceOn, args=("Balcony", "Light", env, 'User Activity',))
    t.start()
    pool.append(t)
  time.sleep(random.uniform(0.03, 0.05))
  if(random.randint(0, 3) == 1): 
    t = threading.Thread(target=deviceOff, args=("Balcony", "Window", env, 'User Activity',))
    t.start()
    pool.append(t)
  elif(random.randint(0, 3) == 2):
    t = threading.Thread(target=deviceOn, args=("Balcony", "Window", env, 'User Activity',))
    t.start()
    pool.append(t)
  time.sleep(random.uniform(0.6, 0.6*2))
  if(random.randint(0, 3) == 1): 
    t = threading.Thread(target=deviceOff, args=("Balcony", "Curtain", env, 'User Activity',))
    t.start()
    pool.append(t)
  elif(random.randint(0, 3) == 2):
    t = threading.Thread(target=deviceOn, args=("Balcony", "Curtain", env, 'User Activity',))
    t.start()
    pool.append(t)
  time.sleep(random.uniform(0.6, 0.6*2))
  t2 = threading.Thread(target=deviceOn, args=("Balcony", "WashingMachine", env, 'User Activity',))
  t2.start()
  pool.append(t2)
  time.sleep(random.uniform(0.6*5, 0.6*8))
  if(random.randint(0, 3) == 1): 
    t = threading.Thread(target=deviceOff, args=("Balcony", "Light", env, 'User Activity',))
    t.start()
    pool.append(t)
  time.sleep(random.uniform(0.03, 0.05))
  t3 = threading.Thread(target=deviceOn, args=("Balcony", "Door", env, 'User Activity',))
  t3.start()  
  pool.append(t3)
  time.sleep(random.uniform(0.03, 0.05))
  stateDecrease(globalFrame.thread_list,"Balcony", "HumanState", env)
  stateIncrease(globalFrame.thread_list,"BedroomTwo", "HumanState", env)
  time.sleep(random.uniform(0.03, 0.05))
  t4 = threading.Thread(target=deviceOff, args=("Balcony", "Door", env, 'User Activity',))
  t4.start()
  pool.append(t4)
  
  for item in pool:
    item.join()


def collectClothes():
  pool = []
  t1 = threading.Thread(target=deviceOn, args=("Balcony", "Door", env, 'User Activity',))
  t1.start()
  pool.append(t1)
  time.sleep(random.uniform(0.03, 0.05))
  stateDecrease(globalFrame.thread_list,"BedroomTwo", "HumanState", env)
  stateIncrease(globalFrame.thread_list,"Balcony", "HumanState", env)
  time.sleep(random.uniform(0.03, 0.05))
  if(random.randint(0, 3) == 1): 
    t = threading.Thread(target=deviceOff, args=("Balcony", "Door", env, 'User Activity',))
    t.start()  
    pool.append(t)
  time.sleep(random.uniform(0.03, 0.05))
  if(random.randint(0, 3) == 1): 
    t = threading.Thread(target=deviceOn, args=("Balcony", "Light", env, 'User Activity',))
    t.start()
    pool.append(t)
  time.sleep(random.uniform(0.03, 0.05))
  if(random.randint(0, 3) == 1): 
    t = threading.Thread(target=deviceOff, args=("Balcony", "Window", env, 'User Activity',))
    t.start()
    pool.append(t)
  elif(random.randint(0, 3) == 2):
    t = threading.Thread(target=deviceOn, args=("Balcony", "Window", env, 'User Activity',))
    t.start()
    pool.append(t)
  time.sleep(random.uniform(0.6, 0.6*2))
  if(random.randint(0, 3) == 1): 
    t = threading.Thread(target=deviceOff, args=("Balcony", "Curtain", env, 'User Activity',))
    t.start()
    pool.append(t)
  elif(random.randint(0, 3) == 2):
    t = threading.Thread(target=deviceOn, args=("Balcony", "Curtain", env, 'User Activity',))
    t.start()
    pool.append(t)
  time.sleep(random.uniform(0.6*3, 0.6*5))
  if(random.randint(0, 3) == 1): 
    t = threading.Thread(target=deviceOff, args=("Balcony", "Light", env, 'User Activity',))
    t.start()
    pool.append(t)
  time.sleep(random.uniform(0.03, 0.05))
  t3 = threading.Thread(target=deviceOn, args=("Balcony", "Door", env, 'User Activity',))
  t3.start()  
  pool.append(t3)
  time.sleep(random.uniform(0.03, 0.05))
  stateDecrease(globalFrame.thread_list,"Balcony", "HumanState", env)
  stateIncrease(globalFrame.thread_list,"BedroomTwo", "HumanState", env)
  time.sleep(random.uniform(0.03, 0.05))
  t4 = threading.Thread(target=deviceOff, args=("Balcony", "Door", env, 'User Activity',))
  t4.start()
  pool.append(t4)
  
  for item in pool:
    item.join()
  
    
def Reservation(start_time):
	time.sleep(start_time - 30*0.6)
	t1 = threading.Thread(target=deviceOn, args=("Bathroom", "WaterHeater", env, 'Application',))
	t1.start()

	time.sleep(35*0.6)
	t2 = threading.Thread(target=deviceOn, args=("Bathroom", "TowelDryer", env, 'Application',))
	t2.start()
	
	t1.join()
	t2.join()

def getUp(room):
  time.sleep(35*0.6)
  t2 = threading.Thread(target=deviceOn, args=(room, "Curtain", env, 'Application',))
  t2.start()
	
  t2.join()