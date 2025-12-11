from tools import Tools


class DiscLog:
    def __init__(self, a: int, b: int, p: int):
        self.p = p
        self.a = a
        self.b = b % self.p

        self.tools = Tools()

    def compute_k(self) -> int:
        root = self.tools.int_sqrt(self.p)
        k = root
        if k * k < self.p:
            k += 1
        return k

    def build_sequences(self) -> tuple[int, list, list]:
        k = self.compute_k()

        y_values = []
        a_k = self.tools.bin_pow(self.a, k, self.p)
        cur_y = a_k
        for i in range(1, k + 1):
            y_values.append((i, cur_y))
            cur_y = (cur_y * a_k) % self.p

        z_values = []
        cur_a = 1
        for j in range(1, k + 1):
            cur_a = (cur_a * self.a) % self.p
            value = (self.b * cur_a) % self.p
            z_values.append((j, value))
        return k, y_values, z_values

    def solve(self) -> tuple[int, int, int, int, int]:
        k, y_values, z_values = self.build_sequences()

        table = {}
        for i, value in y_values:
            if value not in table:
                table[value] = i

        for j, value in z_values:
            if value in table:
                i = table[value]
                x_mod = (i * k - j) % (self.p - 1)

                if self.check_x(x_mod):
                    return x_mod, k, i, j, value

        return None, k, None, None, None

    def check_x(self, x: int) -> bool:
        return self.tools.bin_pow(self.a, x, self.p) == (self.b % self.p)
