# Write a Python program to calculate the geometric sum up to 'n' terms.

# Note: In mathematics, a geometric series is a series with a constant ratio between successive terms.
# n = 3, constant ratio = 2, sum = 1/2^0 + 1/2^1 + 1/2^2 + 1/2^3

def gpSeries(n):
    sum = 0
    if n == 0:
        return 1
    
    sum += 1/pow(2,n) + gpSeries(n-1)
    return sum

if __name__ == "__main__":
    sum = gpSeries(3)
    print(sum)