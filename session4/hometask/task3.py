lst_numbers = input("Please enter numbers separated by space:" )
unique_numbers = []

for num in lst_numbers:
    if lst_numbers.count(num) == 1:
        unique_numbers.append(num)

print("Unique numbers:", unique_numbers)