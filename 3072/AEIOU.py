"""Count Vowels"""
def main():
    """Count vowels in a sentence."""
    text = input()
    vowels = []
    for letter in text:
        if letter.lower() in "aeiou":
            vowels.append(letter)
    print(len(vowels))
main()
