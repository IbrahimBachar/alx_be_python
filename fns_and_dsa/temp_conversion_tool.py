FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

choice = float(input("Enter the temperature to convert: "))
type = input("Is this temperature is Celsius or Fahrenheit? (C/F): ")

if type == "F":

    def convert_to_celsius(fahrenheit):
        celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
        print(f"{choice}℉ is {celsius}℃")

    convert_to_celsius(choice)
elif type == "C":
    def convert_to_fahrenheit(celsius):
        fahrenheit = CELSIUS_TO_FAHRENHEIT_FACTOR * celsius + 32
        print(f"{choice}℃ is {fahrenheit}℉")

    convert_to_fahrenheit(choice)