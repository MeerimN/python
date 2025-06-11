# Task 4: Find the Second Largest Number in a List (No max() or sort())
# Ask the user to enter a list of numbers. Find and print the second largest number without using max() or sort().

# Example:
# Enter numbers: 10 45 78 23 89 56  
# Second largest number: 78

# Finding largest number
# lst_numbers = input("Please enter numbers separated by space:" )
# numbers = lst_numbers.split()
# largest = numbers[0]
# for num in numbers:
#     if num > largest:
#         largest = num
# print("The largest number:", largest)

# Finding second largest number
lst_numbers = input("Please enter numbers separated by space:" )
numbers = [int(x) for x in lst_numbers.split()]
first = second = float('-inf')
for num in numbers:
    if num > first:
        second = first
        first = num
    elif first > num > second:
         second = num
print("The second largest number:", second)