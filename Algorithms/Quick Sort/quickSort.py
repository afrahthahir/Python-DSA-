
#Quick sort using Hoare's partition scheme

def swap(a, b, arr):
    
    if a != b:
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp

def partition(start, end, arr):
    pivot_index = start 
    # start = pivot_index + 1
    pivot = arr[pivot_index]

    while start < end:

        while start < len(arr)-1 and arr[start] <= pivot:
            start += 1

        while end > 0 and arr[end] > pivot:
            end -= 1
        if start < end:
            swap(start, end, arr)

    swap(pivot_index, end, elements)
    return end

    

def quickSort(start, end, elements):
   if start < end:
        pi = partition(start, end, elements)
        quickSort(start, pi-1, elements) #left partition
        quickSort(pi+1, end, elements) #right partition



if __name__ == "__main__":
    # elements = [3, 7, 9, 11]
    # quickSort(0, len(elements)-1, elements)
    # print(elements)
    tests = [
        [11, 9, 29, 7, 2, 15, 28],
        [3, 7, 9, 11],
        [25, 22, 21, 20],
        [29, 15, 28],
        [],
        [6],
        [15, 15, 40, 35, 46, 90, 10, 18, 13]
    ]
    for elements in tests:
        quickSort(0, len(elements)-1, elements)
        print(elements)


#Hoares Partition scheme (positioning the pivot in the right position)

# first element is taken as pivot
# start ptr moves from pivot (ie) start = pivot
# last element is end pointer
# start pointer should stop when start > pivot, if not start += 1
# end pointer should stop when end < pivot, if not end -= 1
# when start stops, end should move, when end stops, start should move
# when start and end stops, we should swap start and end values
# continue this process until we get end < start
# when end < start, pivot element is now moved to end ptr. 


# Now repeat this process by finding pivot for start = 0, and end = pivot - 1 (Left partition Recursion)
# Now repeat this process by finding pivot for start = pivot + 1 and end = last element (Right partition Recursion)


