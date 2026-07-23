"""Temperature"""
def main():
    """Convert temperature"""
    temp = float(input())
    start = input()
    end = input()
    if start == "F":                    # F to C
        temp = (temp - 32) * 5 / 9
    elif start == "K":                  # K to C
        temp -= 273.15
    elif start == "R":                  # R to C
        temp = temp * 5 / 9 - 273.15
    if end == "F":                      # C to F
        temp = temp * 9 / 5 + 32
    elif end == "K":                    # C to K
        temp += 273.15
    elif end == "R":                    # C to R
        temp = (temp + 273.15) * 9 / 5
    print(f"{temp:.2f}")
main()
