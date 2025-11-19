import os
from rsa import RSA


def main():
    p, q = 179, 317

    keys = []
    rsa = RSA(p, q)
    n = p * q

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        print("-------|| Алгоритм RSA ||-------\n")
        print("   Главное меню")
        print("1. Сгенерировать ключи")
        print("2. Зашировать")
        print("3. Расшифровать")
        print("4. Полный цикл")
        print("5. Выход")

        action = input('Выберите действие (введите цифру): ')

        if action == '1':
            os.system('cls' if os.name == 'nt' else 'clear')

            print("-------|| Алгоритм RSA ||-------")
            print("      Сгенерировать ключи\n")

            count = input("Введите желаемое кол-во ключей (по умолчанию 3): ")
            count = int(count) if count else 3
            e_start = input(
                "Введите начальное число e для подбора пар (по умолчанию 3): ")
            e_start = int(e_start) if e_start else 3

            print(f"[I] Начата генерация {count} ключей")
            keys = rsa.get_ed(e_start, count)
            print(f"[I] Генерация {count} ключей успешно завершена")

            print("\nПолученные ключи:")
            for i, key in enumerate(keys):
                print(
                    f"{i + 1}) (e, n): ({key[0]}, {n}) | (d, n): ({key[1]}, {n})")

            input("Нажмите Enter для продолжения...")

        elif action == '2':
            os.system('cls' if os.name == 'nt' else 'clear')

            print("-------|| Алгоритм RSA ||-------")
            print("           Зашировать\n")

            if not keys:
                keys = rsa.get_ed(3, 3)

            text = input("Введите текст для зашифровки: ")

            print("\nИмеющиеся ключи:")
            for i, key in enumerate(keys):
                print(
                    f"{i + 1}) (e, n): ({key[0]}, {n}) | (d, n): ({key[1]}, {n})")
            key = int(input("Введите номер нужного ключа: "))

            print("[I] Начало зашифровки")
            shifr = rsa.shifr(text, keys[key - 1][0])
            print("[I] Шифрование завершено")

            print(f"\nПолученный шифр:\n{" ".join(shifr)}")

            input("Нажмите Enter для продолжения...")

        elif action == '3':
            os.system('cls' if os.name == 'nt' else 'clear')

            print("-------|| Алгоритм RSA ||-------")
            print("          Расшифровать\n")

            if not keys:
                keys = rsa.get_ed(3, 3)

            shifr = input("Введите шифр для расшифровки: ").replace(" ", "")

            print("\nИмеющиеся ключи:")
            for i, key in enumerate(keys):
                print(
                    f"{i + 1}) (e, n): ({key[0]}, {n}) | (d, n): ({key[1]}, {n})")
            key = int(input("Введите номер нужного ключа: "))

            print("[I] Начало расшифровки")
            try:
                text = rsa.deshifr(shifr, keys[key - 1][1])
                print("[I] Расшифровка завершена")

                print(f"\nПолученный текст:\n{text}")
            except:
                print("[E] Неподходящий ключ")

            input("Нажмите Enter для продолжения...")

        elif action == '4':
            os.system('cls' if os.name == 'nt' else 'clear')

            print("-------|| Алгоритм RSA ||-------")
            print("          Полный цикл\n")

            if not keys:
                keys = rsa.get_ed(3, 3)

            text = input("Введите текст для зашифровки: ")

            print("\nИмеющиеся ключи:")
            for i, key in enumerate(keys):
                print(
                    f"{i + 1}) (e, n): ({key[0]}, {n}) | (d, n): ({key[1]}, {n})")
            key = int(input("Введите номер нужного ключа: "))

            print("[I] Начало зашифровки")
            shifr = rsa.shifr(text, keys[key - 1][0])
            print("[I] Шифрование завершено")

            print(f"\nПолученный шифр:\n{" ".join(shifr)}")

            print("[I] Начало расшифровки")
            text = rsa.deshifr(shifr, keys[key - 1][1])
            print("[I] Расшифровка завершена")

            print(f"\nПолученный текст:\n{text}")

            input("Нажмите Enter для продолжения...")

        elif action == '5' or action == '':
            print("\n[I] Завершение работы программы")
            break


if __name__ == "__main__":
    main()
