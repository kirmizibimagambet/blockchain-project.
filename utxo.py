class UTXO:
    def __init__(self):
        self.balances = {}  # Әрбір аккаунттың балансы
        self.default_balance = 100  # Әрбір аккаунтқа бастапқы 100 монета

    def process_transaction(self, transaction):
        """Транзакцияны өңдеу және баланс жаңарту"""
        sender = transaction.sender
        receiver = transaction.receiver
        amount = transaction.amount + transaction.fee

        # Егер жіберушінің балансы жеткіліксіз болса, транзакция қабылданбайды
        if self.balances.get(sender, self.default_balance) < amount:
            return False

        # Балансты жаңарту
        self.balances[sender] = self.balances.get(sender, self.default_balance) - amount
        self.balances[receiver] = self.balances.get(receiver, self.default_balance) + transaction.amount
        return True  # Транзакция сәтті орындалды
