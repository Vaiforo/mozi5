import math
from brut_rsa import Brut_RSA
from rsa import RSA
from tools import Tools


def main():
    e, n = 251, 61889
    C = "23824"

    tools = Tools()

    brut_rsa = Brut_RSA()

    factorization_results = []
    ckeys = []

    while True:
        tools.clean_cmd()

        print("-------|| Взлом RSA ||-------\n")
        print("   Главное меню")
        print("1. Факторизовать n")
        print("2. Подобрать ЗК")
        print("3. Расшифровать")
        print("4. Полный цикл")
        print("5. Выход")

        action = input('Выберите действие (введите цифру): ')

        if action == '1':
            tools.clean_cmd()

            print("-------|| Взлом RSA ||-------")
            print("       Факторизовать n\n")

            vvod = input(f"Введите n (по умолчанию {n}): ")
            input_n = int(vvod) if vvod else n

            print(f"[I] Начало факторизации n = {input_n}")
            divivers = brut_rsa.find_divivers(input_n)

            factorization_results = brut_rsa.get_factorization_results(
                divivers, input_n)
            print(
                f"[I] Факторизация завершена, найдено {len(factorization_results)} пар p и q")

            print(f"\nСписок возможных p и q для n = {input_n}:")
            for res in factorization_results:
                print(*res)

            input("Нажмите Enter для продолжения...")

        elif action == '2':
            tools.clean_cmd()

            print("-------|| Взлом RSA ||-------")
            print("        Подобрать ЗК\n")

            if not factorization_results:
                divivers = brut_rsa.find_divivers(n)

                factorization_results = brut_rsa.get_factorization_results(
                    divivers, n)

            vvod = input(f"Введите e (по умолчанию {e}): ")
            input_e = int(input_n) if vvod else e

            print(f"[I] Начало подбора закрытого ключа для e = {input_e}")

            ckeys = []
            for pq in factorization_results:
                d = brut_rsa.find_key(*pq, input_e)
                if d:
                    ckeys.append([d, math.prod(pq), *pq])

            print(
                f"[I] Подбор закрытых ключей завершён, найдено {len(ckeys)} возможны закрытых ключей")

            print(f"\nСписок возможных ЗК для e = {input_e:}")
            for ckey in ckeys:
                print(*ckey[:2])

            input("Нажмите Enter для продолжения...")

        elif action == '3':
            tools.clean_cmd()

            print("-------|| Взлом RSA ||-------")
            print("        Расшифровать\n")

            if not ckeys:
                divivers = brut_rsa.find_divivers(n)

                factorization_results = brut_rsa.get_factorization_results(
                    divivers, n)

                for pq in factorization_results:
                    d = brut_rsa.find_key(*pq, e)
                    if d:
                        ckeys.append([d, math.prod(pq), *pq])

            shifr = input(f"Введите зашифрованный текст (по умолчанию {C}): ")
            shifr = shifr if shifr else C

            print("Достпуные закрытые ключи:")
            for i, ckey in enumerate(ckeys):
                print(f"{i + 1}. {ckey[:2]}")
            ckey_id = input(
                "Введите номер желаемого закрытого ключа (по умолчанию 1): ")
            ckey = ckeys[int(ckey_id) - 1] if ckey_id else ckeys[0]

            rsa = RSA(*ckey[2:])

            text = rsa.deshifr(shifr, ckey[0])
            print(f"\nРасшифрованное сообщение: {text}")

            input("Нажмите Enter для продолжения...")

        elif action == '4':
            tools.clean_cmd()

            print("-------|| Взлом RSA ||-------")
            print("        Расшифровать\n")

            vvod = input(f"Введите n (по умолчанию {n}): ")
            input_n = int(vvod) if vvod else n

            print(f"[I] Начало факторизации n = {input_n}")
            divivers = brut_rsa.find_divivers(input_n)

            factorization_results = brut_rsa.get_factorization_results(
                divivers, input_n)
            print(
                f"[I] Факторизация завершена, найдено {len(factorization_results)} пар p и q")

            print(f"\nСписок возможных p и q для n = {input_n}:")
            for res in factorization_results:
                print(*res)

            vvod = input(f"\nВведите e (по умолчанию {e}): ")
            input_e = int(input_n) if vvod else e

            print(f"[I] Начало подбора закрытого ключа для e = {input_e}")

            ckeys = []
            for pq in factorization_results:
                d = brut_rsa.find_key(*pq, input_e)
                if d:
                    ckeys.append([d, math.prod(pq), *pq])

            print(
                f"[I] Подбор закрытых ключей завершён, найдено {len(ckeys)} возможны закрытых ключей")

            print(f"\nСписок возможных ЗК для e = {input_e:}")
            for ckey in ckeys:
                print(*ckey[:2])

            shifr = input(
                f"\nВведите зашифрованный текст (по умолчанию {C}): ")
            shifr = shifr if shifr else C

            print("Достпуные закрытые ключи:")
            for i, ckey in enumerate(ckeys):
                print(f"{i + 1}. {ckey[:2]}")
            ckey_id = input(
                "Введите номер желаемого закрытого ключа (по умолчанию 1): ")
            ckey = ckeys[int(ckey_id) - 1] if ckey_id else ckeys[0]

            rsa = RSA(*ckey[2:])

            text = rsa.deshifr(shifr, ckey[0])
            print(f"\nРасшифрованное сообщение: {text}")

            input("Нажмите Enter для продолжения...")

        elif action == '5' or action == '':
            print("\n[I] Завершение работы программы")
            break


if __name__ == "__main__":
    main()
