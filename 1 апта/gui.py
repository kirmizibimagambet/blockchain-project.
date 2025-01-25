import tkinter as tk
from blockchain import Blockchain

blockchain = Blockchain()

# Блокчейнге бірнеше блок қосу
blockchain.add_block("Block 1 Data")
blockchain.add_block("Block 2 Data")
blockchain.add_block("Block 3 Data")

def display_blocks():
    for widget in frame.winfo_children():
        widget.destroy()

    for block in blockchain.chain:
        text = f"Index: {block.index}\nTimestamp: {block.timestamp}\nHash: {block.hash}\nPrevious Hash: {block.previous_hash}\nData: {block.data}\n\n"
        label = tk.Label(frame, text=text, anchor="w", justify="left")
        label.pack(fill="x")

# GUI
root = tk.Tk()
root.title("Blockchain Explorer")

frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

btn = tk.Button(root, text="Show Blockchain", command=display_blocks)
btn.pack()

root.mainloop()
