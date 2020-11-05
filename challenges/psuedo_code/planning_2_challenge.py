'''
Planning challenge 2!

For each piece here, write out the pseudocode as comments FIRST, then write your code!
'''


'''
1. Shipping

You are building a system to handle shipping orders. Each order should be a dictionary that has 3 pieces of information:
-destination (string) (for the purposes of this challenge this can be any place, no need to make a full address)
-date_shipped (string)
-weight (float) (how many pounds the package is)

make a list of dictionaries that has three keys: destination, date shipped, and weight

Assign 3 separate orders to 3 separate variables
'''
print('\nPART 1')

order1 = {'destination': 'New York', 'date_shipped': '10/29/20', 'weight': 3.05}
order2 = {'destination': 'Florida', 'date_shipped': '9/29/20', 'weight': 50.3}
order3 = {'destination': 'California', 'date_shipped': '8/1/20', 'weight': 20.45}


'''
2. Building the database

Now, let's put the orders all into a database togther (all the orders are storedin 1 variable). 

Your database can either be a dictionary or a list. 

Print out the database to make sure all the info is in there. 

'''
print('\nPART 2')

shipping_order = [order1, order2, order3]

print(shipping_order)
'''
3. Define a function called add_order() that adds one more order to your database, and make sure it works!
Any new orders should be in the same format as your existing ones. 
'''
print('\nPART 3')
order4 = {'destination': 'Texas', 'date_shipped': '10/28/20', 'weight': 31.05}
order5 = {'destination': 'Louisiana', 'date_shipped': '8/29/20', 'weight': 52.3}

def add_order(order_list, order):
	# append to order to order_list
	order_list.append(order)

print(shipping_order)
add_order(shipping_order, order4)
print(shipping_order)
'''
4. Define a function called complete_order() to mark a specific order in your database complete

This means that it should add a new key/value pair called 'complete' to a specific order, and set the value to True

Test this out and print out your database to make sure it works!

HINT: Think about how your choice of list/dictionary in part 2 informs how someone would reference an order in the database
'''
print('\nPART 4')

def complet_order(order):
	pass

# iterate each order
# parameter order number. name of our data base
# 




