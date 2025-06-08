num = int(input("Please enter a whole number: "))
if (num > 0):
    print(f"Number {num} is positive")
elif (num < 0):  
    print(f"Number {num} is negative")
else:
    print("Number is zero")   

if num % 2 == 0:
    print(f"Number {num} is even")
else:
    print(f"Number {num} is odd")
