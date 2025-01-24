import hashlib

class Transaction:
    def __init__(self, sender, receiver, amount, fee):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.fee = fee
        self.tx_hash = self.compute_hash()
    
    def compute_hash(self):
        data = f"{self.sender}{self.receiver}{self.amount}{self.fee}"
        return hashlib.sha256(data.encode()).hexdigest()
