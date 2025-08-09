# Day 17: User Name Generator
# Write a function called user_name, that creates a username
# for the user. The function should ask a user to input their name.
# The function should then reverse the name and attach a
# randomly issued number between 0 – 9 at the end of the name.
# The function should return the username.

from random import randint
def user_name():
    

    name = input("Enter Your Name: ")

    nameRev = name[::-1]
    random_int = randint(0, 10)

    userName  = nameRev + str(random_int)
    
    print(f"Your Username is, {userName}")
    
user_name()