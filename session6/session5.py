# def greet(name):
#     return "Hello, " + name + "!"
# print(greet("Alice"))

# def greet(name, age):
#   return {
#     "name": name,
#     "age": age
#   }
# print(greet('Abdul', 25))
# print(greet(age=26, name='Kris'))

# def function1():
#     name = input("Enter name: ")
#     return name

# def function2():
#     age = input("Enter age: ")
#     return age

# def function3(name, age):
#     return {
#         "name": name,
#         "age": age
#     }

# name = function1()
# age = function2()

# print(function3(name, age))

# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n - 1)

# print(factorial(5))  # result is 120 which is 5 * 4 * 3 * 2 * 1 = 120

## factorial(5) > factorial(4) > factorial(3) > factorial(2) > factorial(1)

# def fibonacci(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# print([fibonacci(n) for n in range(5)])

# output  [0, 1, 1, 2, 3]

# Except 
# try:
#     num = int(input("Enter a number: "))
#     print(10 / num)
# except ValueError:
#     print("Please enter an integer value")
# except ZeroDivisionError:
#     print("Please enter non-zero integer value")
# except:
#     print("Something went wrong")


students = {
    "Anna" : 85, 
    "John" : 48, 
    "Katie" : 77, 
    "Carlos" : 65, 
    "Brandy" : 45, 
    "Jake" : 51 
    }
name = input("Please enter a student's name: ")

try:
    print(name, students[name])
except KeyError:
    print(f"{name} not found, please enter existing user")

