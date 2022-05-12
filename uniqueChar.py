# Implement an algorithm using Python to determine if all characters in a string are unique,
# What if you can not use additional data structures.

MAX_CHAR = 256

def checkUnique(userStr):
    charNum = len(userStr)

    if charNum > MAX_CHAR:
        return False

    charsCount = [False] * MAX_CHAR

    for index in range(charNum):
        charIndex = ord(userStr[index])
        if charsCount[charIndex] == True:
            return False
        charsCount[charIndex] = True
    return True
        

if __name__ == '__main__':
    userString = input("Enter any word:\n").lower()
    if (checkUnique(userString)):
        print(f'The word you entered, {userString}, contains unique characters only.')

    else:
        print(f'The word you entered, {userString}, contains duplicate characters.')