import hashlib  # Хэш функциялары үшін қажет

class Block:
    def __init__(self, previous_hash, transactions):
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.merkle_root = self.compute_merkle_root()
        self.block_hash = self.compute_hash()

    def compute_merkle_root(self):
        # Меркле түбірін есептеу (мұнда өзіңіздің merkle_tree.py файлындағы функцияңызды пайдаланыңыз)
        from merkle_tree import merkle_root
        return merkle_root([tx.tx_hash for tx in self.transactions])

    def compute_hash(self):
        # Блоктың хэшін есептеу
        data = f"{self.previous_hash}{self.merkle_root}"
        return hashlib.sha256(data.encode()).hexdigest()
