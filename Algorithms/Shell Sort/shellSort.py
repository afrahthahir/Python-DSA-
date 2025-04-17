
def shellSort(arr):
    size = len(arr)
    gap = size // 2

    while gap > 0:

        for i in range(gap, size):
            # print(i)
            anchor = arr[i]
            j = i
            
            while j>=gap and arr[j-gap] > anchor:
                arr[j] = arr[j-gap] #copying the greater element to arr[j] (ie) anchor position
                j -= gap
            
            arr[j] = anchor

        gap = gap // 2

    

if __name__ == "__main__":
    elements = [21, 38, 29, 17, 4, 25, 11, 32, 9]
    shellSort(elements)
    print(elements)
    # tests = [
    #     [21, 38, 29, 17, 4, 25, 11, 32, 9],
    #     [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
    #     [],
    #     [1, 5, 8, 9],
    #     [234, 3, 1, 56, 34, 12, 9, 12, 1300],
    #     [5]
    # ]
    # for elements in tests:
    #     shellSort(elements)
    #     print(elements)


# Shellsort optimization of insertion sort
# consider a gap = 3, you have to compare the previous gap element with the current element (anchor)
# if the prev gap element > anchor, that means it should come at the right side so copy prev gap element to anchor position
# when we reach prev gap position by j-=gap, paste the anchor in the arr[j] prev element position
# this gap comparison should be in a while loop until we reach the last gap element we do the above process
# to find a gap we should len(arr)//2, and do the above process until gap > 0