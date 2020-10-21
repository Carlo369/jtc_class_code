# define the create_account function 
def create_account():
	username = input("Please enter username ")
	password = input("Please enter password ")
	account = {'username': username, 'password': password, 'balance': float(0)}
	return account

def deposit(account, amount):
	account['balance'] = float(amount) + account['balance']

def withdraw(account, amount):
	if amount <= account['balance']:
		account['balance'] = account['balance'] - float(amount)
	else:
		print("Sorry, you don't have that amount in your account")

