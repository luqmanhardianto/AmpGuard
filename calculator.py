from config import VOLTAGE_VALUE, SAFETY_FACTOR
from math import sqrt



def calculate_current(collect_input):
    load_type =collect_input["load_type"]
    margin_of_safety = SAFETY_FACTOR[load_type]
    current = collect_input["current"]
    return  apply_safety_factor(
        current=current,
        safety_factor=margin_of_safety
        )

def calculate_load(collect_input):
    load_type = collect_input["load_type"]
    voltage_type = collect_input["voltage_type"]
    power = collect_input["power"]
    power_factor = collect_input["power_factor"]
    margin_of_safety = SAFETY_FACTOR[load_type]
    # 220v calculation
    if voltage_type == "single_phase":
        result = (power/(VOLTAGE_VALUE[voltage_type]*power_factor))


    # 380v calculation
    elif voltage_type == "three_phase":
        result = (power/(sqrt(3)*VOLTAGE_VALUE[voltage_type]*power_factor))

    return apply_safety_factor(
        current=result,
        safety_factor=margin_of_safety
        )

def apply_safety_factor(current, safety_factor):
    return current (1+(safety_factor/100))