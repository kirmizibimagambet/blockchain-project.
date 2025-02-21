import tkinter as tk
from blockchain import Blockchain
from transaction import Transaction
from validator import Validator
import rsa
import random

class WalletApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Blockchain Wallet")

        self.blockchain = Blockchain()
        self.validators = [Validator(f"validator_{i}", random.randint(1000, 5000)) for i in range(5)]
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
        
         # Блок Эксплорер (блоктарды көрсету)
        self.explorer_label = tk.Label(root, text="Блок Эксплорер")
        self.explorer_label.pack()

        self.blocks_listbox = tk.Listbox(root, height=10, width=50)
        self.blocks_listbox.pack()
        self.blocks_listbox.bind("<<ListboxSelect>>", self.show_block_transactions)

        #  Транзакциялар үшін листбокс қосу
        self.tx_listbox = tk.Listbox(self.root, height=5, width=50)
        self.tx_listbox.pack()
        
         # Стейкинг и делегация
        self.stake_label = tk.Label(root, text="Стейкинг монет")
        self.stake_label.pack()

        self.stake_amount_entry = tk.Entry(root)
        self.stake_amount_entry.pack()
        self.stake_amount_entry.insert(0, "Сома для стейкинга")

        self.delegate_button = tk.Button(root, text="Делегировать монеты", command=self.delegate_stake)
        self.delegate_button.pack()

        # Список валидаторов
        self.validator_label = tk.Label(root, text="Валидаторы")
        self.validator_label.pack()

        self.validators_listbox = tk.Listbox(root, height=5, width=50)
        self.validators_listbox.pack()
        
        self.update_explorer()

    def update_explorer(self):
        """ Блоктар тізімін жаңарту """
        self.blocks_listbox.delete(0, tk.END)

        for block in self.blockchain.chain:
            transactions_str = ", ".join(str(tx) for tx in block.transactions)
            self.blocks_listbox.insert(tk.END, f"Block {block.index} | Hash: {block.hash[:10]}...")

        # Обновление списка валидаторов
        self.validators_listbox.delete(0, tk.END)
        for validator in self.validators:
            self.validators_listbox.insert(tk.END,
                                           f"Validator {validator.address[:10]} | Stake: {validator.get_stake()}")

    def show_block_transactions(self, event):
        selected_index = self.blocks_listbox.curselection()
        if not selected_index:
            return

        block_index = selected_index[0]
        block = self.blockchain.chain[block_index]

        self.tx_listbox.delete(0, tk.END)
        for tx in block.transactions:
            self.tx_listbox.insert(tk.END, f"{tx.sender[:10]} -> {tx.receiver[:10]} | {tx.amount}")

    
    def create_transaction(self):
        receiver = self.receiver_entry.get()
        amount = float(self.amount_entry.get())
        fee = float(self.fee_entry.get())

        if self.blockchain.utxo.get_balance(self.address) < amount + fee:
            print("Қателік: Баланс жеткіліксіз!")
            return

        tx = Transaction(self.address, receiver, amount, fee, self.private_key)

        self.blockchain.add_block([tx])
        print("Жаңа блок қосылды!")

        self.balance_label.config(text=f"Баланс: {self.blockchain.utxo.get_balance(self.address)}")

        #  Блок Эксплорер жаңарту
        self.update_explorer()
        
         # Метод для делегирования стейка с учетом комиссии и вознаграждения
    def delegate_stake(self):
        """ Делегирование монет валидатору """
        amount = float(self.stake_amount_entry.get())  # Стейк, который мы делегируем
        fee = float(self.fee_entry.get())  # Комиссия

        # Проверяем, достаточно ли средств на балансе
        if self.blockchain.utxo.get_balance(self.address) < amount + fee:
            print("Қателік: Баланс жеткіліксіз!")
            return

        # Выбираем валидатора для делегации
        selected_index = self.validators_listbox.curselection()
        if not selected_index:
            print("Қателік: Валидатор таңдалмаған!")
            return

        validator_index = selected_index[0]
        validator = self.validators[validator_index]

        # Обновляем баланс для отправителя
        self.blockchain.utxo.update_balance(self.address, -(amount + fee))  # Уменьшаем баланс отправителя
        self.blockchain.utxo.update_balance(validator.address, amount)  # Увеличиваем баланс валидатора

        # Рассчитываем 5% от стейка и добавляем его как вознаграждение валидатору
        reward = amount * 0.05  # 5% от суммы стейка
        self.blockchain.utxo.update_balance(validator.address, reward)  # Вознаграждение валидатору

        # Обновляем интерфейс (баланс)
        self.balance_label.config(text=f"Баланс: {self.blockchain.utxo.get_balance(self.address)}")
        print(f"Монеты делегированы валидатору {validator.address[:10]} с вознаграждением {reward}!")

        # Обновляем блоки в интерфейсе
        self.update_explorer()



root = tk.Tk()
app = WalletApp(root)
root.mainloop()
