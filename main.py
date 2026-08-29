import menus

power_factor = 0.75

readme = f"""
    AmpGuard is circuit breaker size calculator 
    """

def ask_choice(question,options):
    print(f"\n{question}")

    for index, label in options.items():
        print(f"{index} - {label}")

    while True:
        try:
            choice = input("> ")
            return options[choice]
        except (ValueError, KeyError):
            print("invalid choice. try again.")

def ask_number(question, unit=""):
    while True:
        try:
            value = float(input(f"{question} {unit}: "))
            return value
        except ValueError:
            print("please enter a valid number.")

while True:
    print(readme)
    method = ask_choice(
        question="choose base calculator method:",
        options=menus.CALCULATOR_METHOD
        )

    calculator = menus.CALCULATORS[method]
    
    print(f"result ampere for your load is : {calculator} A")
    break

