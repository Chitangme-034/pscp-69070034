"""isPrime_large"""
def main():
    """prime number"""
    num = int(input())
    if num < 2:
        print("NO")
        return
    i = 2
    while i <= num ** 0.5:
        if not num % i:
            print("NO")
            return
        i += 1
    print("YES")
main()
