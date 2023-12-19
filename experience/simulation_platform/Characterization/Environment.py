from Characterization.device.AC import AC
from Characterization.device.AirPurifier import AirPurifier
from Characterization.device.Curtain import Curtain
from Characterization.device.Door import Door
from Characterization.device.Heater import Heater
from Characterization.device.Humidifier import Humidifier
from Characterization.device.MicrowaveOven import MicrowaveOven
from Characterization.device.TV import TV
from Characterization.device.Light import Light
from Characterization.device.Printer import Printer
from Characterization.device.Speaker import Speaker
from Characterization.device.WaterDispenser import WaterDispenser
from Characterization.device.Window import Window
from Characterization.state.AirQuality import AirQuality
from Characterization.state.Brightness import Brightness
from Characterization.state.HumanState import HumanState
from Characterization.state.Humidity import Humidity
from Characterization.state.Noise import Noise
from Characterization.state.Temperature import Temperature
from Characterization.state.Weather import Weather
from Characterization.device.TowelDryer import TowelDryer
from Characterization.device.WashingMachine import WashingMachine
from Characterization.device.WaterHeater import WaterHeater
from Characterization.device.Fridge import Fridge
from Characterization.device.CookerHood import CookerHood

import requests
from config import getIP



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

def getEnvonment(ip,space):
    env = dict()
    space_dict = dict()
    url = ip + "/room_list"
    room_list = requests.get(url).json()
    for room in room_list:
        device_dict = dict()
        env_state = dict()
        
        url = ip + "/room_state/" + room
        room_state = requests.get(url).json()
        temperature = Environment Change
        brightness = Environment Change
        airquality = Environment Change
        humanstate = Environment Change
        humidity = Environment Change
        noise = Environment Change
        weather = Environment Change
        for state in room_state:
            match state:
                case "Temperature":
                    temperature = Temperature(room,space)
                    env_state["Temperature"] = temperature
                case "Brightness":
                    brightness = Brightness(room,space)
                    env_state["Brightness"] = brightness
                case "AirQuality":
                    airquality = AirQuality(room,space)
                    env_state["AirQuality"] = airquality
                case "HumanState":
                    humanstate = HumanState(room,space)
                    env_state["HumanState"] = humanstate
                case "Humidity":
                    humidity = Humidity(room,space)
                    env_state["Humidity"] = humidity
                case "Noise":
                    noise = Noise(room,space)
                    env_state["Noise"] = noise
                case "Weather":
                    weather = Weather(room,space)
                    env_state["Weather"] = weather

        url = ip + "/room_device/" + room
        room_device = requests.get(url).json()

        for device in room_device:
            match device[:-3]:
                case "AC":
                    device_dict["AC"] = AC(room,space)
                case "Window":
                    device_dict["Window"] = Window(room,space)
                case "Light":
                    device_dict["Light"] = Light(room,space)
                case "Curtain":
                    device_dict["Curtain"] = Curtain(room,space)
                case "Door":
                    device_dict["Door"] = Door(room,space)
                case "Heater":
                    device_dict["Heater"] = Heater(room,space)
                case "Humidifier":
                    device_dict["Humidifier"] = Humidifier(room,space)
                case "MicrowaveOven":
                    device_dict["MicrowaveOven"] = MicrowaveOven(room,space)
                case "Printer":
                    device_dict["Printer"] = Printer(room,space)
                case "AirPurifier":
                    device_dict["AirPurifier"] = AirPurifier(room,space)
                case "Speaker":
                    device_dict["Speaker"] = Speaker(room,space)
                case "TV":
                    device_dict["TV"] = TV(room,space)
                case "WaterDispenser":
                    device_dict["WaterDispenser"] = WaterDispenser(room,space)
                case "Fridge":
                    device_dict["Fridge"] = Fridge(room,space)
                case "WaterHeater":
                    device_dict["WaterHeater"] = WaterHeater(room,space)
                case "TowelDryer":
                    device_dict["TowelDryer"] = TowelDryer(room,space)
                case "WashingMachine":
                    device_dict["WashingMachine"] = WashingMachine(room,space)
                case "CookerHood":
                    device_dict["CookerHood"] = CookerHood(room,space)

        room_temp = dict()
        room_temp["device_dict"] = device_dict
        room_temp["env_state"] = env_state
        temp = get_dict(room, room_temp)
        room_temp["action_dict"] = temp["action_dict"]
        room_temp["enable_dict"] = temp["enable_dict"]
        room_temp["ext_action_list"] = temp["ext_action_list"]
        space_dict[room] = room_temp

    env["space_dict"] = space_dict
    return env

env = Environment Change

def setEnv(space):
    global env
    env = getEnvonment(getIP(),space)
    
def getEnv():
    global env
    return env
    