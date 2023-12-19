import json
import random
import threading
import time
import os
from DataFrame import globalFrame
from personBehavior.BehaviorSequence import *


def personWeekEnd():
    random_day = random.randint(0, 2)
    if random_day == 0:
        t_environment = threading.Thread(target=environmentNormal)
        t_environment.start()
    else:
        t_environment = threading.Thread(target=environmentRaining)
        t_environment.start()
    t_personOne = threading.Thread(target=weekendPersonOne)
    t_personOne.start()
    t_personTwo = threading.Thread(target=weekendPersonOne)
    t_personTwo.start()
    t_personThree = threading.Thread(target=weekendPersonTwo)
    t_personThree.start()
    t_personFour = threading.Thread(target=weekendPersonTwo)
    t_personFour.start()
    t_personFive = threading.Thread(target=weekendPersonTwo)
    t_personFive.start()

    
    t_environment.join()
    t_personOne.join()
    print("t_personOne end")
    t_personTwo.join()
    print("t_personTwo end")
    t_personThree.join()
    print("t_personThree end")
    t_personFour.join()
    print("t_personFour end")
    t_personFive.join()
    print("t_personFive end")


def processWeekDay():
    random_day = random.randint(0, 2)
    if random_day == 0:
        t_environment = threading.Thread(target=environmentNormal)
        t_environment.start()
    else:
        t_environment = threading.Thread(target=environmentRaining)
        t_environment.start()
    
    t_personOne = threading.Thread(target=personOne)
    t_personOne.start()
    t_personTwo = threading.Thread(target=personTwo)
    t_personTwo.start()
    t_personThree = threading.Thread(target=personThree)
    t_personThree.start()
    t_personFour = threading.Thread(target=personFour)
    t_personFour.start()
    t_personFive = threading.Thread(target=personFive)
    t_personFive.start()
    t_personSix = threading.Thread(target=personSix)
    t_personSix.start()
    t_personSeven = threading.Thread(target=personSeven)
    t_personSeven.start()
    t_personEight = threading.Thread(target=personEight)
    t_personEight.start()
    t_personNine = threading.Thread(target=personNine)
    t_personNine.start()
    t_personTen = threading.Thread(target=personTen)
    t_personTen.start()
    t_11 = threading.Thread(target=personOne)
    t_11.start()
    t_12 = threading.Thread(target=personTwo)
    t_12.start()
    t_13 = threading.Thread(target=personThree)
    t_13.start()
    t_14 = threading.Thread(target=personFour)
    t_14.start()
    t_15 = threading.Thread(target=personFive)
    t_15.start()
    t_16 = threading.Thread(target=personSix)
    t_16.start()
    t_17 = threading.Thread(target=personSeven)
    t_17.start()
    t_18 = threading.Thread(target=personEight)
    t_18.start()
    t_19 = threading.Thread(target=personNine)
    t_19.start()
    t_20 = threading.Thread(target=personTen)
    t_20.start()
    
    t_environment.join()
    t_personOne.join()
    print("t_personOne end")
    t_personTwo.join()
    print("t_personTwo end")
    t_personThree.join()
    print("t_personThree end")
    t_personFour.join()
    print("t_personFour end")
    t_personFive.join()
    print("t_personFive end")
    t_personSix.join()
    print("t_personSix end")
    t_personSeven.join()
    print("t_personSeven end")
    t_personEight.join()
    print("t_personEight end")
    t_personNine.join()
    print("t_personNine end")
    t_personTen.join()
    print("t_personTen end")
    t_11.join()
    print("t_11 end")
    t_12.join()
    print("t_12 end")
    t_13.join()
    print("t_13 end")
    t_14.join()
    print("t_14 end")
    t_15.join()
    print("t_15 end")
    t_16.join()
    print("t_16 end")
    t_17.join()
    print("t_17 end")
    t_18.join()
    print("t_18 end")
    t_19.join()
    print("t_19 end")
    t_20.join()
    print("t_20 end")

    time.sleep(1)


def runWeek(start):
    for week in range(start, start + 5):
        globalFrame.df.drop(globalFrame.df.index, inplace=True)
        print(week)
        if (week) > 9:
            globalFrame.start_time = time.mktime(time.strptime("2023-09-" + str(week) + " 00:00:01", "%Y-%m-%d %H:%M:%S"))
        else:
            globalFrame.start_time = time.mktime(time.strptime("2023-09-0" + str(week) + " 00:00:01", "%Y-%m-%d %H:%M:%S"))
        # thread_process = threading.Thread(target=processWeekDay)
        processWeekDay()
        # thread_process.start()
        # thread_process.join()
        print(len(globalFrame.thread_list))
        for item in globalFrame.thread_list:
            item.join()
        globalFrame.thread_list = []
        with globalFrame.df_lock:
            globalFrame.df.to_excel('./data/output_day_' + str(week) + '.xlsx', index=False, sheet_name='week ' + str(week))
        time.sleep(1)
    return week


def runWeekEnd(start):
    for weekend in range(start, start + 2):
        globalFrame.df.drop(globalFrame.df.index, inplace=True)
        print(weekend)
        if (weekend) > 9:
            globalFrame.start_time = time.mktime(time.strptime("2023-09-" + str(weekend) + " 00:00:01", "%Y-%m-%d %H:%M:%S"))
        else:
            globalFrame.start_time = time.mktime(time.strptime("2023-09-0" + str(weekend) + " 00:00:01", "%Y-%m-%d %H:%M:%S"))
        # thread_process = threading.Thread(target=personWeekEnd)
        personWeekEnd()
        # thread_process.start()
        # thread_process.join()
        for item in globalFrame.thread_list:
            item.join()
        globalFrame.thread_list = []
        with globalFrame.df_lock:
            globalFrame.df.to_excel('./data/output_day_' + str(weekend) + '.xlsx', index=False, sheet_name='week ' + str(weekend))
        time.sleep(2)
    return weekend


if __name__ == '__main__':
    os.chdir("/home/rjl/experience/benchmark")
    try:
        os.stat('data')
    except FileNotFoundError:
        os.mkdir('data')
    t_changeTime = threading.Thread(target=globalFrame.changeTime)
    t_changeTime.start()
            
    # globalFrame.df.drop(globalFrame.df.index, inplace=True)
    # globalFrame.start_time = time.mktime(time.strptime("2023-09-03" + " 00:00:01", "%Y-%m-%d %H:%M:%S"))
    # processWeekDay()
    # for item in globalFrame.thread_list:
    #     item.join()
    # globalFrame.thread_list = []
    # with globalFrame.df_lock:
    #     globalFrame.df.to_excel('./data/output_day_3.xlsx', index=False)
        
    # temp_env = {}
    # for space in env['space_dict']:
    #     temp_room = {}
    #     temp_device = {}
    #     temp_state = {}
    #     for device in env['space_dict'][space]['device_dict']:
    #         temp_device[device] = env['space_dict'][space]['device_dict'][device].on
    #     for state in env['space_dict'][space]['env_state']:
    #         temp_state[state] = env['space_dict'][space]['env_state'][state].value
    #     temp_room['device'] = temp_device
    #     temp_room['state'] = temp_state
    #     temp_env[space] = temp_room
    
    # temp_env['Corridor']['HumanState'] = env['space_dict'][space]['env_state']['HumanState'].count
    
    # json_str = json.dumps(temp_env, indent=4)
    # with open('./data/output_init_state.json', 'w') as json_file:
    #     json_file.write(json_str)
    
    # time.sleep(1)

    # week_end = runWeek(4)
    # weekend_end = runWeekEnd(week_end + 1)
    # week_end = runWeek(weekend_end + 1)
    # weekend_end = runWeekEnd(week_end + 1)

    t_test = threading.Thread(target=test)
    t_test.start()
    t_test.join()
    for item in globalFrame.thread_list:
        item.join()
    with globalFrame.df_lock:
        globalFrame.df.to_excel('./data/test.xlsx', index=False, sheet_name='test')

    globalFrame.flag = False
    t_changeTime.join()
