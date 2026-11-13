"""======Test class statistica======"""

from statistica import House_goods, Food

def test_statistica_zero():
    house_goods = House_goods()

    assert house_goods.result_expense() == 0

def test_statistica_add():
    food = Food()

    food += {"price_expense": 100.0}

    assert food.result_expense() == 100.0