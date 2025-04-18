# Write a Python program to calculate the value of 'a' to the power of 'b' using recursion.

# Test Data :
# (power(3,4) -> 81 -> 3 * 3^3 * 3^2 * 3^1 *3^0
def power(a,b):
    result = a

    if b == 0:
        return 1
    
    result *= power(a, b-1)
    return result

if __name__ == "__main__":
    po = power(4,3)
    print(po)