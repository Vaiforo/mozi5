import os
from rsa import RSA


def main():
    rsa = RSA()

    print(rsa.blocking('121027419922242124141532', 22213))


if __name__ == "__main__":
    main()
