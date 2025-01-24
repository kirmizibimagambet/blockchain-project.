from block import Block
from transaction import Transaction

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block("0", [])
        self.chain.append(genesis_block)

    def add_block(self, transactions):
        previous_hash = self.chain[-1].block_hash
        new_block = Block(previous_hash, transactions)
        self.chain.append(new_block)

    def validate_chain(self):
        for i in range(1, len(self.chain)):
            if self.chain[i].previous_hash != self.chain[i - 1].block_hash:
                return False
        return True