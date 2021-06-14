input = "ababa"

# Factorial(n) = n * n-1 * Factorial(n-2)

def is_palindrome(string):
    n = len(string)

    for i in range(n):
        if string[i] != string[n-1-i]:
            return False

    return True


print(is_palindrome(input))