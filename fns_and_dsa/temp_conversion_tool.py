# Global Conversion Factors....
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_OFFSET = 32  # Offset used in Fahrenheit to Celsius conversion

# Funct to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    # Using the global conversion factor for F to C
    return (fahrenheit - FAHRENHEIT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Funct to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    # Using the global conversion factor for C to F
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_OFFSET

# Main funct to interact with the user
def main():
    try:
        # User input for temperature
        temp = float(input("Enter the temperature to convert: "))
        
        # User input for the unit of temperature (C or F)
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        if unit == 'F':
            # Convert Fahrenheit to Celsius
            celsius = convert_to_celsius(temp)
            print(f"{temp}°F is {celsius}°C")
        elif unit == 'C':
            # Convert Celsius to Fahrenheit
            fahrenheit = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {fahrenheit}°F")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
