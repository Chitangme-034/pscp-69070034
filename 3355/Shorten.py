"""Shorten"""
def main():
    """Ranges"""
    result = []
    start = int(input())
    if start == -1:
        print("")
        return
    end = start
    while True:
        num = int(input())
        if num == -1:
            if start == end:
                result.append(str(start))
            else:
                result.append(str(start) + "-" + str(end))
            break
        if num == end + 1:
            end = num
        else:
            if start == end:
                result.append(str(start))
            else:
                result.append(str(start) + "-" + str(end))

            start = num
            end = num
    print(", ".join(result))
main()
