"""Flower Field"""
def main():
    """Last planted flower"""
    l, n = map(int, input().split())
    diagonal = 1
    total = 1
    while total < n:
        diagonal += 1
        total += diagonal
    band = (diagonal - 1) // l + 1
    print(band)
main()
