from math import sqrt
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
    "welding":2,
    "motor":1.25,
    "resistive":1.25
}

VOLTAGE_VALUE = {
    "single_phase":220,
    "three_phase":380
}

THREE_PHASE_FACTOR = sqrt(3)
