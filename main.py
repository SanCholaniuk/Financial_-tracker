"""===Main menu==="""
from operation import *
import json

try:
    with open("C:\\Users\\Admin\\Desktop\\financial_ tracker\\tracker.json", "r") as file:
        data = json.load(file)
        actualy_balance = data["actualy balance"]
        statistic = data["statistics"]
        transactions = data["transaction"]


except FileNotFoundError:
    actualy_balance = 0
    statistic = {}
    transactions = []
    
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
        actualy_balance = add_income(actualy_balance)

    elif action == "2" or action == "add expense":
        transactions, actualy_balance = add_expense(transactions, actualy_balance)

    elif action == "3" or action == "show balance":
        show_balance(actualy_balance)   

    elif action == "4" or action == "show all transaction":
        show_all_transaction(transactions)

    elif action == "5" or action == "statistics":
        statistic = my_statistic(transactions)

    elif action == "6" or action == "the most expenses":
        most_expenses(statistic)
    
    elif action == "7" or action == "exit":
        print("\nYou close the programe. Your data is saved.")

        data = {
            "actualy balance": actualy_balance,
            "statistics": statistic,
            "transaction": transactions
        }

        with open("C:\\Users\\Admin\\Desktop\\financial_ tracker\\tracker.json", "w") as file:
            json.dump(data, file, indent = 4)  

        break

    else:
        print("\nPlease, choose the function")