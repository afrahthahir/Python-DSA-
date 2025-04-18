# Write a Python program to get the sum of a non-negative integer using recursion.

def sumOfDigits(n):
    # iterative approach
    # sum = 0
    # while n:
    #     sum += n % 10
    #     n = n // 10
    
    # return sum

    # recursive approach
    sum = 0
    if not n:
        return sum
    sum += n % 10 + sumOfDigits(n // 10)
    return sum

if __name__ == "__main__":
    sumOfDigits = sumOfDigits(3345)
    print(sumOfDigits)
    