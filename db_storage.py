from storage import Storage
import psycopg

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


            cursor.execute("""
                SELECT
                transactions.name_expense,
                transactions.price_expense,
                type_expense.name,
                transactions.date_expense
                FROM transactions
                JOIN type_expense
                ON transactions.type_expense_id = type_expense.id;
                """)
            
            transactions = []
            for row in cursor.fetchall():
                transactions.append({
                "name_expense": row[0],
                "price_expense": float(row[1]),
                "type_expense": row[2],
                "date_expense": row[3],
                })

            
            return actual_balance, transactions, {}

        except Exception as error:
            print(f"Error - {error}") 
            return 0.0, [], {}

        finally:
            cursor.close()
            conn.close()


    def save(self,  actual_balance, transactions, new_transactions , full_statistic):

        try:

            conn = self.connect()
            cursor = conn.cursor()
            
            cursor.execute(
                "UPDATE actual_balance SET actual_balance = %s WHERE id = 1", (actual_balance,)
            )

            for item in new_transactions:
                cursor.execute(
                "INSERT INTO transactions (name_expense, price_expense, type_expense_id, date_expense) VALUES (%s, %s, (SELECT id FROM type_expense WHERE name = %s), %s);",
            (
                item["name_expense"],
                item["price_expense"],
                item["type_expense"],
                item["date_expense"],
            )
            )
            
            print("\nThe data are save succsesfull!")
            
            conn.commit()
            return True
            

        except Exception as error:
            print(f"Error - {error}")        
            conn.rollback()
            return False
            
            
        finally:
            cursor.close()
            conn.close()



    def get_statistic(self):

        try:
            conn = self.connect()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT
                    type_expense.name,
                    SUM(transactions.price_expense)
                FROM transactions
                JOIN type_expense
                    ON transactions.type_expense_id = type_expense.id
                GROUP BY type_expense.name;
            """)

            result = cursor.fetchall()

            full_statistic = {}

            for row in result:
                full_statistic[row[0]] = float(row[1])

            return full_statistic

        except Exception as error:
            print(f"Error - {error}")
            return {}

        finally:
            cursor.close()
            conn.close()


#from contextlib import contextmanager
#from storage import Storage
#import psycopg


#class DB_Storage(Storage):

#  def __init__(self, database):
#    self.database_config = database

#  @contextmanager
#  def _get_connection(self):
#    conn = psycopg.connect(**self.database_config)
#    cursor = conn.cursor()
#    try:
#      yield conn, cursor
#    finally:
#      cursor.close()
#      conn.close()

#  def _fetch_balance(self, cursor)
#
#    cursor.execute("SELECT actual_balance FROM actual_balance;")
#    row = cursor.fetchone()
#    return float(row[0]) if row else 0.0

#  def _fetch_transactions(self, cursor)
#    cursor.execute("""
#            SELECT
#                transactions.name_expense,
#                transactions.price_expense,
#                transactionse.name,
#                transactions.date_expense
#            FROM transactions t
#            JOIN type_expense te ON t.type_expense_id = te.id;
#        """)
#    return [{
#        "name_expense": row[0],
#        "price_expense": float(row[1]),
#        "type_expense": row[2],
#        "date_expense": row[3],
#    } for row in cursor.fetchall()]

#  def load(self):
#    try:
#      with self._get_connection() as (_, cursor):
#        actual_balance = self._fetch_balance(cursor)
#        transactions = self._fetch_transactions(cursor)
#        return actual_balance, transactions, {}
#    except Exception as error:
#      print(f"Error loading from DB: {error}")
#      return 0.0, [], {}

#  def save(self, actual_balance, transactions, new_transactions, full_statistic):
#    try:
#      with self._get_connection() as (conn, cursor):
#        # Оновлення балансу
#        cursor.execute(
#            "UPDATE actual_balance SET actual_balance = %s WHERE id = 1",
#            (actual_balance,),
#        )

#        for item in new_transactions:
#          cursor.execute(
#              """
#                    INSERT INTO transactions 
#                    (name_expense, price_expense, type_expense_id, date_expense) 
#                    VALUES (%s, %s, (SELECT id FROM type_expense WHERE name = %s), %s);
#                """,
#              (
#                  item["name_expense"],
#                  item["price_expense"],
#                  item["type_expense"],
#                  item["date_expense"],
#              ),
#          )
#
#        conn.commit()
#        print("\nThe data are saved successfully!")
#        return True

#    except Exception as error:
#      print(f"Error saving to DB: {error}")
#      return False
#
#  def get_statistic(self):
#    try:
#      with self._get_connection() as (_, cursor):
#        cursor.execute("""
#                SELECT
#                    te.name,
#                    SUM(t.price_expense)
#                FROM transactions t
#                JOIN type_expense te ON t.type_expense_id = te.id
#                GROUP BY te.name;
#            """)
#        return {row[0]: float(row[1]) for row in cursor.fetchall()}

#    except Exception as error:
#      print(f"Error fetching statistics: {error}")
#      return {}