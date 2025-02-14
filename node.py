from block import Block
from blockchain import Blockchain
from transaction import Transaction
from wallet import Wallet

class Node:
    def _init_(self, name):
        self.name = name
        self.blockchain = Blockchain()
        self.peers = []

    def add_peer(self, peer):
        """Жаңа түйінді қосу"""
        self.peers.append(peer)

    def share_block(self, block):
        """Барлық түйіндерге жаңа блокты тарату"""
        for peer in self.peers:
            peer.receive_block(block)

    def receive_block(self, block):
        """Жаңа блок қабылдау және синхрондау"""
        if not self.blockchain.chain:  # Егер блокчейн бос болса, жаңа блокты қосу
            self.blockchain.chain.append(block)
            print(f"{self.name} жаңа блокты қабылдады: {block.hash[:10]}...")
            return

        latest_block = self.blockchain.chain[-1]

        if block.previous_hash == latest_block.hash:  # Блок реттілігі дұрыс па?
            self.blockchain.chain.append(block)
            print(f"{self.name} жаңа блокты қабылдады: {block.hash[:10]}...")
        else:
            print(f"{self.name}: блок синхрондалмады! Қайта сұраныс жіберу керек.")

    def create_block(self, transactions):
        """Жаңа блок жасау және тарату"""
        latest_block = self.blockchain.chain[-1] if self.blockchain.chain else None
        previous_hash = latest_block.hash if latest_block else '0'  # Алдыңғы блок хэшін алу
        new_block = Block(index=latest_block.index + 1 if latest_block else 0, previous_hash=previous_hash, transactions=transactions)
        self.blockchain.chain.append(new_block)

        print(f"{self.name} жаңа блок құрды: {new_block.hash[:10]}...")
        self.share_block(new_block)



# *Түйіндер құру*
node1 = Node("Node 1")  # Блок жасаушы түйін
node2 = Node("Node 2")
node3 = Node("Node 3")

# *Түйіндерді байланыстыру*
node1.add_peer(node2)
node1.add_peer(node3)

# *Әмияндар*
wallet1 = Wallet()
wallet2 = Wallet()

# *Транзакциялар жасау*
transaction1 = Transaction(wallet1.get_address(), wallet2.get_address(), 50, 2, wallet1.private_key)
transaction2 = Transaction(wallet2.get_address(), wallet1.get_address(), 30, 1, wallet2.private_key)

# *Node 1 жаңа блок жасайды*
node1.create_block([transaction1, transaction2])

# *Node 2 және Node 3 жаңа блокты қабылдайды*
node2.receive_block(node1.blockchain.chain[-1])
node3.receive_block(node1.blockchain.chain[-1])

# *Блокчейндерді тексеру*
print(f"Node 1 Blockchain Valid: {node1.blockchain.is_chain_valid()}")
print(f"Node 2 Blockchain Valid: {node2.blockchain.is_chain_valid()}")
print(f"Node 3 Blockchain Valid: {node3.blockchain.is_chain_valid()}")
