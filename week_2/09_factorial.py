"""
Factorial(n) = n * Factorial(n - 1)
Factorial(n - 1) = (n - 1) * Factorial(n - 2)
....
Factorial(1) = 1

"""

def factorial(n): # 5
    if n ==1 :
        return 1

    return n * factorial(n-1)  # 5* factorial(4)


print(factorial(5))

input = "abcba"


