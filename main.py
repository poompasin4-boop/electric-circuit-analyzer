# Electric Circuit Analyzer
# Author: Poompasin
# Basic Ohm's Law calculation

def ohms_law(voltage=None, current=None, resistance=None):
    if voltage is None:
        return current * resistance
    elif current is None:
        return voltage / resistance
    elif resistance is None:
        return voltage / current
    else:
        return "Please leave one value empty"

print("Electric Circuit Analyzer")
print("Ohm's Law Calculator")

V = float(input("Enter voltage (V): "))
R = float(input("Enter resistance (Ohm): "))

I = ohms_law(voltage=V, resistance=R)

print(f"Current = {I:.2f} A")
