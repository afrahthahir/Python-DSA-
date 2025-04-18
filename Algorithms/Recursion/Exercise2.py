# Write a Python program to sum recursion lists using recursion.

def sumOfNestedList(arr, index, mainIndex, mainList):
    #iterative approach

    # sum = 0
    # for i in range(len(arr)):
    #     if type(arr[i]) == list:

    #         # print(type(arr[i]))
    #         for j in range(len(arr[i])):
    #             sum += arr[i][j]

    #     else:
    #         sum += arr[i]
    # return sum

    #recursive approach

    sum = 0
    
    if mainIndex < len(mainList):

        if index >= len(arr): # To keep track of the original list when the nested lists are done 
            index = mainIndex+1
            arr = mainList

        if index < len(arr) and type(arr[index]) != list:
            sum += arr[index] + sumOfNestedList(arr, index+1, mainIndex, mainList)

        if index < len(arr) and type(arr[index]) == list:
            mainIndex = index
            sum += sumOfNestedList(arr[index], 0, mainIndex, mainList)
    
    return sum 

if __name__ == "__main__":
    nestedList = [1, 2, [3,4], 5, 6, [7, 8, 9, 0], [10, 20, 5]]
    listSum = sumOfNestedList(nestedList, 0, 0, nestedList)
    print(listSum)
    # print(type(nestedList[2]))


