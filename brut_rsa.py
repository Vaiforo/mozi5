from tools import Tools


class Brut_RSA:
    def __init__(self):
        self.tools = Tools()

    def check_simple(self, num: int) -> bool:
        for diviver in range(2, int(num ** 0.5) + 1):
            if num % diviver == 0:
                return False
        return True

    def find_divivers(self, n: int) -> list:
        divivers = []
        for diviver in range(2, int(n ** 0.5) + 1):
            if n % diviver == 0 and self.check_simple(diviver) and self.check_simple(n // diviver):
                divivers.append(diviver)
        return divivers

    def get_factorization_results(self, divivers: list, n: int) -> list:
        return [[diviver, n // diviver] for diviver in divivers]

    def find_key(self, p: int, q: int, e: int):
        return self.tools.inv(e, (p - 1) * (q - 1))
