# Task 1: Reverse a List
# Write a program that reverses a list using a for loop.
# Example:

# Input:
# Enter numbers separated by space: 1 2 3 4 5
# Output:
# Reversed List: [5, 4, 3, 2, 1]

inp = input("Please enter numbers separated by space:" )
numbers = inp.split()
reversed_list = []
for i in range(len(numbers)-1, -1, -1):
    reversed_list.append(numbers[i])
print("Reversed List:", reversed_list)