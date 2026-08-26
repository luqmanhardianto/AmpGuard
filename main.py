import math

method = ["load"]
load_type = ["motors"]
voltage_type = 380
safety_factor = 25
power_factor = 0.9
readme = f"""
    AmpGuard is circuit breaker size calculator 
    based on {method} method
    for now this app can calculated for a few limitation
    load - {load_type}
    voltage - {voltage_type} VAC
    safety factor - {safety_factor} %
    power factor - {power_factor}
"""

def calculate_load(load, voltage,power_factor, safety_factor):
    """
    calculate ampere using load method
    """
    return (load/(math.sqrt(3)*voltage*power_factor))*(1+(safety_factor/100))

while True:
    print(readme)

    load_power = int(input("What is the power load of your motor in (watts)?"))
    result = calculate_load(
        load=load_power, 
        voltage=voltage_type, 
        power_factor=power_factor,
        safety_factor=safety_factor
        )
    print(f"result ampere for your load is : {result} A")
    break

