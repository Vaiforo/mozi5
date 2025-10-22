import math


class Enthropi:
    def __init__(self):
        self.alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    def cleaner(self, text: str) -> str:
        return "".join(char for char in text.lower() if char in self.alphabet)

    def give_k_gramms(self, symbols: str, k: int) -> list:
        k_gramms = []
        len_symbols = len(symbols)
        for i in range(len_symbols - k + 1):
            k_gramms.append(symbols[i:i + k])
        return sorted(set(k_gramms))

    def k_gramms_generator(self, text: str, k_end: int, k_start: int = 1) -> dict[int: str]:
        text = self.cleaner(text)
        all_k_gramms = {}
        for k in range(k_start, k_end + 1):
            all_k_gramms[k] = self.give_k_gramms(text, k)
        return all_k_gramms

    def finder(self, text: str, gramm: str, k: int) -> int:
        count = 0
        for i in range(len(text) - k + 1):
            if gramm == text[i:i + k]:
                count += 1
        return count

    def get_frequencies(self, text: str, k_gramms: list, k: int) -> list:
        frequencies = {}
        for k_gramm in k_gramms:
            frequencies[k_gramm] = self.finder(text, k_gramm, k)
        all_count = sum(list(frequencies.values()))
        for k_gramm in k_gramms:
            frequencies[k_gramm] = frequencies[k_gramm] / all_count
        return list(frequencies.values())

    def analyze(self,  text: str, all_k_gramms: dict) -> dict:
        text = self.cleaner(text)
        all_frequencies = {}
        for k in all_k_gramms:
            k_gramms = all_k_gramms[k]
            all_frequencies[k] = self.get_frequencies(text, k_gramms, k)
        return all_frequencies

    def enthropi(self, frequencies: dict, k: int):
        HkT = 0
        for freq in frequencies:
            HkT += freq * math.log2(freq)
        return -HkT / k
