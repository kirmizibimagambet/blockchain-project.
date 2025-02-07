class UTXO:
    def __init__(self):
        self.utxos = {}

    def initialize_balance(self, address):
        if address not in self.utxos:
            self.utxos[address] = 100  # Бастапқы баланс 100 теңге

    def process_transaction(self, transaction):
        sender = transaction.sender
        receiver = transaction.receiver
        amount = transaction.amount
        fee = transaction.fee

        if sender not in self.utxos or self.utxos[sender] < amount + fee:
            return False

        self.utxos[sender] -= (amount + fee)
        self.utxos[receiver] = self.utxos.get(receiver, 0) + amount
        return True

    def get_balance(self, address):
        return self.utxos.get(address, 0)
