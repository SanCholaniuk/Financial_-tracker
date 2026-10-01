"""Operation file"""

def add_income(actualy_balance):

    """Function for accrual of balance"""
    
    new_balance = (float(input("\nEnter the balance what you want to add - ")))

    if new_balance < 0:
        print("\nCannot add a negative amount")
        return None

    actualy_balance += new_balance

    return actualy_balance


def add_expense(transactions, actualy_balance):

    """Function for expense procesing"""
   
    name_expense = input("\nEnter the name of the purchased product - ")
    price_expense = float(input("\nEnter the price your expense - "))

    if price_expense <= 0:
        print("\nExpense must be greater than zero")
        return transactions, actualy_balance

    if price_expense > actualy_balance:
        print("\nCan`t buy a god. Not enough funds")
        return transactions, actualy_balance

    type_expense = input("\nEnter the type your expense (house goods, food, study, enterteimant or other) - ").lower()
    date_expense = input("\nEnter the date when you bought the ware - ")

    expense_keylist = ("name expense", "price expense", "type expense", "date expanse")
    expense_valuelist = (name_expense, price_expense, type_expense, date_expense)

    expense = dict(zip(expense_keylist,expense_valuelist))

    transactions.append(expense)

    actualy_balance = actualy_balance - price_expense 
      
    return transactions, actualy_balance



def show_balance(actualy_balance):
    
    """Function for show of balance"""

    print(f"\nYour actualy balance - ({actualy_balance})")


def show_all_transaction(transactions):

    """Function for show all transaction"""
    print(transactions)



def my_statistic(transactions):

    """Function for cost statistics"""
    
    house_goods = 0
    food = 0   
    study = 0 
    enterteimant = 0
    other = 0

    print("\n")

    for expense in transactions:

        if expense["type expense"] == "house goods":
            house_goods += expense["price expense"]

        elif expense["type expense"] == "food":
            food += expense["price expense"]
    
        elif expense["type expense"] == "study":
            study += expense["price expense"]

        elif expense["type expense"] == "enterteimant":
            enterteimant += expense["price expense"]
    
        else:
            other += expense["price expense"]
   
    statistic = {
        "house goods": house_goods,
        "food": food,
        "study": study,
        "enterteimant": enterteimant,
        "other":other
    }

    print(statistic)

    return statistic


def most_expenses(statistic):

    """Function for most expenses"""

    most_statistic = 0
    value_statistic = ""

    for expense in statistic.values():
        if most_statistic < expense:
            most_statistic = expense

    for key, value in statistic.items():
        if value == most_statistic:
            value_statistic = key
        

    print(f"\nThe most expenses - {most_statistic} on {value_statistic}")