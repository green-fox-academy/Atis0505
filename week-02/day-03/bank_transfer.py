import sys
accounts = [
	{ 'client_name': 'Igor', 'account_number': 11234543, 'balance': 203004099.2 },
	{ 'client_name': 'Vladimir', 'account_number': 43546731, 'balance': 5204100071.23 },
	{ 'client_name': 'Sergei', 'account_number': 23456311, 'balance': 1353600.0 }
]

# Create function that returns the name and balance of cash on an account

# Create function that transfers an amount of cash from one account to another
# it should have three parameters:
#  - from account_number
#  - to account_number
#  - amount to transfer
#
# Print "404 - account not found" if any of the account numbers don't exist


# name, ac_number, balance = input("Give me datas separatly with \"-\": ").split("-")
# num = int(ac_number)
# money = int(balance)

def transfer(from_acc,to_acc,amount):
    change_balance(from_acc, -amount)
    change_balance(to_acc, amount)

def change_balance(account_number, amount):
    temp_index = get_index_by_id(account_number)
    if accounts[temp_index(account_number)]["balance"] + amount > 0
        accounts[temp_index(account_number)]["balance"] += amount
        else:
            error("403 - forbidden")
            
def error(error_message):
    print(error_message)
    sys.exit()


def get_index_by_id(account_number):
    for account in accounts:
        if account['account_number'] == account_number:
            return accounts.index(account)
    print("404 - account not found")
    sys.exit()

print(accounts[get_index_by_id(11234543)]['balance'])
print(accounts[get_index_by_id(43546731)]['balance'])
transfer(1123454, 43546731, 50000)
print(accounts[get_index_by_id(11234543)]['balance'])
print(accounts[get_index_by_id(43546731)]['balance'])