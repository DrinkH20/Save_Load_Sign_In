from saved_data import *

user_accts = users

user_type = input("Do you have an account with us? y/n ")

if user_type == "y":
    name = input("what is your username?")
    password = input("what is your password")

    for i in user_accts:
        if i == (name, password):
            print("your in")
else:
    user_name = input("What would your like your username to be? ")
    user_password = input("What would you like your password to be? ")
    user_accts.append((user_name, user_password))
    print(user_accts[len(user_accts) - 1])

file = open("saved_data.py", "w")

file.write("users = " + str(user_accts) + "\n")

file.close()
