from tools import Tools


class Factorization:
    def __init__(self, m: int):
        self.m = m
        self.tools = Tools()

    def int_sqrt(self, n: int) -> int:
        if n < 0:
            raise ValueError("Квадратный корень определён только для n >= 0")

        if n in (0, 1):
            return n

        x = n
        y = (x + 1) // 2
        while y < x:
            x = y
            y = (x + n // x) // 2
        return x

    def is_perfect_square(self, n: int) -> bool:
        if n < 0:
            return False
        r = self.int_sqrt(n)
        return r * r == n

    def prepare_sieve_for_mod(self, mod: int) -> list:
        m = self.m
        residues = [False] * mod

        for x in range(mod):
            residues[(x * x) % mod] = True

        sieve = [False] * mod
        for x in range(mod):
            z = (x * x - m) % mod
            sieve[x] = residues[z]

        return sieve

    def quadratic_sieve(self, a: int, b: int, c: int):
        m = self.m
        mods = [a, b, c]

        sieves = {}
        for mod in mods:
            sieves[mod] = self.prepare_sieve_for_mod(mod)

        x_start = self.int_sqrt(m) + 1
        x_end = (m + 1) // 2

        for x in range(x_start, x_end + 1):
            ok = True
            for mod in mods:
                sieve = sieves[mod]
                idx = x % mod
                if not sieve[idx]:
                    ok = False
                    break

            if not ok:
                continue

            z = x * x - m
            if z <= 0:
                continue

            if not self.is_perfect_square(z):
                continue

            y = self.int_sqrt(z)
            p = x + y
            q = x - y

            if p <= 1 or q <= 1:
                continue
            if p * q != m:
                continue

            if p > q:
                p, q = q, p
            return p, q, x, y
        return None

    def rho_pollard(self, x1: int, x2: int, max_steps: int = 10**6):
        m = self.m

        x_slow = x1 % m
        x_fast = x2 % m

        for step in range(1, max_steps + 1):
            x_slow = (x_slow * x_slow + 1) % m

            x_fast = (x_fast * x_fast + 1) % m
            x_fast = (x_fast * x_fast + 1) % m

            a_n = abs(x_fast - x_slow) % m

            d_n = self.tools.gcd(a_n, m)

            if 1 < d_n < m:
                p = d_n
                q = m // d_n
                if p > q:
                    p, q = q, p
                return p, q, step, x_slow, x_fast, a_n, d_n

            if d_n == m:
                return None
        return None
