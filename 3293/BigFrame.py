"""Text Frame"""
def main():
    """Rectangular frame"""
    texts = []
    for _ in range(5):
        text = input().rstrip()
        texts.append(text)
    longest = 0
    for text in texts:
        if len(text) > longest:
            longest = len(text)
    border = "*" * (longest + 4)
    print(border)
    for text in texts:
        spaces = longest - len(text)
        print("* " + text + " " * spaces + " *")
    print(border)
main()
