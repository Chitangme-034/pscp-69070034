"""Count Vowels"""
def main():
    """Count each vowel"""
    text = input().lower()
    vowels = ["a", "e", "i", "o", "u"]
    count = [0, 0, 0, 0, 0]
    for letter in text:
        if letter in vowels:
            index = vowels.index(letter)
            count[index] += 1
    for index in range(5):
        if count[index]:
            print(vowels[index], ":", count[index])
main()
