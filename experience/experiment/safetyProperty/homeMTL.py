import requests
import os,sys,re
BASE_DIR = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
sys.path.append(BASE_DIR)

from Environment import env,device_list,state_list

time_template = {
    "trigger":"",
    "time":"",
    "condition":"",
    "fix":""
}

template = {
  "trigger":"",
  "condition":"",
  "fix":"",
  "flag":''
}

LTL = {
  "G !(BedroomOne.temperature_up & BedroomOne.temperature_down)",
  "G !(BedroomTwo.temperature_up & BedroomTwo.temperature_down)",
  "G !(LivingRoom.temperature_up & LivingRoom.temperature_down)",
  "G !(Kitchen.temperature_up & Kitchen.temperature_down)",
  
  "G !(BedroomOne.temperature_down & (BedroomOne.HumanState.detected & BedroomOne.Temperature.low))",
  "G !(BedroomTwo.temperature_down & (BedroomTwo.HumanState.detected & BedroomTwo.Temperature.low))",
  "G !(LivingRoom.temperature_down & (LivingRoom.HumanState.detected & LivingRoom.Temperature.low))",
  "G !(Kitchen.temperature_down & (Kitchen.HumanState.detected & Kitchen.Temperature.low))",
  "G !(Balcony.temperature_down & (Balcony.HumanState.detected & Balcony.Temperature.low))",
  
  "G !(BedroomOne.HumanState.undetected & BedroomTwo.HumanState.undetected & LivingRoom.HumanState.undetected & Kitchen.HumanState.undetected & Balcony.HumanState.undetected & Bathroom.HumanState.undetected & Cloakroom.HumanState.undetected & BedroomOne.Curtain.on)",
  "G !(BedroomOne.HumanState.undetected & BedroomTwo.HumanState.undetected & LivingRoom.HumanState.undetected & Kitchen.HumanState.undetected & Balcony.HumanState.undetected & Bathroom.HumanState.undetected & Cloakroom.HumanState.undetected & BedroomTwo.Curtain.on)",
  # "G !(BedroomOne.HumanState.undetected & BedroomTwo.HumanState.undetected & LivingRoom.HumanState.undetected & Kitchen.HumanState.undetected & Balcony.HumanState.undetected & Bathroom.HumanState.undetected & Cloakroom.HumanState.undetected & Balcony.Curtain.on)",
  # "G !(BedroomOne.HumanState.undetected & BedroomTwo.HumanState.undetected & LivingRoom.HumanState.undetected & Kitchen.HumanState.undetected & Balcony.HumanState.undetected & Bathroom.HumanState.undetected & Cloakroom.HumanState.undetected & LivingRoom.Curtain.on)",
  # "G !(BedroomOne.HumanState.undetected & BedroomTwo.HumanState.undetected & LivingRoom.HumanState.undetected & Kitchen.HumanState.undetected & Balcony.HumanState.undetected & Bathroom.HumanState.undetected & Cloakroom.HumanState.undetected & Kitchen.Curtain.on)",
  
  "G !(Context.Weather.raining & BedroomOne.Window.on)",
  "G !(Context.Weather.raining & BedroomTwo.Window.on)",
  "G !(Context.Weather.raining & LivingRoom.Window.on)",
  "G !(Context.Weather.raining & Kitchen.Window.on)",
  "G !(Context.Weather.raining & Balcony.Window.on)",
}
 
EventState = {
  "G (BedroomOne.curtain_on & !(BedroomOne.HumanState.undetected))",
  "G (BedroomTwo.curtain_on & !(BedroomTwo.HumanState.undetected))",
}

MTL = [
  "G(BedroomOne.humidity_up -> (F[0, 60*60] !BedroomOne.humidity_up))",
  "G(BedroomTwo.humidity_up -> (F[0, 60*60] !BedroomTwo.humidity_up))",
  "G(LivingRoom.humidity_up -> (F[0, 60*60] !LivingRoom.humidity_up))",
  
  "G((Kitchen.AirQuality.low) -> (F[0, 5*60] Kitchen.air_quality_up))",
  
  "G(LivingRoom.human_undetected -> (F[0, 1*60] !(LivingRoom.Door.on)))",  
  
  "G((Kitchen.Fridge.on) -> (F[0, 3*60] !(Kitchen.Fridge.on)))",
  
  "G((Bathroom.TowelDryer.on) -> (F[0, 60*60] !(Bathroom.TowelDryer.on)))",
]
  
def getPreConditionLTL(preCondition):
    ltl = ''
    if preCondition != '':
        pre_condition_list = preCondition.split(' ')
        if len(pre_condition_list) == 3:
            temp_one_list = ''
            temp_two_list = ''
            if pre_condition_list[1] == '>':
                temp_one_list = pre_condition_list[0]
                temp_two_list = pre_condition_list[2]
            elif pre_condition_list[1] == '<':
                temp_one_list = pre_condition_list[2]
                temp_two_list = pre_condition_list[0]
            ltl = f'({temp_one_list}.high & {temp_two_list}.middle) | ' \
                  f'({temp_one_list}.high & {temp_two_list}.low) | ' \
                  f'({temp_one_list}.middle & {temp_two_list}.low)'
        elif len(pre_condition_list) == 5:
            temp_one_list = pre_condition_list[0]
            temp_two_list = pre_condition_list[2]
            if pre_condition_list[4] == '2':
                ltl = f'{temp_one_list}.high & {temp_two_list}.low'
            elif pre_condition_list[4] == '-2':
                ltl = f'{temp_one_list}.low & {temp_two_list}.high'
        elif len(pre_condition_list) == 7 and '&&' in pre_condition_list:
            temp_one_list = ''
            temp_two_list = ''
            if pre_condition_list[1] == '>':
                temp_one_list = pre_condition_list[0]
                temp_two_list = pre_condition_list[2]
            elif pre_condition_list[1] == '<':
                temp_one_list = pre_condition_list[2]
                temp_two_list = pre_condition_list[0]
            ltl = f'(({temp_one_list}.high & {temp_two_list}.middle) | ' \
                  f'({temp_one_list}.high & {temp_two_list}.low) | ' \
                  f'({temp_one_list}.middle & {temp_two_list}.low))'
            if pre_condition_list[6] == '0':
                ltl = ltl + f' & {pre_condition_list[4]}.off'
            elif pre_condition_list[6] == '1':
                ltl = ltl + f' & {pre_condition_list[4]}.on'
        elif len(pre_condition_list) == 11 and '&&' in pre_condition_list:
            temp_one_list = ''
            temp_two_list = ''
            if pre_condition_list[1] == '>':
                temp_one_list = pre_condition_list[0]
                temp_two_list = pre_condition_list[2]
            elif pre_condition_list[1] == '<':
                temp_one_list = pre_condition_list[2]
                temp_two_list = pre_condition_list[0]
            ltl = f'(({temp_one_list}.high & {temp_two_list}.middle) | ' \
                  f'({temp_one_list}.high & {temp_two_list}.low) | ' \
                  f'({temp_one_list}.middle & {temp_two_list}.low))'
            if pre_condition_list[6] == '0':
                ltl = ltl + f' & {pre_condition_list[4]}.off'
            elif pre_condition_list[6] == '1':
                ltl = ltl + f' & {pre_condition_list[4]}.on'
            if pre_condition_list[10] == '0':
                ltl = ltl + f' & {pre_condition_list[8]}.off'
            elif pre_condition_list[10] == '1':
                ltl = ltl + f' & {pre_condition_list[8]}.on'
    return ltl

def getLTL(list):
  result_list = []
  url = "http://47.101.169.122:5003/effect_node/" + list[0]+ '/effect_' + list[1]
  results = requests.get(url).json()
  for result in results:
    ltl_action = ''
    action_item = result['room'] + '.' + result['device'][0:len(result['device']) - 3] + '.' + result['action'][7:len(result['action'])]
    ltl_action = action_item
    pre_condition_item = getPreConditionLTL(result['pre_condition'])
    if pre_condition_item != '':
      ltl_action = ltl_action + ' & ' + '(' + pre_condition_item + ')'
    result_list.append('(' + ltl_action + ')')
  return result_list

def getActionPre(list):
  result_list = []
  url = "http://47.101.169.122:5003/effect_node/" + list[0]+ '/effect_' + list[1]
  results = requests.get(url).json()
  for result in results:
    ltl_action = ''
    action_item = result['room'] + '.' + result['device'][0:len(result['device']) - 3] + '.' + result['action'][7:len(result['action'])]
    ltl_action = action_item
    pre_condition_item = getPreConditionLTL(result['pre_condition'])
    # if pre_condition_item != '':
    #   ltl_action = ltl_action + ' & ' + '(' + pre_condition_item + ')'
    result_list.append([ltl_action, pre_condition_item])
  return result_list
      
def change(string):
  string_list = []
  iter = re.finditer(r'[a-zA-Z.!]+', string)
  for i in iter:
    value = i.group()
    if len(value.split('.')) == 2:
      return
    temp_value = value
    if '!' in value:
      symbol = '!='
    else:
      symbol = '=='
    if '!' in value:
      temp_value = value[1:]
    temp_list = temp_value.split('.')
    if temp_list[1] in device_list: 
      if temp_list[2] == 'on':
        end = 1
      else:
        end = 0
      temp = "env['space_dict']['" + temp_list[0] + "']['device_dict']['" + temp_list[1] + "'].get() "  + symbol + str(end)
    else:
      if temp_list[1] not in ['HumanState','Weather']: 
        if temp_list[2] == 'low':
          end = -1
        elif temp_list[2] == 'middle':
          end = 0
        else:
          end = 1
      elif temp_list[1] == 'HumanState':
        if temp_list[2] == 'detected':
          end = 1
        else:
          end = 0
      else:
        end = "'" + temp_list[2] + "'"
      temp = "env['space_dict']['" + temp_list[0] + "']['env_state']['" + temp_list[1] + "'].get() " +  symbol  + str(end)
    string_list.append([value,temp])
  return string_list

def getRegulation():
  regulation = []
  for mtl in MTL:
    trigger = ''
    condition = ''
    fix = []
    temp_mtl = mtl.replace(" ", "")
    temp_mtl = temp_mtl[2:-1]
    item_list = temp_mtl.split('->')
    front = item_list[0]
    end = item_list[1][1:-1]
    time_temp = re.search(r"[FG]\[[0-9,*]+\]",end).group()
    time = time_temp[2:-1].split(',')[1]
    end = end[len(time_temp):]
    if len(front.split('.')) == 2:  # 5/7
      if len(end.split('.')) == 2:  # 5
        effect_list = getLTL(front.split('.'))
        for item in effect_list:
          fix = []
          item = item.replace(' ','')
          action = re.search(r"[a-zA-Z.]+",item).group()
          room = action.split('.')[0]
          type = action.split('.')[1]
          value = action.split('.')[2]
          condition = item
          trigger_temp = change(condition)
          for i in trigger_temp:
            condition = condition.replace(i[0],i[1],1)
          condition = condition.replace("&", " and ")
          condition = condition.replace("|", " or ")
          pre_temp = change(item[2+len(action):-1])
          pre = item[2+len(action):-1]
          for i in pre_temp:
            pre = pre.replace(i[0],i[1],1)
          pre = pre.replace("&", " and ")
          pre = pre.replace("|", " or ")  
          if '!' in end: 
            # pre_value = ''
            match value:
              case 'on':
                # pre_value = '1'
                action = room + '.' + type + '.' + 'action_off'
              case 'off':
                # pre_value = '0'
                action = room + '.' + type + '.' + 'action_on'
            trigger = "'" + toSnake(type) + '_' + value + "'" + '==' + 'df.iat[index, 0]' +  ' and ' + "'" + room + "'" + '==' + 'df.iat[index, 2]'
            # if type in device_list:
            #   if pre:
            #     pre = '(' + pre + ')' + ' and ' + '(' +  pre_value + " == " + "env['space_dict']['" + room + "']['device_dict']['" + type + "'].get()" + ')'
            #   else:
            #     pre = '(' +  pre_value + " == " + "env['space_dict']['" + room + "']['device_dict']['" + type + "'].get()" + ')'
            fix.append([action,pre])
            regulation.append({
              "mtl":mtl,
              "trigger":trigger,
              "time":time,
              "condition":condition,
              "fix":fix,
              "flag":'G',
              "contact": 'or',
              'undo': action
            })  
          else:
            condition = ' not ' + '(' + condition + ')'
            action = room + '.' + type + '.' + 'action_' + value
            # pre_value = ''
            # match value:
            #   case 'on':
            #     pre_value = '0'
            #   case 'off':
            #     pre_value = '1'
            trigger = "'" + toSnake(type) + '_' + value + "'" + '==' + 'df.iat[index, 0]' +  ' and ' + "'" + room + "'" + '==' + 'df.iat[index, 2]'
            # if type in device_list:
            #   if pre:
            #     pre = '(' + pre + ')' + ' and ' + '(' +  pre_value + " == " + "env['space_dict']['" + room + "']['device_dict']['" + type + "'].get()" + ')'
            #   else:
            #     pre = '(' +  pre_value + " == " + "env['space_dict']['" + room + "']['device_dict']['" + type + "'].get()" + ')'
            fix.append([action, pre])
            regulation.append({
              "mtl":mtl,
              "trigger":trigger,
              "time":time,
              "condition":condition,
              "fix":fix,
              "flag":'F',
              "contact": 'or',
              'undo': action
            })     
      else:  # 7
        temp = front.split('.')
        trigger = "df.iat[index, 2] == " + "'"  + temp[0] + "'" + " and " + "df.iat[index, 0] == " + "'"  + temp[1] + "'"
        if end[0] == '!' :
          contact = 'or'
          undo = 'trigger'
          flag = 'G'
          condition = end[1:]
          temp_condition = change(end[1:])
          for state in end[2:-1].split('&'):
            for fix_item in getFix(state,False):
              fix.append(fix_item)
        else:
          undo = ''
          flag = 'F'
          contact = 'and'
          condition = end
          temp_condition = change(end)
          for state in end[1:-1].split('&'):
            for fix_item in getFix(state,True):
              fix.append(fix_item)
        for i in temp_condition:
          condition = condition.replace(i[0],i[1],1)
        if end[0] != '!' :  
          condition = ' not ' + '(' + condition + ')'
        condition = condition.replace('&', ' and ')
        condition = condition.replace('|', ' or ')
        regulation.append({
          "mtl":mtl,
          "trigger":trigger,
          "time":time,
          "condition":condition,
          "fix":fix,
          "flag":flag,
          "contact": 'or',
          "undo": undo
        })      
    else:   # 6/8
      if len(end.split('.')) == 2:  # 6        
        for item in front[1:-1].split('&'):
          if trigger:
            f = getAction(item,False)
            if f not in trigger:
              trigger = trigger + ' or ' + f
          else:
            trigger = getAction(item,False)
        condition_pre = front[1:-1]
        condition_pre_temp = change(condition_pre)
        for i in condition_pre_temp:
          condition_pre = condition_pre.replace(i[0],i[1],1)
        condition_pre = condition_pre.replace("&", " and ")
        condition_pre = condition_pre.replace("|", " or ")
        if '!' in end:
          undo = ''
          effect_list = getLTL(end[1:].split('.'))
        else:
          undo = 'Undo'
          effect_list = getLTL(end.split('.'))
        # condition = ' | '.join(effect_list)
        condition = ''
        fix = []
        for item in effect_list:
          item_condition = item
          item = item.replace(' ','')
          action = re.search(r"[a-zA-Z.]+",item).group()
          room = action.split('.')[0]
          type = action.split('.')[1]
          value = action.split('.')[2]          
          pre_temp = change(item[2+len(action):-1])
          pre = item[2+len(action):-1]
          for i in pre_temp:
            pre = pre.replace(i[0],i[1],1)
          pre = pre.replace("&", " and ")
          pre = pre.replace("|", " or ")  
          if '!' in end: 
            flag = 'F'
            contact = 'and'
            pre_value = ''
            match value:
              case 'on':
                pre_value = '1'
              case 'off':
                pre_value = '0'
            if value == 'on':
              action = room + '.' + type + '.' + 'action_off'
            else:
              action = room + '.' + type + '.' + 'action_on'
            if type in device_list:
              if pre:
                pre = '(' + pre + ')' + ' and ' + '(' +  pre_value + " == " + "env['space_dict']['" + room + "']['device_dict']['" + type + "'].get()" + ')'
              else:
                pre = '(' +  pre_value + " == " + "env['space_dict']['" + room + "']['device_dict']['" + type + "'].get()" + ')'
            fix.append([action,pre])
          else:
            flag= 'G'
            contact = 'or'
            pre_value = ''
            match value:
              case 'on':
                pre_value = '0'
              case 'off':
                pre_value = '1'
            if type in device_list:
              if pre:
                pre = '(' + pre + ')' + ' and ' + '(' +  pre_value + " == " + "env['space_dict']['" + room + "']['device_dict']['" + type + "'].get()" + ')'
              else:
                pre = '(' +  pre_value + " == " + "env['space_dict']['" + room + "']['device_dict']['" + type + "'].get()" + ')'
            action = room + '.' + type + '.' + 'action_' + value
            fix.append([action, pre])   
        
          condition_temp = change(item_condition)
          for i in condition_temp:
            item_condition = item_condition.replace(i[0],i[1],1)
          item_condition = item_condition.replace("&", " and ")
          item_condition = item_condition.replace("|", " or ")
          if condition:
            condition = '(' + item_condition + ')' + ' or ' + '(' +  condition + ')'
          else:
            condition = item_condition
        if '!' not in end:
          condition = ' not ' + '(' + condition + ')'
        condition = '(' + condition_pre + ')' + ' and ' + '(' +  condition + ')'
        regulation.append({
          "mtl":mtl,
          "trigger":trigger,
          "time":time,
          "condition":condition,
          "fix":fix,
          "flag":flag,
          "contact":contact,
          "undo":undo
        })  
      else:  # 8
        trigger = ''
        condition = ''
        fix = []
        for item in front[1:-1].split('&'):
          if trigger:
            trigger = trigger + ' or ' + getAction(item,False)
          else:
            trigger = getAction(item,False)
        if end[0] == '!' :
          contact = 'or'
          undo = 'trigger'
          flag = 'G'
          condition = end[1:]
          temp_condition = change(end[1:])
          for state in end[2:-1].split('&'):
            for fix_item in getFix(state,False):
              fix.append(fix_item)
        else:
          undo = ''
          flag = 'F'
          contact = 'and'
          condition = end
          temp_condition = change(end)
          for state in end[1:-1].split('&'):
            for fix_item in getFix(state,True):
              fix.append(fix_item)
        for i in temp_condition:
          condition = condition.replace(i[0],i[1],1)
        if end[0] != '!' :  
          condition = ' not ' + '(' + condition + ')'
        condition = condition.replace('&', ' and ')
        condition = condition.replace('|', ' or ')
        regulation.append({
          "mtl":mtl,
          "trigger":trigger,
          "time":time,
          "condition":condition,
          "fix":fix,
          "flag":flag,
          "contact":contact,
          "undo":undo
        })  
  return regulation

def getFix(state,flag):
  fix = []
  state_temp = state.split('.')
  room = state_temp[0]
  type = state_temp[1]
  value = state_temp[2]
  pre_value = ''
  match value:
    case 'on':
      pre_value = '1'
    case 'off':
      pre_value = '0'
    case 'high':
      pre_value = '1'
    case 'middle':
      pre_value = '0'
    case 'low':
      pre_value = '-1'
  if not flag:
    if type in device_list:
      # if value == 'on':
      #   fix.append([room + '.' + type + '.' + 'action_off',pre_value + " == " + "env['space_dict']['" + room + "']['device_dict']['" + type + "'].get()"])
      # else:
      #   fix.append([room + '.' + type + '.' + 'action_on',pre_value + " == " + "env['space_dict']['" + room + "']['device_dict']['" + type + "'].get()"])
        
      if value == 'on':
        fix.append([room + '.' + type + '.' + 'action_off',""])
      else:
        fix.append([room + '.' + type + '.' + 'action_on',""])
    else:
      if room != 'Context' and type != 'HumanState':
        if value == 'high':
          action_list = getActionPre([room, type.lower() + '_down'])
          for action_item in action_list:
            action_temp = action_item[0].split('.')
            action = action_temp[0] + '.' + action_temp[1] + '.'  + 'action_' + action_temp[2]
            pre = action_item[1]
            pre_list = change(pre)
            for i in pre_list:
              pre = pre.replace(i[0],i[1],1)
            if action_temp[2] == 'on':
              v = '0'
            else:
              v = '1'
            if pre:
              pre = '(' + pre + ')' + ' and ' + '(' +  pre_value + " == " + "env['space_dict']['" + room + "']['env_state']['" + type + "'].get()" + ' and ' + v + " == " + "env['space_dict']['" + action_temp[0] + "']['device_dict']['" + action_temp[1] + "'].get()" + ')'
            else:
              pre = '(' +  pre_value + " == " + "env['space_dict']['" + room + "']['env_state']['" + type + "'].get()" + ' and ' + v + " == " + "env['space_dict']['" + action_temp[0] + "']['device_dict']['" + action_temp[1] + "'].get()" + ')'
            pre = pre.replace('&', ' and ')
            pre = pre.replace('|', ' or ')
            action_item[0] = action
            action_item[1] = pre
            fix.append(action_item)
        elif value == 'middle':
          action_list = getActionPre([room, type.lower() + '_down'])
          for action_item in action_list:
            action_temp = action_item[0].split('.')
            action = action_temp[0] + '.' + action_temp[1] + '.'  + 'action_' + action_temp[2]
            pre = action_item[1]
            pre_list = change(pre)
            for i in pre_list:
              pre = pre.replace(i[0],i[1],1)
            if action_temp[2] == 'on':
              v = '0'
            else:
              v = '1'
            if pre:
              pre = '(' + pre + ')' + ' and ' + '(' +  pre_value + " == " + "env['space_dict']['" + room + "']['env_state']['" + type + "'].get()" + ' and ' + v + " == " + "env['space_dict']['" + action_temp[0] + "']['device_dict']['" + action_temp[1] + "'].get()" + ')'
            else:
              pre = '(' +  pre_value + " == " + "env['space_dict']['" + room + "']['env_state']['" + type + "'].get()" + ' and ' + v + " == " + "env['space_dict']['" + action_temp[0] + "']['device_dict']['" + action_temp[1] + "'].get()" + ')'
            pre = pre.replace('&', ' and ')
            pre = pre.replace('|', ' or ')
            action_item[0] = action
            action_item[1] = pre
            fix.append(action_item)
          action_list = getActionPre([room, type.lower() + '_up'])
          for action_item in action_list:
            action_temp = action_item[0].split('.')
            action = action_temp[0] + '.' + action_temp[1] + '.'  + 'action_' + action_temp[2]
            pre = action_item[1]
            pre_list = change(pre)
            for i in pre_list:
              pre = pre.replace(i[0],i[1],1)
            if action_temp[2] == 'on':
              v = '0'
            else:
              v = '1'
            if pre:
              pre = '(' + pre + ')' + ' and ' + '(' +  pre_value + " == " + "env['space_dict']['" + room + "']['env_state']['" + type + "'].get()" + ' and ' + v + " == " + "env['space_dict']['" + action_temp[0] + "']['device_dict']['" + action_temp[1] + "'].get()" + ')'
            else:
              pre = '(' +  pre_value + " == " + "env['space_dict']['" + room + "']['env_state']['" + type + "'].get()" + ' and ' + v + " == " + "env['space_dict']['" + action_temp[0] + "']['device_dict']['" + action_temp[1] + "'].get()" + ')'
            pre = pre.replace('&', ' and ')
            pre = pre.replace('|', ' or ')
            action_item[0] = action
            action_item[1] = pre
            fix.append(action_item)
        else:
          action_list = getActionPre([room, type.lower() + '_up'])
          for action_item in action_list:
            action_temp = action_item[0].split('.')
            action = action_temp[0] + '.' + action_temp[1] + '.'  + 'action_' + action_temp[2]
            pre = action_item[1]
            pre_list = change(pre)
            for i in pre_list:
              pre = pre.replace(i[0],i[1],1)
            if action_temp[2] == 'on':
              v = '0'
            else:
              v = '1'
            if pre:
              pre = '(' + pre + ')' + ' and ' + '(' +  pre_value + " == " + "env['space_dict']['" + room + "']['env_state']['" + type + "'].get()" + ' and ' + v + " == " + "env['space_dict']['" + action_temp[0] + "']['device_dict']['" + action_temp[1] + "'].get()" + ')'
            else:
              pre = '(' +  pre_value + " == " + "env['space_dict']['" + room + "']['env_state']['" + type + "'].get()" + ' and ' + v + " == " + "env['space_dict']['" + action_temp[0] + "']['device_dict']['" + action_temp[1] + "'].get()" + ')'
            pre = pre.replace('&', ' and ')
            pre = pre.replace('|', ' or ')
            action_item[0] = action
            action_item[1] = pre
            fix.append(action_item)
  else:
    if type in device_list:
      # fix.append([room + '.' + type + '.' + 'action_' + value, pre_value + " != " + "env['space_dict']['" + room + "']['device_dict']['" + type + "'].get()"])
      fix.append([room + '.' + type + '.' + 'action_' + value, ""])
    else:
      if room != 'Context' and type != 'HumanState':
        if value == 'high':
          action_list = getActionPre([room, type.lower() + '_up'])
          for action_item in action_list:
            action_temp = action_item[0].split('.')
            action = action_temp[0] + '.' + action_temp[1] + '.'  + 'action_' + action_temp[2]
            pre = action_item[1]
            pre_list = change(pre)

            for i in pre_list:
              pre = pre.replace(i[0],i[1],1)
            if action_temp[2] == 'on':
              v = '0'
            else:
              v = '1'

            if pre:
              pre = '(' + pre + ')' + ' and ' + '(' +  pre_value + " != " + "env['space_dict']['" + room + "']['env_state']['" + type + "'].get()" + ' and ' + v + " == " + "env['space_dict']['" + action_temp[0] + "']['device_dict']['" + action_temp[1] + "'].get()" + ')'
            else:
              pre = '(' +  pre_value + " != " + "env['space_dict']['" + room + "']['env_state']['" + type + "'].get()" + ' and ' + v + " == " + "env['space_dict']['" + action_temp[0] + "']['device_dict']['" + action_temp[1] + "'].get()" + ')'
            pre = pre.replace('&', ' and ')
            pre = pre.replace('|', ' or ')
            action_item[0] = action
            action_item[1] = pre
            fix.append(action_item)
        elif value == 'middle':
          action_list = getActionPre([room, type.lower() + '_down'])
          for action_item in action_list:
            action_temp = action_item[0].split('.')
            action = action_temp[0] + '.' + action_temp[1] + '.'  + 'action_' + action_temp[2]
            pre = action_item[1]
            pre_list = change(pre)
            for i in pre_list:
              pre = pre.replace(i[0],i[1],1)
            if action_temp[2] == 'on':
              v = '0'
            else:
              v = '1'
            if pre:
              pre = '(' + pre + ')' + ' and ' + '(' +  pre_value + " != " + "env['space_dict']['" + room + "']['env_state']['" + type + "'].get()" + ' and ' + v + " == " + "env['space_dict']['" + action_temp[0] + "']['device_dict']['" + action_temp[1] + "'].get()" + ')'
            else:
              pre = '(' +  pre_value + " != " + "env['space_dict']['" + room + "']['env_state']['" + type + "'].get()" + ' and ' + v + " == " + "env['space_dict']['" + action_temp[0] + "']['device_dict']['" + action_temp[1] + "'].get()" + ')'      
            pre = pre.replace('&', ' and ')
            pre = pre.replace('|', ' or ')
            if pre:
              pre = '(' + pre + ') and ' + "env['space_dict']['" + room + "']['env_state']['" + type + "'].value == 1"
            else:
              pre = "env['space_dict']['" + room + "']['env_state']['" + type + "'].value == 1"
            action_item[0] = action
            action_item[1] = pre
            fix.append(action_item)
          action_list = getActionPre([room, type.lower() + '_up'])
          for action_item in action_list:
            action_temp = action_item[0].split('.')
            action = action_temp[0] + '.' + action_temp[1] + '.'  + 'action_' + action_temp[2]
            pre = action_item[1]
            pre_list = change(pre)
            for i in pre_list:
              pre = pre.replace(i[0],i[1],1)
            if action_temp[2] == 'on':
              v = '0'
            else:
              v = '1'
            if pre:
              pre = '(' + pre + ')' + ' and ' + '(' +  pre_value + " != " + "env['space_dict']['" + room + "']['env_state']['" + type + "'].get()" + ' and ' + v + " == " + "env['space_dict']['" + action_temp[0] + "']['device_dict']['" + action_temp[1] + "'].get()" + ')'
            else:
              pre = '(' +  pre_value + " != " + "env['space_dict']['" + room + "']['env_state']['" + type + "'].get()" + ' and ' + v + " == " + "env['space_dict']['" + action_temp[0] + "']['device_dict']['" + action_temp[1] + "'].get()" + ')'
            pre = pre.replace('&', ' and ')
            pre = pre.replace('|', ' or ')
            if pre:
              pre = '(' + pre + ') and ' + "env['space_dict']['" + room + "']['env_state']['" + type + "'].value == -1"
            else:
              pre = "env['space_dict']['" + room + "']['env_state']['" + type + "'].value == -1"
            action_item[0] = action
            action_item[1] = pre
            fix.append(action_item)
        else:
          action_list = getActionPre([room, type.lower() + '_down'])
          for action_item in action_list:
            action_temp = action_item[0].split('.')
            action = action_temp[0] + '.' + action_temp[1] + '.'  + 'action_' + action_temp[2]
            pre = action_item[1]
            pre_list = change(pre)
            for i in pre_list:
              pre = pre.replace(i[0],i[1],1)
            if action_temp[2] == 'on':
              v = '0'
            else:
              v = '1'
            if pre:
              pre = '(' + pre + ')' + ' and ' + '(' +  pre_value + " != " + "env['space_dict']['" + room + "']['env_state']['" + type + "'].get()" + ' and ' + v + " == " + "env['space_dict']['" + action_temp[0] + "']['device_dict']['" + action_temp[1] + "'].get()" + ')'
            else:
              pre = '(' +  pre_value + " != " + "env['space_dict']['" + room + "']['env_state']['" + type + "'].get()" + ' and ' + v + " == " + "env['space_dict']['" + action_temp[0] + "']['device_dict']['" + action_temp[1] + "'].get()" + ')'
            pre = pre.replace('&', ' and ')
            pre = pre.replace('|', ' or ')
            action_item[0] = action
            action_item[1] = pre
            fix.append(action_item)  
  return fix

def getAction(state, flag):
  actions = ''
  state_temp = state.split('.')
  room = state_temp[0]
  type = state_temp[1]
  value = state_temp[2]
  if not flag:
    if type in device_list:
      if actions:
        actions = actions + ' or ' + '(' + "'" + toSnake(type) + '_' + value + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + room  + "'" + '==' + 'df.iat[index, 2]' + ')'
      else: 
        actions = '(' + "'" + toSnake(type) + '_' + value + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + room  + "'" + '==' + 'df.iat[index, 2]' + ')'
    else:
      if type == 'HumanState':
        if actions:
          actions = actions + ' or ' + '(' + "'" + 'human_' + value + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + room  + "'" + '==' + 'df.iat[index, 2]' + ')'
        else: 
          actions = '(' + "'" + 'human_' + value + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + room  + "'" + '==' + 'df.iat[index, 2]' + ')'
      elif type == 'Weather':
        if actions:
          actions = actions + ' or ' + '(' + "'" + 'weather_change' + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + room  + "'" + '==' + 'df.iat[index, 2]' + ')'
        else: 
          actions = '(' + "'" + 'weather_change' + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + room  + "'" + '==' + 'df.iat[index, 2]' + ')'
      else:
        if value == 'high':
          action_list = []
          url = "http://47.101.169.122:5003/effect_node/" + room+ '/effect_' + toSnake(type) + '_up'
          results = requests.get(url).json()
          for result in results:
            ltl_action = ''
            action_item = result['room'] + '.' + result['device'][0:len(result['device']) - 3] + '.' + result['action'][7:len(result['action'])]
            ltl_action = action_item
            action_list.append(ltl_action)
          for action in action_list:
            temp_action = action.split('.')
            if '(' + "'" + toSnake(temp_action[1]) + '_' + temp_action[2] + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + temp_action[0]  + "'" + '==' + 'df.iat[index, 2]' + ')' not in actions:
              if actions:
                actions = actions + ' or ' + '(' + "'" + toSnake(temp_action[1]) + '_' + temp_action[2] + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + temp_action[0]  + "'" + '==' + 'df.iat[index, 2]' + ')'
              else: 
                actions = '(' + "'" + toSnake(temp_action[1]) + '_' + temp_action[2] + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + temp_action[0]  + "'" + '==' + 'df.iat[index, 2]' + ')'
          if '(' + "'" + toSnake(type) + '_up' + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + room  + "'" + '==' + 'df.iat[index, 2]' + ')' not in actions:
            if actions:
              actions = actions + ' or ' + '(' + "'" + toSnake(type) + '_up' + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + room  + "'" + '==' + 'df.iat[index, 2]' + ')'
            else: 
              actions = '(' + "'" + toSnake(type) + '_up' + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + room  + "'" + '==' + 'df.iat[index, 2]' + ')'
        elif value == 'middle':
          action_list = []
          url = "http://47.101.169.122:5003/effect_node/" + room+ '/effect_' + toSnake(type) + '_up'
          results = requests.get(url).json()
          for result in results:
            ltl_action = ''
            action_item = result['room'] + '.' + result['device'][0:len(result['device']) - 3] + '.' + result['action'][7:len(result['action'])]
            ltl_action = action_item
            action_list.append(ltl_action)
          for action in action_list:
            temp_action = action.split('.')
            if '(' + "'" + toSnake(temp_action[1]) + '_' + temp_action[2] + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + temp_action[0]  + "'" + '==' + 'df.iat[index, 2]' + ')' not in actions:
              if actions:
                actions = actions + ' or ' + '(' + "'" + toSnake(temp_action[1]) + '_' + temp_action[2] + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + temp_action[0]  + "'" + '==' + 'df.iat[index, 2]' + ')'
              else: 
                actions = '(' + "'" + toSnake(temp_action[1]) + '_' + temp_action[2] + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + temp_action[0]  + "'" + '==' + 'df.iat[index, 2]' + ')'
          if '(' + "'" + toSnake(type) + '_up' + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + room  + "'" + '==' + 'df.iat[index, 2]' + ')' not in actions:
            if actions:
              actions = actions + ' or ' + '(' + "'" + toSnake(type) + '_up' + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + room  + "'" + '==' + 'df.iat[index, 2]' + ')'
            else: 
              actions = '(' + "'" + toSnake(type) + '_up' + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + room  + "'" + '==' + 'df.iat[index, 2]' + ')'
          action_list = []
          url = "http://47.101.169.122:5003/effect_node/" + room+ '/effect_' + toSnake(type) + '_down'
          results = requests.get(url).json()
          for result in results:
            ltl_action = ''
            action_item = result['room'] + '.' + result['device'][0:len(result['device']) - 3] + '.' + result['action'][7:len(result['action'])]
            ltl_action = action_item
            action_list.append(ltl_action)
          for action in action_list:
            temp_action = action.split('.')
            if '(' + "'" + toSnake(temp_action[1]) + '_' + temp_action[2] + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + temp_action[0]  + "'" + '==' + 'df.iat[index, 2]' + ')' not in actions:
              if actions:
                actions = actions + ' or ' + '(' + "'" + toSnake(temp_action[1]) + '_' + temp_action[2] + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + temp_action[0]  + "'" + '==' + 'df.iat[index, 2]' + ')'
              else: 
                actions = '(' + "'" + toSnake(temp_action[1]) + '_' + temp_action[2] + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + temp_action[0]  + "'" + '==' + 'df.iat[index, 2]' + ')'
          if '(' + "'" + toSnake(type) + '_down' + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + room  + "'" + '==' + 'df.iat[index, 2]' + ')' not in actions:
            if actions:
              actions = actions + ' or ' + '(' + "'" + toSnake(type) + '_down' + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + room  + "'" + '==' + 'df.iat[index, 2]' + ')'
            else:
              actions = '(' + "'" + toSnake(type) + '_down' + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + room  + "'" + '==' + 'df.iat[index, 2]' + ')'
        else:
          action_list = []
          url = "http://47.101.169.122:5003/effect_node/" + room+ '/effect_' + toSnake(type) + '_down'
          results = requests.get(url).json()
          for result in results:
            ltl_action = ''
            action_item = result['room'] + '.' + result['device'][0:len(result['device']) - 3] + '.' + result['action'][7:len(result['action'])]
            ltl_action = action_item
            action_list.append(ltl_action)
          for action in action_list:
            temp_action = action.split('.')
            if '(' + "'" + toSnake(temp_action[1]) + '_' + temp_action[2] + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + temp_action[0]  + "'" + '==' + 'df.iat[index, 2]' + ')' not in actions:
              if actions:
                actions = actions + ' or ' + '(' + "'" + toSnake(temp_action[1]) + '_' + temp_action[2] + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + temp_action[0]  + "'" + '==' + 'df.iat[index, 2]' + ')'
              else: 
                actions = '(' + "'" + toSnake(temp_action[1]) + '_' + temp_action[2] + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + temp_action[0]  + "'" + '==' + 'df.iat[index, 2]' + ')'
          if '(' + "'" + toSnake(type) + '_down' + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + room  + "'" + '==' + 'df.iat[index, 2]' + ')' not in actions:
            if actions:
              actions = actions + ' or ' + '(' + "'" + toSnake(type) + '_down' + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + room  + "'" + '==' + 'df.iat[index, 2]' + ')'
            else: 
              actions = '(' + "'" + toSnake(type) + '_down' + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + room  + "'" + '==' + 'df.iat[index, 2]' + ')'
  else:
    if type in device_list:
      if value == 'on':
        if actions:
          actions = actions + ' or ' + '(' + "'" + toSnake(type) + '_off' + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + room  + "'" + '==' + 'df.iat[index, 2]' + ')'
        else: 
          actions = '(' + "'" + toSnake(type) + '_off' + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + room  + "'" + '==' + 'df.iat[index, 2]' + ')'
      else:
        if actions:
          actions = actions + ' or ' + '(' + "'" + toSnake(type) + '_on' + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + room  + "'" + '==' + 'df.iat[index, 2]' + ')'
        else: 
          actions = '(' + "'" + toSnake(type) + '_on' + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + room  + "'" + '==' + 'df.iat[index, 2]' + ')'
    else:
      if type == 'HumanState':
        if value == 'detected':
          if actions:
            actions = actions + ' or ' + '(' + "'" + 'human_undetected' + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + room  + "'" + '==' + 'df.iat[index, 2]' + ')'
          else: 
            actions = '(' + "'" + 'human_undetected' + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + room  + "'" + '==' + 'df.iat[index, 2]' + ')'
        else:
          if actions:
            actions = actions + ' or ' + '(' + "'" + 'human_detected' + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + room  + "'" + '==' + 'df.iat[index, 2]' + ')'
          else: 
            actions = '(' + "'" + 'human_detected' + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + room  + "'" + '==' + 'df.iat[index, 2]' + ')'
      elif type == 'Weather':
        if actions:
          actions = actions + ' or ' + '(' + "'" + 'weather_change' + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + room  + "'" + '==' + 'df.iat[index, 2]' + ')'
        else: 
          actions = '(' + "'" + 'weather_change' + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + room  + "'" + '==' + 'df.iat[index, 2]' + ')'
      else:
        if value == 'high':
          action_list = []
          url = "http://47.101.169.122:5003/effect_node/" + room+ '/effect_' + toSnake(type) + '_down'
          results = requests.get(url).json()
          for result in results:
            ltl_action = ''
            action_item = result['room'] + '.' + result['device'][0:len(result['device']) - 3] + '.' + result['action'][7:len(result['action'])]
            ltl_action = action_item
            action_list.append(ltl_action)
          for action in action_list:
            temp_action = action.split('.')
            if '(' + "'" + toSnake(temp_action[1]) + '_' + temp_action[2] + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + temp_action[0]  + "'" + '==' + 'df.iat[index, 2]' + ')' not in actions:
              if actions:
                actions = actions + ' or ' + '(' + "'" + toSnake(temp_action[1]) + '_' + temp_action[2] + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + temp_action[0]  + "'" + '==' + 'df.iat[index, 2]' + ')'
              else: 
                actions = '(' + "'" + toSnake(temp_action[1]) + '_' + temp_action[2] + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + temp_action[0]  + "'" + '==' + 'df.iat[index, 2]' + ')'
          if '(' + "'" + toSnake(type) + '_down' + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + room  + "'" + '==' + 'df.iat[index, 2]' + ')' not in actions:
            if actions:
              actions = actions + ' or ' + '(' + "'" + toSnake(type) + '_down' + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + room  + "'" + '==' + 'df.iat[index, 2]' + ')'
            else: 
              actions = '(' + "'" + toSnake(type) + '_down' + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + room  + "'" + '==' + 'df.iat[index, 2]' + ')'
        elif value == 'middle':
          action_list = []
          url = "http://47.101.169.122:5003/effect_node/" + room+ '/effect_' + toSnake(type) + '_up'
          results = requests.get(url).json()
          for result in results:
            ltl_action = ''
            action_item = result['room'] + '.' + result['device'][0:len(result['device']) - 3] + '.' + result['action'][7:len(result['action'])]
            ltl_action = action_item
            action_list.append(ltl_action)
          for action in action_list:
            temp_action = action.split('.')
            if '(' + "'" + toSnake(temp_action[1]) + '_' + temp_action[2] + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + temp_action[0]  + "'" + '==' + 'df.iat[index, 2]' + ')' not in actions:
              if actions:
                actions = actions + ' or ' + '(' + "'" + toSnake(temp_action[1]) + '_' + temp_action[2] + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + temp_action[0]  + "'" + '==' + 'df.iat[index, 2]' + ')'
              else: 
                actions = '(' + "'" + toSnake(temp_action[1]) + '_' + temp_action[2] + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + temp_action[0]  + "'" + '==' + 'df.iat[index, 2]' + ')'
          if '(' + "'" + toSnake(type) + '_up' + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + room  + "'" + '==' + 'df.iat[index, 2]' + ')' not in actions:
            if actions:
              actions = actions + ' or ' + '(' + "'" + toSnake(type) + '_up' + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + room  + "'" + '==' + 'df.iat[index, 2]' + ')'
            else: 
              actions = '(' + "'" + toSnake(type) + '_up' + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + room  + "'" + '==' + 'df.iat[index, 2]' + ')'
          
          action_list = []
          url = "http://47.101.169.122:5003/effect_node/" + room+ '/effect_' + toSnake(type) + '_down'
          results = requests.get(url).json()
          for result in results:
            ltl_action = ''
            action_item = result['room'] + '.' + result['device'][0:len(result['device']) - 3] + '.' + result['action'][7:len(result['action'])]
            ltl_action = action_item
            action_list.append(ltl_action)
          for action in action_list:
            temp_action = action.split('.')
            if '(' + "'" + toSnake(temp_action[1]) + '_' + temp_action[2] + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + temp_action[0]  + "'" + '==' + 'df.iat[index, 2]' + ')' not in actions:
              if actions:
                actions = actions + ' or ' + '(' + "'" + toSnake(temp_action[1]) + '_' + temp_action[2] + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + temp_action[0]  + "'" + '==' + 'df.iat[index, 2]' + ')'
              else: 
                actions = '(' + "'" + toSnake(temp_action[1]) + '_' + temp_action[2] + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + temp_action[0]  + "'" + '==' + 'df.iat[index, 2]' + ')'
          if '(' + "'" + toSnake(type) + '_down' + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + room  + "'" + '==' + 'df.iat[index, 2]' + ')' not in actions:
            if actions:
              actions = actions + ' or ' + '(' + "'" + toSnake(type) + '_down' + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + room  + "'" + '==' + 'df.iat[index, 2]' + ')'
            else:
              actions = '(' + "'" + toSnake(type) + '_down' + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + room  + "'" + '==' + 'df.iat[index, 2]' + ')'
        else:
          action_list = []
          url = "http://47.101.169.122:5003/effect_node/" + room+ '/effect_' + toSnake(type) + '_up'
          results = requests.get(url).json()
          for result in results:
            ltl_action = ''
            action_item = result['room'] + '.' + result['device'][0:len(result['device']) - 3] + '.' + result['action'][7:len(result['action'])]
            ltl_action = action_item
            action_list.append(ltl_action)
          for action in action_list:
            temp_action = action.split('.')
            if '(' + "'" + toSnake(temp_action[1]) + '_' + temp_action[2] + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + temp_action[0]  + "'" + '==' + 'df.iat[index, 2]' + ')' not in actions:
              if actions:
                actions = actions + ' or ' + '(' + "'" + toSnake(temp_action[1]) + '_' + temp_action[2] + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + temp_action[0]  + "'" + '==' + 'df.iat[index, 2]' + ')'
              else: 
                actions = '(' + "'" + toSnake(temp_action[1]) + '_' + temp_action[2] + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + temp_action[0]  + "'" + '==' + 'df.iat[index, 2]' + ')'
          if '(' + "'" + toSnake(type) + '_up' + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + room  + "'" + '==' + 'df.iat[index, 2]' + ')' not in actions:
            if actions:
              actions = actions + ' or ' + '(' + "'" + toSnake(type) + '_up' + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + room  + "'" + '==' + 'df.iat[index, 2]' + ')'
            else: 
              actions = '(' + "'" + toSnake(type) + '_up' + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + room  + "'" + '==' + 'df.iat[index, 2]' + ')'
  return actions

def toSnake(strings):
  lst = []
  for i,v in enumerate(strings):
    if v.isupper() and i != 0:
      if strings[i+1:i+2] and not strings[i+1:i+2].isupper():
        lst.append("_")
    lst.append(v)
  return "".join(lst).lower()

def getEvent(strings, flag):
  events = ''
  state_list = strings.split(' ')
  if len(state_list) == 3:
    if state_list[1] == '>':
      state_one = state_list[0]
      state_two = state_list[2]
    else:
      state_one = state_list[2]
      state_two = state_list[0]
  elif len(state_list) == 5:
    if state_list[4] == '-2':
      state_one = state_list[0]
      state_two = state_list[2]
    else:
      state_one = state_list[2]
      state_two = state_list[0]
        
  event_list = state_one.split('.')
  if events:
    events = '(' + events + ')' + ' or ' + '(' + "'" + toSnake(event_list[1]) + '_up'  + "'" + '==' + 'df.iat[index, 0]'+ ' and ' + "'" + event_list[0]  + "'" + '==' + 'df.iat[index, 2]' + ')'
  else:
    events = '(' + "'" + toSnake(event_list[1]) + '_up'  + "'" + '==' + 'df.iat[index, 0]'+ ' and ' + "'" + event_list[0]  + "'" + '==' + 'df.iat[index, 2]' + ')'
  event_list = state_two.split('.')
  if events:
    events = '(' + events + ')' + ' or ' + '(' + "'" + toSnake(event_list[1]) + '_down'  + "'" + '==' + 'df.iat[index, 0]'+ ' and ' + "'" + event_list[0]  + "'" + '==' + 'df.iat[index, 2]' + ')'
  else:
    events = '(' + "'" + toSnake(event_list[1]) + '_down'  + "'" + '==' + 'df.iat[index, 0]'+ ' and ' + "'" + event_list[0]  + "'" + '==' + 'df.iat[index, 2]' + ')'
  return events          
    
def getStateCondition(state):
  condition = ''
  state_temp = state.split('.')
  room = state_temp[0]
  type = state_temp[1]
  value = state_temp[2]   
  if type in device_list or (type in ['HumanState','Weather']):
    condition = state
  else:
    if value == 'high':
      url = "http://47.101.169.122:5003/effect_node/" + room+ '/effect_' + toSnake(type) + '_up'
      results = requests.get(url).json()
      for result in results:
        ltl_action = ''
        action_item = result['room'] + '.' + result['device'][0:len(result['device']) - 3] + '.' + result['action'][7:len(result['action'])]
        ltl_action = action_item
        pre_condition_item = getPreConditionLTL(result['pre_condition'])
        if condition:
          if pre_condition_item:
            condition = '(' + condition + ')' + ' | ' + '(' + ltl_action + ' & ' + '(' + pre_condition_item + ')' + ')'
          else:
            condition = '(' + condition + ')' + ' | ' + '(' + ltl_action + ')'
        else:
          if pre_condition_item:
            condition = ltl_action + ' & ' + '(' + pre_condition_item + ')'
          else:
            condition = ltl_action
      condition = '(' + condition + ')' + ' & ' + room + '.' + type + '.' + 'middle'       
    elif value == 'middle':
      url = "http://47.101.169.122:5003/effect_node/" + room+ '/effect_' + toSnake(type) + '_up'
      results = requests.get(url).json()
      for result in results:
        ltl_action = ''
        action_item = result['room'] + '.' + result['device'][0:len(result['device']) - 3] + '.' + result['action'][7:len(result['action'])]
        ltl_action = action_item
        pre_condition_item = getPreConditionLTL(result['pre_condition'])
        if condition:
          if pre_condition_item:
            condition = '(' + condition + ')' + ' | ' + '(' + ltl_action + ' & ' + '(' + pre_condition_item + ')' + ')'
          else:
            condition = '(' + condition + ')' + ' | ' + '(' + ltl_action + ')'
        else:
          if pre_condition_item:
            condition = ltl_action + ' & ' + '(' + pre_condition_item + ')'
          else:
            condition = ltl_action
      condition = '(' + condition + ')' + ' & ' + room + '.' + type + '.' + 'low'
      
      url = "http://47.101.169.122:5003/effect_node/" + room+ '/effect_' + toSnake(type) + '_down'
      results = requests.get(url).json()
      for result in results:
        ltl_action = ''
        action_item = result['room'] + '.' + result['device'][0:len(result['device']) - 3] + '.' + result['action'][7:len(result['action'])]
        ltl_action = action_item
        pre_condition_item = getPreConditionLTL(result['pre_condition'])
        if condition:
          if pre_condition_item:
            condition = '(' + condition + ')' + ' | ' + '(' + ltl_action + ' & ' + '(' + pre_condition_item + ')' + ')'
          else:
            condition = '(' + condition + ')' + ' | ' + '(' + ltl_action + ')'
        else:
          if pre_condition_item:
            condition = ltl_action + ' & ' + '(' + pre_condition_item + ')'
          else:
            condition = ltl_action
      condition = '(' + condition + ')' + ' & ' + room + '.' + type + '.' + 'high'
    else:
      url = "http://47.101.169.122:5003/effect_node/" + room+ '/effect_' + toSnake(type) + '_down'
      results = requests.get(url).json()
      for result in results:
        ltl_action = ''
        action_item = result['room'] + '.' + result['device'][0:len(result['device']) - 3] + '.' + result['action'][7:len(result['action'])]
        ltl_action = action_item
        pre_condition_item = getPreConditionLTL(result['pre_condition'])
        if condition:
          if pre_condition_item:
            condition = '(' + condition + ')' + ' | ' + '(' + ltl_action + ' & ' + '(' + pre_condition_item + ')' + ')'
          else:
            condition = '(' + condition + ')' + ' | ' + '(' + ltl_action + ')'
        else:
          if pre_condition_item:
            condition = ltl_action + ' & ' + '(' + pre_condition_item + ')'
          else:
            condition = ltl_action
      condition = '(' + condition + ')' + ' & ' + room + '.' + type + '.' + 'middle'
  return '(' + condition + ')'
        
def LTLRegulation():
  regulation = []
  for item in EventState:
    event_state  = item[3:-1]
    event_state = event_state.replace(' ','')
    temp = event_state.split('&')
    trigger = "'" + temp[0].split('.')[1]+ "'" + '==' + 'df.iat[index, 0]' +  ' and ' + "'" + temp[0].split('.')[0]  + "'" + '==' + 'df.iat[index, 2]'
    temp_trigger = temp[0]
    state = event_state[1+len(temp_trigger):]
    temp_state = state
    if state[0] == '!':
      temp_state = state[1:]
    iter = re.finditer(r'[a-zA-Z.!]+', temp_state)
    for i in iter:
      value = i.group() 
      replaces = change(value)
      for replace in replaces:
        state = state.replace(replace[0],replace[1],1)
    state = state.replace('&', ' and ')
    state = state.replace('|', ' or ')
    state = state.replace('!', ' not ')
    condition = 'not ('  + state + ')'
    if '!' in event_state[1+len(temp_trigger):]: # 不能
      fix = []
      flag = 'or'
      fix_states = event_state[3+len(temp_trigger):-1].split('&')
      for fix_state in fix_states:
        if(getFix(fix_state, False)):
          fix.append(getFix(fix_state, False))
      if len(temp_trigger.split('.')) == 3:
        if(getFix(temp_trigger, False)):
          fix.append(getFix(temp_trigger, False))
    else: # 必须
      fix = []
      flag = 'and'
      fix_states = event_state[2+len(temp_trigger):-1].split('&')
      for fix_state in fix_states:
        if(getFix(fix_state, True)):
          fix.append(getFix(fix_state, True))
    r = temp_trigger.split('.')[0]
    d = (temp_trigger.split('.')[1]).split('_')[0]
    v = (temp_trigger.split('.')[1]).split('_')[1]
    if d.capitalize() in device_list:
      if (v == 'on'):
        fix.append(getFix(r + '.' + d.capitalize() + '.' + 'off',True))
      else:
        fix.append(getFix(r + '.' + d.capitalize() + '.' + 'on',True))
    template = {
      "ltl":item,
      "trigger":trigger,
      "condition":condition,
      "fix":fix,
      "flag":flag 
    }
    regulation.append(template)
  for ltl in LTL:    
    ltl = ltl.replace(' ', '')
    if 'G!' in ltl: 
      temp_ltl = ltl[3:-1]
    else:                           
     temp_ltl = ltl[2:-1]
    count = 0
    for item in temp_ltl.split('&'):
      if len(item.split('.')) == 2:
        count = count + 1
    if count == 0:
      condition = ''
      trigger  = ''
      fix = []
      for state in temp_ltl.split('&'):
        if condition:
          condition = condition + ' & ' + getStateCondition(state)
        else:
          condition = getStateCondition(state)
        if 'G!' in ltl:
          f = getAction(state, False)
        else:
          f = getAction(state, True)
        if trigger:
          if f not in trigger:
            trigger = '(' + trigger + ')' + ' or ' + '(' + f + ')'
        else:
          trigger = f 
      for t in change(condition):
        condition = condition.replace(t[0], t[1], 1)
      if 'G!' not in ltl:
        condition = ' not ' + '(' + condition + ')'
      condition = condition.replace('!', ' not ')
      condition = condition.replace('&', ' and ')
      condition = condition.replace('|', ' or ')
      if 'G!' in ltl:
        flag = 'or'
        for state in temp_ltl.split('&'):
          f = getFix(state, False)
          if f:
            fix.append(f)
      else: # 必须
        flag = 'and'
        for state in temp_ltl.split('&'):
          f = getFix(state, True)
          if f:
            fix.append(f)
      regulation.append({
        "trigger":trigger,
        "condition":condition,
        "fix":fix,
        "flag":flag,
        "ltl":ltl
      })
    elif count == 1:
      fix = []
      trigger = ''
      temp = temp_ltl.split('&')
      effect = temp[0]
      condition = ' | '.join(getLTL(effect.split('.')))
      for t in change(condition):
        condition = condition.replace(t[0], t[1], 1)
      if '!' in temp[1]:
        flag = 'or'
        states = temp_ltl[len(effect)+3:-1]
        for state in states.split('&'):
          f = getFix(state, False)
          if f:
            fix.append(f)
      else:
        flag = 'or'
        condition = ' not ' + '(' + condition + ')'
        states = temp_ltl[len(effect)+2:-1]
      for state in states.split('&'):
        f = getAction(state, False)
        if trigger:
          if f not in trigger:
            trigger = '(' + trigger + ')' + ' or ' + '(' + f + ')'
        else:
          trigger = f
      url = "http://47.101.169.122:5003/effect_node/" + effect.split('.')[0]+ '/effect_' + effect.split('.')[1]
      results = requests.get(url).json()
      fix_temp = []
      for result in results:
        ltl_action = result['room'] + '.' + result['device'][0:len(result['device']) - 3] + '.' + result['action'][7:len(result['action'])]
        state_temp = ltl_action.split('.')
        room = state_temp[0]
        type = state_temp[1]
        value = state_temp[2]
        p = ''
        pre_condition_item = getPreConditionLTL(result['pre_condition'])
        pre_condition_item = pre_condition_item.replace(' ', '')
        for pre in change(pre_condition_item):
          pre_condition_item = pre_condition_item.replace(pre[0], pre[1], 1)
        pre_condition_item = pre_condition_item.replace('!', ' not ')
        pre_condition_item = pre_condition_item.replace('&', ' and ')
        pre_condition_item = pre_condition_item.replace('|', ' or ')  
        if '!' in temp[1]:
          if value == 'on':
            p = '0' + " != " + "env['space_dict']['" + room + "']['device_dict']['" + type + "'].get()"
            if pre_condition_item:
                p = '(' + p + ')' + ' and '  + '(' + pre_condition_item + ')'
            ltl_action = room + '.' + type + '.' + 'action_off'
          else:
            p = '1' + " != " + "env['space_dict']['" + room + "']['device_dict']['" + type + "'].get()"
            if pre_condition_item:
                p = '(' + p + ')' + ' and '  + '(' + pre_condition_item + ')'
            ltl_action = room + '.' + type + '.' + 'action_on'
          if trigger:
              trigger = trigger + ' or ' + '(' + "'" + toSnake(type) + '_' + value + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + room  + "'" + '==' + 'df.iat[index, 2]' +  ')'
          else:
            trigger = "'" + toSnake(type) + '_' + value + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + room  + "'" + '==' + 'df.iat[index, 2]' 
        else:
          if value == 'on':
            if trigger:
              trigger = trigger + ' or ' + '(' + "'" + toSnake(type) + '_off' + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + room  + "'" + '==' + 'df.iat[index, 2]' + ')'
            else:
              trigger = "'" + toSnake(type) + '_off' + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + room  + "'" + '==' + 'df.iat[index, 2]' 
            p = '1' + " != " + "env['space_dict']['" + room + "']['device_dict']['" + type + "'].get()"
            if pre_condition_item:
              p = '(' + p + ')' + ' and '  + '(' + pre_condition_item + ')'
          else:
            if trigger:
              trigger = trigger + ' or ' + '(' + "'" + toSnake(type) + '_on' + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + room  + "'" + '==' + 'df.iat[index, 2]' + ')'
            else:
              trigger = "'" + toSnake(type) + '_on' + "'" + '==' + 'df.iat[index, 0]'+ ' and '  + "'" + room  + "'" + '==' + 'df.iat[index, 2]' 
            p = '0' + " != " + "env['space_dict']['" + room + "']['device_dict']['" + type + "'].get()"
            if pre_condition_item:
              p = '(' + p + ')' + ' and '  + '(' + pre_condition_item + ')'
          ltl_action = room + '.' + type + '.' + 'action_' + value
        fix_item = [ltl_action, p]
        fix_temp.append(fix_item)
      fix.append(fix_temp)
      for t in change(states):
        states = states.replace(t[0], t[1], 1)
      condition = '(' + states + ')' + ' and ' + '(' + condition + ')'
      condition = condition.replace('!', ' not ')
      condition = condition.replace('&', ' and ')
      condition = condition.replace('|', ' or ')
      regulation.append({
        "trigger":trigger,
        "condition":condition,
        "fix":fix,
        "flag":flag,
        "ltl":ltl
      })
    else:
      effect_list = temp_ltl.split('&')
      trigger = ''
      fix = []
      condition = ''
      for effect in effect_list:
        if not condition:
          condition = ' | '.join(getLTL(effect.split('.')))
        else:
          condition = '(' + condition + ')' +' & ' + '(' + ' | '.join(getLTL(effect.split('.'))) + ')'
        url = "http://47.101.169.122:5003/effect_node/" + effect.split('.')[0]+ '/effect_' + effect.split('.')[1]
        results = requests.get(url).json()
        fix_temp = []
        for result in results:
          if result['pre_condition']:
            events = getEvent(result['pre_condition'], result['name'].split('_')[2])
            if trigger:
              trigger = '(' + trigger  + ')' + ' or ' + '(' + events + ')'
            else:
              trigger = events
          ltl_action = result['room'] + '.' + result['device'][0:len(result['device']) - 3] + '.' + result['action'][7:len(result['action'])]
          state_temp = ltl_action.split('.')
          room = state_temp[0]
          type = state_temp[1]
          value = state_temp[2]
          p = ''
          pre_condition_item = getPreConditionLTL(result['pre_condition'])
          pre_condition_item = pre_condition_item.replace(' ', '')
          for pre in change(pre_condition_item):
            pre_condition_item = pre_condition_item.replace(pre[0], pre[1], 1)
          pre_condition_item = pre_condition_item.replace('!', ' not ')
          pre_condition_item = pre_condition_item.replace('&', ' and ')
          pre_condition_item = pre_condition_item.replace('|', ' or ')  
          if 'G!' in ltl: 
            if value == 'on':
              p = '0' + " != " + "env['space_dict']['" + room + "']['device_dict']['" + type + "'].get()"
              if pre_condition_item:
                p = '(' + p + ')' + ' and '  + '(' + pre_condition_item + ')'
              ltl_action = room + '.' + type + '.' + 'action_off'
            else:
              p = '1' + " != " + "env['space_dict']['" + room + "']['device_dict']['" + type + "'].get()"
              if pre_condition_item:
                p = '(' + p + ')' + ' and '  + '(' + pre_condition_item + ')'
              ltl_action = room + '.' + type + '.' + 'action_on'
            if trigger:
              trigger = '(' + trigger + ')' + ' or ' + '(' + "'" + toSnake(type) + '_' + value + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + room  + "'" + '==' + 'df.iat[index, 2]' + ')'
            else:
              trigger = "'" + toSnake(type) + '_' + value + "'" + '==' + 'df.iat[index, 0]'+ ' and '  + "'" + room  + "'" + '==' + 'df.iat[index, 2]' 
          else:
            if value == 'on':
              p = '1' + " != " + "env['space_dict']['" + room + "']['device_dict']['" + type + "'].get()"
              if pre_condition_item:
                p = '(' + p + ')' + ' and '  + '(' + pre_condition_item + ')'
            else:
              p = '0' + " != " + "env['space_dict']['" + room + "']['device_dict']['" + type + "'].get()"
              if pre_condition_item:
                p = '(' + p + ')' + ' and '  + '(' + pre_condition_item + ')'
            ltl_action = room + '.' + type + '.' + 'action_' + value
            if value == 'on':
              if trigger:
                trigger = '(' + trigger + ')' + ' or ' + '(' + "'" + toSnake(type) + '_' + 'off'  + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + room  + "'" + '==' + 'df.iat[index, 2]' + ')'
              else:
                trigger = "'" + toSnake(type) + '_' + 'off' + "'" + '==' + 'df.iat[index, 0]'+ ' and '  + "'" + room  + "'" + '==' + 'df.iat[index, 2]' 
            else:
              if trigger:
                trigger = '(' + trigger + ')' + ' or ' + '(' + "'" + toSnake(type) + '_' + 'on' + "'" + '==' + 'df.iat[index, 0]' + ' and '  + "'" + room  + "'" + '==' + 'df.iat[index, 2]' + ')'
              else:
                trigger = "'" + toSnake(type) + '_' + 'on' + "'" + '==' + 'df.iat[index, 0]'+ ' and '  + "'" + room  + "'" + '==' + 'df.iat[index, 2]' 
          fix_item = [ltl_action, p]
          fix_temp.append(fix_item)
        fix.append(fix_temp)
      for t in change(condition):
        condition = condition.replace(t[0], t[1], 1)
      condition = condition.replace('!', ' not ')
      condition = condition.replace('&', ' and ')
      condition = condition.replace('|', ' or ')
      if 'G!' not in ltl: 
        condition = ' not '+  '(' + condition + ')'
        flag = 'and'
      else:
        flag = 'or'
      regulation.append({
        "trigger":trigger,
        "condition":condition,
        "fix":fix,
        "flag":flag,
        "ltl":ltl
      })
  return regulation
# getMTL()
regulations = getRegulation()
ltlRegulations = LTLRegulation()
# for item in regulations:
#       print(item)
#       print()
# print()
# for item in ltlRegulations:
#     print(item)
#     print()
