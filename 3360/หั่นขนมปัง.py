"""Bread"""
def main():
    """Largest pieces"""
    w, h, _, _ = map(int, input().split())
    x_cuts = list(map(int, input().split()))
    y_cuts = list(map(int, input().split()))
    widths = []
    previous = 0
    for cut in x_cuts:
        widths.append(cut - previous)
        previous = cut
    widths.append(w - previous)
    heights = []
    previous = 0
    for cut in y_cuts:
        heights.append(cut - previous)
        previous = cut
    heights.append(h - previous)
    largest = 0
    second_largest = 0
    for width in widths:
        for height in heights:
            area = width * height
            if area >= largest:
                second_largest = largest
                largest = area
            elif area > second_largest:
                second_largest = area
    print(largest, second_largest)
main()
