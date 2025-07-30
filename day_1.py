# Day 1: Division and Square-root
# Write a function called divide_or_square that takes one
# argument (a number), and returns the square root of the number
# if it is divisible by 5, returns its remainder if it is not divisible by 5.
# For example, if you pass 10 as an argument, then your function
# should return 3.16 as the square root.

from math import sqrt

def divide_or_square(num):
    if num >= 5:
        num_sqrt = sqrt(num)
    
    else:
        not_divisible = print(f"{num} is not divisible by 5")  

    print(num_sqrt)

divide_or_square(num = int(input("Put in your number: ")))