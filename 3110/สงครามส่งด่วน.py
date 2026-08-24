"""Express Delivery"""
def main():
    """Calculate delivery fee"""
    start, destination = input().split()
    weight = float(input())
    if start == "BKK" and destination == "CNX":
        base = 10
        rate = 30
    elif start == "CNX" and destination == "UBP":
        base = 15
        rate = 40
    elif start == "UBP" and destination == "BKK":
        base = 20
        rate = 40
    elif start == "BKK" and destination == "PKT":
        base = 25
        rate = 50
    elif start == "PKT" and destination == "CNX":
        base = 30
        rate = 60
    elif start == "UBP" and destination == "PKT":
        base = 40
        rate = 70
    else:
        print("Error")
        return
    price = base + weight * rate
    print(f"{price:.2f}")
main()
