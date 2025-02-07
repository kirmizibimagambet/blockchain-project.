import tkinter as tk
from blockchain import Blockchain
from transaction import Transaction
import rsa

class WalletApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Blockchain Wallet")

        self.blockchain = Blockchain()
        self.public_key, self.private_key = rsa.newkeys(512)
        self.address = self.public_key.save_pkcs1().decode()

        self.blockchain.utxo.initialize_balance(self.address)

        self.balance_label = tk.Label(root, text=f"Баланс: {self.blockchain.utxo.get_balance(self.address)}")
        self.balance_label.pack()

        self.receiver_entry = tk.Entry(root)
        self.receiver_entry.pack()
        self.receiver_entry.insert(0, "Қабылдаушы адресі")

        self.amount_entry = tk.Entry(root)
        self.amount_entry.pack()
        self.amount_entry.insert(0, "Сома")

        self.fee_entry = tk.Entry(root)
        self.fee_entry.pack()
        self.fee_entry.insert(0, "Транзакция комиссиясы")

        self.send_button = tk.Button(root, text="Жіберу", command=self.create_transaction)
        self.send_button.pack()

    def create_transaction(self):
        receiver = self.receiver_entry.get()
        amount = float(self.amount_entry.get())
        fee = float(self.fee_entry.get())

        if self.blockchain.utxo.get_balance(self.address) < amount + fee:
            print("Қателік: Баланс жеткіліксіз!")
            return

        tx = Transaction(self.address, receiver, amount, fee, self.private_key)
        self.blockchain.add_block([tx])

        self.balance_label.config(text=f"Баланс: {self.blockchain.utxo.get_balance(self.address)}")
        print("Транзакция жіберілді!")

root = tk.Tk()
app = WalletApp(root)
root.mainloop()
