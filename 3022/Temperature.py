"""Temperature"""
def main():
    """Convert temperature"""
    temp = float(input())
    start = input()
    end = input()
    if start == "F":
        temp = (temp - 32) * 5 / 9
    elif start == "K":
        temp -= 273.15
    elif start == "R":
        temp = temp * 5 / 9 - 273.15
    if end == "F":
        temp = temp * 9 / 5 + 32
    elif end == "K":
        temp += 273.15
    elif end == "R":
        temp = (temp + 273.15) * 9 / 5
    print(f"{temp:.2f}")
main()
