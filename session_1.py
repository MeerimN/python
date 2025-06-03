

# print(5 * 10.5)
# print(50 / 10.5)
# print(5 + 10.5)
# print(5 - 10.5) 
# 
# print(10 ** 2) # 10 power of 2 (10 * 10)
# print(10 ** 3) # 10 * 10 * 10
# print(10 % 2) # modulus || remainder
# print(11 % 2) # what is the closest whole number that would be divisible?
              # # 11 - 10 = 1 --> the answer
              
#mutliline_str = """This is line 1
#This is line 2
#This is line 3
#"""

# String indexing
# indexing always starts from 0
# You can go from the back of the string with the index starting -1 

word = "Hello World"

# String slicing
# start location | end location
# print(word[0:5]) # prints hello

# print(word[6:11]) # prints world

# print(word[::2]) # jumps 2  HloWrd
# print(word[::3]) # HlWl

# print(word[::-1]) # reverses the word 

# String concatination 
# joining 2 or more strings together

str1 = "aKumo"
str2 = "Solutions"

# joined = str1 + str2
# print(joined)     # result aKumoSolutions

# print(str1 + str2) #same 

# print(str1, str2) # add space  aKumo Solutions
# print(str1, str2, sep='?')  # add space or any other symbol or text
# print(str1, str2, end='\n', sep='?') # default values for end='\n' and for sep=' '

# print("This is line 1.\nThis is line 2.\nThis is line 3.") 
# This is line 1.
# This is line 2.
# This is line 3

# word = "This is line 1.\nThis is line 2.\nThis is line 3."
# print(word)

# len(<string>) --> calculates the length of the string

# print(len(word)) # shows how many characters (does not count from 0 but from 1)

# inp = input("Please provide some sort of word: ")
# print(inp)

# input function always takes string input
#inp = input("Please provide number 1: ")
#inp2 = input("Please provide number 2: ")
#print(inp + inp2)  # result 35  ( 3 and 5)

# int() converts data type to integer (if it's correct i.e if it is whole number)
# inp = int(input("Please provide number 1: "))
# inp2 = int(input("Please provide number 2: "))
# print(inp + inp2)  # result 7 ( 3 and 4 )

# inp = float(input("Please provide number 1: "))
# inp2 = float(input("Please provide number 2: "))
# print(inp + inp2)  # result 9.6 (4 and 5.6)

# Task 1
# take 2 inputs (integers)
# print (multiplication answer)
# print (division answer)
# print (modulus answer)

# inp1 = int(input("Number 1: "))
# inp2 = int(input("Number 2: "))
# print(inp1 * inp2)
# print(inp1 // inp2)
# print(inp1 % inp2)
# / float division
# // integer division


# Task 2
# take 1 input (string)
# print (length of the string)

# word = input("Word: ")
# print(len(word))

# Task 3
# Take celcius degree and convert it to fahrenheit formula: (C * 9/5) + 32
celsius = float(input("Please provide a celsius degree: "))
fahrenheit = (celcius * 9/5) + 32
print(fahrenheit)


