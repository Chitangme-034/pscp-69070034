"""Count Remainder"""
def main():
    """Count numbers with the given remainder"""
    start = int(input())
    end = int(input())
    divisor = int(input())
    remainder = int(input())
    count = 0
    for number in range(start, end + 1):
        if number % divisor == remainder:
            count += 1
    print(count)
main()
