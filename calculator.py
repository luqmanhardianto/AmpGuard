from config import VOLTAGE_VALUE, SAFETY_FACTOR, THREE_PHASE_FACTOR

def apply_safety_factor(current, safety_factor):
    return current *(1+(safety_factor/100))

def calculate_single_phase_current(power,voltage,power_factor):
    return power / (voltage * power_factor)

def calculate_three_phase_current(power,voltage,power_factor):
    return power / (THREE_PHASE_FACTOR * voltage * power_factor)

LOAD_CALCULATORS={
    "single_phase":calculate_single_phase_current,
    "three_phase":calculate_three_phase_current
}

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

    safety_factor = SAFETY_FACTOR[load_type]
    voltage = VOLTAGE_VALUE[voltage_type]

    calculators = LOAD_CALCULATORS[voltage_type]

    current = calculators(
        power=power,
        voltage=voltage,
        power_factor=power_factor
    )

    return apply_safety_factor(
        current=current,
        safety_factor=safety_factor
        )