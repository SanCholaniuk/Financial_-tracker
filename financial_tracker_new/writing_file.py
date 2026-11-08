from abc import ABC, abstractmethod
import json
import psycopg


class Storage(ABC):

    @abstractmethod
    def save(self, actual_balance, transactions, full_statistic):
        pass


    @abstractmethod
    def load(self):
        pass



class JSON_Storage(Storage):

    def __init__(self, datafile):
        self.datafile = datafile
        
    def load(self):
            
            try:
                with open(self.datafile, "r") as file:
                    
                    data = json.load(file)

                    return (
                        data.get("actual balance", 0.0),
                        data.get("transactions", []),
                        data.get("full statistic",{})
                        )

            except FileNotFoundError:
                return (
                    0.0,
                    [],
                    {}
                    )                            


    
    def save(self,  actual_balance, transactions, full_statistic):

        data = {
            "actual balance": actual_balance,
            "transactions": transactions,
            "full statistic": full_statistic,
        }
        with open(self.datafile, "w") as file:
            json.dump(data, file, indent=4)

        print("\nThe data are save succsesfull!")



class DB_Storage(Storage):

    def __init__(self, database):
        self.database_config = database


    def connect(self):
        
        return psycopg.connect(**self.database_config)

    
    def load(self):


        try:

            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT actual_balance FROM actual_balance;"
            )
            row_balance = cursor.fetchone()
            actual_balance = float(row_balance[0]) if row_balance else 0.0


            cursor.execute(
                "SELECT name_expense, price_expense, type_expense, date_expense FROM transactions;"
                )
            
            transactions = []
            for row in cursor.fetchall():
                transactions.append({
                "name_expense": row[0],
                "price_expense": float(row[1]),
                "type_expense": row[2],
                "date_expense": row[3],
                })

            cursor.execute(
                "SELECT house_goods, food, study, entertainment, other FROM full_statistic;"
            )

            full_statistic = {}
            row_stat = cursor.fetchone()
            if row_stat:
                full_statistic = {
                    "house_goods": float(row_stat[0]),
                    "food": float(row_stat[1]),
                    "study": float(row_stat[2]),
                    "entertainment": float(row_stat[3]),
                    "other": float(row_stat[4]),
                    }

            
            return actual_balance, transactions, full_statistic

        except Exception as error:
            print(f"Error - {error}") 
            return 0.0, [], {}

        finally:
            cursor.close()
            conn.close()


    def save(self,  actual_balance, transactions, full_statistic):

        try:

            conn = self.connect()
            cursor = conn.cursor()
            
            cursor.execute(
                "UPDATE actual_balance SET actual_balance = (%s) WHERE id = 1", (actual_balance,)
            )

            cursor.execute("DELETE FROM full_statistic;")
            cursor.execute("DELETE FROM transactions;")

            for item in transactions:
                cursor.execute(
                "INSERT INTO transactions (name_expense, price_expense, type_expense, date_expense) VALUES (%s, %s, %s, %s);",
            (
                item["name_expense"],
                item["price_expense"],
                item["type_expense"],
                item["date_expense"],
            )
            )

            cursor.execute(
                    " INSERT INTO full_statistic (house_goods, food, study, entertainment, other) VALUES (%s, %s, %s, %s, %s); ",
                (
                full_statistic.get("house_goods", 0.0),
                full_statistic.get("food", 0.0),
                full_statistic.get("study", 0.0),
                full_statistic.get("entertainment", 0.0),
                full_statistic.get("other", 0.0),
                )
            )
            
            print("\nThe data are save succsesfull!")
            
            conn.commit()

        except Exception as error:
            print(f"Error - {error}")        
            conn.rollback()
            
        finally:
            cursor.close()
            conn.close()