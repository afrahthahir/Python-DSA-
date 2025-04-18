# Write a Python program to get the factorial of a non-negative integer using recursion.

def factorial(n):

   if n == 1:
       return n
   
   return n * factorial(n-1) 




if __name__ == "__main__":

    fact = factorial(6)
    print(fact)
    