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

def ask_number(question, unit="", min_val=None, max_val=None):
    while True:
        try:
            value = float(input(f"{question} {unit}: "))

            if min_val is not None and value < min_val :
                print(f"error : number must be at least {min_val}.")
                continue

            if max_val is not None and value > max_val:
                print(f"error : number cannot be greater than {max_val}.")
                continue
            
            return value
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")

def display_result(answer, result,unit=""):
    return print(f"\n{answer} {result} {unit}")
