from cli import ask_choice, display_result
from config import CALCULATOR_METHOD, INPUT_COLLECTORS, CALCULATORS



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