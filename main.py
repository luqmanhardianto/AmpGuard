import inputs
from cli import ask_choice
from menus import CALCULATOR_METHOD

power_factor = 0.75

readme = f"""
    AmpGuard is circuit breaker size calculator 
    """

while True:
    print(readme)

    method = ask_choice(
        question="choose base calculator method:",
        options=CALCULATOR_METHOD
    )

    print(method)
    break