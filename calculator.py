import math

def calculate_load(load, voltage,power_factor, safety_factor):
    """
    calculate ampere using load method
    """
    return (load/(math.sqrt(3)*voltage*power_factor))*(1+(safety_factor/100))

def calculate_current(current,safety_factor):
    """
    calculate ampere using current method
    """
    return (current*(1+(safety_factor/100)))