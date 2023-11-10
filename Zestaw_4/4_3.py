def factorial(n):
    if n == 0:
        return 1
    for i in range(1, n):
        n *= i
    return n

assert factorial(5) == 120