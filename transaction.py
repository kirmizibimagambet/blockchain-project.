import rsa
from hash_algorithm import simple_hash  

class Transaction:
    def __init__(self, sender, receiver, amount, fee, private_key):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.fee = fee
        self.tx_hash = self.calculate_hash()
        self.signature = self.sign_transaction(private_key)

    def __str__(self):
        return f"{self.sender[:6]} -> {self.receiver[:6]} | {self.amount} BTC + {self.fee} fee"

    def calculate_hash(self):
        """ Транзакция деректерінен хэш есептеу """
        data = f"{self.sender}{self.receiver}{self.amount}{self.fee}"
        return simple_hash(data)  

    def sign_transaction(self, private_key):
        """ Транзакцияны жеке кілт арқылы қол қою """
        if not isinstance(private_key, rsa.PrivateKey):  # Тек PrivateKey қабылдайды
            raise TypeError(f"Invalid private key format: {type(private_key)}. Expected rsa.PrivateKey.")
        return rsa.sign(self.tx_hash.encode(), private_key, 'SHA-256')

    def verify_signature(self, public_key):
        """ Қолтаңбаны ашық кілт арқылы тексеру """
        try:
            if isinstance(public_key, str):  # Егер public_key жол болса, оны rsa.PublicKey-ке айналдыру
                public_key = rsa.PublicKey.load_pkcs1(public_key.encode('utf-8'))
            
            rsa.verify(self.tx_hash.encode('utf-8'), self.signature, public_key)
            return True
        except rsa.VerificationError:
            return False
