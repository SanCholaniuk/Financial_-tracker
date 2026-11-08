from operation import *
from writing_file import *

"""===A loop for the user to choose where it is best for them to store their information==="""

print("Choose the source of data usage and storage\n")

while True:

    choise_source = input("Enter file or database(1 or 2)? - ").lower()


    if choise_source == "1" or choise_source == "file":

        source = JSON_Storage("C:\\Users\\Admin\\Desktop\\financial_tracker_new\\tracker.json")
        actual_balance, transactions, full_statistic = source.load()

        break


    elif choise_source == "2" or choise_source == "database":

        database_config = {
        "dbname": "financial_tracker",
        "user": "postgres",
        "password": "password",
        "host": "localhost",
        "port": "5432",
    } 

        source = DB_Storage(database_config)
        actual_balance, transactions, full_statistic = source.load()
        
        break

    else:
        print("Please, Choose the source of data usage and storage")


"""===Function of tracker==="""
    
while True:

    print("\n\n---Finance tracker---\n\n"
    "1 - Add income\n" 
    "2 - Add expense\n" 
    "3 - Show balance\n" 
    "4 - Show all transaction\n" 
    "5 - Statistic\n"
    "6 - The most expenses\n" 
    "7 - Exit\n")


    action = input("Enter your action(number or full name) - ").lower()

    if action == "1" or action == "add income":
        actual_balance = add_income(actual_balance)

    elif action == "2" or action == "add expense":
        transactions, actual_balance = add_expense(transactions, actual_balance)

    elif action == "3" or action == "show balance":
        show_balance(actual_balance)   

    elif action == "4" or action == "show all transactions":
        show_all_transactions(transactions)

    elif action == "5" or action == "statistics":
        full_statistic = my_statistic(transactions)

    elif action == "6" or action == "the most expenses":
        most_expenses(full_statistic)
    
    elif action == "7" or action == "exit":

            source.save(actual_balance, transactions, full_statistic)

            break
        
    else:
        print("\nPlease, choose the function")
