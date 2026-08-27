import math

method_type = {
    "1":"current",
    "2":"load"
}

load_type = {
    "1":"motor",
    "2":"welding",
    "3":"resistive"
}

voltage_type = {
    "1":220,
    "2":380
}

safety_factor = {
    "welder":100,
    "motor":25,
    "resistive":25
}

power_factor = 0.75

readme = f"""
    AmpGuard is circuit breaker size calculator 
    based on {list(method_type.values())} method
    for now this app can calculated for a few limitation
    load - {list(load_type.values())}
    voltage - {list(voltage_type.values())} VAC
    safety factor - {safety_factor} % dependent on load type
    power factor - {power_factor}
"""

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

while True:
    print(readme)

    method_type_list = """"""
    for list in method_type:
        method_type_list += f"{list} - {method_type[list]}\n"
    print(method_type_list)
    method = input("chose base calculator method :")

    load_power = int(input("What is the power load of your motor in (watts)?"))
    
    result = calculate_load(
        load=load_power, 
        voltage=voltage_type["2"], 
        power_factor=power_factor,
        safety_factor=safety_factor["motor"]
        )
    result2 = load_power/voltage_type["2"]
    print(f"result ampere for your load is : {result} A or {result2} A")
    break

