FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9 
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5 
FAHRENHEIT_OFFSET = 32 

def convert_to_celsius(fahrenheit):
    return (fahrenheit - FAHRENHEIT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_OFFSET

converter = float(input("Enter the temperature to convert: "))

fc = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
if fc == "F":
    res = convert_to_celsius(converter)
    print("f to c is: ", res)

elif fc == "C":
    res = convert_to_fahrenheit(converter)
    print("c to f is: ", res)
    
else :
    print("Invalid input. Please enter 'C' or 'F'.")
    exit()