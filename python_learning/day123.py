#✅ Day 1 Done: Python installed, first program running!
#✅ Day 2 Done: Comfortable with variables and basic math!
#✅ Day 3 Done: Can handle lists and string operations!
# ##Practice
print("Hello World!")
name = input("What's your name? ")
print(f"Nice to meet you, {name}!")

#Say "Hello, World!" With Python
print("Hello, World!")

#Getting List of all Python keywords
import keyword
print("The list of keywords are : ")
print(keyword.kwlist)

#Arithmetic Operators
a = int(input("Add first number: "))
b = int(input("Add second number: "))
print(a + b)
print(a - b)
print(a * b)

#Python: Division if a=3 b=5
print(a // b) #Floor Division 0
print(a / b) #True Division 0.6

##Python If-Else
#Task
#Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird
n = int(input().strip())    
if n % 2 != 0:
    print("Weird")  
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")  
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")  
elif n % 2 == 0 and n > 20:
    print("Not Weird")
##Practical Solved Problems of Conditional Statements
#vote or not
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")

#Check if a number is positive  ---Using If
num=int(input("Enter the number:"))
if num>=0:
    print("Positive number")

#Check if a user has balance to buy an item ---Using If-Else
amount= float(input("Enter the amount of items:"))
balance= float(input("Enter the balance remaining:"))
if amount<= balance:
    print("Purchase the items")
else:
    print("Not purchase")

#Suggest a mode of transport based on distance  ---Using If-Elif-Else
distance= float(input("Enter the distance:"))
if distance<= 2:
    print("Walk")
elif distance<=5:
    print("Use bicycle")
elif distance<=15:
    print("Use bike")    
elif distance<=400:
    print("Use Car or Bus")
else:
    print("Use train or aeroplane")
        
#Login with username and password ---Using Nested If-Else
username=input("Enter the username:")
password=input("Enter the password:")

if username=="admin":
    if password=="12345":
        print("Access Granted")
    else:
        print("Password incorrect")
else:
    print("Incorrect user password")

#Check if number is even --Using Ternary Operator
num=int(input("Enter the number"))
print("Even" if num % 2 == 0 else "Odd")

#Assign grade --Matching Case
grade = input("Enter your grade (A/B/C):").upper() #.upper() is used to convert whatever the user types into uppercase letters.

match grade:
    case 'A':
        print("Excellent")
    case 'B':
        print("Good")
    case 'C':
        print("Average")
    case _:
        print("Fail")

# Activity Suggestion based on weather condition
weather=input("Enter the weather(sunny/rainy/cloudy/snowy)").lower()

match weather:
    case "sunny":
        print("Sunny weather")
    case "rainy":
        print("Rainy weather")
    case "cloudy":
        print("Cloudy weather")
    case "snowy":
        print("Snow weather")
    case _:   #In Python’s match syntax, there is no default: keyword like in C or Java. Instead, we use case _:
        print("Incorrect")
#Loops
n = int(input())
for i in range(n):
    print(i * i)

#Print Function
n = int(input())
for i in range(1, n + 1):
    print(i, end='')
print()

#Write a function
def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
year = int(input())
print(is_leap(year))

  

# Finding largest number among three numbers
x = int(input("Enter first number: "))  
y = int(input("Enter second number: "))  
z = int(input("Enter third number: "))
if (x >= y) and (x >= z):
    largest = x
elif (y >= x) and (y >= z):
    largest = y
else:
    largest = z
print("The largest number is:", largest)

# Swapping of numbers
a,b=5,10    
print("Before swapping: a =",a,"b =",b)
a,b=b,a
print("After swapping: a =",a,"b =",b)

#Problems Python Basics

#1.Input in python
"""The string Hello is printed as it is.
   The integer 20 is increased by 10 and results in 30.
   The floating-point number 5.5 is multiplied by 10 and results in 55.0."""
# Take string input and print it
s = input("Enter a string: ")
print(s)

# Take integer input, add 10 and print
n = int(input("Enter an integer: "))
print(n + 10)

# Take float input, multiply by 10 and print
f = float(input("Enter a floating-point number: "))
print(f * 10)

#2.Multi Printing
##a is printed n=5 times in a single line without space between them.
a = input()
n = int(input())
print(a*n)

#3.Type Conversion
##The integer value of 10.23 is 10

d = float(input())   # read double value
print(int(d))        # typecast to integer and print

#4.TypeCast and Double It
##Typecast "5" to int and then double it 5 * 2 = 10
num = int(input())
print(num*2)