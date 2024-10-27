import importlib
import json
import random
import threading
import time
import os
from util.DataFrame import globalFrame
from Characterization.Environment import setEnv, getEnv
from ExternalChange.ExternalChange import *
from config import setIP, getIP


def labWeekEnd(module, env):
    random_day = random.randint(0, 2)
    if random_day == 0:
        t_environment = threading.Thread(target=environmentNormal, args=(env,))
        t_environment.start()
    else:
        t_environment = threading.Thread(target=environmentRaining, args=(env,))
        t_environment.start()
    t_personOne = threading.Thread(target=module.weekendPersonOne)
    t_personOne.start()
    t_personTwo = threading.Thread(target=module.weekendPersonOne)
    t_personTwo.start()
    t_personThree = threading.Thread(target=module.weekendPersonTwo)
    t_personThree.start()
    t_personFour = threading.Thread(target=module.weekendPersonTwo)
    t_personFour.start()
    t_personFive = threading.Thread(target=module.weekendPersonTwo)
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


def labWeekDay(module, env):
    random_day = random.randint(0, 2)
    if random_day == 0:
        t_environment = threading.Thread(target=environmentNormal, args=(env,))
        t_environment.start()
    else:
        t_environment = threading.Thread(target=environmentRaining, args=(env,))
        t_environment.start()

    t_personOne = threading.Thread(target=module.personOne)
    t_personOne.start()
    t_personTwo = threading.Thread(target=module.personTwo)
    t_personTwo.start()
    t_personThree = threading.Thread(target=module.personThree)
    t_personThree.start()
    t_personFour = threading.Thread(target=module.personFour)
    t_personFour.start()
    t_personFive = threading.Thread(target=module.personFive)
    t_personFive.start()
    t_personSix = threading.Thread(target=module.personSix)
    t_personSix.start()
    t_personSeven = threading.Thread(target=module.personSeven)
    t_personSeven.start()
    t_personEight = threading.Thread(target=module.personEight)
    t_personEight.start()
    t_personNine = threading.Thread(target=module.personNine)
    t_personNine.start()
    t_personTen = threading.Thread(target=module.personTen)
    t_personTen.start()
    t_11 = threading.Thread(target=module.personOne)
    t_11.start()
    t_12 = threading.Thread(target=module.personTwo)
    t_12.start()
    t_13 = threading.Thread(target=module.personThree)
    t_13.start()
    t_14 = threading.Thread(target=module.personFour)
    t_14.start()
    t_15 = threading.Thread(target=module.personFive)
    t_15.start()
    t_16 = threading.Thread(target=module.personSix)
    t_16.start()
    t_17 = threading.Thread(target=module.personSeven)
    t_17.start()
    t_18 = threading.Thread(target=module.personEight)
    t_18.start()
    t_19 = threading.Thread(target=module.personNine)
    t_19.start()
    t_20 = threading.Thread(target=module.personTen)
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


def homeWeekEnd(module, env):
    print("homeWeekEnd")
    random_day = random.randint(0, 2)
    if random_day == 0:
        t_environment = threading.Thread(target=environmentNormal, args=(env,))
        t_environment.start()
    else:
        t_environment = threading.Thread(target=environmentRaining, args=(env,))
        t_environment.start()

    t_personOne = threading.Thread(target=module.weekendpersonOne)
    t_personOne.start()
    t_personTwo = threading.Thread(target=module.weekendpersonTwo)
    t_personTwo.start()
    t_personThree = threading.Thread(target=module.weekendpersonThree)
    t_personThree.start()

    t_environment.join()
    t_personOne.join()
    print("t_personOne end")
    t_personTwo.join()
    print("t_personTwo end")
    t_personThree.join()
    print("t_personThree end")


def homeWeekDay(module, env):
    print("homeWeekDay")
    random_day = random.randint(0, 2)
    if random_day == 0:
        t_environment = threading.Thread(target=environmentNormal, args=(env,))
        t_environment.start()
    else:
        t_environment = threading.Thread(target=environmentRaining, args=(env,))
        t_environment.start()

    t_personOne = threading.Thread(target=module.personOne)
    t_personOne.start()
    t_personTwo = threading.Thread(target=module.personTwo)
    t_personTwo.start()
    t_personThree = threading.Thread(target=module.personThree)
    t_personThree.start()

    t_environment.join()
    t_personOne.join()
    print("t_personOne end")
    t_personTwo.join()
    print("t_personTwo end")
    t_personThree.join()
    print("t_personThree end")


def simulationWeekEnd(module, env):
    print("simulationWeekEnd")
    random_day = random.randint(0, 2)
    if random_day == 0:
        t_environment = threading.Thread(target=environmentNormal, args=(env,))
        t_environment.start()
    else:
        t_environment = threading.Thread(target=environmentRaining, args=(env,))
        t_environment.start()

    t_environment.join()


def simulationWeekDay(module, env):
    print("simulationWeekDay")
    random_day = random.randint(0, 2)
    if random_day == 0:
        t_environment = threading.Thread(target=environmentNormal, args=(env,))
        t_environment.start()
    else:
        t_environment = threading.Thread(target=environmentRaining, args=(env,))
        t_environment.start()

    t_environment.join()


def runWeek(mouth, start, space, module, env):
    for week in range(start, start + 5):
        globalFrame.df.drop(globalFrame.df.index, inplace=True)
        print(week)
        if (week) > 9:
            globalFrame.start_time = time.mktime(
                time.strptime("2024-" + mouth + "-" + str(week) + " 00:00:01", "%Y-%m-%d %H:%M:%S"))
        else:
            globalFrame.start_time = time.mktime(
                time.strptime("2024-" + mouth + "-0" + str(week) + " 00:00:01", "%Y-%m-%d %H:%M:%S"))
        if (space == "Lab"):
            labWeekDay(module, env)
        elif (space == "Home"):
            homeWeekDay(module, env)
        elif (space == "simulation"):
            simulationWeekDay(module, env)
        for item in globalFrame.thread_list:
            item.join()
        globalFrame.thread_list = []
        with globalFrame.df_lock:
            globalFrame.df.to_excel('./data/' + space + '/output_day_' + str(week) + '.xlsx', index=False,
                                    sheet_name='week ' + str(week))
        time.sleep(1)
    return week


def runWeekEnd(mouth, start, space, module, env):
    for weekend in range(start, start + 2):
        globalFrame.df.drop(globalFrame.df.index, inplace=True)
        print(weekend)
        if (weekend) > 9:
            globalFrame.start_time = time.mktime(
                time.strptime("2024-" + mouth + "-" + str(weekend) + " 00:00:01", "%Y-%m-%d %H:%M:%S"))
        else:
            globalFrame.start_time = time.mktime(
                time.strptime("2024-" + mouth + "-0" + str(weekend) + " 00:00:01", "%Y-%m-%d %H:%M:%S"))
        if (space == "Lab"):
            labWeekEnd(module, env)
        elif (space == "Home"):
            homeWeekEnd(module, env)
        elif (space == "simulation"):
            simulationWeekEnd(module, env)
        for item in globalFrame.thread_list:
            item.join()
        globalFrame.thread_list = []
        with globalFrame.df_lock:
            globalFrame.df.to_excel('./data/' + space + '/output_day_' + str(weekend) + '.xlsx', index=False,
                                    sheet_name='week ' + str(weekend))
        time.sleep(2)
    return weekend


def runLab():
    setIP("http://47.101.169.122:5004")
    setEnv("Lab")
    env = getEnv()
    module_name = 'HumanActivity.LabHumanActivity'
    module = importlib.import_module(module_name)

    try:
        os.stat('data')
    except FileNotFoundError:
        os.mkdir('data')
    try:
        os.stat('data/Lab')
    except FileNotFoundError:
        os.mkdir('data/Lab')
    globalFrame.df.drop(globalFrame.df.index, inplace=True)
    globalFrame.start_time = time.mktime(time.strptime("2024-04-01" + " 00:00:01", "%Y-%m-%d %H:%M:%S"))
    labWeekDay(module, env)
    for item in globalFrame.thread_list:
        item.join()
    globalFrame.thread_list = []
    with globalFrame.df_lock:
        globalFrame.df.to_excel('./data/Lab/output_day_00.xlsx', index=False)
    temp_env = {}
    for space in env['space_dict']:
        temp_room = {}
        temp_device = {}
        temp_state = {}
        for device in env['space_dict'][space]['device_dict']:
            env['space_dict'][space]['device_dict'][device].lock.acquire()
            temp_device[device] = getDeviceState(space, device, env)
            env['space_dict'][space]['device_dict'][device].lock.release()
        for state in env['space_dict'][space]['env_state']:
            env['space_dict'][space]['env_state'][state].lock.acquire()
            temp_state[state] = getStateValue(space, state, env)
            env['space_dict'][space]['env_state'][state].lock.release()
        temp_room['device'] = temp_device
        temp_room['state'] = temp_state
        temp_env[space] = temp_room
    json_str = json.dumps(temp_env, indent=4)
    with open('./data/Lab/output_init_state.json', 'w') as json_file:
        json_file.write(json_str)

    time.sleep(1)
    week_end = runWeek("4", 2, "Lab", module, env)
    weekend_end = runWeekEnd("4", week_end + 1, "Lab", module, env)
    week_end = runWeek("4", weekend_end + 1, "Lab", module, env)
    weekend_end = runWeekEnd("4", week_end + 1, "Lab", module, env)
    week_end = runWeek("4", weekend_end + 1, "Lab", module, env)
    weekend_end = runWeekEnd("4", week_end + 1, "Lab", module, env)
    week_end = runWeek("4", weekend_end + 1, "Lab", module, env)
    weekend_end = runWeekEnd("4", week_end + 1, "Lab", module, env)


def runHome():
    setIP("http://47.101.169.122:5005")
    setEnv("Home")
    env = getEnv()
    module_name = 'HumanActivity.HomeHumanActivity'
    module = importlib.import_module(module_name)
    try:
        os.stat('data')
    except FileNotFoundError:
        os.mkdir('data')
    try:
        os.stat('data/Home')
    except FileNotFoundError:
        os.mkdir('data/Home')
    globalFrame.df.drop(globalFrame.df.index, inplace=True)
    globalFrame.start_time = time.mktime(time.strptime("2024-09-01" + " 00:00:01", "%Y-%m-%d %H:%M:%S"))
    homeWeekDay(module, env)
    for item in globalFrame.thread_list:
        item.join()
    globalFrame.thread_list = []
    with globalFrame.df_lock:
        globalFrame.df.to_excel('./data/Home/output_day_00.xlsx', index=False)
    temp_env = {}
    for space in env['space_dict']:
        temp_room = {}
        temp_device = {}
        temp_state = {}
        for device in env['space_dict'][space]['device_dict']:
            env['space_dict'][space]['device_dict'][device].lock.acquire()
            temp_device[device] = getDeviceState(space, device, env)
            env['space_dict'][space]['device_dict'][device].lock.release()
        for state in env['space_dict'][space]['env_state']:
            env['space_dict'][space]['env_state'][state].lock.acquire()
            temp_state[state] = getStateValue(space, state, env)
            env['space_dict'][space]['env_state'][state].lock.release()
        temp_room['device'] = temp_device
        temp_room['state'] = temp_state
        temp_env[space] = temp_room

    json_str = json.dumps(temp_env, indent=4)
    with open('./data/Home/output_init_state.json', 'w') as json_file:
        json_file.write(json_str)

    time.sleep(1)

    week_end = runWeek("9", 2, "Home", module, env)
    weekend_end = runWeekEnd("9", week_end + 1, "Home", module, env)
    week_end = runWeek("9", weekend_end + 1, "Home", module, env)
    weekend_end = runWeekEnd("9", week_end + 1, "Home", module, env)
    week_end = runWeek("9", weekend_end + 1, "Home", module, env)
    weekend_end = runWeekEnd("9", week_end + 1, "Home", module, env)
    week_end = runWeek("9", weekend_end + 1, "Home", module, env)
    weekend_end = runWeekEnd("9", week_end + 1, "Home", module, env)


if __name__ == '__main__':

    t_changeTime = threading.Thread(target=globalFrame.changeTime)
    t_changeTime.start()

    runLab()
    # runHome()

    globalFrame.flag = False
    t_changeTime.join()
