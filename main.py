import inputs

power_factor = 0.75

readme = f"""
    AmpGuard is circuit breaker size calculator 
    """

while True:
    print(readme)
    load_type = inputs.ask_load_types()
    print(load_type)

    get_current = inputs.ask_current()
    print(get_current)
    break

