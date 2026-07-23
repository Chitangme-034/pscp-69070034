"""Palace"""
def main():
    """brick"""
    x = int(input())        # room number
    floor = 1               # start from 1st floor
    while floor ** 2 < x:   # find the first floor where floor² is greater than or equal to x
        floor += 1
    far = (floor**2) - x    # calculate how far x is from the last room on this floor
    room = 2*(floor) - 1    # calculate the number of rooms on this floor
    if not far % 2:         # distance is even
        print(room - 1)
    else:                   # distance is odd
        print(room - 2)
main()
