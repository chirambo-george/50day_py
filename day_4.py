# Day 4: Only Floats
# Write a function called only_floats, which takes two
# parameters a and b, and returns 2 if both arguments are floats,
# returns 1 if only one argument is a float, and returns 0 
# if neither argument is a float. If you pass (12.1, 23) 
# as an argument, your function should return a 1.


def only_floats(a, b):
    if (type(a) == float) or (type(b) == float):
        print("found a floating point value in the input")
    else:
        print(f'-> {a} and {b} are not floating point values')
    
    return a, b

only_floats(5,3.0)
