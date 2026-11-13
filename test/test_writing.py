from json_storage import JSON_Storage
from db_storage import DB_Storage
import json

def test_load_json_empty():
    
    storage = JSON_Storage("empty.json")

    result = storage.load()

    assert result == (0.0, [], {})

def test_load_json_full(tmp_path):

    file_path = tmp_path / "full.json"

    actual_balance = 100.0

    transactions = [
        {
            "name_expense": "flowers",
            "price_expense": 900.0,
            "type_expense": "other",
            "date_expense": "2026-11-08 18:50:33"
        }
    ]

    full_statistic = {
        "house_goods": 0.0,
        "food": 0.0,
        "study": 0.0,
        "entertainment": 0.0,
        "other": 900.0
    }
    data = {
            "actual balance": actual_balance,
            "transactions": transactions,
            "full statistic": full_statistic
        }

    with open(file_path, "w") as file:                   
        json.dump(data, file,  indent=4)


    storage = JSON_Storage(file_path)

    result = storage.load()

    assert result == (actual_balance, transactions, full_statistic)


def test_save(monkeypatch):

    # Arrange
    database_config = {}
    source = DB_Storage(database_config)

    executed_queries = []
    committed = False

    class FakeCursor:

        def execute(self, query, params=None):
            executed_queries.append((query, params))

        def close(self):
            pass
