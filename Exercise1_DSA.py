# Ask the user to input a temperature
temperature = float(input("Enter the temperature value: "))

# Ask the user to select the conversion type
print("Select the conversion type:")
print("1 = Fahrenheit to Celsius\n2 = Celsius to Fahrenheit")
conversion = int(input("Enter your choice (1 or 2): "))

# Perform the appropriate conversion based on the user's choice
if conversion == 1:
    celsius = (temperature - 32) * 5 / 9
    print(f"{temperature}°F is equal to {celsius:.2f}°C.")
    
elif conversion == 2:
    fahrenheit = (temperature * 9 / 5) + 32
    print(f"{temperature}°C is equal to {fahrenheit:.2f}°F.")
    
else:
    print("Invalid choice. Please select either 1 or 2.")
