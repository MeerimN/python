# Task 2: Remove Duplicates from a List
# Ask the user to enter multiple words separated by spaces. Store them in a list and remove duplicate words while maintaining the original order.

# Example:
# Enter words: apple banana apple cherry banana apple  
# Filtered List: ['apple', 'banana', 'cherry']

lst_words = input("Please enter words separated by space:" )
words = lst_words.split()
filtered_list = []
for word in words:
    if word not in filtered_list:
       filtered_list.append(word)
print("Filtered List: ", filtered_list)       
