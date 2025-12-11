import os


class Tools:
    def __init__(self):
        self.alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"

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

    def gcd(self, a: int, b: int) -> tuple:
        a, b = (a, b) if a > b else (b, a)

        if b == 0:
            return 0

        while b != 1:
            if a % b == 0:
                return b

            a, b = b, a % b

        return b

    def inv(self, a: int, b: int) -> int:
        if self.gcd(a, b) == 1:
            a %= b
            coef_old, coef_new, rem_old, rem_new = 0, 1, b, a
            while rem_new:
                q = rem_old // rem_new
                coef_old, coef_new = coef_new, coef_old - q * coef_new
                rem_old, rem_new = rem_new, rem_old - q * rem_new

            return coef_old % b
        return 0

    def bin_pow(self, base: int, exponent: int, mod: int) -> int:
        result = 1
        base %= mod
        while exponent > 0:
            if exponent % 2 == 1:
                result = (result * base) % mod
            base = (base * base) % mod
            exponent //= 2
        return result

    def int_sqrt(self, n: int) -> int:
        if n < 0:
            raise ValueError("n должно быть неотрицательным")
        if n < 2:
            return n

        x = n // 2
        while True:
            y = (x + n // x) // 2
            if y >= x:
                return x
            x = y

    def cleaner(self, text: str, replace_e: bool = True, replace_b: bool = True, replace_: bool = False, rem_: bool = True) -> str:
        text = text.lower()
        space = ""
        if replace_e:
            text = text.replace("ё", "е")
        if replace_b:
            text = text.replace("ъ", "ь")
        if replace_:
            text = text.replace(" ", "_")
            space = "_"
        if rem_:
            text = text.replace(" ", "")
        return "".join(char for char in text if char in self.alphabet or char == space)

    def clean_cmd(self):
        os.system('cls' if os.name == 'nt' else 'clear')
