#1) Build a Shopping Cart
# You can use either lists or dictionaries. The program should have the following capabilities:
shopping_cart = {} #decleared an empty shopping cart to 

def add_item():
    """ a function thst adds items to the cart"""
    item = input("what would you like to add?")
    quantity = int(input(f"how many {item} would you like?"))
    
    if item not in shopping_cart:
        shopping_cart[item] = quantity   # adds the item(key) and its quantity(value)q to the store(dict)   
        print(f"{item} has been added to your shopping cart")

def remove_item():
    """ a function to remove items from the cart"""
    item = input("what would you like to remove")
    if item in shopping_cart:
        del shopping_cart[item]
        print(f"{item} has been deleted from your shopping cart")
    else:
        print("you don't have this ittem in the cart")
    
    

def show_shopping_cart():
    """ a function that shows items in the cart"""
    print(f" your cart contains: {shopping_cart}")
    
while True:
    user_choice = input("What would you like to do? add, remove, show, or 'q' to quit")
    
    if user_choice.lower() == 'add':
        add_item()

    elif user_choice.lower() == 'remove':
        remove_item()
        
    elif user_choice.lower() == "show":
        show_shopping_cart()
        
    elif user_choice.lower() == "q":
        show_shopping_cart()
        print("thank you for shopping with us")
        break
    else: 
        print("Please enter a valid response")

#2) Set Practice
#Remove all duplicates from the following list

nums_list = [1, 1, 1, 2, 2, 3, 5, 6, 4, 12, 11, 12, 12, 14, 16, 16, 16, 1, 1, 1, 2, 2]
my_set=set(nums_list)
print (my_set)
num_list=list(my_set)
print(num_list)

#Out put the intersection of the following the following sets.

set1 = {20, 24, 26, 27}
set2 = {26, 35, 63, 27}
set_intersect=set1.intersection(set2)
print(set_intersect)
    #------othervway------:
se_intersect=set1 & set2
print(se_intersect)


#Output the difference between the following sets

set3 = {100, 65, 89, 200}
set4 = {65, 103, 54, 200}
set_d=set3 - set4
print(set_d)
    #-----other vway:----:
se_d=set3.difference(set4)
print(se_d)
