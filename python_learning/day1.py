##Practice
print("Hello World!")
name = input("What's your name? ")
print(f"Nice to meet you, {name}!")

#Say "Hello, World!" With Python
print("Hello, World!")

#Arithmetic Operators
a = int(input())
b = int(input())
print(a + b)
print(a - b)
print(a * b)

#Python: Division if a=3 b=5
print(a // b) #Floor Division 0
print(a / b) #True Division 0.6

##Python If-Else
n = int(input().strip())    
if n % 2 != 0:
    print("Weird")  
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")  
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")  