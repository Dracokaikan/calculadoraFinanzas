from finance import create_account, add_transaction, get_account_balance, get_total_balance
# Crear el menú
def main(): # Función Principal
  
  #Creamos un diccionario para almacenar las cuentas
  accounts = []
  
  while True:
    print("Bienvenido a la calculadora")
    print("1.- Crear Cuenta")
    print("2.- Agregar transaccion")
    print("3.- Consultar saldo cuenta")
    print("4.- Consultar saldo total")
    print("5.- Salir")
  
# Capturar la opción de entrada
    opcion = int(input("Ingrese la opción deseada: "))
  
    if opcion == 1:
      print("Crear cuenta")
      name = input("Ingrese su nombre: ")
      account_type = input("Ingrese tipo de cuenta: ")
      account_id = create_account(accounts, name, account_type)
      print(f"Cuenta {name} creada con el id {account_id}")
      
    elif opcion == 2:
      account_id = int(input("Ingrese el ID de la cuenta: "))
      description = input("Ingrese la desctipción de la trnasacción: ")
      amount = float(input("Ingrese el monto de la transacción: "))
      add_transaction(accounts, description, account_id, amount)
      print(f"Transaccion de {amount} realizada en la cuenta {account_id}")
      
    elif opcion == 3:
      account_id = int(input("Ingrese el ID de la cuenta: "))
      balance = get_account_balance(accounts, account_id)
      print(f"El saldo de la cuenta {account_id} es {balance}")
    
    elif opcion == 4: 
      total_balance = get_total_balance(accounts)
      print(f"El saldo total de la cuenta {account_id}")
    
    elif opcion == 5:
      print("Gracias por usar la calculadora.")
      break
    
    else:
      print("Opción invalida, por favor intente nuevamente.")
      
if __name__ == "__main__":
  main()