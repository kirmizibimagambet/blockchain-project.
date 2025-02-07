from hash_algorithm import simple_hash 

class MerkleTree:
    def __init__(self, transactions):
        self.transactions = transactions
        self.root = self.build_tree(transactions)

    def build_tree(self, transactions):
        if not transactions:
            return None

        if len(transactions) == 1:
            return simple_hash (transactions[0])

        new_level = []
        for i in range(0, len(transactions) - 1, 2):
            new_level.append(simple_hash (transactions[i] + transactions[i + 1]))

        if len(transactions) % 2 == 1:
            new_level.append(simple_hash (transactions[-1]))

        return self.build_tree(new_level)
