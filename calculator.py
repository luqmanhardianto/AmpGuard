from menus import SAFETY_FACTOR
from cli import display_result

def calculate_current(collect_input):
    margin_of_safety = SAFETY_FACTOR[collect_input['load_type']]
    current = collect_input['current']
    result = current * (1+(margin_of_safety/100))
    return  display_result(
        answer="circuit breaker size is:",
        result=result,
        unit="A"
        )

def calculate_load(collect_input):
    load_type = collect_input["load-type"]
    voltage_type = collect_input{"voltage_type"}
    power = collect_input["power"]
    return print(f"{load_type} {voltage_type} {power}")