# When I try to find number 5 in below list using binary search, it doesn't work and returns me -1 index. Why is that?

# numbers = [1,4,6,9,10,5,7]

#Because Binary Search works only on sorted lists, the given list is unsorted so binary search didnt work


# Find index of all the occurances of a number from sorted list

# numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
# number_to_find = 15  
# This should return 5,6,7 as indices containing number 15 in the array


def binarySearch(list, searchVal):

    leftIndex = 0
    rightIndex = len(list) - 1
    occurences = []

    while leftIndex <= rightIndex:
        
        midIndex = (leftIndex + rightIndex) // 2
        midNumber = list[midIndex]

        if midNumber == searchVal:
            if midIndex not in occurences:
                occurences.append(midIndex)
            rightIndex = rightIndex - 1
            continue
        
        # Search value falls in right of midnumber, so searching from midIndex+1 to len(list)-1
        if midNumber < searchVal:
            leftIndex = midIndex + 1

        # Search value falls in left of midNumber, so searching from 0 to midIndex-1
        else:
            rightIndex = midIndex - 1

    return occurences if occurences else -1
    






if __name__ == "__main__":
    numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
    number_to_find = 34
    print("Index of all occurances of the number",binarySearch(numbers, number_to_find))