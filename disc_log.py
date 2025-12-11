from tools import Tools

class DiscLog:
    def __init__(self, a: int, b: int, p: int):
        self.a = a
        self.b = b
        self.p = p

        self.tools = Tools()

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

    def compute_k(self) -> int:

        root = self.int_sqrt(self.p)
        k = root
        if k * k < self.p:
            k += 1
        return k

    def build_sequences(self):

        k = self.compute_k()
        p = self.p
        a = self.a
        b = self.b % p

        y_values = []
        a_k = self.tools.bin_pow(a, k, p)
        cur_y = a_k
        for i in range(1, k + 1):
            y_values.append((i, cur_y))
            cur_y = (cur_y * a_k) % p

        z_values = []
        cur_a = 1
        for j in range(1, k + 1):
            cur_a = (cur_a * a) % p
            value = (b * cur_a) % p
            z_values.append((j, value))

        return k, y_values, z_values

    def solve(self):
        k, y_values, z_values = self.build_sequences()

        table = {}
        for i, value in y_values:
            if value not in table:
                table[value] = i

        for j, value in z_values:
            if value in table:
                i = table[value]
                x_raw = i * k - j
                x_mod = x_raw % (self.p - 1)

                if self.check_x(x_mod):
                    return x_mod, k, i, j, value

        return None, k, None, None, None

    def check_x(self, x: int) -> bool:
        return self.tools.bin_pow(self.a, x, self.p) == (self.b % self.p)
