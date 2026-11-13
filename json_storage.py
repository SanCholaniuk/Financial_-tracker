from storage import Storage
import json


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

    
    def save(self,  actual_balance, transactions, new_transactions, full_statistic):

        data = {
            "actual balance": actual_balance,
            "transactions": transactions,
            "full statistic": full_statistic,
        }
        with open(self.datafile, "w") as file:
            json.dump(data, file, indent=4)

        print("\nThe data are save succsesfull!")


    def get_statistic(self):
         _, _, full_statistic = self.load()
         return full_statistic