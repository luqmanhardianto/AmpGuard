from menus import SAFETY_FACTOR, VOLTAGE_TYPE
from cli import display_result

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
    margin_of_safety = SAFETY_FACTOR[load_type]
    if voltage_type == VOLTAGE_TYPE["1"]:
        result = (power/voltage_type)*(1+(margin_of_safety/100))
    elif voltage_type == VOLTAGE_TYPE["2"]:
        result = (power/voltage_type)*(1+(margin_of_safety/100))
    return display_result(
        answer="circuit breaker size is:",
        result=result,
        unit="A"
        )

calculate_load({
    "load_type":"motor",
    "voltage_type":380,
    "power":2200
    })