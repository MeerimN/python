# Numeric data types
# binary (0 and 1)
# bin function translates from decimal to binary
# print(0b010101)   ## result is 21
# print(bin(21))    ## result is 0b10101

# Hexidecimal 
# =16  starts with 0x (0-9) (a-f)
# hex function translates form decimal to hex
# print(0x123fd3) ## result 1195987
# print(hex(100)) ## result 0x64
# Octal 
# = 8 from 0-7 
# 0o octal number
# print(0o4361) #result 2289
# print(oct(35)) #result 0o43

# Variable conventions (bet practices)
# snake_casing, camelCasing
# last_name --> snake casing
# lastName --> camel casing
# in Python we use always snake_casing 
# regular_variable = "Hello"

# _hidden_variable =   # you should not touch it or modify it. 

# Booleans
# is a data type, which only has 2 states: true or false

# Boolean Operators
my_var = True
my_var2 = False  

# and, or not 
# and operator is used to connect 2 booleans to form a single decision. (False is a priority)

# print(True and True) ## True and True --> True 
# print(True and False) ## True and False --> False 

# print(False and False) ## False and False --> False

# or operator
# is used to connect 2 booleans to form a single decision. (True is a priority)
# print(True or True) ## True and True --> True 
# print(True or False) ## True and False --> True



# print(False or False) ## False and False --> False

# not operator 
# used to return the opposite of the boolean

# print(not True) # --> False
# print(not False) # --> True

# print(True and False or True) # --> True
# print(True or True and False or not True) # --> True (and goes first)
# if <condition> or/and <condition2>

# Comparison Operators 
# all comparison operators return Boolean data type.
# < Less than
# > Greater than
# <= Less than or equal
# >= Greater than or equal
# == Equal
# print(30 < 50) # True
# print(50 == 50) # True 

# if condition always takes boolean data type
# if condition always runs when the final decision is True
# indentation = tab
    # if <condition> and <condition2>:
    # if <condition>:
        #indentation
        #<code>
# elif <condition1> or <condition2>
    # indentation or tab
    # <code>
# else:
    # indentation or tab
    # <code>

# word1 = input("Word1: ")
# word2 = input("Word2: ")
# if len(word1) > len(word2):
    # print(word1)
# elif len(word1) < len(word2):
    # print(word2) 

# inp1 = input("Please provide word1: ")
# inp2 = input("Please provide word2: ")

# if len(inp1) > len(inp2):
    # print(f"Word {inp1} is longer")
# elif len(inp1) < len(inp2):
    # print(f"Word {inp2} is longer")  
# else:
    # print("Words are equal") 

# inp = int(input("Please provide score (0-100): "))
# if(inp >= 90 and inp <= 100):
    # print("Your grade is A")

# elif(inp >= 80 and inp <= 89):
    # print("Your grade is B")

# elif(inp >= 70 and inp <= 79):
    # print("Your grade is C")

# elif(inp >= 60 and inp <= 69):
    # print("Your grade is D")

# elif(iinp >= 0 and inp <= 59):
    # print("Your grade is F")

# else:
    # print("Plese provide correct input")


year = int(input("Please provide a year: "))
if year % 400 == 0 or year % 4 == 0 and not year % 100 == 0:
    print("It's a leap year")
else:
    print("It's not a leap year")



year = int(input("Please provide a year: "))
if year % 4 == 0 or year % 400 == 0:
    print("It's a leap year")

elif year % 100 == 0 and year % 4 == 0:
    print("It's not a leap year")

else:
    print("It's not a leap year")




