# Display options for calculation
print("1 = Voltage Calculator\n2 = Resistance Calculator\n3 = Current Calculator")
choice = int(input("Select option: "))

# Add calculations
if choice == 1:
    resistance = float(input("Resistance: "))
    current = float(input("Current: "))
    print(f"Voltage = {resistance * current} V")
elif choice == 2:
    voltage = float(input("Voltage: "))
    current = float(input("Current: "))
    print(f"Resistance = {voltage / current} Ω")
elif choice == 3:
    voltage = float(input("Voltage: "))
    resistance = float(input("Resistance: "))
    print(f"Current = {voltage / resistance} A")
# Add invalid option message
else:
    print("Please choose only from 1-3")
