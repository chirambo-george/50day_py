# Day 3: Register Check
# Write a function called register_check that checks how many
# students are in school. The function takes a dictionary as a
# parameter. If the student is in school, the dictionary says ‘yes’. If
# the student is not in school, the dictionary says ‘no’. Your
# function should return the number of students in school. Use the
# dictionary below. Your function should return 3.
# register = {'Michael':'yes','John': 'no', 'Peter':'yes', 'Mary': 'yes'}

register = {}

while True:  # Outer loop to allow repetition

    name = input("Enter Student Name: ")
    status = input(f"Is {name} in School (yes/no)? ")

    register.update({name:status})
    print(register)


    # Ask the user if they want to repeat
    repeat = input("Do you want to add another student? (yes/no): ").strip().lower()
    
    if repeat != 'yes':
        print(f"Register: {register}")
        break  # Exit the outer loop if the user doesn't want to continue
