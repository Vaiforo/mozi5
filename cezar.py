import re


class CezarShipher:
    def __init__(self):
        self.alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
        self.m = len(self.alphabet)
        self.letter_of_index = {char: i for i,
                                char in enumerate(self.alphabet)}
        self.index_of_letter = {i: char for i,
                                char in enumerate(self.alphabet)}
        self.rus_letters = re.compile(r"[а-я]", re.IGNORECASE)

    def cleaner(self, text: str) -> str:
        text = text.lower().replace("ё", "е")
        # return "".join(char for char in text if char.isalpha())
        return text

    def shifr_char(self, char: str, k: int, deshifr: bool = False) -> str:
        if not self.rus_letters.match(char):
            return char

        idx = self.letter_of_index[char]
        if deshifr:
            new_idx = (idx - k) % self.m
        else:
            new_idx = (idx + k) % self.m

        return self.index_of_letter[new_idx]

    def shifrover(self, text: str, k: int, deshifr: bool = False) -> str:
        if not deshifr:
            text = self.cleaner(text)
        return "".join(self.shifr_char(ch, k, deshifr=deshifr) for ch in text)

    def brute_deshifrover(self, text: str):
        results = {}
        for k in range(1, self.m):
            results[k] = self.shifrover(text, k, True)
        return results

    def word_funder(self, text: str):
        mini_words = {
            "а", "и", "но", "что", "кто", "как", "это", "не", "он", "она", "оно", "мы", "вы", "они", "судьи", "тот", "есть",
            "да", "ли", "бы", "же", "вы", "ты", "у", "по", "на", "от", "за", "для", "о", "в", "к", "из", "так", "вот", "там", "раз"
        }

        count = 0
        for word in mini_words:
            if word in text:
                count += 1
        return count
