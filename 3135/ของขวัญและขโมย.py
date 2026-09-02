"""Festival Gift"""
def main():
    """Examine the gift"""
    n, k, t = input().split()
    n = int(n)
    k = int(k)
    t = int(t)
    current = 1
    count = 1
    while True:
        current = (current + k - 1) % n + 1
        if current == t:
            count += 1
            break
        if current == 1:
            break
        count += 1
    print(count)
main()
