"""B - Fully pair?"""
def main():
    """dance"""
    text = input()
    count = {}
    for char in text:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    result = ""
    for char in text:
        if count[char] % 2 == 1:
            result += char
            count[char] = 0
    if not result:
        print("fully paired")
    else:
        print(result)
main()
