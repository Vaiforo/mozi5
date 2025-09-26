class Afins:
    def __init__(self):
        self.alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
        self.m = 32
        self.letter_to_index = {char: i for i,
                                char in enumerate(self.alphabet)}
        self.index_to_letter = {i: char for i,
                                char in enumerate(self.alphabet)}

    def cleaner(self, text: str) -> str:
        # text = text.lower().replace("ё", "е").replace("ъ", "ь").replace(" ", "_")
        text = text.lower().replace("ё", "е").replace(" ", "_")
        return "".join(char for char in text if char.isalpha() or char == "_")

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
            a %= self.m
            coef_old, coef_new, rem_old, rem_new = 0, 1, self.m, a
            while rem_new:
                q = rem_old // rem_new
                coef_old, coef_new = coef_new, coef_old - q * coef_new
                rem_old, rem_new = rem_new, rem_old - q * rem_new

            return coef_old % self.m
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
            if char == "_":
                continue
            if char in frequencies:
                frequencies[char] += 1
            else:
                frequencies[char] = 1

        for char in frequencies:
            frequencies[char] /= len(text.replace("_", ""))

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

        n = len(all_chars)
        if n < 2:
            return []

        cs = 4
        num_chunks = (n + cs - 1) // cs

        pairs = []

        for z in range(1, num_chunks + 1):
            i1 = min(cs * z, n)
            j0 = cs * (z - 1)
            j1 = min(cs * z, n)

            for i in range(i1):
                for j in range(j0, j1):
                    if i < j:
                        pairs.append((all_chars[i], all_chars[j]))
        return pairs

    def encrypt(self, text: str, a: int, b: int) -> str:
        text = self.cleaner(text)

        shifr = ''
        for x in text:
            if x == "_":
                shifr += "_"
                continue
            shifr += self.index_to_letter[(a *
                                           self.letter_to_index[x] + b) % self.m]
        return shifr

    def decrypt(self, shifr: str, a: int, b: int) -> str:
        text = ''
        for y in shifr:
            if y == "_":
                text += "_"
                continue
            text += self.index_to_letter[self.inv(a, self.m) *
                                         (self.letter_to_index[y] - b) % self.m]
        return text

    def brute_force(self, shifr: str) -> str:
        chars = self.analyze(shifr)
        pairs = self.give_pairs(chars)

        variants = {}

        e = self.letter_to_index['е']
        o = self.letter_to_index['о']

        for pair in pairs:
            let1 = self.letter_to_index[pair[0]]
            let2 = self.letter_to_index[pair[1]]

            for _ in range(2):
                solutions = self.solve_system(e, let1, o, let2, self.m)
                for solution in solutions:
                    text = self.decrypt(shifr, solution[0], solution[1])

                    if len(set(text)) == 1 and len(text) > 10:
                        continue

                    cnt_wrds = self.word_funder(text)
                    if cnt_wrds not in variants:
                        variants[cnt_wrds] = [[solution, text]]
                    else:
                        variants[cnt_wrds].append([solution, text])
                let1, let2 = let2, let1

        return variants
