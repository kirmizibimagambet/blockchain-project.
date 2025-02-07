from block import Block
from utxo import UTXO
from merkle_tree import MerkleTree

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.utxo = UTXO()

    def create_genesis_block(self):
        return Block(0, "0", [])

    def add_block(self, transactions):
        valid_transactions = []
        for tx in transactions:
            if self.utxo.process_transaction(tx) and tx.verify_signature(tx.sender):
                valid_transactions.append(tx)

        if valid_transactions:
            previous_block = self.chain[-1]
            new_block = Block(len(self.chain), previous_block.hash, valid_transactions)
            self.chain.append(new_block)

    def is_valid_merkle_root(self, block):
        tx_hashes = [tx.tx_hash for tx in block.transactions]
        merkle_tree = MerkleTree(tx_hashes)
        return merkle_tree.root == block.merkle_root

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

            if not self.is_valid_merkle_root(current_block):
                return False

            for tx in current_block.transactions:
                if not self.utxo.process_transaction(tx):
                    return False

        return True
