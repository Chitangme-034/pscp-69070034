"""Giraffes"""
def main():
    """Magic"""
    giraffes = int(input())
    heights = []
    for _ in range(giraffes):
        heights.append(int(input()))
    count = 0
    if giraffes == 1:
        count = 1
    else:
        for i in range(giraffes):
            if not i:
                if heights[i] > heights[i + 1]:
                    count += 1
            elif i == giraffes - 1:
                if heights[i] > heights[i - 1]:
                    count += 1
            elif (heights[i] > heights[i - 1]
                  and heights[i] > heights[i + 1]):
                count += 1
    print(count)
main()
