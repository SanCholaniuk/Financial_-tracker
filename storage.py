from abc import ABC, abstractmethod


class Storage(ABC):

    @abstractmethod
    def save(self, actual_balance, transactions, new_transactions, full_statistic):
        pass


    @abstractmethod
    def load(self):
        pass


    @abstractmethod
    def get_statistic(self):
        pass