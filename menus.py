import calculator
CALCULATOR_METHOD = {
    "1":"current",
    "2":"load"
}

CALCULATORS = {
    "current":calculator.current_calculator,
    "load":calculator.laod_calculator
}

LAOD_TYPE = {
    "1":"motor",
    "2":"welding",
    "3":"resistive"
}

VOLTAGE_TYPE = {
    "1":220,
    "2":380
}

SAFETY_FACTOR = {
    "welding":100,
    "motor":25,
    "resistive":25
}