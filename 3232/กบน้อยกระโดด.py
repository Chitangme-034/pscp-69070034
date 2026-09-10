"""Little Frog Jump"""
def main():
    """Minimum number of jumps"""
    x, y = input().split()
    x = int(x)
    y = int(y)
    jump = x
    total = 0
    count = 0
    while jump > 0:
        total += jump
        count += 1
        if total >= y:
            print(count)
            return
        jump -= 2
    print(-1)
main()
