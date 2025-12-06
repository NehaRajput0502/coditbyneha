# Swapping of numbers
a,b=5,10
print("Before swapping: a =",a,"b =",b)
a,b=b,a
print("After swapping: a =",a,"b =",b)

# Factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1) 
num = int(input("Enter a number to find its factorial: "))
print("Factorial of", num, "is", factorial(num))


