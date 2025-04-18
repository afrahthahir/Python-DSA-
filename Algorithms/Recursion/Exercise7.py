# Write a Python program to calculate the sum of harmonic series upto n terms.
# The harmonic sum is the sum of reciprocals of the positive integers. n=4 1 + 1/2 + 1/3 + 1/4

def harmonicSeries(n):
    #iterative approach
    # sum = 0
    # while n:
    #     sum += 1/n
    #     n -= 1
    # return sum

    #recursive approach
    sum = 0
    if not n:
        return sum
    sum += 1/n + harmonicSeries(n-1)
    return sum


if __name__ == "__main__":
    sum = harmonicSeries(5)
    print(sum)