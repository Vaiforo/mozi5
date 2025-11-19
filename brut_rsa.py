class Brut_RSA:
    def __init__(self):
        ...

    def check_simple(self, num: int) -> bool:
        for diviver in range(2, int(num ** 0.5) + 1):
            if num % diviver == 0:
                return False
        return True

    def find_divivers(self, num: int) -> list:
        divivers = []