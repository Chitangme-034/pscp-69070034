"""Festival Gift"""
def main():
    """Examine the gift"""
    n, k, t = map(int, input().split())
    current = 1
    count = 1

    if t == 1:
        print(1)
    else:
        while True:
            current = (current + k) % n
            if current == 1:
                print(count)
                break
            count += 1
            if current == t:
                print(count)
                break
main()
