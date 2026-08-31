from config import VOLTAGE_TYPE
from cli import display_result
from math import sqrt

SAFETY_FACTOR = {
    "welding":100,
    "motor":25,
    "resistive":25
}

VOLTAGE = {
    "single_phase":220,
    "three_phase":380
}

def calculate_current(collect_input):
    load_type =collect_input["load_type"]
    margin_of_safety = SAFETY_FACTOR[load_type]
    current = collect_input["current"]
    result = current * (1+(margin_of_safety/100))
    return  display_result(
        answer="circuit breaker size is:",
        result=result,
        unit="A"
        )

def calculate_load(collect_input):
    load_type = collect_input["load_type"]
    voltage_type = collect_input["voltage_type"]
    power = collect_input["power"]
    power_factor = collect_input["power_factor"]
    margin_of_safety = SAFETY_FACTOR[load_type]

    # 220v calculation
    if voltage_type == "single_phase":
        result = (power/(VOLTAGE[voltage_type]*(power_factor/100)))*(1+(margin_of_safety/100))

    # 380v calculation
    elif voltage_type == "three_phase":
        result = (power/(sqrt(3)*VOLTAGE[voltage_type]*(power_factor/100)))*(1+(margin_of_safety/100))
    return display_result(
        answer="circuit breaker size is:",
        result=result,
        unit="A"
        )