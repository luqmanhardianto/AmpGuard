from config import VOLTAGE, SAFETY_FACTOR
from cli import display_result
from math import sqrt



def calculate_current(collect_input):
    load_type =collect_input["load_type"]
    margin_of_safety = SAFETY_FACTOR[load_type]
    current = collect_input["current"]
    result = current * (1+(margin_of_safety/100))
    return  result

def calculate_load(collect_input):
    load_type = collect_input["load_type"]
    voltage_type = collect_input["voltage_type"]
    power = collect_input["power"]
    power_factor = collect_input["power_factor"]
    margin_of_safety = SAFETY_FACTOR[load_type]

    # 220v calculation
    if voltage_type == "single_phase":
        result = (power/(VOLTAGE[voltage_type]*power_factor))*(1+(margin_of_safety/100))

    # 380v calculation
    elif voltage_type == "three_phase":
        result = (power/(sqrt(3)*VOLTAGE[voltage_type]*power_factor))*(1+(margin_of_safety/100))
    return result