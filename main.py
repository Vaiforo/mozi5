from tools import Tools
from disc_log import DiscLog


def main():
    a = 5
    b = 16190
    p = 30803

    tools = Tools()
    disc = DiscLog(a, b, p)

    while True:
        tools.clean_cmd()

        print("-------|| Дискретный логарифм ||-------\n")
        print("   Главное меню")
        print("1. Найти k")
        print("2. Найти y_n и z_n")
        print("3. Найти дискретный логарифм x")
        print("4. Выход")

        action = input('Выберите действие (введите цифру): ')

        if action == '1':
            tools.clean_cmd()

            print("-------|| Дискретный логарифм ||-------")
            print("                Найти k")

            k = disc.compute_k()
            print(f"a = {a}")
            print(f"b = {b}")
            print(f"p = {p}")
            print(f"k = [sqrt(p)] + 1 = {k}")

            input("\nНажмите Enter для продолжения...")

        elif action == '2':
            tools.clean_cmd()

            print("-------|| Дискретный логарифм ||-------")
            print("            Найти y_n и z_n")

            k, y_values, z_values = disc.build_sequences()
            print(f"k = {k}")

            limit_raw = input(
                "Сколько первых элементов показать (по умолчанию 10): ")
            limit = int(limit_raw) if limit_raw else 10

            limit = max(1, min(limit, k))

            print("\nПоследовательность y_n = a^(n * k) (mod p):")
            for i, value in y_values[:limit]:
                print(f"y_{i} = {value}")

            print("\nПоследовательность z_n = b * a^n (mod p):")
            for j, value in z_values[:limit]:
                print(f"z_{j} = {value}")

            input("\nНажмите Enter для продолжения...")

        elif action == '3':
            tools.clean_cmd()

            print("-------|| Дискретный логарифм ||-------")
            print("      Найти дискретный логарифм x")

            x, k, i, j, val = disc.solve()

            if x is None:
                print("[E] Не удалось найти решение: совпадения элементов не найдено")
            else:
                print("[I] Найдено решение:")
                print(f"k = {k}")
                print(f"Совпадение: y_{i} = z_{j} = {val}")
                print(f"x = i * k - j (mod p-1) = {x}")
                print(f"Проверка: a^x mod p = {tools.bin_pow(a, x, p)}")

            input("\nНажмите Enter для продолжения...")

        elif action == '4' or action == '':
            print("\n[I] Завершение работы программы")
            break


if __name__ == "__main__":
    main()
