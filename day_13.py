# Day 13: Pay Your Tax
# Write a function called your_vat. The function takes no
# parameter. The function asks the user to input the price of an
# item and VAT (vat should be a percentage). The function should
# return the price of the item plus VAT. If the price is 220 and,
# VAT is 15% your code should return a vat inclusive price of 253.
# Make sure that your code can handle ValueError. Ensure the
# code runs until valid numbers are entered. (hint: Your code
# should include a while loop).

def your_vat(price):
    while True:
        price = float(input("Enter price of product: "))
        
        vat_amt = 0.15 * price
        vat_inc_price = price + vat_amt
        

        print(vat_inc_price)
    
        repeat = input("Do you want to add another item(y/n): ")
        if repeat != 'y':
            
            break
    
    
    return price
your_vat(-220)
