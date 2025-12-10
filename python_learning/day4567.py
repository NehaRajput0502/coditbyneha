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