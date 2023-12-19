from environment.device.AC import AC
from environment.device.AirPurifier import AirPurifier
from environment.device.Curtain import Curtain
from environment.device.Door import Door
from environment.device.Heater import Heater
from environment.device.Humidifier import Humidifier
from environment.device.MicrowaveOven import MicrowaveOven
from environment.device.WashingMachine import WashingMachine
from environment.device.CookerHood import CookerHood
from environment.device.Fridge import Fridge
from environment.device.TowelDryer import TowelDryer
from environment.device.WaterHeater import WaterHeater
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

import imp
import os
import re

device_list = []
state_list = []
def get_dir(path,type):
    try:
        file_list = os.listdir(path)
    except:
        file_list = []
    if file_list:
        for file in file_list:
            file = os.path.join(path, file)
            if os.path.isdir(file):
                get_dir(file,type)
            else:
                if file.endswith(".py"):
                    with open(file, encoding="utf-8") as f:
                        for line in f.readlines():
                            cls_match = re.match(r"class\s(.*?)[\(:]", line)
                            if cls_match:
                                cls_name = cls_match.group(1)
                                try:
                                    module = imp.load_source('mycl', file)
                                    cls_a = getattr(module, cls_name)
                                    if cls_a:
                                        if type == 'device':
                                            device_list.append(cls_name)
                                        else:
                                            state_list.append(cls_name)
                                except:
                                    pass

def getHomeEnvonment():
    env = dict()
    space_dict = dict()

    # context
    device_dict = dict()
    env_state = dict()
    env_state["Temperature"] = Temperature()
    env_state["Humidity"] = Humidity()
    env_state["Brightness"] = Brightness()
    env_state["AirQuality"] = AirQuality()
    env_state["Weather"] = Weather()
    room_temp = dict()
    room_temp["device_dict"] = device_dict
    room_temp["env_state"] = env_state
    space_dict["Context"] = room_temp

    # BedroomOne
    device_dict = dict()
    env_state = dict()
    env_state["Temperature"] = Temperature()
    env_state["Brightness"] = Brightness()
    env_state["Humidity"] = Humidity()
    env_state["AirQuality"] = AirQuality()
    env_state["HumanState"] = HumanState(1)

    device_dict["AC"] = AC()
    device_dict["Heater"] = Heater()
    device_dict["Door"] = Door()
    device_dict["Humidifier"] = Humidifier()
    device_dict["Light"] = Light()
    device_dict["Curtain"] = Curtain()
    device_dict["AirPurifier"] = AirPurifier()
    device_dict["Window"] = Window()
    room_temp = dict()
    room_temp["device_dict"] = device_dict
    room_temp["env_state"] = env_state
    space_dict["BedroomOne"] = room_temp

    # BedroomTwo
    device_dict = dict()
    env_state = dict()
    env_state["Temperature"] = Temperature()
    env_state["Brightness"] = Brightness()
    env_state["Humidity"] = Humidity()
    env_state["AirQuality"] = AirQuality()
    env_state["HumanState"] = HumanState(2)

    device_dict["AC"] = AC()
    device_dict["Heater"] = Heater()
    device_dict["Door"] = Door()
    device_dict["Humidifier"] = Humidifier()
    device_dict["Light"] = Light()
    device_dict["Curtain"] = Curtain()
    device_dict["AirPurifier"] = AirPurifier()
    device_dict["Window"] = Window()
    room_temp = dict()
    room_temp["device_dict"] = device_dict
    room_temp["env_state"] = env_state
    space_dict["BedroomTwo"] = room_temp

    # Balcony
    device_dict = dict()
    env_state = dict()
    env_state["Temperature"] = Temperature()
    env_state["Brightness"] = Brightness()
    env_state["Humidity"] = Humidity()
    env_state["AirQuality"] = AirQuality()
    env_state["HumanState"] = HumanState(0)

    device_dict["Door"] = Door()
    device_dict["Light"] = Light()
    device_dict["Curtain"] = Curtain()
    device_dict["WashingMachine"] = WashingMachine()
    device_dict["Window"] = Window()
    room_temp = dict()
    room_temp["device_dict"] = device_dict
    room_temp["env_state"] = env_state
    space_dict["Balcony"] = room_temp

    # LivingRoom
    device_dict = dict()
    env_state = dict()
    env_state["Temperature"] = Temperature()
    env_state["Brightness"] = Brightness()
    env_state["Humidity"] = Humidity()
    env_state["AirQuality"] = AirQuality()
    env_state["HumanState"] = HumanState(0)

    device_dict["AC"] = AC()
    device_dict["Door"] = Door()
    device_dict["Heater"] = Heater()
    device_dict["Humidifier"] = Humidifier()
    device_dict["Light"] = Light()
    device_dict["Speaker"] = Speaker()
    device_dict["Curtain"] = Curtain()
    device_dict["AirPurifier"] = AirPurifier()
    device_dict["Window"] = Window()
    room_temp = dict()
    room_temp["device_dict"] = device_dict
    room_temp["env_state"] = env_state
    space_dict["LivingRoom"] = room_temp

    # Kitchen 
    device_dict = dict()
    env_state = dict()
    env_state["Temperature"] = Temperature()
    env_state["Brightness"] = Brightness()
    env_state["Humidity"] = Humidity()
    env_state["AirQuality"] = AirQuality()
    env_state["HumanState"] = HumanState(0)

    device_dict["Light"] = Light()
    device_dict["Curtain"] = Curtain()
    device_dict["Door"] = Door()
    device_dict["Window"] = Window()
    device_dict["WaterDispenser"] = WaterDispenser()
    device_dict["CookerHood"] = CookerHood()
    device_dict["Fridge"] = Fridge()
    room_temp = dict()
    room_temp["device_dict"] = device_dict
    room_temp["env_state"] = env_state
    space_dict["Kitchen"] = room_temp
    
    # Bathroom 
    device_dict = dict()
    env_state = dict()
    env_state["Temperature"] = Temperature()
    env_state["Brightness"] = Brightness()
    env_state["Humidity"] = Humidity()
    env_state["AirQuality"] = AirQuality()
    env_state["HumanState"] = HumanState(0)

    device_dict["Light"] = Light()
    device_dict["Door"] = Door()
    device_dict["TowelDryer"] = TowelDryer()
    device_dict["WaterHeater"] = WaterHeater()
    room_temp = dict()
    room_temp["device_dict"] = device_dict
    room_temp["env_state"] = env_state
    space_dict["Bathroom"] = room_temp
    
    # Cloakroom 
    device_dict = dict()
    env_state = dict()
    env_state["Temperature"] = Temperature()
    env_state["Brightness"] = Brightness()
    env_state["Humidity"] = Humidity()
    env_state["AirQuality"] = AirQuality()
    env_state["HumanState"] = HumanState(0)

    device_dict["Light"] = Light()
    device_dict["Door"] = Door()
    room_temp = dict()
    room_temp["device_dict"] = device_dict
    room_temp["env_state"] = env_state
    space_dict["Cloakroom"] = room_temp

    env["space_dict"] = space_dict
    return env

def getEnvonment():
    env = dict()
    space_dict = dict()

    # context
    device_dict = dict()
    env_state = dict()
    env_state["Temperature"] = Temperature()
    env_state["Humidity"] = Humidity()
    env_state["Brightness"] = Brightness()
    env_state["AirQuality"] = AirQuality()
    env_state["Weather"] = Weather()
    room_temp = dict()
    room_temp["device_dict"] = device_dict
    room_temp["env_state"] = env_state
    space_dict["Context"] = room_temp

    # Lab
    device_dict = dict()
    env_state = dict()
    env_state["Temperature"] = Temperature()
    env_state["Brightness"] = Brightness()
    env_state["Humidity"] = Humidity()
    env_state["Noise"] = Noise()
    env_state["AirQuality"] = AirQuality()
    env_state["HumanState"] = HumanState()

    device_dict["AC"] = AC()
    device_dict["Heater"] = Heater()
    device_dict["Door"] = Door()
    device_dict["Humidifier"] = Humidifier()
    device_dict["Light"] = Light()
    device_dict["Speaker"] = Speaker()
    device_dict["Printer"] = Printer()
    device_dict["Curtain"] = Curtain()
    device_dict["AirPurifier"] = AirPurifier()
    device_dict["Window"] = Window()
    room_temp = dict()
    room_temp["device_dict"] = device_dict
    room_temp["env_state"] = env_state
    space_dict["Lab"] = room_temp

    # MeetingRoomOne
    device_dict = dict()
    env_state = dict()
    env_state["Temperature"] = Temperature()
    env_state["Brightness"] = Brightness()
    env_state["Humidity"] = Humidity()
    env_state["Noise"] = Noise()
    env_state["AirQuality"] = AirQuality()
    env_state["HumanState"] = HumanState()

    device_dict["AC"] = AC()
    device_dict["TV"] = TV()
    device_dict["Door"] = Door()
    device_dict["Heater"] = Heater()
    device_dict["Humidifier"] = Humidifier()
    device_dict["Light"] = Light()
    device_dict["Speaker"] = Speaker()
    device_dict["Curtain"] = Curtain()
    device_dict["AirPurifier"] = AirPurifier()
    device_dict["Window"] = Window()
    room_temp = dict()
    room_temp["device_dict"] = device_dict
    room_temp["env_state"] = env_state
    space_dict["MeetingRoomOne"] = room_temp

    # MeetingRoomTwo
    device_dict = dict()
    env_state = dict()
    env_state["Temperature"] = Temperature()
    env_state["Brightness"] = Brightness()
    env_state["Humidity"] = Humidity()
    env_state["Noise"] = Noise()
    env_state["AirQuality"] = AirQuality()
    env_state["HumanState"] = HumanState()

    device_dict["AC"] = AC()
    device_dict["TV"] = TV()
    device_dict["Door"] = Door()
    device_dict["Door"] = Door()
    device_dict["Heater"] = Heater()
    device_dict["Humidifier"] = Humidifier()
    device_dict["Light"] = Light()
    device_dict["Speaker"] = Speaker()
    device_dict["Curtain"] = Curtain()
    device_dict["AirPurifier"] = AirPurifier()
    device_dict["Window"] = Window()
    room_temp = dict()
    room_temp["device_dict"] = device_dict
    room_temp["env_state"] = env_state
    space_dict["MeetingRoomTwo"] = room_temp

    # TeaRoom
    device_dict = dict()
    env_state = dict()
    env_state["Temperature"] = Temperature()
    env_state["Brightness"] = Brightness()
    env_state["Humidity"] = Humidity()
    env_state["Noise"] = Noise()
    env_state["AirQuality"] = AirQuality()
    env_state["HumanState"] = HumanState()

    # device_dict["AC"] = AC()
    device_dict["WaterDispenser"] = WaterDispenser()
    device_dict["MicrowaveOven"] = MicrowaveOven()
    device_dict["Door"] = Door()
    # device_dict["Heater"] = Heater()
    device_dict["Humidifier"] = Humidifier()
    device_dict["Light"] = Light()
    # device_dict["Speaker"] = Speaker()
    device_dict["Curtain"] = Curtain()
    device_dict["AirPurifier"] = AirPurifier()
    device_dict["Window"] = Window()
    room_temp = dict()
    room_temp["device_dict"] = device_dict
    room_temp["env_state"] = env_state
    space_dict["TeaRoom"] = room_temp

    # Corridor 
    device_dict = dict()
    env_state = dict()
    env_state["Temperature"] = Temperature()
    env_state["Brightness"] = Brightness()
    env_state["Humidity"] = Humidity()
    env_state["Noise"] = Noise()
    env_state["AirQuality"] = AirQuality()
    env_state["HumanState"] = HumanState()

    device_dict["Light"] = Light()
    device_dict["Speaker"] = Speaker()
    device_dict["Door"] = Door()
    room_temp = dict()
    room_temp["device_dict"] = device_dict
    room_temp["env_state"] = env_state
    space_dict["Corridor"] = room_temp

    env["space_dict"] = space_dict
    return env

# env = getEnvonment()
env = getHomeEnvonment()
path = "./environment/device"
get_dir(path, 'device')
path = "./environment/state"
get_dir(path, 'state')

def getEnv():
    return env

def setEnv(e):
    global env
    env = e