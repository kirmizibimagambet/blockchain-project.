import tkinter as tk
from blockchain import Blockchain
from transaction import Transaction

# Блокчейнді құру
blockchain = Blockchain()

# Тест үшін транзакциялар қосамыз
transactions = [
    Transaction("Alice", "Bob", 10, 1),
    Transaction("Bob", "Charlie", 5, 1),
    Transaction("Charlie", "Alice", 2, 1)
]

# Блокты блокчейнге қосу
blockchain.add_block(transactions)

def display_blocks():
    """GUI-де блоктарды көрсету функциясы"""
    for widget in frame.winfo_children():
        widget.destroy()

    for block in blockchain.chain:
        text = (
            f"Index: {block.index}\n"
            f"Timestamp: {block.timestamp}\n"
            f"Previous Hash: {block.previous_hash}\n"
            f"Merkle Root: {block.merkle_root}\n"
            f"Hash: {block.hash}\n"
            f"Transactions:\n"
        )
        for tx in block.transactions:
            text += f"  {tx.sender} -> {tx.receiver}: {tx.amount} (Fee: {tx.fee}) [{tx.tx_hash}]\n"

        text += "\n"

        label = tk.Label(frame, text=text, anchor="w", justify="left", bg="lightgray", padx=5, pady=5)
        label.pack(fill="x")

# GUI терезесін құру
root = tk.Tk()
root.title("Blockchain Explorer")

frame = tk.Frame(root)
frame.pack(fill="both", expand=True, padx=10, pady=10)

btn = tk.Button(root, text="Show Blockchain", command=display_blocks)
btn.pack(pady=5)

root.mainloop()
