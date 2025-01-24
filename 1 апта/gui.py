import tkinter as tk
from blockchain import Blockchain

# Blockchain объектісін жасау
blockchain = Blockchain()

# Блокчейнге бірнеше блок қосу
blockchain.add_block("Block 1 Data")
blockchain.add_block("Block 2 Data")
blockchain.add_block("Block 3 Data")


def display_blocks():
    # Алдымен барлық ескі виджеттерді жою
    for widget in frame.winfo_children():
        widget.destroy()

    # Блокчейннің жарамдылығын тексеру
    if not blockchain.is_chain_valid():
        error_label = tk.Label(frame, text="❌ Blockchain is invalid!", fg="red", font=("Arial", 14, "bold"))
        error_label.pack()
        return  # Егер жарамсыз болса, блоктарды көрсетпейміз

    # Егер жарамды болса, блоктарды көрсету
    for block in blockchain.chain:
        text = f"Index: {block.index}\nTimestamp: {block.timestamp}\nHash: {block.hash}\nPrevious Hash: {block.previous_hash}\nData: {block.data}\n\n"
        label = tk.Label(frame, text=text, anchor="w", justify="left")
        label.pack(fill="x")


# GUI құру
root = tk.Tk()
root.title("Blockchain Explorer")

# Блоктарды көрсететін Frame
frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

# Блоктарды көрсету түймесі
btn = tk.Button(root, text="Show Blockchain", command=display_blocks)
btn.pack()

root.mainloop()

