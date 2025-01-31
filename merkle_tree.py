from hash_algorithm import simple_hash

class MerkleTree:
    def __init__(self, transactions):
        self.transactions = transactions
        self.root = self.build_merkle_root()

    def build_merkle_root(self):
        """Меркле түбірін есептеу"""
        if not self.transactions:
            return None

        tx_hashes = [tx.tx_hash for tx in self.transactions]

        while len(tx_hashes) > 1:
            if len(tx_hashes) % 2 != 0:
                tx_hashes.append(tx_hashes[-1])  # Егер тақ болса, соңғыны қайталаймыз

            new_level = []
            for i in range(0, len(tx_hashes), 2):
                combined_hash = simple_hash(tx_hashes[i] + tx_hashes[i+1])
                new_level.append(combined_hash)

            tx_hashes = new_level

        return tx_hashes[0]  # Соңғы түбірді қайтарамыз
