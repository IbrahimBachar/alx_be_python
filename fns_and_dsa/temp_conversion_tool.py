FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

choice = float(input("Enter the temperature to convert: "))
type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

if type == "F":

    def convert_to_celsius(fahrenheit):
        celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
        print(f"{choice}℉ is {celsius}℃")

    convert_to_celsius(choice)
elif type == "C":
    def convert_to_fahrenheit(celsius):
        fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
        print(f"{choice}℃ is {fahrenheit}℉")

    convert_to_fahrenheit(choice)
else:
    print("Invalid input! Please try to with C or F")