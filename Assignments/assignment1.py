# Intro to Programming Using Python - Assignment #1
# Completed by:
# 1. Print out the following text:
# You've reached [your name].
# I'm not available right now, so leave a message and I'll call you back.
print("You've reached Carlos Sanchez.\nI'm not available right now, so leave a messageand I'll call you right back.")
print()
# 2. Create five variables for your first name, last name, shoe size, height, and
# age.
# And then print them out on one line.
first_name = 'Carlos'
last_name = 'Sanchez'
shoe_size = 8
height = '5 foot, 3'
age = 45

print(f'My name is {first_name}{last_name}; my shoe size, {shoe_size}; my height, {height}; and age, {age}.')

# 3. If subtotal = 10.58 and tip = 0.22 (22%) then calculate the total bill amount
# in a variable named total and print it out.
print()
subtotal = 10.58
tip = 0.22 
total = subtotal + subtotal*tip
print(total)
print()
# 4. Convert 158.8 into an integer.
print(int(158.8))

# Convert 75 into a float.
print(float(75))

# Convert "244.9" into a float and then an integer.
print(float(244.9))
print(int(244.9))

print()
# 5. Use \t and \n in a string and then print it out so that it matches
#(approximately) the following:
# -in the woods
#               which
#                   stutter
#                           and
#
#                               sing

print("-in the woods\n\t\twhich\n\t\t\tstutter\n\t\t\t\tand\n\t\t\t\t\tsing")

print()
# 6. Put your first name and total from above into an f-string (f"...") so that it
#reads:
# Mattan, your total is $12.91
# (remember to round the total to the nearest cent)
print(f'{first_name}, your total is ${round(total, 2)}')
print()
# 7. Use input() to ask a user for the city they live in, and then print it back to
#them.
city = input('What city do you live in? ')
print(city)
# 8. Build a future value calculator by using input() to get values from the user.
# (Make sure you convert them into integers or floats before doing any math on
#them.)
# Print out the result.
number = input("Please insert a number. ")
future_value = (1+.5)*int(number)**2
print(f'Your future value is {future_value}.')
# Hint: Future Value = Present Value x (1 + rate of return) ^ number of periods












