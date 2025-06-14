
laptop = {
    "Dell": {
        "software": {
            "os": "linux mint",
            "version": "22.04",
            "applications": ["python", "vscode", "slack"]
        },

        "hardware": {
            "model": "XPS 15",
            "cpu": "Intel Core i5, (6 cores)",
            "ram": "8gb",
            "storage": "256gb",
            "screen": "ips",
        }
    },

    "MacBook": {
        "software": {
            "os": "Mac OS",
            "version": "Ventura 13.7.5",
            "applications": ["zoom", "vscode", "slack"]
        },
        "hardware": {
            "model": "MacBook Pro",
            "cpu": "6-Core Intel Core i7",
            "ram": "32gb",
            "storage": "500gb",
            "screen": "ips",
        }
    },
     "Acer": {
        "software": {
            "os": "Linux Ubuntu",
            "version": "22.04",
            "applications": ["python", "nodejs", "slack"]
        },

        "hardware": {
            "model": "Swift 16",
            "cpu": "Inter Core i9, (16 cores)",
            "ram": "32gb",
            "storage": "1tb",
            "screen": "oled"
        }
     }
    }

# laptop_names = []
# for key, value in laptop.items():
#     laptop_names.append(key)
# print(laptop_names)

# for key, value in laptop.items():

#     print(f"Laptop: {key}\nOS: {value['software']['os']}\nVersion: {value['software']['version']}")
#     print()

    # Output 
#     Laptop: Dell
# OS: linux mint
# Version: 22.04

# Laptop: MacBook
# OS: Mac OS
# Version: Ventura 13.7.5

# Laptop: Acer
# OS: Linux Ubuntu
# Version: 22.04

    # or another version
    # print(f"Laptop: {key}")
    # print(f"OS: {value['software']['os']}")
    # print(f"Version: {value['software']['version']}")

# Exercise  Print only laptop, and applications info in 1 line
# for key, value in laptop.items():
#   print(f"Laptop: {key}")
#   print("Applications: ", end = "")
#   for app in value["software"]["applications"]:
#     print(app, end = ' ')

#   print()

# Output
# Laptop: Dell
# Applications: python vscode slack 
# Laptop: MacBook
# Applications: zoom vscode slack 
# Laptop: Acer
# Applications: python nodejs slack 

# Exercise 
# fruits = {"banana": 2, "apple": 1, "pear": 3}
# fruits["cherry"] = 4
# fruits["pineapple"] = 7  # adds to dictionary
# fruits.pop("apple")   # deletes from dictionary

# print(fruits)

# output {'banana': 2, 'pear': 3, 'cherry': 4, 'pineapple': 7}
""
# var = {"key": "value"}

# sets are mutable
# stores only unique values
# does not contain duplicates

# sets = {"value1", "value2", 10}
# print(sets)

# lst = [10,1,-1,1,1]
# print(lst)
# sets = {10,1,-10,-1,1,0,9,11,12, False, True} # as False is = 0 and True=1 it removes it
# print(sets)   # output {1}


# Function 
# is a block of reusable code designed to perform a specific task, 
# helps in organizing code, making it readable, modular and reusable

# return is python keyword that is used only in functions 
# return is used to putput a data type 


# def greet(name):
#     return(f"Hello, {name}")
# inp = input("What is your name? ")
# greet(inp)

# def add(num1, num2):
#     print(num1 + num2)
# sum = add(5,10) 
# print(sum)   
