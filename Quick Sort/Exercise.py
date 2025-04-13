
def swap(a, b, arr):
    if a != b:
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp

def partition(start, end, arr):
    
    pivot_index = start
    pivot = arr[end]
    i = pivot_index

    while i < end:

        while pivot_index < end and arr[pivot_index] <= pivot:
            pivot_index += 1

        i = pivot_index
        
        while arr[i] > pivot:
            i += 1
        
        swap(i, pivot_index, arr)

    return pivot_index




def lomutoQuickSort(start, end, elements):
    if start < end:
        pi = partition(start, end, elements)
        lomutoQuickSort(start, pi-1, elements)
        lomutoQuickSort(pi+1, end, elements)



if __name__ == "__main__":
    # elements = [11, 9, 29, 7, 2, 15, 28]
    # lomutoQuickSort(0, len(elements)-1, elements)
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
        lomutoQuickSort(0, len(elements)-1, elements)
        print(elements)


#Lomuto partition scheme (positioning the pivot in the right position)

#pivotindex starts from 0, stops when pivotindex element > pivot, if not move
#when pivotindex stops, introduce i which starts from pivot index
#i stops when pivotindex element < pivot, if not move
#swap i and pivotindex 
#continue this process until i reaches the end 
#you will see the pivot element is in its right position

#Repeat the parition process for left partition with start = 0, end = pivotindex-1
#Repeat the partition process for right partition with start = pivotindex + 1 , end = len(arr)-1


