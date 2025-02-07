import time
from transaction import Transaction
from hash_algorithm import simple_hash
from merkle_tree import MerkleTree

class Block:
    def __init__(self, index, previous_hash, transactions):
        self.index = index
        self.timestamp = time.time()
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.merkle_root = self.calculate_merkle_root()
        self.hash = self.calculate_hash()

    def calculate_merkle_root(self):
        """Меркле түбірін есептеу"""
        merkle_tree = MerkleTree(self.transactions)
        return merkle_tree.root

    def calculate_hash(self):
        """Блоктың хэші"""
        block_string = f"{self.index}{self.timestamp}{self.previous_hash}{self.merkle_root}"
        return simple_hash(block_string)
