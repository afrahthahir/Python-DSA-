# Write a Python program to solve the Fibonacci sequence using recursion.
# 0 1 1 2 3 5 8 13

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


if __name__ == "__main__":
    fib = fibonacci(6)
    print(fib)
