"""Temperature"""
def main():
    """Convert temperature"""
    temperature = float(input())
    from_unit = input()
    to_unit = input()
    if from_unit == "C":        #Celsius
        celsius = temperature
    elif from_unit == "F":      #Fahrenheit
        celsius = (temperature - 32) * 5 / 9
    elif from_unit == "K":      #Kelvin
        celsius = temperature - 273.15
    else:                       # R / Rankine
        celsius = (temperature * 5 / 9) - 273.15
    if to_unit == "C":
        answer = celsius
    elif to_unit == "F":
        answer = celsius * 9 / 5 + 32
    elif to_unit == "K":
        answer = celsius + 273.15
    else:
        answer = (celsius + 273.15) * 9 / 5
    print(f"{answer:.2f}")
main()
