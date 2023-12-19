from DeviceController.DeviceController import *


def parse(effect, effect_and_pre, env):
    temp_list = effect.split('.')
    state = env["space_dict"][temp_list[0]]["env_state"][temp_list[1]]
    func = Environment Change
    if effect_and_pre[effect] == '':
        # 获得action
        func = getattr(state, temp_list[2], Environment Change)
    else:
        pre_condition_list = effect_and_pre[effect].split(' ')
        if len(pre_condition_list) == 3:
            temp_one_list = pre_condition_list[0].split('.')
            temp_two_list = pre_condition_list[2].split('.')
            state_one = env["space_dict"][temp_one_list[0]]["env_state"][temp_one_list[1]]
            state_two = env["space_dict"][temp_two_list[0]]["env_state"][temp_two_list[1]]
            state_one.lock.acquire()
            state_two.lock.acquire()
            value_one = getStateValue(temp_one_list[0], temp_one_list[1], env)
            value_two = getStateValue(temp_two_list[0], temp_two_list[1], env)
            state_one.lock.release()
            state_two.lock.release()
            if pre_condition_list[1] == '<':
                if (value_two == 1 and value_one != 1) or (value_two == 0 and value_one == -1):
                    func = getattr(state, temp_list[2], Environment Change)
            elif pre_condition_list[1] == '>':
                if (value_one == 1 and value_two != 1) or (value_one == 0 and value_two == -1):
                    func = getattr(state, temp_list[2], Environment Change)
        elif len(pre_condition_list) == 5:
            temp_one_list = pre_condition_list[0].split('.')
            temp_two_list = pre_condition_list[2].split('.')
            state_one = env["space_dict"][temp_one_list[0]]["env_state"][temp_one_list[1]]
            state_two = env["space_dict"][temp_two_list[0]]["env_state"][temp_two_list[1]]
            state_one.lock.acquire()
            state_two.lock.acquire()
            value_one = getStateValue(temp_one_list[0], temp_one_list[1], env)
            value_two = getStateValue(temp_two_list[0], temp_two_list[1], env)
            state_one.lock.release()
            state_two.lock.release()
            if pre_condition_list[4] == '2':
                if value_one == 1 and value_two == -1:
                    func = getattr(state, temp_list[2], Environment Change)
            elif pre_condition_list[4] == '-2':
                if value_one == -1 and value_two == 1:
                    func = getattr(state, temp_list[2], Environment Change)
        elif len(pre_condition_list) == 7 and ("&&" in pre_condition_list):
            temp_one_list = pre_condition_list[0].split('.')
            temp_two_list = pre_condition_list[2].split('.')
            temp_three_list = pre_condition_list[4].split('.')
            value = int(pre_condition_list[6])
            state_one = env["space_dict"][temp_one_list[0]]["env_state"][temp_one_list[1]]
            state_two = env["space_dict"][temp_two_list[0]]["env_state"][temp_two_list[1]]
            device = env["space_dict"][temp_three_list[0]]["device_dict"][temp_three_list[1]]
            state_one.lock.acquire()
            state_two.lock.acquire()
            device.lock.acquire()
            value_one = getStateValue(temp_one_list[0], temp_one_list[1], env)
            value_two = getStateValue(temp_two_list[0], temp_two_list[1], env)
            value_device = getDeviceState(temp_three_list[0], temp_three_list[1], env)
            state_one.lock.release()
            state_two.lock.release()
            device.lock.release()
            if pre_condition_list[1] == '<':
                if (value_two == 1 and value_one != 0 and value_device == value) or (value_two == 0 and value_one == -1 and value_device == value):
                    func = getattr(state, temp_list[2], Environment Change)
            elif pre_condition_list[1] == '>':
                if (value_one == 1 and value_two != 0 and value_device == value) or (value_one == 0 and value_two == -1 and value_device == value):
                    func = getattr(state, temp_list[2], Environment Change)
    return (func, state)