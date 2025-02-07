import rsa
from hash_algorithm import simple_hash  # custom_hash орнына simple_hash

class Transaction:
    def __init__(self, sender, receiver, amount, fee, private_key):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.fee = fee
        self.tx_hash = self.calculate_hash()
        self.signature = self.sign_transaction(private_key)

    def calculate_hash(self):
        """ Транзакция деректерінен хэш есептеу """
        data = f"{self.sender}{self.receiver}{self.amount}{self.fee}"
        return simple_hash(data)  # custom_hash орнына simple_hash

    def sign_transaction(self, private_key):
        """ Транзакцияны жеке кілт арқылы қол қою """
        return rsa.sign(self.tx_hash.encode(), private_key, 'SHA-256')

    def verify_signature(self, public_key):
        """ Қолтаңбаны ашық кілт арқылы тексеру """
        try:
            if isinstance(public_key, str):  # Егер public_key string болса, оны қайта жүктеу керек
                public_key = rsa.PublicKey.load_pkcs1(public_key.encode())
            
            rsa.verify(self.tx_hash.encode(), self.signature, public_key)
            return True
        except rsa.VerificationError:
            return False
