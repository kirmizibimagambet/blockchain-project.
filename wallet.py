import rsa

class Wallet:
    def __init__(self):
        self.public_key, self.private_key = self.generate_keys()

    def generate_keys(self):
        """Ашық және жеке кілттерді жасау"""
        return rsa.newkeys(512)

    def get_address(self):
        """Пайдаланушы адресін қайтару (ашық кілттің хэші)"""
        return self.public_key.save_pkcs1(format='PEM').decode('utf-8')
