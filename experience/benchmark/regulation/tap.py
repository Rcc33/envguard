import random
import time
import pandas as pd
import threading

def conflict(device, Location, thread_list, env):
    # if random.randrange(1, 5) == 1: 
    #     time.sleep(random.uniform(10*0.6, 100*0.6))
    if random.randint(1, 2) == 1: 
        time.sleep(random.uniform(1*0.6, 2*0.6))
        if device == 'AC' and Location in ['TeaRoom', 'Corridor']:
            return
        if device == 'Window' and Location == 'Corridor':
            return
        t1 = threading.Thread(target=env["space_dict"][Location]['device_dict'][device].action_on,
                                    args=(env["space_dict"][Location]['device_dict'][device], env, 'offline',))
        t1.start()
        thread_list.append(t1)

def tap(env, Name, Location, PayloadData,thread_list):
    if Name == 'ac_on':
        t1 = threading.Thread(target=conflict, args=('Window', Location, thread_list, env,))
        t1.start()
        thread_list.append(t1)
    
    if Name == 'window_on':
        t1 = threading.Thread(target=conflict, args=('AC', Location, thread_list, env,))
        t1.start()
        thread_list.append(t1)
        
    if Name == 'weather_change' and PayloadData.split(': ')[1] == 'raining':
        t1 = threading.Thread(target=conflict, args=('Window', "Lab", thread_list, env,))
        t1.start()
        thread_list.append(t1)
        t2 = threading.Thread(target=conflict, args=('Window', "MeetingRoomOne", thread_list, env,))
        t2.start()
        thread_list.append(t2)
        t3 = threading.Thread(target=conflict, args=('Window', "MeetingRoomTwo", thread_list, env,))
        t3.start()
        thread_list.append(t3)
        t4 = threading.Thread(target=conflict, args=('Window', "TeaRoom", thread_list, env,))
        t4.start()
        thread_list.append(t4)
    
    
    # if Name == 'human_detected':
    #     if Location in ['Corridor', 'TeaRoom']:
    #         print('tap 1')
    #         t1 = threading.Thread(target=env["space_dict"][Location]['device_dict']['Light'].action_on,
    #                               args=(env["space_dict"][Location]['device_dict']['Light'], env, 'app',))
    #         t1.start()
    #         thread_list.append(t1)
    # if Name == 'temperature_up':     
    #     if (Location in ['Lab', 'MeetingRoomOne', 'MeetingRoomTwo', 'TeaRoom']) and PayloadData.split(': ')[1] == 'high':
    #         print('tap 2')
    #         t1 = threading.Thread(target=env["space_dict"][Location]['device_dict']['Window'].action_off,
    #                               args=(env["space_dict"][Location]['device_dict']['Window'], env, 'app',))
    #         t1.start()
    #         t2 = threading.Thread(target=env["space_dict"][Location]['device_dict']['Curtain'].action_off,
    #                               args=(env["space_dict"][Location]['device_dict']['Curtain'], env, 'app',))
    #         t2.start()
    #         thread_list.append(t1)
    #         thread_list.append(t2)
    if Name == 'humidity_down':
        if (Location in ['Lab', 'MeetingRoomOne', 'MeetingRoomTwo']) and PayloadData.split(': ')[1] == 'low':
            print('tap 3')
            t1 = threading.Thread(target=env["space_dict"][Location]['device_dict']['Humidifier'].action_on,
                                  args=(env["space_dict"][Location]['device_dict']['Humidifier'], env, 'app',))
            t1.start()
            thread_list.append(t1)
    # if Name == 'air_quality_down':
    #     if (Location in ['Lab', 'MeetingRoomOne', 'MeetingRoomTwo']) and PayloadData.split(': ')[1] == 'low':
    #         print('tap 4')
    #         t1 = threading.Thread(target=env["space_dict"][Location]['device_dict']['AirPurifier'].action_on,
    #                               args=(env["space_dict"][Location]['device_dict']['AirPurifier'], env, 'app',))
    #         t1.start()

    #         thread_list.append(t1)
    
    # if Name == 'human_undetected':
    #     if Location in ['Lab', 'MeetingRoomOne', 'MeetingRoomTwo']:
    #         print('tap 5')
    #         t1 = threading.Thread(target=env["space_dict"][Location]['device_dict']['Light'].action_off,
    #                               args=(env["space_dict"][Location]['device_dict']['Light'], env, 'app',))
    #         t1.start()

    #         thread_list.append(t1)
    if Name == 'human_undetected':
        if Location in ['Lab', 'MeetingRoomOne', 'MeetingRoomTwo']:
            print('tap 7')
            t1 = threading.Thread(target=env["space_dict"][Location]['device_dict']['AC'].action_off,
                                  args=(env["space_dict"][Location]['device_dict']['AC'], env, 'app',))
            t1.start()
            thread_list.append(t1)
    if Name == 'human_undetected':
        if Location in ['MeetingRoomOne', 'MeetingRoomTwo']:
            print('tap 6')
            t1 = threading.Thread(target=env["space_dict"][Location]['device_dict']['TV'].action_off,
                                  args=(env["space_dict"][Location]['device_dict']['TV'], env, 'app',))
            t1.start()
            thread_list.append(t1)