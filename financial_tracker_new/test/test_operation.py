from operation import add_income, add_expense, show_balance, show_all_transactions, most_expenses

"""======Test function add_income======"""

def test_add_income(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "500")

    assert add_income(1000) == 1500

def test_add_income_zero(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "0")

    assert add_income(1000) == 1000

def test_add_income_negative(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "-500")

    assert add_income(1000) == 1000

"""======Test function add_expense======"""

def test_add_expense_minus_balance(monkeypatch):

    monkeypatch.setattr("builtins.input", lambda _: "200")

    result = add_expense([] , 1000)

    assert result[1] == 800


def test_add_expense_new_transaction(monkeypatch):

    inputs = iter(["Warcraft 3", 999.0, "entertainment"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = add_expense([] , 1000)

    assert result[0] == [{"name_expense": "Warcraft 3", "price_expense": 999.0, "type_expense": "entertainment", "date_expense": result[0][0]["date_expense"]}]


"""======Test function show_balance======"""

def test_show_balance(capsys):

    show_balance(1000)

    balance = capsys.readouterr()

    assert balance.out == "\nYour actual balance - (1000)\n"

"""======Test function all_transaction======"""

def test_show_all_transactions(capsys):

    test_transactions = [{'name_expense': 'Warcraft 3', 'price_expense': 999.0, 'type_expense': 'entertainment', 'date_expanse': '14.10.2026'}]

    show_all_transactions(test_transactions)
    
    present_transactions  = capsys.readouterr()

    expected_transactions = "[{'name_expense': 'Warcraft 3', 'price_expense': 999.0, 'type_expense': 'entertainment', 'date_expanse': '14.10.2026'}]"

    assert present_transactions.out.strip() ==  expected_transactions .strip()

"""======Test function most_expenses======"""

def test_most_expenses(capsys):

    test_expenses = {'house_goods': 1599.0, 'food': 0, 'study': 999.0, 'enterteimant': 999.0, 'other': 1958.0}

    most_expenses(test_expenses)

    present_expenses = capsys.readouterr()

    assert  present_expenses.out == "\nThe most expenses - 1958.0 on other\n"