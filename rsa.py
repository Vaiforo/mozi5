class RSA:
    def __init__(self):
        self.alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
        self.p, self.q = 179, 317
        self.letter_to_index = {char: i for i,
                                char in enumerate(self.alphabet, start=10)}
        self.letter_to_index[" "] = 99
        self.index_to_letter = {i: char for i,
                                char in enumerate(self.alphabet, start=10)}
        self.index_to_letter[99] = " "

    def cleaner(self, text: str) -> str:
        text = text.lower().replace("ё", "е")
        return "".join(char for char in text if char.isalpha() or char == " " and char in self.alphabet)

    def shifr(self, text: str) -> str:
        M = ""
        text = self.cleaner(text)
        for char in text:
            M += str(self.letter_to_index[char])
        return M

    def deshifr(self, M: str) -> str:
        text = ""
        for index in range(0, len(M), 2):
            text += self.index_to_letter[int(M[index:index + 2])]
        return text

    def blocking(self, M: str, n: int) -> list:
        blocks = []
        block = M[0]
        for char in M[1:]:
            if int(block + char) < n:
                block += char
            else:
                blocks.append(block)
                block = char
        blocks.append(block)
        return blocks
