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

            if value <= 0 :
                print("value must be greater than 0.")
                continue
            
            return value
        except ValueError:
            print("please enter a valid number.")

def display_result(answer, result,unit=""):
    return print(f"\n{answer} {result} {unit}")
