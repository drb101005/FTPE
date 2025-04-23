#Error Handling
def perform_division():
    try:
        a,b=float(input("Enter first number: ")),float(input("Enter second number: "))
        print(f"{a} / {b} = {a/b}")
    except ZeroDivisionError: print("Error: Cannot divide by zero")
    except ValueError: print("Error: Invalid number")
    except Exception as e: print(f"Error: {e}")
perform_division()