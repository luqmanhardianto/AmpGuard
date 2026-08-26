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

while True:
    print(readme)

    method_type = input(f"method calculate, type {method}:")
    load_power = input("What is the power load of your motor (watts)?")
    result = (int(load_power)/(math.sqrt(3)*voltage_type*power_factor))*(1+(safety_factor/100))
    print(f"result ampere for your load is : {result} A")
    break

