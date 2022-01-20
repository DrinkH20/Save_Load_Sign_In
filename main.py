from saved_data import *

user_acts = users

user_type = input("Do you have an account with us? y/n ")

if user_type == "y":
    name = input("what is your username?")
    password = input("what is your password")

    for i in user_acts:
        if i == (name, password):
            print("your in")

elif user_type == "n":
    user_name = input("What would your like your username to be? ")
    user_password = input("What would you like your password to be? ")
    user_acts.append((user_name, user_password))
    print(user_acts[len(user_acts) - 1])

    file = open("saved_data.py", "w")
    file.write("users = " + str(user_acts) + "\n")
    file.close()
else:
    print("Invalid answer")
