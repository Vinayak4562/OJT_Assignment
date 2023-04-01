
def celsius(fahrenheit):    
    celsius = (fahrenheit - 32) * 5 / 9                          # Converts a temperature in Fahrenheit to Celsius
    return celsius

temperature_f = int (input("Enter the Temperature: "))           # To take input from user
temperature_c = celsius(temperature_f)
print(f"{temperature_f} degrees Fahrenheit is {temperature_c:.2f} degrees Celsius")


# Out Put: 75 degrees Fahrenheit is 23.89 degrees Celsius
