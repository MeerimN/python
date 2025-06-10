# for loop until 5:
# print

# iterator = variable used within loop  the value of which changes based on the sequence
# sequence data type = data type that has start point and end point
# string support indexing through indexing we can get the start of the string and end

# for <iterator> in <sequence_data type>
# <code that needs to be repeated>

# inp = input("Input: ")
# Input (each character we access through index)
# for char in inp:
    # print (char)


# inp = input("Input Word: ")
# inp2 = input("Input a Character: ")
# 
# for char in inp:
    # if char == inp2:
       # print(char)


# inp = input("Input Word: ")
# inp2 = input("Input a Character: ")
# 
# counter = 0
# for char in inp:
    # if (char) == inp2:
       # counter += 1 
# 
# print(counter)

# for num in range (1, 10, 2):  # <start> <end> <jump>
# 
    # print(num)    

# inp = int(input("Input: "))
# 
# for num in range (inp):
    # if num % 2 == 0:
        # print(num)

# While loops
# unlike for loop, while does not have a start or end
# is based on conditions
# if the condition is true: code will be repeated until it turns False.

# while <condition>: num1 < num2
   # <code>

# inp = int(input("Input: "))
# num = 0
# while num < inp:
#     print(num)
#     num += 1

# break / continue - used with loops only
# break - stops the loop
# 

# for i in range (1, 10):
#     if i == 8:
#         break
#     else:
#         print(i)   

# for i in range (1, 10):
#        if i == 5:
#           continue
#        else:
#           print(i) 
                  


# Lists | Tuple | Dictionaries  | Sets --> Data types that can hold 0 or more vlaues
# List is a data type that can hold 0 or more values
# List starts with []

# print the r in world
# lst = ["Hello", "world", 10, 10.5, True, ["Hello", "Test"]]
# print(lst[1][2])

# # print each fruit by itself
# lst_fruits = ["pineapple", "pear", "aoricot", "peach"]
# # append function adds element at the end of the list
# lst_fruits.append('apple')
# lst_fruits.append('grape')

# print(lst_fruits)

#insert
# lst_fruits = ["pineapple", "pear", "aoricot", "peach"]
# lst_fruits.insert(2, 'apple')
# lst_fruits.insert(0, 'banana')
# print(lst_fruits)

# lst_fruits = ["pineapple", "pear", "apricot", "peach"]
# lst_fruits.pop()
# print(lst_fruits)

# lst_fruits = ["pineapple", "pear", "apricot", "peach"]
# lst_fruits.pop(1)
# print(lst_fruits)

# lst_fruits = ["pineapple", "pear", "apricot", "peach", "pear"]

# lst_fruits[0] = lst_fruits[-1]  # [0 is the location pineapple and [-1 is asking to replace it with pear ie last one]]
# print(lst_fruits)

lst_fruits = ["pineapple", "pear", "kiwi", "apricot", "peach", "pear", "cherry", "melon"]
filetered_fruits = []

inp = input("Input a character: ")
for fruit in lst_fruits:
   if inp in fruit:
      filetered_fruits.append(fruit)

if len(filetered_fruits) == 0:
    print("No fruit contains this character")
else:
    print(filetered_fruits)
    