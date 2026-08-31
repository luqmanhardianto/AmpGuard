from cli import ask_choice, display_result
from config import CALCULATOR_METHOD
from calculator import calculate_current, calculate_load
from inputs import collect_current_inputs, collect_load_inputs

INPUT_COLLECTORS = {
    "current":collect_current_inputs,
    "load":collect_load_inputs
}

CALCULATORS = {
    "current":calculate_current,
    "load":calculate_load
}

readme = """
    AmpGuard is circuit breaker size calculator 
    """

while True:
    print(readme)

    method = ask_choice(
        question="choose base calculator method:",
        options=CALCULATOR_METHOD
    )

    collector = INPUT_COLLECTORS[method]
    data = collector()
    calculators = CALCULATORS[method]
    result = calculators(data)

    display_result(
        answer="circuit breaker ampere rating is :",
        result=result,
        unit="A"
    )
    break