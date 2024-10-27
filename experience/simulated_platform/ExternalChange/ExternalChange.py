import threading
import time
import random
from DeviceController.DeviceController import *
from util.DataFrame import globalFrame

def environmentNormal(env):
    pool = []
    
    time.sleep(random.uniform(0.6*30, 0.6*60*1))
    if random.randint(0, 1) == 1:
        t0 = threading.Thread(target=weatherChange, args=('sunny', env, ))
        t0.start()
        pool.append(t0)
    # 01.00-02.00
    time.sleep(random.uniform(0.6*30, 0.6*60*1))
    t1 = threading.Thread(target=stateDecrease, args=(globalFrame.thread_list,"Context", "Temperature", env, ))
    t1.start()
    pool.append(t1)
    # 06.00
    time.sleep(random.uniform(0.6*60*5, 0.6*60*5.2))
    t2 = threading.Thread(target=stateIncrease, args=(globalFrame.thread_list,"Context", "Brightness", env, ))
    t2.start()
    pool.append(t2)

    # 9.30-10.00
    time.sleep(random.uniform(0.6*60*3.5, 0.6*60*4))
    t3 = threading.Thread(target=stateIncrease, args=(globalFrame.thread_list,"Context", "Brightness", env, ))
    t3.start()
    pool.append(t3)

    # 10.00-10.30
    time.sleep(random.uniform(0.6*60*0.5, 0.6*60*0.6))
    t4 = threading.Thread(target=stateDecrease, args=(globalFrame.thread_list,"Context", "Humidity", env, ))
    t4.start()
    pool.append(t4)
    
    time.sleep(random.uniform(0.6*60*0.5, 0.6*60*0.6))
    # t1 = threading.Thread(target=stateIncrease, args=(globalFrame.thread_list,"Context", "Temperature", env, ))
    # t1.start()
    # pool.append(t1)

    # 13.00-13.30
    time.sleep(random.uniform(0.6*60*2.5, 0.6*60*2.9))
    if random.randint(0, 1) == 1:
        t5 = threading.Thread(target=weatherChange, args=('cloudy', env, ))
        t5.start()
        pool.append(t5)

    # 14.00-14.30
    time.sleep(random.uniform(0.6*60*1, 0.6*60*1.5))
    t6 = threading.Thread(target=stateIncrease, args=(globalFrame.thread_list,"Context", "Temperature", env, ))
    t6.start()
    pool.append(t6)

    # 17.00
    time.sleep(random.uniform(0.6*60*3, 0.6*60*3.2))
    t7 = threading.Thread(target=weatherChange, args=('sunny', env, ))
    t7.start()
    pool.append(t7)

    time.sleep(random.uniform(0.6*60*0.5, 0.6*60*0.8))
    t8 = threading.Thread(target=stateDecrease, args=(globalFrame.thread_list,"Context", "Brightness", env, ))
    t8.start()
    pool.append(t8)

    # 18.00
    time.sleep(random.uniform(0.6*60*0.5, 0.6*60*1))
    t9 = threading.Thread(target=stateIncrease, args=(globalFrame.thread_list,"Context", "Humidity", env, ))
    t9.start()
    pool.append(t9)

    time.sleep(random.uniform(0.6*60*0.2, 0.6*60*0.3))
    t10 = threading.Thread(target=stateDecrease, args=(globalFrame.thread_list,"Context", "Temperature", env, ))
    t10.start()
    pool.append(t10)

    # 20.00
    time.sleep(random.uniform(0.6*60*2, 0.6*60*3))
    t11 = threading.Thread(target=stateDecrease, args=(globalFrame.thread_list,"Context", "Temperature", env, ))
    t11.start()
    pool.append(t11)
    
    time.sleep(random.uniform(0.6*5, 0.6*10))
    if random.randint(0, 1) == 1:
        t12 = threading.Thread(target=weatherChange, args=('cloudy', env, ))
        t12.start()
        pool.append(t12)

    time.sleep(random.uniform(0.6*60*0.2, 0.6*60*0.5))
    t13 = threading.Thread(target=stateDecrease, args=(globalFrame.thread_list,"Context", "Brightness", env, ))
    t13.start()
    pool.append(t13)

    for item in pool:
        item.join()

def environmentRaining(env):
    pool = []
    # 1-1.30
    time.sleep(random.uniform(0.6*60*1, 0.6*60*1.5))
    if random.randint(0, 1) == 1:
        t0 = threading.Thread(target=weatherChange, args=('raining', env, ))
        t0.start()
        pool.append(t0)
        time.sleep(random.uniform(0.6*60*0.2, 0.6*60*0.3))
    time.sleep(random.uniform(0.6*60*0.2, 0.6*60*0.3))
    # 02.00-02.30
    time.sleep(random.uniform(0.6*60*0.8, 0.6*60*0.9))
    t1 = threading.Thread(target=weatherChange, args=('cloudy', env, ))
    t1.start()
    pool.append(t1)
    
    time.sleep(random.uniform(0.6*60*0.5, 0.6*60*0.6))
    t1 = threading.Thread(target=stateDecrease, args=(globalFrame.thread_list,"Context", "Temperature", env, ))
    t1.start()
    pool.append(t1)

    # 04.00-05.00
    time.sleep(random.uniform(0.6*60*1.5, 0.6*60*1.9))
    t2 = threading.Thread(target=weatherChange, args=('sunny', env, ))
    t2.start()
    pool.append(t2)

    # 6.30-7.36
    time.sleep(random.uniform(0.6*60*2.5, 0.6*60*2.6))
    t3 = threading.Thread(target=stateIncrease, args=(globalFrame.thread_list,"Context", "Brightness", env, ))
    t3.start()
    pool.append(t3)

    # 9.00-10.12
    time.sleep(random.uniform(0.6*60*2.5, 0.6*60*2.6))

    # 09.42-11.12
    time.sleep(random.uniform(0.6*60*0.7, 0.6*60*1))
    t5 = threading.Thread(target=weatherChange, args=('cloudy', env, ))
    t5.start()
    pool.append(t5)

    # 10.42-12.18
    time.sleep(random.uniform(0.6*60*1, 0.6*60*1.1))
    t6 = threading.Thread(target=stateDecrease, args=(globalFrame.thread_list,"Context", "Temperature", env, ))
    t6.start()
    pool.append(t6)

    # 11.42-13.24
    time.sleep(random.uniform(0.6*60*1, 0.6*60*1.1))
    t7 = threading.Thread(target=weatherChange, args=('raining', env, ))
    t7.start()
    pool.append(t7)
    time.sleep(random.uniform(0.6*60*0.2, 0.6*60*0.3))

    # 12.12-14.00
    time.sleep(random.uniform(0.6*60*0.3, 0.6*20))
    t8 = threading.Thread(target=stateDecrease, args=(globalFrame.thread_list,"Context", "Humidity", env, ))
    t8.start()
    pool.append(t8)
    
    time.sleep(random.uniform(0.6*60*0.5, 0.6*60*0.6))
    t1 = threading.Thread(target=stateIncrease, args=(globalFrame.thread_list,"Context", "Temperature", env, ))
    t1.start()
    pool.append(t1)
    
    time.sleep(random.uniform(0.6*10, 0.6*15))
    
    t4 = threading.Thread(target=stateIncrease, args=(globalFrame.thread_list,"Context", "Brightness", env, ))
    t4.start()
    pool.append(t4)

    # 15.42-17.30
    time.sleep(0.6*60*3)
    t9 = threading.Thread(target=weatherChange, args=('cloudy', env, ))
    t9.start()
    pool.append(t9)


    # 18.00-20.00
    time.sleep(random.uniform(0.6*60*2.3, 0.6*60*2.5))
    t10 = threading.Thread(target=stateDecrease, args=(globalFrame.thread_list,"Context", "Brightness", env, ))
    t10.start()
    pool.append(t10)

    # 18.30-20.36
    time.sleep(random.uniform(0.6*60*0.5, 0.6*60*0.6))
    # t11 = threading.Thread(target=stateDecrease, args=(globalFrame.thread_list,"Context", "Temperature", env, ))
    # t11.start()
    # pool.append(t11)

    # 19.42-21.48
    time.sleep(0.6*60*1.2)
    t12 = threading.Thread(target=stateIncrease, args=(globalFrame.thread_list,"Context", "Humidity", env, ))
    t12.start()
    pool.append(t12)
    
    time.sleep(random.uniform(0.6*60*0.5, 0.6*60*0.6))
    t11 = threading.Thread(target=stateDecrease, args=(globalFrame.thread_list,"Context", "Temperature", env, ))
    t11.start()
    pool.append(t11)

    # 20.42-22.54
    time.sleep(random.uniform(0.6*60*0.5, 0.6*60*0.6))
    t13 = threading.Thread(target=stateDecrease, args=(globalFrame.thread_list,"Context", "Brightness", env, ))
    t13.start()
    pool.append(t13)    
    time.sleep(random.uniform(0.6*10, 0.6*35))
    if random.randint(0, 1) == 1:
        t0 = threading.Thread(target=weatherChange, args=('raining', env, ))
        t0.start()
        pool.append(t0)

    for item in pool:
        item.join()
