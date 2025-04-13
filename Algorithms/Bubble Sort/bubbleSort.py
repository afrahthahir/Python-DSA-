
def bubbleSort(arr):
    size = len(arr)
    for j in range(size-1):
        swapped = False

        for i in range(size-1-j):
            if arr[i] > arr[i+1]:
                tmp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = tmp
                swapped = True

        if not swapped:
            break
            
    return arr


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 20]
    alreadySortedArr = [1, 2, 3, 4, 5]
    stringArr = ["babu", "shyam", "zara", "afrah", "kishore"]
    sortedArray = bubbleSort(stringArr)
    print("Sorted array is:", sortedArray)


# Time Complexity: O(n^2)
# Space Complexity: O(1)

# outer loop for first iteration j=0, largest number will come at the end.
# 2 iterations j=1, two large numbers will come at the end. 
# So, for the arr to be sorted, we need j=n-1 iterations. (No need to iterate the last element because it is already compared with prev element)

# inner loop range will be (size-1-j) because the last j elements are already sorted.
#For already sorted array, we can break the loop if no swaps are made in the inner loop in the first iteration of outer loop.