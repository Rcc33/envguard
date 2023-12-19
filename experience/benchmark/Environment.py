from environment.device.AC import AC
from environment.device.AirPurifier import AirPurifier
from environment.device.Curtain import Curtain
from environment.device.Door import Door
from environment.device.Heater import Heater
from environment.device.Humidifier import Humidifier
from environment.device.MicrowaveOven import MicrowaveOven
from environment.device.TV import TV
from environment.device.Light import Light
from environment.device.Printer import Printer
from environment.device.Speaker import Speaker
from environment.device.WaterDispenser import WaterDispenser
from environment.device.Window import Window
from environment.state.AirQuality import AirQuality
from environment.state.Brightness import Brightness
from environment.state.HumanState import HumanState
from environment.state.Humidity import Humidity
from environment.state.Noise import Noise
from environment.state.Temperature import Temperature
from environment.state.Weather import Weather

def get_dict(space_name, space):
    temp = dict()
    temp["action_dict"] = dict()
    temp["enable_dict"] = dict()
    temp["ext_action_list"] = list()
    for key, value in space["device_dict"].items():
        for k, v in value.action_dict.items():
            name = space_name + '.' + key + '.' + k
            temp["action_dict"][name] = v
        for k, v in value.enable_dict.items():
            name = space_name + '.' + key + '.' + k
            temp["enable_dict"][name] = v
        for item in value.ext_action_list:
            temp["ext_action_list"].append(space_name + '.' + key + '.' + item)
    for key, value in space["env_state"].items():
        for k, v in value.action_dict.items():
            name = space_name + '.' + key + '.' + k
            temp["action_dict"][name] = v
        for k, v in value.enable_dict.items():
            name = space_name + '.' + key + '.' + k
            temp["enable_dict"][name] = v
        for item in value.ext_action_list:
            temp["ext_action_list"].append(space_name + '.' + key + '.' + item)
    return temp


def getEnvonment():
    env = dict()
    space_dict = dict()

    # context
    device_dict = dict()
    env_state = dict()
    env_state["Temperature"] = Temperature("Context")
    env_state["Humidity"] = Humidity("Context")
    env_state["Brightness"] = Brightness("Context")
    env_state["AirQuality"] = AirQuality("Context")
    env_state["Weather"] = Weather("Context")
    room_temp = dict()
    room_temp["device_dict"] = device_dict
    room_temp["env_state"] = env_state
    temp = get_dict("Context", room_temp)
    room_temp["action_dict"] = temp["action_dict"]
    room_temp["enable_dict"] = temp["enable_dict"]
    room_temp["ext_action_list"] = temp["ext_action_list"]
    space_dict["Context"] = room_temp

    # Lab
    device_dict = dict()
    env_state = dict()
    env_state["Temperature"] = Temperature("Lab")
    env_state["Brightness"] = Brightness("Lab")
    env_state["Humidity"] = Humidity("Lab")
    env_state["Noise"] = Noise("Lab")
    env_state["AirQuality"] = AirQuality("Lab")
    env_state["HumanState"] = HumanState("Lab")

    device_dict["AC"] = AC(env_state, "Lab")
    device_dict["Heater"] = Heater(env_state, "Lab")
    device_dict["Humidifier"] = Humidifier(env_state, "Lab")
    device_dict["Light"] = Light(env_state, "Lab")
    device_dict["Speaker"] = Speaker(env_state, "Lab")
    device_dict["Printer"] = Printer(env_state, "Lab")
    device_dict["Curtain"] = Curtain(space_dict["Context"]["env_state"],env_state, "Lab")
    device_dict["AirPurifier"] = AirPurifier(env_state, "Lab")
    device_dict["Window"] = Window(space_dict["Context"]["env_state"], env_state, "Lab")
    room_temp = dict()
    room_temp["device_dict"] = device_dict
    room_temp["env_state"] = env_state
    temp = get_dict("Lab", room_temp)
    room_temp["action_dict"] = temp["action_dict"]
    room_temp["enable_dict"] = temp["enable_dict"]
    room_temp["ext_action_list"] = temp["ext_action_list"]
    space_dict["Lab"] = room_temp

    # MeetingRoomOne
    device_dict = dict()
    env_state = dict()
    env_state["Temperature"] = Temperature("MeetingRoomOne")
    env_state["Brightness"] = Brightness("MeetingRoomOne")
    env_state["Humidity"] = Humidity("MeetingRoomOne")
    env_state["Noise"] = Noise("MeetingRoomOne")
    env_state["AirQuality"] = AirQuality("MeetingRoomOne")
    env_state["HumanState"] = HumanState("MeetingRoomOne")

    device_dict["AC"] = AC(env_state, "MeetingRoomOne")
    device_dict["TV"] = TV(env_state, "MeetingRoomOne")
    device_dict["Heater"] = Heater(env_state, "MeetingRoomOne")
    device_dict["Humidifier"] = Humidifier(env_state, "MeetingRoomOne")
    device_dict["Light"] = Light(env_state, "MeetingRoomOne")
    # device_dict["Speaker"] = Speaker(env_state, "MeetingRoomOne")
    device_dict["Curtain"] = Curtain(space_dict["Context"]["env_state"],env_state, "MeetingRoomOne")
    device_dict["AirPurifier"] = AirPurifier(env_state, "MeetingRoomOne")
    device_dict["Window"] = Window(space_dict["Context"]["env_state"], env_state, "MeetingRoomOne")
    room_temp = dict()
    room_temp["device_dict"] = device_dict
    room_temp["env_state"] = env_state
    temp = get_dict("MeetingRoomOne", room_temp)
    room_temp["action_dict"] = temp["action_dict"]
    room_temp["enable_dict"] = temp["enable_dict"]
    room_temp["ext_action_list"] = temp["ext_action_list"]
    space_dict["MeetingRoomOne"] = room_temp

    # MeetingRoomTwo
    device_dict = dict()
    env_state = dict()
    env_state["Temperature"] = Temperature("MeetingRoomTwo")
    env_state["Brightness"] = Brightness("MeetingRoomTwo")
    env_state["Humidity"] = Humidity("MeetingRoomTwo")
    env_state["Noise"] = Noise("MeetingRoomTwo")
    env_state["AirQuality"] = AirQuality("MeetingRoomTwo")
    env_state["HumanState"] = HumanState("MeetingRoomTwo")

    device_dict["AC"] = AC(env_state, "MeetingRoomTwo")
    device_dict["TV"] = TV(env_state, "MeetingRoomTwo")
    device_dict["Heater"] = Heater(env_state, "MeetingRoomTwo")
    device_dict["Humidifier"] = Humidifier(env_state, "MeetingRoomTwo")
    device_dict["Light"] = Light(env_state, "MeetingRoomTwo")
    # device_dict["Speaker"] = Speaker(env_state, "MeetingRoomTwo")
    device_dict["Curtain"] = Curtain(space_dict["Context"]["env_state"],env_state, "MeetingRoomTwo")
    device_dict["AirPurifier"] = AirPurifier(env_state, "MeetingRoomTwo")
    device_dict["Window"] = Window(space_dict["Context"]["env_state"], env_state, "MeetingRoomTwo")
    room_temp = dict()
    room_temp["device_dict"] = device_dict
    room_temp["env_state"] = env_state
    temp = get_dict("MeetingRoomTwo", room_temp)
    room_temp["action_dict"] = temp["action_dict"]
    room_temp["enable_dict"] = temp["enable_dict"]
    room_temp["ext_action_list"] = temp["ext_action_list"]
    space_dict["MeetingRoomTwo"] = room_temp

    # TeaRoom
    device_dict = dict()
    env_state = dict()
    env_state["Temperature"] = Temperature("TeaRoom")
    env_state["Brightness"] = Brightness("TeaRoom")
    env_state["Humidity"] = Humidity("TeaRoom")
    env_state["Noise"] = Noise("TeaRoom")
    env_state["AirQuality"] = AirQuality("TeaRoom")
    env_state["HumanState"] = HumanState("TeaRoom")

    # device_dict["AC"] = AC(env_state, "TeaRoom")
    device_dict["WaterDispenser"] = WaterDispenser(env_state, "TeaRoom")
    device_dict["MicrowaveOven"] = MicrowaveOven(env_state, "TeaRoom")
    # device_dict["Heater"] = Heater(env_state, "TeaRoom")
    device_dict["Humidifier"] = Humidifier(env_state, "TeaRoom")
    device_dict["Light"] = Light(env_state, "TeaRoom")
    # device_dict["Speaker"] = Speaker(env_state, "TeaRoom")
    device_dict["Curtain"] = Curtain(space_dict["Context"]["env_state"],env_state, "TeaRoom")
    device_dict["AirPurifier"] = AirPurifier(env_state, "TeaRoom")
    device_dict["Window"] = Window(space_dict["Context"]["env_state"], env_state, "TeaRoom")
    room_temp = dict()
    room_temp["device_dict"] = device_dict
    room_temp["env_state"] = env_state
    temp = get_dict("TeaRoom", room_temp)
    room_temp["action_dict"] = temp["action_dict"]
    room_temp["enable_dict"] = temp["enable_dict"]
    room_temp["ext_action_list"] = temp["ext_action_list"]
    space_dict["TeaRoom"] = room_temp

    # Corridor 
    device_dict = dict()
    env_state = dict()
    env_state["Temperature"] = Temperature("Corridor")
    env_state["Brightness"] = Brightness("Corridor")
    env_state["Humidity"] = Humidity("Corridor")
    env_state["Noise"] = Noise("Corridor")
    env_state["AirQuality"] = AirQuality("Corridor")
    env_state["HumanState"] = HumanState("Corridor")

    device_dict["Light"] = Light(env_state, "Corridor")
    device_dict["Speaker"] = Speaker(env_state, "Corridor")
    room_temp = dict()
    room_temp["device_dict"] = device_dict
    room_temp["env_state"] = env_state
    temp = get_dict("Corridor", room_temp)
    room_temp["action_dict"] = temp["action_dict"]
    room_temp["enable_dict"] = temp["enable_dict"]
    room_temp["ext_action_list"] = temp["ext_action_list"]
    space_dict["Corridor"] = room_temp

    # adjacent
    space_dict["Lab"]["device_dict"]["Door"] = Door(
        space_dict["Corridor"]["env_state"], space_dict["Lab"]["env_state"], "Lab")
    space_dict["MeetingRoomOne"]["device_dict"]["Door"] = Door(
        space_dict["Corridor"]["env_state"], space_dict["MeetingRoomOne"]["env_state"], "MeetingRoomOne")
    space_dict["MeetingRoomTwo"]["device_dict"]["Door"] = Door(
        space_dict["TeaRoom"]["env_state"], space_dict["MeetingRoomTwo"]["env_state"], "MeetingRoomTwo")
    space_dict["TeaRoom"]["device_dict"]["Door"] = Door(
        space_dict["Corridor"]["env_state"], space_dict["TeaRoom"]["env_state"], "TeaRoom")
    space_dict["Corridor"]["device_dict"]["Door"] = Door(
        space_dict["Context"]["env_state"], space_dict["Corridor"]["env_state"], "Corridor")

    env["space_dict"] = space_dict
    return env

env = getEnvonment()