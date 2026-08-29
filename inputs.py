from cli import ask_choice, ask_number
from menus import LOAD_TYPE, VOLTAGE_TYPE

def ask_load_types():
    return ask_choice(
        question="choose load type:",
        options=LOAD_TYPE
    )

def ask_voltage_types():
    return ask_choice(
        question="choose voltage type",
        options=VOLTAGE_TYPE
    )

def ask_current():
    return ask_number(
        question="enter current",
        unit="A"
    )

def ask_power():
    return ask_number(
        question="enter power",
        unit="Watt"
    )