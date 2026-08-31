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

def ask_power_factor():
    return ask_number(
        question="enter power factor",
        unit="0-100%"
    )

def collect_current_inputs():
    return {
        "load_type":ask_load_types(),
        "current":ask_current()
    }

def collect_load_inputs():
    return {
        "load_type":ask_load_types(),
        "voltage_type":ask_voltage_types(),
        "power":ask_power(),
        "power_factor":ask_power_factor()
    }
