# Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.

# Recall that the median of an even-numbered list is the average of the two middle numbers in a sorted list.

# For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:


# For [2] after sorted median is 2
# For [2, 1] after sorted median is 1.5
# For [2, 1, 5] after sorted median is 2
# For [2, 1, 5, 7] after sorted median is 3.5
# For [2, 1, 5, 7, 2] after sorted median is 2
# For [2, 1, 5, 7, 2, 0] after sorted median is 2
# For [2, 1, 5, 7, 2, 0, 5] after sorted median is 2

def runningMedian(arr):
  
  if len(arr) == 1:
      medianValue = arr[0]

  elif len(arr) % 2 == 0:
      midIndex = len(arr)//2
      prevMidIndex = midIndex - 1 
      medianValue = (arr[midIndex] + arr[prevMidIndex]) / 2
      
  else:
      midIndex = len(arr)//2
      medianValue = arr[midIndex]

  print("Running Median of the elements",medianValue)


def insertionSort(elements):

    
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i -1

        while j>=0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j = j-1
        elements[j+1] = anchor

    print("Sorted elements",elements)
    runningMedian(elements)


if __name__ == "__main__":
    elements = [2, 1, 5, 7, 2, 0, 5]
    for i in range(1, len(elements)+1):
        # print(i)
        insertionSort(elements[:i])
        # print(elements[:i])