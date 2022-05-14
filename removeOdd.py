
# Remove Odd numbers from an Array


def removeOdd(arr):
    evenNums = []

    for num in arr:
        if(num % 2 != 0):
            evenNums.append(num)

    return evenNums

randNums = [3, 5, 6, 8, 7, 11, 23, 9, 34]
print(removeOdd(randNums))
