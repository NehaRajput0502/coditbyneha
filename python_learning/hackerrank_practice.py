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

#Loops
n = int(input())
for i in range(n):
    print(i * i)

#1
for i in range(4,50,6):
    print(i)
#2
for i in range(4):
    for j in range(2):
        print(i, j)
#3.1
for i in range(5):
    for j in range(2):
        for k in range(3):
            print(i, j, k)

#3.2
for i in range(5,6,2):
    for j in range(2):
        for k in range(3):
            print(i, j, k)

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

#List Comprehensions
x = int(input())
y = int(input())
z = int(input())   
n = int(input())
result = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if (i + j + k) != n]
print(result)
#Find the Runner-Up Score!
n = int(input())
arr = list(map(int, input().split()))
unique_scores = list(set(arr))
unique_scores.sort()
print(unique_scores[-2])
#Nested Lists
records = []    
for _ in range(int(input())):
    name = input()
    score = float(input())
    records.append([name, score])
records.sort(key=lambda x: x[1])
second_lowest_score = sorted(set([score for name, score in records]))[1]
for name, score in records:
    if score == second_lowest_score:
        print(name)

#Finding the percentage
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
average = sum(student_marks[query_name]) / len(student_marks[query_name])
print(f"{average:.2f}")
#Lists
if __name__ == '__main__':
    N = int(input())
    lst = []
    for _ in range(N):
        command = input().split()
        if command[0] == "insert":
            lst.insert(int(command[1]), int(command[2]))
        elif command[0] == "print":
            print(lst)
        elif command[0] == "remove":
            lst.remove(int(command[1]))
        elif command[0] == "append":
            lst.append(int(command[1]))
        elif command[0] == "sort":
            lst.sort()
        elif command[0] == "pop":
            lst.pop()
        elif command[0] == "reverse":
            lst.reverse()   