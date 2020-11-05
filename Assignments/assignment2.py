# Intro to Programming Using Python - Assignment #2
# Completed by: 

print('Answer 1')
# 1. Write an if statement that checks if user is "mattangriffel"
# and prints out "Welcome professor" if so, or "Who are you?" if not.

user = "mattangriffel"
if user == "mattangriffel":
	print("Welcome professor")
else:
	print("Who are you?")
	
print()
print('Answer 2')
# 2. Write an if statement that checks both the credentials below
# and prints "Successfully logged in." if they're correct or
# "Invalid username/password combination. Try again." if they're not.

user = "mattangriffel"
password = "123456"

if user == 'mattangriffel' and password == '123456':
	print('Successfully logged in.')
else:
	print('Invalid username/password combination. Try again.')

print()
print('Answer 3')
# 3. Write an if statement that checks whether the value of number is divisible
# by two and prints out "even" if it is and "odd" if it's not.
# (Hint: You can check divisiblity using the modulus (%) operator. 
# n % k == 0 evaluates to true if n is an exact multiple of k.)

number = 4

if number % 2 == 0:
	print('even')
else:
	print('odd')

print()
print('Answer 4')
# 4. Create three different lists containing:
# - The names of all your siblings
# - Your top 3 favorite movies
# - The latitude and longitude coordinates of Columbia University

siblings = ['Karen', 'Job', 'Ruth']
my_top_movies = ['Braveheart', 'Ironman', 'Fast & Furious']
Colum_location = [ '40.8075\u00b0 N', '73.9626\u00b0 W']

print()
print('Answer 5')
# 5. Use a for loop on each of the lists above to print out each element on its own line.
for name in siblings:
	print(name)

print()
for movie in my_top_movies:
	print(movie)
print()
for coordinate in Colum_location:
	print(coordinate)

print()
print('Answer 6')
# 6. Use a for loop and the title() function to print out each city name capitalized

cities = ["new york city", "san francisco", "boston", "chicago", "los angeles"]
for city in cities:
	print(city.title())

print()
print('Answer 7')
# 7. A list is different from an element in a list.  What's something you can do
# to the second in Python that you can't do to the first, and vice versa?

print('I can add other elements to a list that do not have to be of the same type.\ni.e intergers, floats, and even dictionaries.\nI cannot have different types within one element.')
person = ["Mattan"]
person = "Mattan"

print()
print('Answer 8')
# 8. Use range() and a for loop to print out:
# - the numbers from 1 to 10
# - the square of each of the numbers from 1 to 10
# - for each number from 1 to 10, print out whether it is even or not
for number in range(1, 11):
	number = number**2
	if number % 2 == 0:
		print(f'{number}: even')
	else:
		print(f'{number}: odd')

# Bonus: In Mathematics, a Marsenne number is a number that is one less than a
# power of two (i.e. 2^n - 1). Starting with an empty list named 
# marsenne_numbers (provided for you below),  use the append() function inside
# of a for loop so that after the loop has run, marsenne_numbers contains a
# list of the first ten Marsenne numbers.
print()
print('Bonus')
marsenne_numbers = []

def     Mersenne_numbers(n):
     return     2**n-1  

for numb in range(1, 11):
         marsenne_numbers.append(Mersenne_numbers(numb))


print(marsenne_numbers)




