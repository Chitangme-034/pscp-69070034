"""School Cooperative"""
from decimal import Decimal, ROUND_HALF_UP
def main():
    """Calculate the final price after discount"""
    member = input()
    n = int(input())

    total = Decimal("0")
    for _ in range(n):
        price = Decimal(input())
        total += price
    if member == "Y":
        final_price = total * Decimal("0.95")
    elif member == "N" and total >= Decimal("500"):
        final_price = total * Decimal("0.97")
    else:
        final_price = total
    final_price = final_price.quantize(
        Decimal("0.01"),
        rounding=ROUND_HALF_UP
    )
    print(final_price)
main()
