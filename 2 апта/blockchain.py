from block import Block
from utxo import UTXO

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.utxo = UTXO()

    def create_genesis_block(self):
        """Генезис блокты құру"""
        return Block(0, "0", [])

    def add_block(self, transactions):
        """Жаңа блок қосу"""
        valid_transactions = [tx for tx in transactions if self.utxo.process_transaction(tx)]
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), previous_block.hash, valid_transactions)
        self.chain.append(new_block)

    def is_chain_valid(self):
        """Блокчейннің дұрыстығын тексеру"""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True
