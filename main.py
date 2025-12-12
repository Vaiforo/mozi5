import os
from fact import Factorization
from tools import Tools


def main():
    m = 562013

    factor = Factorization(m)
    tools = Tools()

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        print("-------|| Методы факторизации числа ||-------\n")
        print("   Главное меню")
        print("1. Факторизация методом квадратичного решета")
        print("2. Факторизация ρ-методом Полларда")
        print("3. Выход\n")

        action = input("Выберите действие: ").strip()

        if action == "1":
            tools.clean_cmd()

            print("-------|| Методы факторизации числа ||-------\n")
            print("  Факторизация методом квадратичного решета\n")

            print("Введите модули решёт a, b, c")
            a, b, c = map(int, input("a b c: ").split())

            result = factor.quadratic_sieve(a, b, c)

            if not result:
                print(
                    "\n[E] Не удалось найти делители методом квадратичного решета")
            else:
                p, q, x, y = result
                print("\n[I] Факторизация выполнена")
                print(f"Найдены делители: p = {p}, q = {q}, p * q = {p * q}")
                print(f"x = {x}, y = {y}")
                print(f"x^2 - m = {x * x - m} = y^2 = {y * y}")

            input("\nНажмите Enter для продолжения...")

        elif action == "2":
            tools.clean_cmd()

            print("-------|| Методы факторизации числа ||-------\n")
            print("       Факторизация ρ-методом Полларда\n")

            print("\n[I] ρ-метод Полларда: f(x) = x^2 + 1 (mod m)")
            print("Введите начальные члены последовательностей x0^(1) и x0^(2)")
            print("Обычно берут одинаковые небольшие числа, например 2 и 2\n")

            x1 = int(input("x0^(1): "))
            x2 = int(input("x0^(2): "))

            result = factor.rho_pollard(x1, x2)

            if result is None:
                print("\n[E] За разумное число шагов делитель не найден")
                print("Попробуйте другие начальные значения x0^(1), x0^(2)")
            else:
                p, q, steps, last_x1, last_x2, last_a, last_d = result
                print("\n[I] Факторизация выполнена ρ-методом Полларда")
                print(f"Найдены делители: p = {p}, q = {q}, p * q = {p * q}")
                print(f"\nДелитель d_n = {last_d} найден на шаге n = {steps}")
                print("\nПоследнее состояние последовательностей:")
                print(f"x_n^(1) = {last_x1}")
                print(f"x_n^(2) = {last_x2}")
                print(f"a_n = |x_n^(2) - x_n^(1)| = {last_a}")

            input("\nНажмите Enter для продолжения...")

        elif action == "3" or action == "":
            print("\n[I] Завершение работы программы")
            break


if __name__ == "__main__":
    main()
