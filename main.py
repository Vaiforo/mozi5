import os
from afins import Afins


def main():
    fraze = ''.join(["пгсаистшгшэюыабтюфюцьцчзсгшдэсдшнвэнчгстзрюь",
                     "апзскмзстшщгчадэсныскщювэсепкнюенсввачнпаьвн",
                     "стсгшпыпасвэлемчгяпымзпфрнчанюаюцлбтсщпбсышф",
                     "чтшглмсвашяцчстпгрцювэзчячвлцюэзютшьнюцйчонч",
                     "ашпеаюнюэшмзпюыапзчнцсгшяцспцюсвмсзпнчкиашмйч"])
    afins = Afins()

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        print("-------|| Афинный шифр ||-------\n")
        print("   Главное меню")
        print("1. Получить обратный элемент")
        print("2. Решить сравнение")
        print("3. Решить систему")
        print("4. Выполнить анализ")
        print("5. Зашифровать")
        print("6. Расшифровать")
        print("7. Взломать")
        print("8. Выход")

        action = input('Выберите действие (введите цифру): ')

        if action == '1':
            os.system('cls' if os.name == 'nt' else 'clear')

            print("-------|| Афинный шифр ||-------")
            print("   Получить обратный элемент\n")

            a = int(input("Введите элемент: "))
            b = int(input("Введите модуль: "))

            print("[I] Получение обратного элемента")
            inv = afins.inv(a, b)
            if inv:
                print("[I] Обратный элемент получен\n")

                print(f"Элмент обратный данному: {inv}")
            else:
                print("[E] Введённый элемент необратим в данном кольце")

            input("Нажмите Enter для продолжения...")

        elif action == '2':
            os.system('cls' if os.name == 'nt' else 'clear')

            print("-------|| Афинный шифр ||-------")
            print("        Решить сравнение\n")

            print("Сравнение вида <ax mod m == b>")
            a = int(input("Введите a: "))
            b = int(input("Введите b: "))
            m = int(input("Введите m: "))

            print(f"[I] Решение сравнения <{a}x mod {m} == {b}>")
            solutions = afins.solve_comparison(a, b, m)
            if solutions:
                print("[I] Сравнение решено")
                print(f"[I] Найдено {len(solutions)} решений\n")

                for i, solution in enumerate(solutions, 1):
                    print(f"Решение {i}: {solution}")
            else:
                print("[E] Не найдено решений")

            input("Нажмите Enter для продолжения...")

        elif action == '3':
            os.system('cls' if os.name == 'nt' else 'clear')

            print("-------|| Афинный шифр ||-------")
            print("         Решить систему\n")

            print("Система вида:")
            print("(ax + y) mod m == b")
            print("(cx + y) mod m == d")
            a = int(input("Введите a: "))
            b = int(input("Введите b: "))
            c = int(input("Введите c: "))
            d = int(input("Введите d: "))
            m = int(input("Введите m: "))

            print(
                f"[I] Решение системы <{a}x mod {m} == {b}> <{c}x mod {m} == {d}>")
            solutions = afins.solve_system(a, b, c, d, m)
            if solutions:
                print("[I] Система решена")
                print(f"[I] Найдено {len(solutions)} решений\n")

                for i, solution in enumerate(solutions, 1):
                    print(f"Решение {i}: x = {solution[0]} y = {solution[1]}")
            else:
                print("[E] Не найдено решений")

            input("Нажмите Enter для продолжения...")

        elif action == '4':
            os.system('cls' if os.name == 'nt' else 'clear')

            print("-------|| Афинный шифр ||-------")
            print("        Выполнить анализ\n")

            shifr = input(
                "Введите фразу для анализа (Enter для использования заготовленной):\n")
            shifr = fraze if not shifr else shifr

            print("[I] Анализ фразы")
            chars = afins.analyze(shifr)
            print("[I] Анализ завершён\n")

            print("Таблица частот:")
            for freq in chars:
                for char in chars[freq]:
                    print(f"{char}: {freq}", end=' | ')
                print()

            pairs = afins.give_pairs(chars)
            print(f"\nПара наиболее часто встречающихся букв: {pairs[0]}")

            input("Нажмите Enter для продолжения...")

        elif action == '5':
            os.system('cls' if os.name == 'nt' else 'clear')

            print("-------|| Афинный шифр ||-------")
            print("          Зашифровать\n")

            shifr = input("Введите фразу для шифрования: ")
            a = int(input("Введите a: "))
            b = int(input("Введите b: "))

            print("[I] Начало шифрования")
            text = afins.encrypt(shifr, a, b)
            print("[I] Шифрование завершено\n")

            print(f"ШТ: {text}")

            input("Нажмите Enter для продолжения...")

        elif action == '6':
            os.system('cls' if os.name == 'nt' else 'clear')

            print("-------|| Афинный шифр ||-------")
            print("          Расшифровать\n")

            shifr = input("Введите фразу для расшифровки: ")
            a = int(input("Введите a: "))
            b = int(input("Введите b: "))

            print("[I] Начало расшифровки")
            text = afins.decrypt(shifr, a, b)
            print("[I] Расшифровка завершена\n")

            print(f"ОТ: {text}")

            input("Нажмите Enter для продолжения...")

        elif action == '7':
            os.system('cls' if os.name == 'nt' else 'clear')

            print("-------|| Афинный шифр ||-------")
            print("            Взломать\n")

            print("[I] Начало взлома")
            variants = afins.brute_force(fraze)
            print("[I] Взлом завершен\n")

            print(f"Наиболее вероятная расшифровка(-ки):")
            keys = sorted(variants.keys(), reverse=True)

            with open("variants.txt", "w", encoding="utf8") as file:
                for key in keys:
                    for variant in variants[key]:
                        file.write(f"Ключ: {variant[0]}\n")
                        file.write(f"ОТ: {variant[1]}\n")

            for key in keys[:1]:
                for variant in variants[key]:
                    print(f"Ключ: {variant[0]}")
                    print(f"ОТ: {variant[1]}\n")

            input("Нажмите Enter для продолжения...")

        elif action == '8' or action == "":
            print("\n[I] Завершение работы программы")
            break


if __name__ == "__main__":
    main()
