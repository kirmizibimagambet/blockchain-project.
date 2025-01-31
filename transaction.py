from hash_algorithm import simple_hash

class Transaction:
    def __init__(self, sender, receiver, amount, fee):
        self.sender = sender  # Жіберуші
        self.receiver = receiver  # Алушы
        self.amount = amount  # Сома
        self.fee = fee  # Комиссия
        self.tx_hash = self.calculate_hash()  # Транзакцияның хэші

    def calculate_hash(self):
        """Транзакцияның хэші"""
        tx_string = f"{self.sender}{self.receiver}{self.amount}{self.fee}"
        return simple_hash(tx_string)
