# Funcion CREAR CUENTA
def create_account(accounts, name, account_type):
  account_id = len(accounts)
  account = [account_id, name, account_type, []]
  accounts.append(account)
  return account_id

def add_transaction(accounts, description, account_id, amount):
  for account in accounts:
    if account[0] == account_id:
      account[3].append([description, amount])
      break
    
def get_account_balance(accounts, account_id):
  balance = 0
  for account in accounts:
    if account[0] == account_id:
      for transaction in account[3]:
        if account[2] == "Ingreseo":
          balance += transaction[1]
        elif account[2] == "Egreso":
          balance -= transaction[1]
      break
  return balance

def get_total_balance(accounts):
  total_balance = 0
  for account in accounts:
    balance = get_account_balance(accounts, account[0])
    total_balance += balance
  return total_balance
