"""Rabbit Lottery"""
def main():
    """Check lottery prize"""
    winning = input().split()
    ticket = input().split()
    win_letter = winning[0]
    win_number = winning[1]
    my_letter = ticket[0]
    my_number = ticket[1]
    if win_letter == my_letter and win_number == my_number:
        print(1000000)
    elif win_number == my_number:
        print(100000)
    elif win_letter == my_letter and win_number[-3:] == my_number[-3:]:
        print(2000)
    elif win_letter == my_letter and win_number[-2:] == my_number[-2:]:
        print(1000)
    elif win_number[-3:] == my_number[-3:]:
        print(200)
    elif win_number[-2:] == my_number[-2:]:
        print(100)
    elif win_letter == my_letter:
        print(20)
    else:
        print(0)
main()
