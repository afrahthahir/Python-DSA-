# Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0) using recursion .
# n = 3, 3 + 1 = 4
# n = 4, 4 + (4-2) = 6
# n = 5, 5 + 3 + 1 = 9

def sumOfSeries(n):
    # iterative approach
    # sum = n
    # x = 2
    # while n - x >= 0:
    #    sum += n - x
    #    x += 2
       
    # return sum

    #recursive approach
    
    sum = 0
    if n <= 0:
        return sum
    sum = n + sumOfSeries(n-2)
    return sum

if __name__ == "__main__":
    sum = sumOfSeries(10)
    print(sum)