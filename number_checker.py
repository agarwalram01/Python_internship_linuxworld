# Simple Positive, Negative, or Zero Checker

def check_number():
    try:
        # Get input from the user
        number = float(input("Enter a number: "))

        # Check if the number is positive, negative, or zero
        if number > 0:
            print("The number is Positive.")
        elif number < 0:
            print("The number is Negative.")
        else:
            print("The number is Zero.")
            
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    check_number()
