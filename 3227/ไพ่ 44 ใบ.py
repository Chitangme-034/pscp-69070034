"""Card Name Converter"""
def main():
    """Code to Full name"""
    card = input().upper()
    value = card[:-1]
    suit = card[-1]
    if value == "A":
        value_name = "ace"
    elif value == "J":
        value_name = "jack"
    elif value == "Q":
        value_name = "queen"
    elif value == "K":
        value_name = "king"
    else:
        value_name = value
    if suit == "D":
        suit_name = "diamonds"
    elif suit == "H":
        suit_name = "hearts"
    elif suit == "S":
        suit_name = "spades"
    else:
        suit_name = "clubs"
    print(value_name + " of " + suit_name)
main()
