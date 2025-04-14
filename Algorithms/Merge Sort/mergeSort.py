
def mergeSort(arr):
   
   if len(arr) <= 1:
    #   return arr
     return
   
   mid = len(arr) // 2
   left = arr[:mid]
   right = arr[mid:]
   
   mergeSort(left)
   mergeSort(right)

   merge_sort_of_two_sorted_lists_optimized(left, right, arr)


#    sorted = merge_sort_of_two_sorted_lists(leftArr, rightArr)
#    return sorted



def merge_sort_of_two_sorted_lists_optimized(a, b, arr):
    i = j = k = 0
    while i < len(a) and j < len(b):
        
        if a[i] <= b[j]:   
          arr[k] = a[i]
          i += 1
        else:
          arr[k] = b[j]
          j += 1

        k += 1
    
    # when i reached end, and j have some more elements
    while j < len(b):
       
       arr[k] = b[j]
       j += 1
       k += 1

    #when j reached end, and i have some more elements
    while i < len(a):
       
       arr[k] = a[i]
       i += 1
       k += 1
       
    

def merge_sort_of_two_sorted_lists(a, b):
    sorted_list = []
    i = j = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:   
          sorted_list.append(a[i])
          i += 1
        else:
          sorted_list.append(b[j])
          j += 1
    
    # when i reached end, and j have some more elements
    while j < len(b):
       
       sorted_list.append(b[j])
       j += 1

    #when j reached end, and i have some more elements
    while i < len(a):
       sorted_list.append(a[i])
       i += 1
       
    return sorted_list




if __name__ == "__main__":

#    merge_sort_of_two_sorted_lists
#    a = [17, 21, 29, 38, 50, 80]
#    b = [4, 9, 25, 32, 40, 50, 60, 70]
#    sortedElements = merge_sort_of_two_sorted_lists(a, b)
#    print(sortedElements)

#   mergeSort
#    elements = [21, 38, 29, 17, 4, 25, 32, 9]
#    sortedList = mergeSort(elements)
#    print(sortedList)

# mergeSort optimized
   tests = [
      [21, 38, 29, 17, 4, 25, 32, 9], 
      [10, 3, 15, 7, 8, 23, 98, 29],
      [],
      [3],
      [9, 8, 7, 2],
      [1, 2, 3, 4, 5]
   ]
   for elements in tests:
        mergeSort(elements)
        print(elements)



# STEP 1 For merge sort,  Merging step Refer function (merge_sort_of_two_sorted_lists) - we can compare each element of two sorted lists and put the smaller in the new list 
# STEP 2 Sorting step - we are going to divide the list in half by recursion until we get length of list is 1
# STEP 3 Try to do all the steps in same list to optimize space complexity, -> merge_sort_of_two_sorted_lists_optimized function
# Tim sort is used in sort in built function which is hybrid of merge sort and insertion sort