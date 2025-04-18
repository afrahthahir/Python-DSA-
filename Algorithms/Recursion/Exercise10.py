# Write a Python program to find the greatest common divisor (GCD) of two integers using recursion.
# Binary GCD Algorithm (Stein's Algorithm)
# If both numbers are 0, the GCD is 0 (i.e., GCD(0, 0) = 0).
# If one number is 0, the GCD is the non-zero number (i.e., GCD(a, 0) = a.
# If both numbers are even, divide both numbers by 2: GCD(a, b) = 2 × GCD(a/2, b/2)
# If one number is even and the other is odd, divide the even number by 2: GCD(a, b) = GCD(a/2, b)(or vice versa)
# If both numbers are odd, subtract the smaller number from the larger one. This reduces the problem to smaller numbers: GCD(a, b) = GCD(∣a − b∣, min⁡(a, b))
# Repeat steps 3–5 until one of the numbers becomes 0. The non-zero number at this point is the GCD.

def findGcd(a,b):
   gcd = 1

   if a == 0 and b == 0:
       return 0
   if a == 0:
       return b
   if b == 0:
       return a
   
   if a % 2 == 0 and b % 2 == 0:
       gcd *= findGcd(a//2, b//2)

   if a % 2 != 0 and b % 2 == 0:
       gcd *= findGcd(a, b//2)

   if a % 2 == 0 and b % 2 != 0 :
       gcd *= findGcd(a//2, b)
   
   if a % 2 != 0 and b % 2 != 0:
       gcd *= findGcd(max(a,b) - min(a,b), min(a,b))

   return gcd
       

if __name__ == "__main__":
    gcd = findGcd(6,24)
    print(gcd)



# Define a function named Recurgcd that calculates the greatest common divisor (GCD)
# of two numbers 'a' and 'b' using recursion and the Euclidean algorithm
def Recurgcd(a, b):
    # Determine the lower and higher values between 'a' and 'b'
    low = min(a, b)
    high = max(a, b)

    # Check if the lower value is 0 (base case for GCD calculation)
    if low == 0:
        # If the lower value is 0, return the higher value (GCD is the non-zero value)
        return high
    # Check if the lower value is 1 (base case for GCD calculation)
    elif low == 1:
        # If the lower value is 1, return 1 (GCD of any number with 1 is 1)
        return 1
    else:
        # If neither base case is met, recursively call the Recurgcd function
        # with the lower value and the remainder of the higher value divided by the lower value
        return Recurgcd(low, high % low)

# Print the result of calling the Recurgcd function with the input values 12 and 14
print(Recurgcd(12, 14))
