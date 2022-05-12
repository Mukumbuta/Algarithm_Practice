def wordCount(word):
    charLength = word.split()
    if len(charLength) == 0:
        return 0

    return len(charLength[-1])


if __name__ == '__main__':
    sentence = input("Enter text:\n")
    print(f'The last word in, {sentence}, is {wordCount(sentence)} letters long.')