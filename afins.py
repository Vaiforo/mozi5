class Afins:
    def __init__(self):
        self.alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
        self.m = 32
        self.letter_to_index = {char: i for i,
                                char in enumerate(self.alphabet)}
        self.index_to_letter = {i: char for i,
                                char in enumerate(self.alphabet)}

    def cleaner(self, text: str) -> str:
        text = text.lower().replace("ё", "е")
        return "".join(char for char in text if char.isalpha())

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
            return pow(a % b, -1, b)
        return 0

    def solve_comparison(self, a: int, b: int, m: int) -> tuple[int, int]:
        a %= m
        b %= m

        if a == 0:
            if b == 0:
                return list(range(m))
            return []

        d = self.gcd(a, m)

        if b % d != 0:
            return []

        a //= d
        b //= d
        m_new = m // d

        inv = self.inv(a, m_new)
        x = b * inv % m_new
        solutions = [(x + k * m_new) % m for k in range(d)]
        return sorted(solutions)

    def solve_system(self, a: int, b: int, c: int, d: int, m: int) -> list[tuple[int, int]]:
        a %= m
        b %= m
        c %= m
        d %= m

        a0 = (a - c) % m
        b0 = (b - d) % m

        if a0 == 0:
            if b0 != 0:
                return []

            return [(x, (b - a * x) % m) for x in range(m)]

        x_c = self.solve_comparison(a0, b0, m)
        if not x_c:
            return []

        solutions = [(x, (b - a * x) % m) for x in x_c]
        return sorted(solutions)

    def analyze(self, text: str) -> dict[float: list[str]]:
        frequencies = {}
        for char in text:
            if char in frequencies:
                frequencies[char] += 1
            else:
                frequencies[char] = 1

        for char in frequencies:
            frequencies[char] /= len(text)

        chars = {}
        for char in frequencies:
            freq = frequencies[char]
            if freq not in chars:
                chars[freq] = [char]
            else:
                chars[freq].append(char)

        return chars
    
    def give_pairs(self, chars: dict) -> list[tuple[int, int]]:
        all_chars = []
        for freq in chars:
            all_chars += chars[freq]
        
        pairs = []
        for i in range(8):
            for j in range(3):
                ...