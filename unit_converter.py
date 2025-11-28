def print_menu():
    
    print("\n--- Simple Unit Converter ---")
    print("1. Length (Kilometers <-> Miles)")
    print("2. Weight (Kilograms <-> Pounds)")
    print("3. Temperature (Celsius <-> Fahrenheit)")
    print("4. Exit")

def length_converter():
    
    print("\nLength Converter:")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    choice = input("Choose conversion (1/2): ")
    
    if choice == '1':
        km = float(input("Enter kilometers: "))
        miles = km * 0.621371
        print(f"{km} km is equal to {miles:.2f} miles")
    elif choice == '2':
        miles = float(input("Enter miles: "))
        km = miles / 0.621371
        print(f"{miles} miles is equal to {km:.2f} km")
    else:
        print("Invalid choice")

def weight_converter():
    print("\nWeight Converter:")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    choice = input("Choose conversion (1/2): ")
    
    if choice == '1':
        kg = float(input("Enter kilograms: "))
        lbs = kg * 2.20462
        print(f"{kg} kg is equal to {lbs:.2f} lbs")
    elif choice == '2':
        lbs = float(input("Enter pounds: "))
        kg = lbs / 2.20462
        print(f"{lbs} lbs is equal to {kg:.2f} kg")
    else:
        print("Invalid choice")

def temperature_converter():
    
    print("\nTemperature Converter:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Choose conversion (1/2): ")
    
    if choice == '1':
        c = float(input("Enter Celsius: "))
        f = (c * 9/5) + 32
        print(f"{c}°C is equal to {f:.2f}°F")
    elif choice == '2':
        f = float(input("Enter Fahrenheit: "))
        c = (f - 32) * 5/9
        print(f"{f}°F is equal to {c:.2f}°C")
    else:
        print("Invalid choice")

def main():
    
    while True:
        print_menu()
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            length_converter()
        elif choice == '2':
            weight_converter()
        elif choice == '3':
            temperature_converter()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
