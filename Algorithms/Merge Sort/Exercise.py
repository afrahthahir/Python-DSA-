
def merge_sort(arr, key, descending = False):
   
   if len(arr) <= 1:
      return
   
   mid = len(arr)//2
   left = [item for item in arr[:mid]]
   right = [item for item in arr[mid:]]

   merge_sort(left, key, descending)
   merge_sort(right, key, descending)

   merge_sort_of_two_sorted_lists_optimized(left, right, arr, key, descending)
   


def merge_sort_of_two_sorted_lists_optimized(a, b, arr, key, descending):
    i = j = k = 0
    while i < len(a) and j < len(b):

      if not descending:

        
        if a[i][key] <= b[j][key]:   
        #   print(a[i][key],  b[j][key])
          arr[k] = a[i]
          i += 1
        else:
          arr[k] = b[j]
          j += 1

        k += 1
        

      else:
         
        if a[i][key] >= b[j][key]:   
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
       
    

if __name__ == "__main__":
    elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]
    # merge_sort(elements, key='time_hours', descending=True)
    # merge_sort(elements, key='name')
    merge_sort(elements, key="age", descending=True)
    print(elements)