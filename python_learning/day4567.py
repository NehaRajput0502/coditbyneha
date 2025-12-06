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

# Check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
number = int(input("Enter a number to check if it's prime: "))
if is_prime(number):
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")
