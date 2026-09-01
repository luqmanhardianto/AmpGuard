from config import VOLTAGE_VALUE, SAFETY_FACTOR, THREE_PHASE_FACTOR

def apply_safety_factor(current, safety_factor):
    return current * safety_factor

def calculate_single_phase_current(power,voltage,power_factor):
    return power / (voltage * power_factor)

def calculate_three_phase_current(power,voltage,power_factor):
    return power / (THREE_PHASE_FACTOR * voltage * power_factor)

LOAD_CALCULATORS={
    "single_phase":calculate_single_phase_current,
    "three_phase":calculate_three_phase_current
}

def calculate_current_method(input):
    return  apply_safety_factor(
        current=input["current"],
        safety_factor=SAFETY_FACTOR[input["load_type"]]
        )

def calculate_load_method(input):

    calculators = LOAD_CALCULATORS[input["voltage_type"]]

    current = calculators(
        power=input["power"],
        voltage=VOLTAGE_VALUE[input["voltage_type"]],
        power_factor=input["power_factor"]
    )

    return apply_safety_factor(
        current=current,
        safety_factor=SAFETY_FACTOR[input["load_type"]]
        )