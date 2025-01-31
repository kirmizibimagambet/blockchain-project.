def simple_hash(data):
    hash_value = 0
    for char in data:
        hash_value += ord(char)
        hash_value *= 31  # Простое умножение
        hash_value %= 1000000  # Ограничение диапазона

    return f"{hash_value:06d}"  # Всегда 6 знаков, дополняем нулями


if __name__ == "__main__":
    print("Хэш:", simple_hash("54"))
    print("Хэш:", simple_hash("Block"))