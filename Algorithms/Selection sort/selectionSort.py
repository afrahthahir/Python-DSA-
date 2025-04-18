
def selectionSort(arr):
    
    # However, if all n-1 are sorted, the last element is automatically sorted. So, range is n-1 for optimization
    for i in range(len(arr)-1): 
        minIndex = i

        for j in range(minIndex+1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        
        if i != minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
        

if __name__ == "__main__":
    # elements = [21, 38, 29, 17, 4, 25, 11, 32, 9]
    tests = [
        [21, 38, 29, 17, 4, 25, 11, 32, 9],
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
        [],
        [1, 5, 8, 9],
        [234, 3, 1, 56, 34, 12, 9, 12, 1300],
        [5],
        [0, 3, 3, 4, 1, 9, 0, 2, 3]
    ]
    for elements in tests:
        selectionSort(elements)
        print(elements)


# For each i element, we are going to find the min element from i+1 to len(arr)
# if found, swap min element with i, else do nothing
# continue this process for all i elements