import os
from rsa import RSA


def main():
    rsa = RSA()

    eds = rsa.get_ed(3)
    print(eds)
    for ed in eds:
        print(ed[0] * ed[1] % rsa.phi_n)


if __name__ == "__main__":
    main()
