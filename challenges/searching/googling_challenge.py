'''
GOOGLING CHALLENGE! 

Today, we'll ask you to write a bunch of small pieces of code.

Unlike previous ones, we have NOT showed you the exact code you'll need to answer the questions.

So, you'll want to search out answers on the web, make sure you understand them, then try them out until they work!

For each question, you should also COPY THE LINK TO THE RESOURCE WHERE YOU FOUND THE SOLUTION in so that you can use it in the future too
'''
import numpy as np

# 1A. Sort the below list in alphabetical order
print('QUESTION 1\n')
my_friends = ['Yusuf', 'Aedan', 'Mia', 'Ash', 'Paul', 'Aeshna', 'Aryn', 'Rob']
sorted_list = sorted(my_friends)
print(sorted_list)

# 1B. Comment your code in 1A to convince yourself you understand how it works

# link where I found this function/command is: https://www.kite.com/python/answers/how-to-sort-a-list-alphabetically-in-python
# this function just takes the list I made and sorts it alphabetically. Items in list are
# ordered by the postion of thier letters in the alphabet. Uppercase letters come before lowercase letters.

# 2A. Get all the keys from the below dictionary, then print them out:
# Hint: there is a single command that can do this
print('QUESTION 2\n')

my_account = {'username': 'pbloom',
			  'password': 'python3.7',
			  'balance': 101.8,
			  'transaction_dates': ['9/18/2020', '9/20/2020', '10/5/2020'],
			  'verified': True}

print(my_account.keys())
# 2B. Comment your code in 2A to convince yourself you understand how it works

# one command that just prints out the keys of a dictionary. This function accesses the key words of a dictionary
# Link to where I found this fuction/command: https://www.tutorialspoint.com/python/dictionary_keys.htm


# 3A Count how many times the word 'wood' appears in the following string:
# Hint: there is a single command that can do this
print('QUESTION 3\n')
my_string = 'how much wood could a woodchuck chuck if a woodchuck could chuck wood?'
print(my_string.count('wood'))

# 3B. Comment your code in 3A to convince yourself you understand how it works

# this function/command counts any words I choose in the string
# Link where I found this function/command: https://stackoverflow.com/questions/17268958/finding-occurrences-of-a-word-in-a-string-in-python-3

# 4A Count how many times the string 'banana' appears in the following list:
# Hint: there is a way to do this with one line of code
print('QUESTION 4\n')
my_list = ['apple', 'banana', 'banana', 'cherry', 'mango', 'banana', 'banana', 'banana']
print(my_list.count('banana'))

# 4B. Comment your code in 4A to convince yourself you understand how it works

# Link where I found this function/command: https://www.programiz.com/python-programming/methods/list/count
# I googled count items in a list python. This counts any item in a list

# 5A Print out all of the unique strings in my_list
# Hint: there is a way to do this with one line of code
print('QUESTION 5\n')
print(list(set(my_list)))


# 5B. Comment your code in 5A to convince yourself you understand how it works
# link to where I found the funtion/command that accesses nonrepeating items in a list:
# https://stackoverflow.com/questions/12897374/get-unique-values-from-a-list-in-python
# I googled print out unique items in a list python. The list function returns the set back into a list fromat

# 6A. Import numpy, then use it to generate a random number between 0-1
print('QUESTION 6\n')

rand_num = np.random.rand()
print(rand_num)

for number in range(100):
	if rand_num < 0 or rand_num > 1:
		print(number,"Out of range.", rand_num)
		break
print("loop fininshed")
# 6B. Comment your code in 6A to convince yourself you understand how it works
# link where I found the numpy random fuction: https://www.w3schools.com/python/numpy_random.asp
# this function generates random number between 0 and 1 python numpy. we tested the function in order to see 
# if the random number function gives truly gives us a number between 0 and 1.

'''
Nice job! Hopefully after doing this challenge you feel a bit more ready to be able to search out new code solutions.
We'll be doing more challenges like this coming up in the future. 

Remember to comment all your code and push your work to your Github repo when you're done!
'''
