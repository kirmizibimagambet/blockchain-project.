class Validator:
    def _init_(self, address: str, initial_stake: int = 0):
        self.address = address  # Уникальный адрес валидатора
        self.stake = initial_stake  # Изначальная ставка (монеты, которые валидатор поставил в сеть)
        self.delegators = {}  # Словарь для хранения делегированных монет (по адресу делегатора)
        self.reward_balance = 0  # Награды, полученные валидатором

    def delegate(self, delegator_address: str, amount: int):
        """
        Делегация монет валидатору от делегатора.
        """
        if delegator_address not in self.delegators:
            self.delegators[delegator_address] = 0
        self.delegators[delegator_address] += amount
        self.stake += amount  # Увеличиваем ставку валидатора на сумму делегации

    def reward(self, reward_amount: int):
        """
        Получение награды за блок и распределение между валидатором и его делегаторами.
        """
        self.reward_balance += reward_amount  # Валидатор получает свою награду
        # Распределяем награду между делегаторами пропорционально их вкладу
        total_delegated = sum(self.delegators.values())
        for delegator_address, stake in self.delegators.items():
            delegator_reward = (reward_amount * stake) / total_delegated
            # Для упрощения, награды делегаторам не сохраняются, но можно добавить логику обновления баланса делегаторов
            print(f"Delegator {delegator_address} receives reward: {delegator_reward:.2f} coins")
        print(f"Validator {self.address} receives total reward: {self.reward_balance:.2f} coins")

    def get_stake(self):
        """
        Возвращает текущую ставку валидатора, включая делегированные монеты.
        """
        return self.stake

    def _str_(self):
        """
        Строковое представление валидатора.
        """
        return f"Validator {self.address} with stake: {self.stake} coins"
