"""Operation file"""
from statistica import House_goods, Food, Study, Entertainment, Other_goods
from datetime import datetime

def add_income(actual_balance):

    """===Function for accrual of balance==="""
    
    new_balance = (float(input("\nEnter the balance what you want to add - ")))

    if new_balance < 0:
        print("\nCannot add a negative amount")
        return actual_balance

    actual_balance += new_balance

    actual_balance = round(actual_balance, 2)

    return actual_balance


def add_expense(transactions, new_transactions, actual_balance):

    """===Function for expense procesing==="""
   
    name_expense = input("\nEnter the name of the purchased product - ")
    price_expense = float(input("\nEnter the price your expense - "))

    if price_expense <= 0:
        print("\nExpense must be greater than zero")
        return transactions, new_transactions, actual_balance


    if price_expense > actual_balance:
        print("\nCan`t buy a god. Not enough funds")
        return transactions, new_transactions, actual_balance

    type_expense = input("\nEnter the type your expense (house goods, food, study, entertainment or other) - ").lower()
    date_expense = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    expense_keylist = ("name_expense", "price_expense", "type_expense", "date_expense")
    expense_valuelist = (name_expense, price_expense, type_expense, date_expense)

    expense = dict(zip(expense_keylist,expense_valuelist))

    new_transactions.append(expense)
    transactions.append(expense)

    actual_balance = actual_balance - price_expense 

    actual_balance = round(actual_balance, 2)
      
    return transactions, new_transactions, actual_balance



def show_balance(actual_balance):
    
    """===Function for show of balance==="""

    print(f"\nYour actual balance - ({actual_balance})")


def show_all_transactions(transactions):

    """===Function for show all transactios==="""
    print(transactions)



def my_statistic(transactions):

    """===Function for cost statistics==="""
    
    statistic = {
        "house goods": House_goods(),
        "food": Food(),
        "study": Study(),
        "entertainment": Entertainment(),
        "other": Other_goods()
    }


    print("\n")

    for expense in transactions:
        good = statistic[expense["type_expense"]]
        good += expense

   

    full_statistic = {
        "house goods": statistic["house goods"].result_expense(),
        "food": statistic["food"].result_expense(),
        "study": statistic["study"].result_expense(),
        "entertainment": statistic["entertainment"].result_expense(),
        "other": statistic["other"].result_expense()
    }

    print(full_statistic)

    return full_statistic


def most_expenses(full_statistic):

    """===Function for most expenses==="""

    most_statistic = 0
    value_statistic = ""

    for key, value in full_statistic.items():
        if most_statistic < value:
            most_statistic = value
            value_statistic = key
        

    print(f"\nThe most expenses - {most_statistic} on {value_statistic}")