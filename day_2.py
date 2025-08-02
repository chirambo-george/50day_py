# Day 2: Strings to Integers
# Write a function called convert_add that takes a list of strings
# as an argument and converts it to integers and sums the list. For
# example [‘1’, ‘3’, ‘5’] should be converted to [1, 3, 5] and
# summed to 9.
nums = ['1', '6', '5']
# print(nums)


string_nums = ['5','4', '4','1']
def convert_add():
    
    for i in range(len(string_nums)):
        string_nums[i] = int(string_nums[i])
        
        
    print(sum(string_nums))
    
convert_add()

