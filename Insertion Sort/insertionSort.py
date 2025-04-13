

def insertionSort(elements):
   
   for i in range(1, len(elements)):
      anchor = elements[i]
      j = i - 1

      while j >= 0 and anchor < elements[j]: 
          elements[j+1] = elements[j]  # copying the greater element to anchor position
          j = j -1

      elements[j+1] = anchor

             

if __name__ == "__main__":
    # elements = [21, 29, 38, 17, 4, 25, 11, 32, 9]
    # insertionSort(elements)
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
        insertionSort(elements)
        print(elements)


# Consider element[0] as sorted
# your anchor is element[1]
# compare your anchor with the left side elements j until u reach index 0
# if your anchor < element[j] that means there are elements > anchor in the left, so they should be placed in the right, so copy the greater element[j] to anchor position
# move further and stop when element[j] < anchor (ie) we have to place anchor after the element[j] (ie) element[j+1] = anchor
# For each ith element, we should check all left j until it reaches 0, repeat the process
