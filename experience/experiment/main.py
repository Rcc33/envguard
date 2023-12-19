from copy import deepcopy
import datetime,os
import random
import time
import pandas as pd
# from safetyProperty.mtl import regulations,ltlRegulations 
from safetyProperty.homeMTL import regulations,ltlRegulations 
import Environment

start = datetime.datetime.now()  
detect = datetime.datetime.now()
end = datetime.datetime.now()

def check(regulation, indexs):
    line = deepcopy(indexs)
    temp_env = deepcopy(Environment.getEnv())
    if (df.shape)[0] == line:
        return
    time_stamp = int(time.mktime(time.strptime(df.iat[line, 4], "%Y-%m-%d %H:%M:%S")))
    end_time_stamp = int(time.mktime(time.strptime(df.iat[line-1, 4], "%Y-%m-%d %H:%M:%S"))) + eval(regulation['time'])
    if regulation['flag'] == 'F':
        while time_stamp <= end_time_stamp:
            ### 改变状态
            state = df.iat[line, 3]
            value = df.iat[line, 5].split(': ')[1]
            if df.iat[line, 3] == 'Human':
                state = 'HumanState'
            if df.iat[line, 6] == 'Environment Change':  
                (Environment.getEnv())['space_dict'][df.iat[line, 2]]['env_state'][state].value = value
            else:
                (Environment.getEnv())['space_dict'][df.iat[line, 2]]['device_dict'][state].on = value
            ### 检查condition
            condition = regulation['condition'].replace("env['space_dict']","(Environment.getEnv())['space_dict']")
            if eval(condition):
                ### 冲突标注
                undo = ''
                if regulation['undo']:
                    if regulation['undo'] == 'trigger':
                        if df.iat[indexs-1, 1] == 'Action':
                            value = df.iat[indexs-1, 5].split(': ')[1]
                            if value == '1':
                                undo = df.iat[indexs-1, 2] + '.' + df.iat[indexs-1, 3] + '.action_off'
                            else:
                                undo = df.iat[indexs-1, 2] + '.' + df.iat[indexs-1, 3] + '.action_on'   
                    else:
                        undo = regulation['undo']
                else:
                    if df.iat[indexs-1, 1] == 'Action':
                        value = df.iat[indexs-1, 5].split(': ')[1]
                        if value == '1':
                            undo = df.iat[indexs-1, 2] + '.' + df.iat[indexs-1, 3] + '.action_off'
                        else:
                            undo = df.iat[indexs-1, 2] + '.' + df.iat[indexs-1, 3] + '.action_on'
                if regulation['contact'] == 'or':
                    fix_list = []
                    for fix in regulation['fix']:
                        f = fix[1].replace("env['space_dict']","(Environment.getEnv())['space_dict']")
                        if fix[1] and eval(f):
                            fix_list.append(fix[0])
                        elif not fix[1]:
                            fix_list.append(fix[0])
                    if len(fix_list) == 1 and fix_list[0] == undo:
                        if df.iat[indexs-1, 9]:
                            df.iat[indexs-1, 9] = df.iat[indexs-1, 9] + ', ' + 'Undo'
                        else:
                            df.iat[indexs-1, 9] = 'Undo'
                        if df.iat[indexs-1, 8]:
                            df.iat[indexs-1, 8] = df.iat[indexs-1, 8] + ', ' + '(' + undo + ')'
                        else:
                            df.iat[indexs-1, 8] = '(' + undo + ')'
                    else:
                        if df.iat[indexs-1, 9]:
                            df.iat[indexs-1, 9] = df.iat[indexs-1, 9] + ', ' + 'Repair'
                        else:
                            df.iat[indexs-1, 9] = 'Repair'
                        if df.iat[indexs-1, 8]:
                            df.iat[indexs-1, 8] = df.iat[indexs-1, 8] + ', ' + '(' + ' or '.join(fix_list)+ ')'
                        else:
                            df.iat[indexs-1, 8] = '(' + ' or '.join(fix_list) + ')'  
                if df.iat[indexs-1, 7]:
                    df.iat[indexs-1, 7] = df.iat[indexs-1, 7] + '; ' + regulation['mtl']
                else:
                    df.iat[indexs-1, 7] = regulation['mtl']                            
                break
            line = line + 1 
            if (df.shape)[0] == line:
                Environment.setEnv(temp_env)
                return
            time_stamp = int(time.mktime(time.strptime(df.iat[line, 4], "%Y-%m-%d %H:%M:%S")))
        Environment.setEnv(temp_env)     
    else:
        global start
        start = datetime.datetime.now() 
        while time_stamp <= end_time_stamp:
            ### 改变状态
            state = df.iat[line, 3]
            value = df.iat[line, 5].split(': ')[1]
            if df.iat[line, 3] == 'Human':
                state = 'HumanState'
            if df.iat[line, 6] == 'Environment Change':  
                (Environment.getEnv())['space_dict'][df.iat[line, 2]]['env_state'][state].value = value
            else:
                (Environment.getEnv())['space_dict'][df.iat[line, 2]]['device_dict'][state].on = value
            ### 检查condition
            condition = regulation['condition'].replace("env['space_dict']","(Environment.getEnv())['space_dict']")
            if not eval(condition):
                # global end
                # end = datetime.datetime.now() 
                # print('  不违规：', end - start)  
                
                Environment.setEnv(temp_env)
                # print()  
                return
            line = line + 1 
            if (df.shape)[0] == line:
                break
            time_stamp = int(time.mktime(time.strptime(df.iat[line, 4], "%Y-%m-%d %H:%M:%S")))
        # global detect
        # detect = datetime.datetime.now() 
        # print('检测：', detect - start)
        ### 冲突标注  
        undo = ""
        if regulation['undo']:
            if regulation['undo'] == 'trigger':
                if df.iat[indexs-1, 1] == 'Action':
                    value = df.iat[indexs-1, 5].split(': ')[1]
                    if value == '1':
                        undo = df.iat[indexs-1, 2] + '.' + df.iat[indexs-1, 3] + '.action_off'
                    else:
                        undo = df.iat[indexs-1, 2] + '.' + df.iat[indexs-1, 3] + '.action_on'   
            else:
                undo = regulation['undo']
        else:
            if df.iat[indexs-1, 1] == 'Action':
                value = df.iat[indexs-1, 5].split(': ')[1]
                if value == '1':
                    undo = df.iat[indexs-1, 2] + '.' + df.iat[indexs-1, 3] + '.action_off'
                else:
                    undo = df.iat[indexs-1, 2] + '.' + df.iat[indexs-1, 3] + '.action_on'
        if regulation['contact'] == 'or':
            fix_list = []
            for fix in regulation['fix']:
                f = fix[1].replace("env['space_dict']","(Environment.getEnv())['space_dict']")
                if fix[1] and eval(f):
                    fix_list.append(fix[0])
                elif not fix[1]:
                    fix_list.append(fix[0])
            if len(fix_list) == 1 and fix_list[0] == undo:
                if df.iat[indexs-1, 9]:
                    df.iat[indexs-1, 9] = df.iat[indexs-1, 9] + ', ' + 'Undo'
                else:
                    df.iat[indexs-1, 9] = 'Undo'
                if df.iat[indexs-1, 8]:
                    df.iat[indexs-1, 8] = df.iat[indexs-1, 8] + ', ' + '(' + undo + ')'
                else:
                    df.iat[indexs-1, 8] = '(' + undo + ')'
            else:
                if df.iat[indexs-1, 9]:
                    df.iat[indexs-1, 9] = df.iat[indexs-1, 9] + ', ' + 'Repair'
                else:
                    df.iat[indexs-1, 9] = 'Repair'
                if df.iat[indexs-1, 8]:
                    df.iat[indexs-1, 8] = df.iat[indexs-1, 8] + ', ' + '(' + ' or '.join(fix_list)+ ')'
                else:
                    df.iat[indexs-1, 8] = '(' + ' or '.join(fix_list) + ')'  
        if df.iat[indexs-1, 7]:
            df.iat[indexs-1, 7] = df.iat[indexs-1, 7] + '; ' + regulation['mtl']
        else:
            df.iat[indexs-1, 7] = regulation['mtl']   
        # global end
        # end = datetime.datetime.now() 
        # print('修复：', end - start)  
    # print()          
    Environment.setEnv(temp_env)
    
if __name__ == '__main__':
    # for item in regulations:
    #     print(item)
    #     print()

    # for item in ltlRegulations:
    #     print(item)
    #     print()
    # print()
         
    # for item in range(4, 18):
    #     file = '../benchmark/data/output_day_' + str(item) + '.xlsx'
    for item in range(10, 25):
        file = '../simulation_platform/data/Home/output_day_' + str(item) + '.xlsx'
        df = pd.DataFrame(pd.read_excel(file,keep_default_na=False))
        df['Property Violation'] = ''
        df['Resolving Action'] = ''
        for index, row in df.iterrows():   # Name Type Location Object TimeStamp PayloadData Source Conflict Fix Method
            state = df.iat[index, 3]
            value = df.iat[index, 5].split(': ')[1]
            if df.iat[index, 6] == 'Environment Change':  
                (Environment.getEnv())['space_dict'][df.iat[index, 2]]['env_state'][state].value = value
            else:
                (Environment.getEnv())['space_dict'][df.iat[index, 2]]['device_dict'][state].on = value
            for regulation in ltlRegulations: 
                trigger = regulation['trigger'].replace("env['space_dict']","(Environment.getEnv())['space_dict']")
                condition = regulation['condition'].replace("env['space_dict']","(Environment.getEnv())['space_dict']")
                # print(regulation['ltl'])
                # print(trigger)
                # print(condition)
                # print()
                # start = datetime.datetime.now()   
                if eval(trigger) and eval(condition):
                    # detect = datetime.datetime.now()
                    # time_detect = detect - start
                    # print('检测：', time_detect)
                    undo = ''
                    if df.iat[index, 1] == 'Action':
                        value = df.iat[index, 5].split(': ')[1]
                        if value == '1':
                            undo = df.iat[index, 2] + '.' + df.iat[index, 3] + '.action_off'
                        else:
                            undo = df.iat[index, 2] + '.' + df.iat[index, 3] + '.action_on'
                    if df.iat[index, 7]:
                        df.iat[index, 7] = df.iat[index, 7] + '; ' + regulation['ltl']
                    else:
                        df.iat[index, 7] = regulation['ltl']
                    fix_list = []
                    temp_fix = []
                    for i,fixs in enumerate(regulation['fix']):
                        list_one = []
                        for j,fix in enumerate(fixs):
                            f = fix[1].replace("env['space_dict']","(Environment.getEnv())['space_dict']")            
                            if fix[1] and eval(f):
                                list_one.append(fix[0])
                            elif not fix[1]:
                                list_one.append(fix[0])
                        temp_fix.append(list_one)
                    if regulation['flag'] == 'or':
                        for item in temp_fix:
                            for action in item:
                                fix_list.append(action)
                        if len(fix_list) == 1 and fix_list[0] == undo:
                            if df.iat[index, 8]:
                                df.iat[index, 8] = df.iat[index, 8] + ', ' + '(' + undo + ')'
                            else:
                                df.iat[index, 8] = '(' + undo + ')'     
                        else:
                            for i, item in enumerate(fix_list):
                                fix_list[i] = '(' + item + ')'
                            
                            if df.iat[index, 8]:
                                df.iat[index, 8] = df.iat[index, 8] + ', ' + '(' + ' or '.join(fix_list)+ ')'
                            else:
                                df.iat[index, 8] = '(' + ' or '.join(fix_list) + ')'      
                    # end = datetime.datetime.now()
                    # time_fix = end-detect
                    # time_total = end-start
                    # print('修复：', time_fix)
                    # print('总计：', time_total+time_detect)
                    # print()
            for regulation in regulations:
                trigger = regulation['trigger'].replace("env['space_dict']","(Environment.getEnv())['space_dict']")
                if eval(trigger):
                    # if index == 272 and regulation['mtl'] == "G((Corridor.AirQuality.low & Corridor.HumanState.detected) -> (F[0, 10*60] Corridor.air_quality_up))":
                    #     print(index, df.iat[index, 0])
                    check(regulation, index+1)
        df.to_excel(file, index=False)        

    