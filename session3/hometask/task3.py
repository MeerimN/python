# Task 3: Find the Longest Word in a List
# Ask the user to enter a list of words. Find and print the longest word from the list.

# Example:
# Enter words: Python Java JavaScript C  
# Longest word: JavaScript 


lst_words = input("Please enter words separated by space:" )
words = lst_words.split()
longest = ""
for word in words:
    if len(word) > len(longest):
        longest = word
print("The longest word:", longest)