# lst = [1,2,3]
# del lst[0]
# print(lst)

# lst = [2,3,1,-1,0,-40,5]

# lst = ["Hello", "Hello", "World"]
# print(lst.index("Hello"))

# Split (only works with strings) split() (default is ' ')
# str1 = "Hello World. This is a test"
# lst_str = str1.split()
# print(lst_str)

# str1 = "Hello, World, This, is a test, "
# x = str1.strip()
# print()

# lst_num = []
# for num in range(1, 11):
#       if num % 2 == 0:
#        lst_num.append(num)

# print(lst_num)

# result [2, 4, 6, 8, 10]

# lst_num = [num2 for num in range(1, 11) for num2 in range(1, 3)]
# print(lst_num)
# result [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]

# lst_num = [num for num in range(1, 11) for num2 in range(1, 6)]
# print(lst_num)
# lst = []

# for num in range(1, 11):
#     lst2 = []
#     for num2 in range(1, 6): 
#     lst2.append(num2)

# print(lst_num)

# table = [[i for i in range(1, 6)] for j in range(4)]
# print(table)

# Nested for loops  (loops within the loops)
# while
#    for
# for 
#    while      etc. 

# for i in range(1,11):
#     print(f"Run {i}")

#     for j in range(1, 6):
#         print(j, end=' ')

#     print() # new line
#     print('-----------')

# # Result
# Run 1
# 1 2 3 4 5 
# -----------
# Run 2
# 1 2 3 4 5 
# -----------    etc 
# Run 10
# 1 2 3 4 5 
# -----------

# Differences between mutable and unmutable data types
# - Mutable --> mutate --> change it's contents 
# - List --> append(), pop(), change the order of the list, reverse the list, sort(), ...

# Immutable data types
# - String
# - Integer

# lst = ["Hello", "World", "test"]
# lst[2] = "aKumo"
# print(lst)         # result ['Hello', 'World', 'aKumo']

# word = "HellO"
# word[-1] = "o"
# print(word)   # this will not replace O to o, error, as it is string which is immutable

# word = "HellO"
# word = word + " aKumo"
# print(word)   # result HellO aKumo we did not change the string itself we just added another string 

# word = " test"
# word.strip()
# print(word) # does not work we still have the space 

# but when we reassign to the value
# word = " test"
# x = word.strip()
# print(x)    # it works 


# word = " test"
# x = word.replace("test", 'aKumo')
# print(x)  

# List   has square brackets []

# Tuple ## read only      regular parenthesis ()
# tpl = (1,2,3,4)
# print(tpl)

# tpl = (1,)
# print(type(tpl))   #result <class 'tuple'>

# tpl = (1,2,3,4)
# print(tpl)
# print(tpl[::-1])  # we are not changing the string but only reading it in reverse order

# tpl = (1, "Hello", True, 50.3, ["Hello", "test", "World"])
# tpl = tpl[:-1:]
# print(tpl)   # result (1, 'Hello', True, 50.3)

# Index()
# does not change the tuple, but it gives the index where the value is located

# tpl = (1, "Hello", True, 50.3, ["Hello", "test", "World"])
# lst = list(tpl)
# print(lst)    # result [1, 'Hello', True, 50.3, ['Hello', 'test', 'World']]
# the tuple was converted to list

# tpl = (1,2,3,4,5, [1,2,3])

# print(tpl[-1])  # result [1, 2, 3]


# lst = [1,2,3,4,5, [1,2,3]]
# lst[-1] = 6
# print(lst)  # result [1, 2, 3, 4, 5, 6]

# tpl = (1, 2, -10, -1, 0, 4, 5)
# print(sorted(tpl))  # result [-10, -1, 0, 1, 2, 4, 5]

# Dictionaries
# are the key value stores

# dictionaries = {}
# sets = {} also use {} but does not store key values

# dictionaries = {"key" : "value", "key2" : "value2", "key3" : "value3"}
# print(dictionaries) # keep the keys unique so it will not replace it ex. key, key2, key3

# x = {1: "value", 2: "value2", 3: "value3"}
# print(x)

# x = {"key": "value", 2: "value2", 3: "value3"}
# print(x["key"])  # result  value

# Exercise dictionary of students 
# students = {
#     1 : {"first name": "Anna", "last_name": "Smith", "DOB": "11.12.2003"}, 
#     2 : {"first name": "Alan", "last_name": "Black", "DOB": "10.08.2000"},
#     3 : {"first name": "Veronica", "last_name": "White", "DOB": "3.10.1999"}
# }

# print(students[1])

# students = {
#     1 : {"first name": "Anna", "last_name": "Smith", "DOB": "11.12.2003"}, 
#     2 : {"first name": "Alan", "last_name": "Black", "DOB": "10.08.2000"},
#     3 : {"first name": "Veronica", "last_name": "White", "DOB": "3.10.1999"}
# }

# for element in students:
#    print(element)  # prints only the keys

# students = {
#     1 : {"first name": "Anna", "last_name": "Smith", "DOB": "11.12.2003"}, 
#     2 : {"first name": "Alan", "last_name": "Black", "DOB": "10.08.2000"},
#     3 : {"first name": "Veronica", "last_name": "White", "DOB": "3.10.1999"}
# }

# for element in students.items():
#    print(element) 
   
#     # result
# (1, {'first name': 'Anna', 'last_name': 'Smith', 'DOB': '11.12.2003'})
# (2, {'first name': 'Alan', 'last_name': 'Black', 'DOB': '10.08.2000'})
# (3, {'first name': 'Veronica', 'last_name': 'White', 'DOB': '3.10.1999'})


students = {
    1 : {"first name": "Anna", "last_name": "Smith", "DOB": "11.12.2003"}, 
    2 : {"first name": "Alan", "last_name": "Black", "DOB": "10.08.2000"},
    3 : {"first name": "Veronica", "last_name": "White", "DOB": "3.10.1999"}
}

# for element in students:
#    print("Hello I'm", (students[]["first_name"]["last_name"]), "I was born in ", (students["DOB"]), "I am the student number ", (students[1]))

# for element in students:
#    print("Hello I'm, (students[]["first_name"]["last_name"])) 

for key, value in students.items():
    print(f"Hello I'm {value['first_name']} {value['last_name']}.I was born in {value['DOB']}")
    print(f"I'm the student number {key}")

    print("---------------------")