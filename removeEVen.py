# Remove Even numbers from a Array

def removeEven(arr):

    oddNums = []

    for number in arr:
        if(number % 2 != 0):
            oddNums.append(number)

    return oddNums

# Driver Code
if __name__ == '__main__':
    randNums = [3, 5, 6, 8, 7, 11, 23, 9, 34]
    print(removeEven(randNums))
    