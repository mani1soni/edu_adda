#Recursion implementation using python
#Recursively find factorial of number

def factorial(n):
    if n==0:
        return 0
    elif n == 1:
        return 1
    else:
        return n*factorial(n-1)

n = int(input())
result = factorial(n)
print(result)
