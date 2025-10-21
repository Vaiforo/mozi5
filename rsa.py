class RSA:
    def __init__(self):
        self.alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
        self.letter_to_index = {char: i for i,
                                char in enumerate(self.alphabet, start=10)}
        self.letter_to_index[" "] = 99
        self.index_to_letter = {i: char for i,
                                char in enumerate(self.alphabet, start=10)}
        self.index_to_letter[99] = " "

        self.p, self.q = 179, 317
        self.n = self.q * self.p
        self.phi_n = (self.q - 1) * (self.p - 1)

    def cleaner(self, text: str) -> str:
        text = text.lower().replace("ё", "е")
        return "".join(char for char in text if char.isalpha() or char == " " and char in self.alphabet)

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

    def shifr_to_M(self, text: str) -> str:
        M = ""
        text = self.cleaner(text)
        for char in text:
            M += str(self.letter_to_index[char])
        return M

    def deshifr_from_M(self, M: str) -> str:
        text = ""
        for index in range(0, len(M), 2):
            text += self.index_to_letter[int(M[index:index + 2])]
        return text

    def blocking(self, M: str) -> list:
        blocks = []
        block = M[0]
        for char in M[1:]:
            if int(block + char) < self.n:
                block += char
            else:
                blocks.append(block)
                block = char
        blocks.append(block)
        return blocks

    def get_ed(self, e_start: int, count_need: int) -> list:
        if e_start < 2:
            e_start = 3

        ed_pairs = []
        pairs_count = 0
        for e in range(e_start, self.phi_n):
            d = self.inv(e, self.phi_n)
            if d:
                ed_pairs.append([e, d])
                pairs_count += 1
            if pairs_count == count_need:
                break
        return ed_pairs

    def solve_CM(self, blocks: list, exponent: int) -> list:
        solved_blocks = []
        for block in blocks:
            solved_blocks.append(str(int(block) ** exponent % self.n))
        return solved_blocks

    def shifr(self, text: str, e: int) -> str:
        M = self.shifr_to_M(text)
        blocks = self.blocking(M)
        return "".join(self.solve_CM(blocks, e))
    
    def deshifr(self, shifr: str, d: int) -> str:
        blocks = self.blocking(shifr)
        M = self.solve_CM(blocks, d)
        # return "".join(self.)