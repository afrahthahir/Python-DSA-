

from util import timing_decorator
    
@timing_decorator    
def linearSearch(list, searchVal):
    
    for i in range(0,len(list)):
        if list[i] == searchVal:
            return i
        
    return -1
    
@timing_decorator
def binarySearch(list, searchVal):

    leftIndex = 0
    rightIndex = len(list) - 1

    while leftIndex <= rightIndex:
        
        midIndex = (leftIndex + rightIndex) // 2
        midNumber = list[midIndex]

        if midNumber == searchVal:
            return midIndex
        
        # Search value falls in right of midnumber, so searching from midIndex+1 to len(list)-1
        if midNumber < searchVal:
            leftIndex = midIndex + 1

        # Search value falls in left of midNumber, so searching from 0 to midIndex-1
        else:
            rightIndex = midIndex - 1

    return -1

@timing_decorator
def binarySearch_recursive(list, searchVal, leftIndex, rightIndex):

    midIndex = (leftIndex + rightIndex) // 2
    midNumber = list[midIndex]

    if leftIndex > rightIndex:
        return -1

    if midNumber == searchVal:
        return midIndex
    
    # Search value falls in right of midnumber, so searching from midIndex+1 to len(list)-1
    if midNumber < searchVal:
        leftIndex = midIndex + 1

    # Search value falls in left of midNumber, so searching from 0 to midIndex-1
    else:
        rightIndex = midIndex - 1

    return binarySearch_recursive(list, searchVal, leftIndex, rightIndex)



if __name__ == "__main__":
    number_list = [12, 23, 32, 45, 56, 67, 89, 90, 100, 150]

    searchValue = 90

    # number_list = [i for i in range(0, 1000000)]
    # searchValue = 999999

    print("Number found in linear search", linearSearch(number_list, searchValue))
    print("Number found in Binary search", binarySearch(number_list, searchValue))
    print("Number found in Binary search Recursive", binarySearch_recursive(number_list, searchValue, 0, len(number_list)-1))