"""Count by ten"""
def main():
    """Divide by 10"""
    number = int(input())
    while number >= 0:
        if not number % 10:
            print(number, end=" ")
        number -= 1
main()
