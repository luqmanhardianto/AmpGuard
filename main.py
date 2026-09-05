from cli import ask_choice, display_result
from config import CALCULATOR_METHOD
from calculator import calculate_current_method, calculate_load_method
from inputs import collect_current_inputs, collect_load_inputs

INPUT_COLLECTORS = {
    "current":collect_current_inputs,
    "load":collect_load_inputs
}

CALCULATORS = {
    "current":calculate_current_method,
    "load":calculate_load_method
}

readme = """
    AmpGuard is circuit breaker size calculator 
    """

def main():
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

if __name__ == "__main__":
    main()