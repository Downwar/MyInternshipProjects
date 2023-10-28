def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084

def kilograms_to_pounds(kilograms):
    return kilograms * 2.20462

def pounds_to_kilograms(pounds):
    return pounds / 2.20462

def temperature_converter():
    print("Temperature Converter:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("Enter your choice (1 or 2): ")

    if choice not in ['1', '2']:
        print("Invalid choice. Please enter 1 or 2.")
        return

    value = input("Enter the temperature value: ")

    try:
        temperature = float(value)
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return

    if choice == '1':
        result = celsius_to_fahrenheit(temperature)
        print(f"{temperature}°C is equal to {result}°F.")
    else:
        result = fahrenheit_to_celsius(temperature)
        print(f"{temperature}°F is equal to {result}°C.")

def length_converter():
    print("Length Converter:")
    print("1. Meters to Feet")
    print("2. Feet to Meters")

    choice = input("Enter your choice (1 or 2): ")

    if choice not in ['1', '2']:
        print("Invalid choice. Please enter 1 or 2.")
        return

    value = input("Enter the length value: ")

    try:
        length = float(value)
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return

    if choice == '1':
        result = meters_to_feet(length)
        print(f"{length} meters is equal to {result} feet.")
    else:
        result = feet_to_meters(length)
        print(f"{length} feet is equal to {result} meters.")

def weight_converter():
    print("Weight Converter:")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")

    choice = input("Enter your choice (1 or 2): ")

    if choice not in ['1', '2']:
        print("Invalid choice. Please enter 1 or 2.")
        return

    value = input("Enter the weight value: ")

    try:
        weight = float(value)
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return

    if choice == '1':
        result = kilograms_to_pounds(weight)
        print(f"{weight} kilograms is equal to {result} pounds.")
    else:
        result = pounds_to_kilograms(weight)
        print(f"{weight} pounds is equal to {result} kilograms.")

if __name__ == "__main__":
    print("Welcome to the Unit Converter!")
    print("Select the type of conversion:")
    print("1. Temperature")
    print("2. Length")
    print("3. Weight")

    conversion_type = input("Enter your choice (1, 2, or 3): ")

    if conversion_type == '1':
        temperature_converter()
    elif conversion_type == '2':
        length_converter()
    elif conversion_type == '3':
        weight_converter()
    else:
        print("Invalid choice. Please enter 1, 2, or 3 for the type of conversion.")
