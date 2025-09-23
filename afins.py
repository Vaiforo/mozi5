class Afins:
    def __init__(self):
        self.alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
        self.m = 32
        self.letter_to_index = {char: i for i,
                                char in enumerate(self.alphabet)}
        self.index_to_letter = {i: char for i,
                                char in enumerate(self.alphabet)}

    def nod(self, a: int, b: int) -> int:
        a, b = (a, b) if a > b else (b, a)

        while b != 1:
            if a % b == 0:
                return 0

            a, b = b, a % b

        return b

    def reciprocal(self, a: int, b: int) -> tuple[int, bool]:
        ...
