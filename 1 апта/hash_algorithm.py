def simple_hash(data):
    hash_value = 0
    for char in data:
        hash_value += ord(char)
        hash_value *= 31  # Бір қарапайым көбейту
        hash_value %= 1000000  # Шектеулі диапазон
    return hash_value

if __name__ == "__main__":
    print("Хэш:", simple_hash("Block Data"))
