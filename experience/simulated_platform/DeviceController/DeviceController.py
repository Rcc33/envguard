import threading

def deviceOn(room, device_name, env, source):
  device = env["space_dict"][room]["device_dict"][device_name]
  func = getattr(device, "action_on")
  func(device, env, source)
  
def deviceOff(room, device_name, env, source):
  device = env["space_dict"][room]["device_dict"][device_name]
  func = getattr(device, "action_off")
  func(device, env, source)
  
def stateIncrease(thread_list, room, state_name, env):
  state = env["space_dict"][room]["env_state"][state_name]
  func = getattr(state, "ext_action_increase")
  t1 = threading.Thread(target=func, args=(state, env,))
  t1.start()
  thread_list.append(t1)
  # func(state, env)

def stateDecrease(thread_list, room, state_name, env):
  state = env["space_dict"][room]["env_state"][state_name]
  func = getattr(state, "ext_action_decrease")
  t1 = threading.Thread(target=func, args=(state, env,))
  t1.start()
  thread_list.append(t1)
  # func(state, env)

def weatherChange(value, env):
  state = env["space_dict"]["Context"]["env_state"]["Weather"]
  func = getattr(state, "ext_action_change")
  func(state, value, env)
  
def getDeviceState(room, device_name, env):
  device = env["space_dict"][room]["device_dict"][device_name]
  func = getattr(device, "ap_on")
  return func(device)

def getStateValue(room, state_name, env):
  state = env["space_dict"][room]["env_state"][state_name]
  func = getattr(state, "ap_value")
  return func(state)
