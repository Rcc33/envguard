import Environment
import pandas as pd
from copy import deepcopy
import time

def funcHome():
  for item in range(2, 30):
    file = '../envguard-dataset/data/Home/output_day_' + str(item) + '.xlsx'
    df = pd.DataFrame(pd.read_excel(file, keep_default_na=False))
    for index, row in df.iterrows():   # Name Type Location Object TimeStamp PayloadData Source Conflict Fix Method
      state = df.iat[index, 3]
      if df.iat[index, 6] == 'None':
        (Environment.getEnv())['space_dict'][df.iat[index, 2]]['env_state'][state].value = df.iat[index, 5].split(': ')[1]
      else:
        (Environment.getEnv())['space_dict'][df.iat[index, 2]]['device_dict'][state].on = df.iat[index, 5].split(': ')[1]
      if df.iat[index, 7] == 'G!(BedroomOne.temperature_up&BedroomOne.temperature_down)':
        temp_env = deepcopy(Environment.getEnv())
        time_stamp = int(time.mktime(time.strptime(df.iat[index, 4], "%Y-%m-%d %H:%M:%S")))
        end_time_stamp = int(time.mktime(time.strptime(df.iat[index, 4], "%Y-%m-%d %H:%M:%S"))) + 300
        line = deepcopy(index)
        while time_stamp <= end_time_stamp:
          line = line + 1
          state = df.iat[line, 3]
          if (df.shape)[0] == line:
            break
          if df.iat[line, 6] == 'None':
            (Environment.getEnv())['space_dict'][df.iat[line, 2]]['env_state'][state].value = df.iat[line, 5].split(': ')[1]
          else:
            (Environment.getEnv())['space_dict'][df.iat[line, 2]]['device_dict'][state].on = df.iat[line, 5].split(': ')[1]
          if "BedroomOne." + df.iat[index, 3] + ".state: 0" in df.iat[line, 5] or (not ((((Environment.getEnv())['space_dict']['BedroomOne']['device_dict']['Window'].get()==1  and  (((Environment.getEnv())['space_dict']['Context']['env_state']['Temperature'].get()==1 and (Environment.getEnv())['space_dict']['BedroomOne']['env_state']['Temperature'].get()==0) or ((Environment.getEnv())['space_dict']['Context']['env_state']['Temperature'].get()==1 and (Environment.getEnv())['space_dict']['BedroomOne']['env_state']['Temperature'].get()==-1) or ((Environment.getEnv())['space_dict']['Context']['env_state']['Temperature'].get()==0 and (Environment.getEnv())['space_dict']['BedroomOne']['env_state']['Temperature'].get()==-1))) or ((Environment.getEnv())['space_dict']['BedroomOne']['device_dict']['Heater'].get()==1)) and (((Environment.getEnv())['space_dict']['BedroomOne']['device_dict']['AC'].get()==1) or ((Environment.getEnv())['space_dict']['BedroomOne']['device_dict']['Window'].get()==1 and (((Environment.getEnv())['space_dict']['BedroomOne']['env_state']['Temperature'].get()==1 and (Environment.getEnv())['space_dict']['Context']['env_state']['Temperature'].get()==0) or ((Environment.getEnv())['space_dict']['BedroomOne']['env_state']['Temperature'].get() ==1  and  (Environment.getEnv())['space_dict']['Context']['env_state']['Temperature'].get() ==-1)  or  ((Environment.getEnv())['space_dict']['BedroomOne']['env_state']['Temperature'].get()==0 and (Environment.getEnv())['space_dict']['Context']['env_state']['Temperature'].get()==-1)))))):
            df.iat[index, 7] = ''
            df.iat[index, 8] = ''
            df.iat[index, 9] = ''
            break
          time_stamp = int(time.mktime(time.strptime(df.iat[line, 4], "%Y-%m-%d %H:%M:%S")))
        Environment.setEnv(temp_env)
      if df.iat[index, 7] == 'G!(BedroomTwo.temperature_up&BedroomTwo.temperature_down)':
        temp_env = deepcopy(Environment.getEnv())
        time_stamp = int(time.mktime(time.strptime(df.iat[index, 4], "%Y-%m-%d %H:%M:%S")))
        end_time_stamp = int(time.mktime(time.strptime(df.iat[index, 4], "%Y-%m-%d %H:%M:%S"))) + 300
        line = deepcopy(index)
        while time_stamp <= end_time_stamp:
          line = line + 1
          state = df.iat[line, 3]
          if (df.shape)[0] == line:
            break
          if df.iat[line, 6] == 'None':
            (Environment.getEnv())['space_dict'][df.iat[line, 2]]['env_state'][state].value = df.iat[line, 5].split(': ')[1]
          else:
            (Environment.getEnv())['space_dict'][df.iat[line, 2]]['device_dict'][state].on = df.iat[line, 5].split(': ')[1]
          if "BedroomTwo." + df.iat[index, 3] + ".state: 0" in df.iat[line, 5] or (not ((((Environment.getEnv())['space_dict']['BedroomTwo']['device_dict']['Window'].get()==1  and  (((Environment.getEnv())['space_dict']['Context']['env_state']['Temperature'].get()==1 and (Environment.getEnv())['space_dict']['BedroomTwo']['env_state']['Temperature'].get()==0) or ((Environment.getEnv())['space_dict']['Context']['env_state']['Temperature'].get()==1 and (Environment.getEnv())['space_dict']['BedroomTwo']['env_state']['Temperature'].get()==-1) or ((Environment.getEnv())['space_dict']['Context']['env_state']['Temperature'].get()==0 and (Environment.getEnv())['space_dict']['BedroomTwo']['env_state']['Temperature'].get()==-1))) or ((Environment.getEnv())['space_dict']['BedroomTwo']['device_dict']['Heater'].get()==1)) and (((Environment.getEnv())['space_dict']['BedroomTwo']['device_dict']['AC'].get()==1) or ((Environment.getEnv())['space_dict']['BedroomTwo']['device_dict']['Window'].get()==1 and (((Environment.getEnv())['space_dict']['BedroomTwo']['env_state']['Temperature'].get()==1 and (Environment.getEnv())['space_dict']['Context']['env_state']['Temperature'].get()==0) or ((Environment.getEnv())['space_dict']['BedroomTwo']['env_state']['Temperature'].get() ==1  and  (Environment.getEnv())['space_dict']['Context']['env_state']['Temperature'].get() ==-1)  or  ((Environment.getEnv())['space_dict']['BedroomTwo']['env_state']['Temperature'].get()==0 and (Environment.getEnv())['space_dict']['Context']['env_state']['Temperature'].get()==-1)))))):
            df.iat[index, 7] = ''
            df.iat[index, 8] = ''
            df.iat[index, 9] = ''
            break
          time_stamp = int(time.mktime(time.strptime(df.iat[line, 4], "%Y-%m-%d %H:%M:%S")))
        Environment.setEnv(temp_env)
      if df.iat[index, 7] == 'G!(LivingRoom.temperature_up&LivingRoom.temperature_down)':
        temp_env = deepcopy(Environment.getEnv())
        time_stamp = int(time.mktime(time.strptime(df.iat[index, 4], "%Y-%m-%d %H:%M:%S")))
        end_time_stamp = int(time.mktime(time.strptime(df.iat[index, 4], "%Y-%m-%d %H:%M:%S"))) + 300
        line = deepcopy(index)
        while time_stamp <= end_time_stamp:
          line = line + 1
          state = df.iat[line, 3]
          if (df.shape)[0] == line:
            break
          if df.iat[line, 6] == 'None':
            (Environment.getEnv())['space_dict'][df.iat[line, 2]]['env_state'][state].value = df.iat[line, 5].split(': ')[1]
          else:
            (Environment.getEnv())['space_dict'][df.iat[line, 2]]['device_dict'][state].on = df.iat[line, 5].split(': ')[1]
          if "LivingRoom." + df.iat[index, 3] + ".state: 0" in df.iat[line, 5] or (not ((((Environment.getEnv())['space_dict']['LivingRoom']['device_dict']['Window'].get()==1  and  (((Environment.getEnv())['space_dict']['Context']['env_state']['Temperature'].get()==1 and (Environment.getEnv())['space_dict']['LivingRoom']['env_state']['Temperature'].get()==0) or ((Environment.getEnv())['space_dict']['Context']['env_state']['Temperature'].get()==1 and (Environment.getEnv())['space_dict']['LivingRoom']['env_state']['Temperature'].get()==-1) or ((Environment.getEnv())['space_dict']['Context']['env_state']['Temperature'].get()==0 and (Environment.getEnv())['space_dict']['LivingRoom']['env_state']['Temperature'].get()==-1))) or ((Environment.getEnv())['space_dict']['LivingRoom']['device_dict']['Heater'].get()==1)) and (((Environment.getEnv())['space_dict']['LivingRoom']['device_dict']['AC'].get()==1) or ((Environment.getEnv())['space_dict']['LivingRoom']['device_dict']['Window'].get()==1 and (((Environment.getEnv())['space_dict']['LivingRoom']['env_state']['Temperature'].get()==1 and (Environment.getEnv())['space_dict']['Context']['env_state']['Temperature'].get()==0) or ((Environment.getEnv())['space_dict']['LivingRoom']['env_state']['Temperature'].get() ==1  and  (Environment.getEnv())['space_dict']['Context']['env_state']['Temperature'].get() ==-1)  or  ((Environment.getEnv())['space_dict']['LivingRoom']['env_state']['Temperature'].get()==0 and (Environment.getEnv())['space_dict']['Context']['env_state']['Temperature'].get()==-1)))))):
            df.iat[index, 7] = ''
            df.iat[index, 8] = ''
            df.iat[index, 9] = ''
            break
          time_stamp = int(time.mktime(time.strptime(df.iat[line, 4], "%Y-%m-%d %H:%M:%S")))
        Environment.setEnv(temp_env)
      if df.iat[index, 7] == 'G!(BedroomOne.temperature_down&(BedroomOne.HumanState.detected&BedroomOne.Temperature.low))':
        temp_env = deepcopy(Environment.getEnv())
        time_stamp = int(time.mktime(time.strptime(df.iat[index, 4], "%Y-%m-%d %H:%M:%S")))
        end_time_stamp = int(time.mktime(time.strptime(df.iat[index, 4], "%Y-%m-%d %H:%M:%S"))) + 300
        line = deepcopy(index)
        while time_stamp <= end_time_stamp:
          line = line + 1
          state = df.iat[line, 3]
          if (df.shape)[0] == line:
            break
          if df.iat[line, 6] == 'None':
            (Environment.getEnv())['space_dict'][df.iat[line, 2]]['env_state'][state].value = df.iat[line, 5].split(': ')[1]
          else:
            (Environment.getEnv())['space_dict'][df.iat[line, 2]]['device_dict'][state].on = df.iat[line, 5].split(': ')[1]
          if "BedroomOne." + df.iat[index, 3] + ".state: 0" in df.iat[line, 5] or (not (((Environment.getEnv())['space_dict']['BedroomOne']['env_state']['HumanState'].get() ==1 and (Environment.getEnv())['space_dict']['BedroomOne']['env_state']['Temperature'].get() ==-1) and ( not (((Environment.getEnv())['space_dict']['BedroomOne']['device_dict']['AC'].get() ==1)  or  ((Environment.getEnv())['space_dict']['BedroomOne']['device_dict']['Window'].get() ==1  and  (((Environment.getEnv())['space_dict']['BedroomOne']['env_state']['Temperature'].get() ==1  and  (Environment.getEnv())['space_dict']['Context']['env_state']['Temperature'].get() ==0)  or  ((Environment.getEnv())['space_dict']['BedroomOne']['env_state']['Temperature'].get() ==1  and  (Environment.getEnv())['space_dict']['Context']['env_state']['Temperature'].get() ==-1)  or  ((Environment.getEnv())['space_dict']['BedroomOne']['env_state']['Temperature'].get() ==0  and  (Environment.getEnv())['space_dict']['Context']['env_state']['Temperature'].get() ==-1))))))):
            df.iat[index, 7] = ''
            df.iat[index, 8] = ''
            df.iat[index, 9] = ''
            break
          time_stamp = int(time.mktime(time.strptime(df.iat[line, 4], "%Y-%m-%d %H:%M:%S")))
        Environment.setEnv(temp_env)
      if df.iat[index, 7] == 'G!(BedroomTwo.temperature_down&(BedroomTwo.HumanState.detected&BedroomTwo.Temperature.low))':
        temp_env = deepcopy(Environment.getEnv())
        time_stamp = int(time.mktime(time.strptime(df.iat[index, 4], "%Y-%m-%d %H:%M:%S")))
        end_time_stamp = int(time.mktime(time.strptime(df.iat[index, 4], "%Y-%m-%d %H:%M:%S"))) + 300
        line = deepcopy(index)
        while time_stamp <= end_time_stamp:
          line = line + 1
          state = df.iat[line, 3]
          if (df.shape)[0] == line:
            break
          if df.iat[line, 6] == 'None':
            (Environment.getEnv())['space_dict'][df.iat[line, 2]]['env_state'][state].value = df.iat[line, 5].split(': ')[1]
          else:
            (Environment.getEnv())['space_dict'][df.iat[line, 2]]['device_dict'][state].on = df.iat[line, 5].split(': ')[1]
          if "BedroomTwo." + df.iat[index, 3] + ".state: 0" in df.iat[line, 5] or (not (((Environment.getEnv())['space_dict']['BedroomTwo']['env_state']['HumanState'].get() ==1 and (Environment.getEnv())['space_dict']['BedroomTwo']['env_state']['Temperature'].get() ==-1) and ( not (((Environment.getEnv())['space_dict']['BedroomTwo']['device_dict']['AC'].get() ==1)  or  ((Environment.getEnv())['space_dict']['BedroomTwo']['device_dict']['Window'].get() ==1  and  (((Environment.getEnv())['space_dict']['BedroomTwo']['env_state']['Temperature'].get() ==1  and  (Environment.getEnv())['space_dict']['Context']['env_state']['Temperature'].get() ==0)  or  ((Environment.getEnv())['space_dict']['BedroomTwo']['env_state']['Temperature'].get() ==1  and  (Environment.getEnv())['space_dict']['Context']['env_state']['Temperature'].get() ==-1)  or  ((Environment.getEnv())['space_dict']['BedroomTwo']['env_state']['Temperature'].get() ==0  and  (Environment.getEnv())['space_dict']['Context']['env_state']['Temperature'].get() ==-1))))))):
            df.iat[index, 7] = ''
            df.iat[index, 8] = ''
            df.iat[index, 9] = ''
            break
          time_stamp = int(time.mktime(time.strptime(df.iat[line, 4], "%Y-%m-%d %H:%M:%S")))
        Environment.setEnv(temp_env)
      if df.iat[index, 7] == 'G!(LivingRoom.temperature_down&(LivingRoom.HumanState.detected&LivingRoom.Temperature.low))':
        temp_env = deepcopy(Environment.getEnv())
        time_stamp = int(time.mktime(time.strptime(df.iat[index, 4], "%Y-%m-%d %H:%M:%S")))
        end_time_stamp = int(time.mktime(time.strptime(df.iat[index, 4], "%Y-%m-%d %H:%M:%S"))) + 300
        line = deepcopy(index)
        while time_stamp <= end_time_stamp:
          line = line + 1
          state = df.iat[line, 3]
          if (df.shape)[0] == line:
            break
          if df.iat[line, 6] == 'None':
            (Environment.getEnv())['space_dict'][df.iat[line, 2]]['env_state'][state].value = df.iat[line, 5].split(': ')[1]
          else:
            (Environment.getEnv())['space_dict'][df.iat[line, 2]]['device_dict'][state].on = df.iat[line, 5].split(': ')[1]
          if "LivingRoom." + df.iat[index, 3] + ".state: 0" in df.iat[line, 5] or (not (((Environment.getEnv())['space_dict']['LivingRoom']['env_state']['HumanState'].get() ==1 and (Environment.getEnv())['space_dict']['LivingRoom']['env_state']['Temperature'].get() ==-1) and ( not (((Environment.getEnv())['space_dict']['LivingRoom']['device_dict']['AC'].get() ==1)  or  ((Environment.getEnv())['space_dict']['LivingRoom']['device_dict']['Window'].get() ==1  and  (((Environment.getEnv())['space_dict']['LivingRoom']['env_state']['Temperature'].get() ==1  and  (Environment.getEnv())['space_dict']['Context']['env_state']['Temperature'].get() ==0)  or  ((Environment.getEnv())['space_dict']['LivingRoom']['env_state']['Temperature'].get() ==1  and  (Environment.getEnv())['space_dict']['Context']['env_state']['Temperature'].get() ==-1)  or  ((Environment.getEnv())['space_dict']['LivingRoom']['env_state']['Temperature'].get() ==0  and  (Environment.getEnv())['space_dict']['Context']['env_state']['Temperature'].get() ==-1))))))):
            df.iat[index, 7] = ''
            df.iat[index, 8] = ''
            df.iat[index, 9] = ''
            break
          time_stamp = int(time.mktime(time.strptime(df.iat[line, 4], "%Y-%m-%d %H:%M:%S")))
        Environment.setEnv(temp_env)
    time.sleep(1)
    df.to_excel(file, index=False)

def funcLab():
  for item in range(2, 30):
    file = '../envguard-dataset/data/Lab/output_day_' + str(item) + '.xlsx'
    df = pd.DataFrame(pd.read_excel(file, keep_default_na=False))
    for index, row in df.iterrows():   # Name Type Location Object TimeStamp PayloadData Source Conflict Fix Method
      
      state = df.iat[index, 3]
      if df.iat[index, 6] == 'None':
        (Environment.getEnv())['space_dict'][df.iat[index, 2]]['env_state'][state].value = df.iat[index, 5].split(': ')[1]
      else:
        (Environment.getEnv())['space_dict'][df.iat[index, 2]]['device_dict'][state].on = df.iat[index, 5].split(': ')[1]
      if 'G!(Lab.temperature_up&Lab.temperature_down)' in df.iat[index, 7]:
        temp_env = deepcopy(Environment.getEnv())
        time_stamp = int(time.mktime(time.strptime(df.iat[index, 4], "%Y-%m-%d %H:%M:%S")))
        end_time_stamp = int(time.mktime(time.strptime(df.iat[index, 4], "%Y-%m-%d %H:%M:%S"))) + 300
        line = deepcopy(index)
        while time_stamp <= end_time_stamp:
          line = line + 1
          if (df.shape)[0] == line:
            break
          state = df.iat[line, 3]
          
          if df.iat[line, 6] == 'None':
            (Environment.getEnv())['space_dict'][df.iat[line, 2]]['env_state'][state].value = df.iat[line, 5].split(': ')[1]
          else:
            (Environment.getEnv())['space_dict'][df.iat[line, 2]]['device_dict'][state].on = df.iat[line, 5].split(': ')[1]
          
          if "Lab." + df.iat[index, 3] + ".state: 0" in df.iat[line, 5] or (not ((((Environment.getEnv())['space_dict']['Lab']['device_dict']['Window'].get()==1  and  (((Environment.getEnv())['space_dict']['Context']['env_state']['Temperature'].get()==1 and (Environment.getEnv())['space_dict']['Lab']['env_state']['Temperature'].get()==0) or ((Environment.getEnv())['space_dict']['Context']['env_state']['Temperature'].get()==1 and (Environment.getEnv())['space_dict']['Lab']['env_state']['Temperature'].get()==-1) or ((Environment.getEnv())['space_dict']['Context']['env_state']['Temperature'].get()==0 and (Environment.getEnv())['space_dict']['Lab']['env_state']['Temperature'].get()==-1))) or ((Environment.getEnv())['space_dict']['Lab']['device_dict']['Heater'].get()==1)) and (((Environment.getEnv())['space_dict']['Lab']['device_dict']['AC'].get()==1) or ((Environment.getEnv())['space_dict']['Lab']['device_dict']['Window'].get()==1 and (((Environment.getEnv())['space_dict']['Lab']['env_state']['Temperature'].get()==1 and (Environment.getEnv())['space_dict']['Context']['env_state']['Temperature'].get()==0) or ((Environment.getEnv())['space_dict']['Lab']['env_state']['Temperature'].get() ==1  and  (Environment.getEnv())['space_dict']['Context']['env_state']['Temperature'].get() ==-1)  or  ((Environment.getEnv())['space_dict']['Lab']['env_state']['Temperature'].get()==0 and (Environment.getEnv())['space_dict']['Context']['env_state']['Temperature'].get()==-1)))))):
            df.iat[index, 7] = ''
            df.iat[index, 8] = ''
            df.iat[index, 9] = ''
            break
          time_stamp = int(time.mktime(time.strptime(df.iat[line, 4], "%Y-%m-%d %H:%M:%S")))
        Environment.setEnv(temp_env)
      if df.iat[index, 7] == 'G!(TeaRoom.temperature_up&TeaRoom.temperature_down)':
        temp_env = deepcopy(Environment.getEnv())
        time_stamp = int(time.mktime(time.strptime(df.iat[index, 4], "%Y-%m-%d %H:%M:%S")))
        end_time_stamp = int(time.mktime(time.strptime(df.iat[index, 4], "%Y-%m-%d %H:%M:%S"))) + 300
        line = deepcopy(index)
        while time_stamp <= end_time_stamp:
          line = line + 1
          if (df.shape)[0] == line:
            break
          state = df.iat[line, 3]
          
          if df.iat[line, 6] == 'None':
            (Environment.getEnv())['space_dict'][df.iat[line, 2]]['env_state'][state].value = df.iat[line, 5].split(': ')[1]
          else:
            (Environment.getEnv())['space_dict'][df.iat[line, 2]]['device_dict'][state].on = df.iat[line, 5].split(': ')[1]
          if "TeaRoom." + df.iat[index, 3] + ".state: 0" in df.iat[line, 5] or (not ((((Environment.getEnv())['space_dict']['TeaRoom']['device_dict']['Window'].get()==1  and  (((Environment.getEnv())['space_dict']['Context']['env_state']['Temperature'].get()==1 and (Environment.getEnv())['space_dict']['TeaRoom']['env_state']['Temperature'].get()==0) or ((Environment.getEnv())['space_dict']['Context']['env_state']['Temperature'].get()==1 and (Environment.getEnv())['space_dict']['TeaRoom']['env_state']['Temperature'].get()==-1) or ((Environment.getEnv())['space_dict']['Context']['env_state']['Temperature'].get()==0 and (Environment.getEnv())['space_dict']['TeaRoom']['env_state']['Temperature'].get()==-1))) or ((Environment.getEnv())['space_dict']['TeaRoom']['device_dict']['Heater'].get()==1)) and (((Environment.getEnv())['space_dict']['TeaRoom']['device_dict']['AC'].get()==1) or ((Environment.getEnv())['space_dict']['TeaRoom']['device_dict']['Window'].get()==1 and (((Environment.getEnv())['space_dict']['TeaRoom']['env_state']['Temperature'].get()==1 and (Environment.getEnv())['space_dict']['Context']['env_state']['Temperature'].get()==0) or ((Environment.getEnv())['space_dict']['TeaRoom']['env_state']['Temperature'].get() ==1  and  (Environment.getEnv())['space_dict']['Context']['env_state']['Temperature'].get() ==-1)  or  ((Environment.getEnv())['space_dict']['TeaRoom']['env_state']['Temperature'].get()==0 and (Environment.getEnv())['space_dict']['Context']['env_state']['Temperature'].get()==-1)))))):
            df.iat[index, 7] = ''
            df.iat[index, 8] = ''
            df.iat[index, 9] = ''
            break
          time_stamp = int(time.mktime(time.strptime(df.iat[line, 4], "%Y-%m-%d %H:%M:%S")))
        Environment.setEnv(temp_env)
      if df.iat[index, 7] == 'G!(MeetingRoomOne.temperature_up&MeetingRoomOne.temperature_down)':
        temp_env = deepcopy(Environment.getEnv())
        time_stamp = int(time.mktime(time.strptime(df.iat[index, 4], "%Y-%m-%d %H:%M:%S")))
        end_time_stamp = int(time.mktime(time.strptime(df.iat[index, 4], "%Y-%m-%d %H:%M:%S"))) + 300
        line = deepcopy(index)
        while time_stamp <= end_time_stamp:
          line = line + 1
          if (df.shape)[0] == line:
            break
          state = df.iat[line, 3]
          
          if df.iat[line, 6] == 'None':
            (Environment.getEnv())['space_dict'][df.iat[line, 2]]['env_state'][state].value = df.iat[line, 5].split(': ')[1]
          else:
            (Environment.getEnv())['space_dict'][df.iat[line, 2]]['device_dict'][state].on = df.iat[line, 5].split(': ')[1]
          if "MeetingRoomOne." + df.iat[index, 3] + ".state: 0" in df.iat[line, 5] or (not ((((Environment.getEnv())['space_dict']['MeetingRoomOne']['device_dict']['Window'].get()==1  and  (((Environment.getEnv())['space_dict']['Context']['env_state']['Temperature'].get()==1 and (Environment.getEnv())['space_dict']['MeetingRoomOne']['env_state']['Temperature'].get()==0) or ((Environment.getEnv())['space_dict']['Context']['env_state']['Temperature'].get()==1 and (Environment.getEnv())['space_dict']['MeetingRoomOne']['env_state']['Temperature'].get()==-1) or ((Environment.getEnv())['space_dict']['Context']['env_state']['Temperature'].get()==0 and (Environment.getEnv())['space_dict']['MeetingRoomOne']['env_state']['Temperature'].get()==-1))) or ((Environment.getEnv())['space_dict']['MeetingRoomOne']['device_dict']['Heater'].get()==1)) and (((Environment.getEnv())['space_dict']['MeetingRoomOne']['device_dict']['AC'].get()==1) or ((Environment.getEnv())['space_dict']['MeetingRoomOne']['device_dict']['Window'].get()==1 and (((Environment.getEnv())['space_dict']['MeetingRoomOne']['env_state']['Temperature'].get()==1 and (Environment.getEnv())['space_dict']['Context']['env_state']['Temperature'].get()==0) or ((Environment.getEnv())['space_dict']['MeetingRoomOne']['env_state']['Temperature'].get() ==1  and  (Environment.getEnv())['space_dict']['Context']['env_state']['Temperature'].get() ==-1)  or  ((Environment.getEnv())['space_dict']['MeetingRoomOne']['env_state']['Temperature'].get()==0 and (Environment.getEnv())['space_dict']['Context']['env_state']['Temperature'].get()==-1)))))):
            df.iat[index, 7] = ''
            df.iat[index, 8] = ''
            df.iat[index, 9] = ''
            break
          time_stamp = int(time.mktime(time.strptime(df.iat[line, 4], "%Y-%m-%d %H:%M:%S")))
        Environment.setEnv(temp_env)
      if df.iat[index, 7] == 'G!(MeetingRoomTwo.temperature_up&MeetingRoomTwo.temperature_down)':
          temp_env = deepcopy(Environment.getEnv())
          time_stamp = int(time.mktime(time.strptime(df.iat[index, 4], "%Y-%m-%d %H:%M:%S")))
          end_time_stamp = int(time.mktime(time.strptime(df.iat[index, 4], "%Y-%m-%d %H:%M:%S"))) + 300
          line = deepcopy(index)
          while time_stamp <= end_time_stamp:
            line = line + 1
            if (df.shape)[0] == line:
              break
            state = df.iat[line, 3]
            if df.iat[line, 6] == 'None':
              (Environment.getEnv())['space_dict'][df.iat[line, 2]]['env_state'][state].value = df.iat[line, 5].split(': ')[1]
            else:
              (Environment.getEnv())['space_dict'][df.iat[line, 2]]['device_dict'][state].on = df.iat[line, 5].split(': ')[1]
            if "MeetingRoomTwo." + df.iat[index, 3] + ".state: 0" in df.iat[line, 5] or (not ((((Environment.getEnv())['space_dict']['MeetingRoomTwo']['device_dict']['Window'].get()==1  and  (((Environment.getEnv())['space_dict']['Context']['env_state']['Temperature'].get()==1 and (Environment.getEnv())['space_dict']['MeetingRoomTwo']['env_state']['Temperature'].get()==0) or ((Environment.getEnv())['space_dict']['Context']['env_state']['Temperature'].get()==1 and (Environment.getEnv())['space_dict']['MeetingRoomTwo']['env_state']['Temperature'].get()==-1) or ((Environment.getEnv())['space_dict']['Context']['env_state']['Temperature'].get()==0 and (Environment.getEnv())['space_dict']['MeetingRoomTwo']['env_state']['Temperature'].get()==-1))) or ((Environment.getEnv())['space_dict']['MeetingRoomTwo']['device_dict']['Heater'].get()==1)) and (((Environment.getEnv())['space_dict']['MeetingRoomTwo']['device_dict']['AC'].get()==1) or ((Environment.getEnv())['space_dict']['MeetingRoomTwo']['device_dict']['Window'].get()==1 and (((Environment.getEnv())['space_dict']['MeetingRoomTwo']['env_state']['Temperature'].get()==1 and (Environment.getEnv())['space_dict']['Context']['env_state']['Temperature'].get()==0) or ((Environment.getEnv())['space_dict']['MeetingRoomTwo']['env_state']['Temperature'].get() ==1  and  (Environment.getEnv())['space_dict']['Context']['env_state']['Temperature'].get() ==-1)  or  ((Environment.getEnv())['space_dict']['MeetingRoomTwo']['env_state']['Temperature'].get()==0 and (Environment.getEnv())['space_dict']['Context']['env_state']['Temperature'].get()==-1)))))):
              df.iat[index, 7] = ''
              df.iat[index, 8] = ''
              df.iat[index, 9] = ''
              break
            time_stamp = int(time.mktime(time.strptime(df.iat[line, 4], "%Y-%m-%d %H:%M:%S")))
          Environment.setEnv(temp_env)
      if df.iat[index, 7] == 'G(Lab.Brightness.high&Lab.HumanState.detected)':
          temp_env = deepcopy(Environment.getEnv())
          time_stamp = int(time.mktime(time.strptime(df.iat[index, 4], "%Y-%m-%d %H:%M:%S")))
          end_time_stamp = int(time.mktime(time.strptime(df.iat[index, 4], "%Y-%m-%d %H:%M:%S"))) + 30
          line = deepcopy(index)
          while time_stamp <= end_time_stamp:
            line = line + 1
            if (df.shape)[0] == line:
              break
            state = df.iat[line, 3]
            if df.iat[line, 6] == 'None':
              (Environment.getEnv())['space_dict'][df.iat[line, 2]]['env_state'][state].value = df.iat[line, 5].split(': ')[1]
            else:
              (Environment.getEnv())['space_dict'][df.iat[line, 2]]['device_dict'][state].on = df.iat[line, 5].split(': ')[1]
            if "human_undetected" == df.iat[index, 0] or ((Environment.getEnv())['space_dict']['Lab']['env_state']['Brightness'].get()==1 and (Environment.getEnv())['space_dict']['Lab']['env_state']['HumanState'].get()==1):
              df.iat[index, 7] = ''
              df.iat[index, 8] = ''
              df.iat[index, 9] = ''
              break
            time_stamp = int(time.mktime(time.strptime(df.iat[line, 4], "%Y-%m-%d %H:%M:%S")))
          Environment.setEnv(temp_env)
    
    df.to_excel(file, index=False)


# funcHome()
funcLab()