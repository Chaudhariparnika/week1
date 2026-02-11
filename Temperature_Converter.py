Celsius = float(input("Enter the temperature in Celsius: "))
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
  
fahrenheit = celsius_to_fahrenheit(Celsius)
print(f"{Celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")