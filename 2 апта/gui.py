import tkinter as tk
from blockchain import Blockchain
from transaction import Transaction

def show_blockchain(blockchain):
    root = tk.Tk()
    root.title("Blockchain Explorer")
    
    for i, block in enumerate(blockchain.chain):
        frame = tk.Frame(root, borderwidth=2, relief="solid")
        frame.pack(pady=10, padx=10)
        
        tk.Label(frame, text=f"Block {i + 1}").pack()
        tk.Label(frame, text=f"Previous Hash: {block.previous_hash}").pack()
        tk.Label(frame, text=f"Merkle Root: {block.merkle_root}").pack()
        tk.Label(frame, text=f"Block Hash: {block.block_hash}").pack()
        
        for tx in block.transactions:
            tk.Label(frame, text=f"Transaction: {tx.tx_hash}").pack()
            tk.Label(frame, text=f"  From: {tx.sender}, To: {tx.receiver}, Amount: {tx.amount}").pack()
    
    root.mainloop()

if __name__ == "__main__":
    blockchain = Blockchain()
    tx1 = Transaction("Alice", "Bob", 50, 1)
    tx2 = Transaction("Bob", "Charlie", 30, 0.5)
    blockchain.add_block([tx1, tx2])
    show_blockchain(blockchain)
