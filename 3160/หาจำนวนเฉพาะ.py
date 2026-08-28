"""Prime Numbers"""
def main():
    """Prime numbers in given range"""
    start, end = map(int, input().split())
    count = 0
    result = ""
    for number in range(start, end + 1):
        if number < 2:
            continue
        prime = True
        for divisor in range(2, number):
            if not number % divisor:
                prime = False
                break
        if prime:
            result += str(number) + " "
            count += 1
    if count > 0:
        print(result.strip())
    print("Total primes:", count)
main()
