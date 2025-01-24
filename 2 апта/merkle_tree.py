import hashlib

def hash(data):
    """Берілген деректердің SHA-256 хэшін қайтарады."""
    return hashlib.sha256(data.encode()).hexdigest()

def merkle_root(transactions):
    """Меркле түбірін есептейді."""
    if not transactions:  # Егер транзакциялар тізімі бос болса
        return hash("0")
    if len(transactions) == 1:  # Егер тек бір ғана элемент болса
        return transactions[0]

    # Жаңа деңгей құру
    new_level = []
    for i in range(0, len(transactions), 2):
        left = transactions[i]
        right = transactions[i + 1] if i + 1 < len(transactions) else transactions[i]
        combined_hash = hash(left + right)
        new_level.append(combined_hash)

    return merkle_root(new_level)
