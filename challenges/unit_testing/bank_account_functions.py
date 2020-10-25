# define the create_account function 
def create_account():
	username = input("Please enter username ")
	password = input("Please enter password ")
	account = {'username': username, 'password': password, 'balance': float(0)}
	return account
# define a deposit function
def deposit(account, amount):
	account['balance'] = float(amount) + account['balance']
	print(account)
# define a withdraw function



def withdraw(account, amount):
	if amount <= account['balance']:
		account['balance'] = account['balance'] - float(amount)
		print(account)
	else:
		print("Sorry, you don't have that amount in your account")
# defining secure deposit and withdraw function

def validate(account, attempts = 0):
	username = input("Please enter username ")
	password = input("Please enter password ")
	if username == account['username'] and password == account['password']:
		# correct
		print("Thank you. You now have access to your account.")
		return 
	else:
		# incorrect
		print('You have entered the wrong username or password')
		attempts +=1
		print(attempts)
		if attempts < 3:
			validate(account, attempts)
		else:
			print('Sorry. You are locked out of your account. Please call your bank representive.')
			quit()



		


def deposit_secure(account, amount):
	validate(account)
	deposit(account, amount)



def withdraw_secure(account, amount):
	validate(account)
	withdraw(account, amount)













