import math





power_factor = 0.75

readme = f"""
    AmpGuard is circuit breaker size calculator 
    based on {list(method_type.values())} method
    for now this app can calculated for a few limitation
    load - {list(load_type.values())}
    voltage - {list(voltage_type.values())} VAC
    safety factor - {safety_factor} % dependent on load type
    power factor - {power_factor}"""

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

    method_type_list = ""
    for list in method_type:
        method_type_list += f"\n{list} - {method_type[list]}"
    print(method_type_list)
    method = input("choose base calculator method :")

    load_type_list = ""
    for list in load_type:
        load_type_list += f"\n{list} - {load_type[list]}"
    print(load_type_list)
    load = input("choose load type :")

    load_input = int(input(f"What is the {method_type[method]} of your {load_type[load]} in ({unit_type[method_type[method]]}) :"))

    result = calculate_load(
        load=load_input, 
        voltage=voltage_type["2"], 
        power_factor=power_factor,
        safety_factor=safety_factor["motor"]
        )
    
    print(f"result ampere for your load is : {result} A")
    break

