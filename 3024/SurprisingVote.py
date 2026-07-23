"""Vote"""
def main():
    """Check surprising score"""
    total = float(input())
    highest = float(input())
    lowest = max(0, total - 2 * highest)
    if highest - lowest > 2:
        print("Surprising")
    else:
        print("Not surprising")
main()
