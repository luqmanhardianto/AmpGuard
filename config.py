from calculator import calculate_current, calculate_load
from inputs import collect_current_inputs, collect_load_inputs

CALCULATOR_METHOD = {
    "1":"current",
    "2":"load"
}


LOAD_TYPE = {
    "1":"motor",
    "2":"welding",
    "3":"resistive"
}

VOLTAGE_TYPE = {
    "1":"single_phase",
    "2":"three_phase"
}

SAFETY_FACTOR = {
    "welding":100,
    "motor":25,
    "resistive":25
}

VOLTAGE = {
    "single_phase":220,
    "three_phase":380
}

INPUT_COLLECTORS = {
    "current":collect_current_inputs,
    "load":collect_load_inputs
}

CALCULATORS = {
    "current":calculate_current,
    "load":calculate_load
}