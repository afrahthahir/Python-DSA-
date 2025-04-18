# Write a Python program to calculate the sum of a list of numbers using recursion.

def sumOfList(arr, index):
    #iterative approach - base condition is return when index > len(arr)

    # sum = 0
    # for i in range(len(arr)):
    #     sum += arr[i]
    # return sum

    #recursive approach - using the base condition found above to return

    sumList = 0
    if index < len(arr):
        sumList += arr[index] + sumOfList(arr, index+1)
        # print(sumList)
    return sumList
    


if __name__ == "__main__":
    elements = [0, 3, 3, 4, 1, 9, 0, 2, 3, 5, 3, 1, 1]
    sumList = sumOfList(elements, 0)
    print(sumList)