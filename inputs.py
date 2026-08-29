from cli import ask_choice, ask_number
from menus import LOAD_TYPE, VOLTAGE_TYPE

def ask_load_types():
    return ask_choice(
        "choose load type:",
        LOAD_TYPE
    )