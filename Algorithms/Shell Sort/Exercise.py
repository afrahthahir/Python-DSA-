
def shellSortDuplicateRemoval(arr):
    size = len(arr)
    gap = size // 2
    
    while gap > 0:

        for i in range(gap, len(arr)):
            # print(i)
            anchor = arr[i]
            j = i

            while j >= gap and arr[j-gap] > anchor:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = anchor
            
            # Deleting duplicates here
            if j>=0 and anchor == arr[j-gap]:  
                del arr[j-gap]
                gap = len(arr) // 2
                break

            
        gap = gap // 2
    

if __name__ == "__main__":
    elements = [2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3]
    tests = [
        [],
        [2],
        [1,2,3,5],
        elements, 
        [1,2,2,4,4,4,5,5,5]
    ]
    for i in tests:
        # dummy = [2, 1, 5, 7, 2, 5, 5, 5, 7, 7]
        shellSortDuplicateRemoval(i)
        print(i)