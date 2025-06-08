password = input("Enter your password: ")

if (len(password) >= 8 and "@" in password and " " not in password):
    print("The password is strong")
else:
    print("The password is weak, please enter another password")