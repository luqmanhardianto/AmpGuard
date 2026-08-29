import calculator
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


while True:
    print(readme)
    method = ask_choice(
        question="choose base calculator method:",
        options=menus.CALCULATOR_METHOD
        )

    load = ask_choice(
        question="choose load type:",
        options=menus.LAOD_TYPE
    )
    
    print(f"result ampere for your load is : {method, load} A")
    break

