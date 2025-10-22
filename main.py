import os
from enthropi import Enthropi
import matplotlib.pyplot as plt


def main():
    fraze = ''.join([
        "Несчастная кошка порезала лапу – Сидит, и ни шагу не может сту",
        "пить. Скорей, чтобы вылечить кошкину лапу Воздушные шарики надо",
        " купить! И сразу столпился народ на дороге – Шумит, и кричит, и на",
        " кошку глядит. А кошка отчасти идет по дороге, Отчасти по воздуху",
        " плавно летит!"
    ])
    k = 5

    enthropi = Enthropi()

    hktks = []

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        print("-------|| Модель открытого текста ||-------\n")
        print("   Главное меню")
        print("1. Рассчитаь Hk(T)/k")
        print("2. Построить график")
        print("3. Выход")

        action = input('Выберите действие (введите цифру): ')

        if action == '1':
            os.system('cls' if os.name == 'nt' else 'clear')

            print("-------|| Модель открытого текста ||-------")
            print("             Рассчитаь Hk(T)/k\n")

            print(f"[I] Поиск всех k-грамм от 1 до {k}")
            all_k_gramms = enthropi.k_gramms_generator(fraze, k)
            print("[I] Все k-граммы найдены")

            print("[I] Расчёт частот")
            all_frequencies = enthropi.analyze(fraze, all_k_gramms)
            print("[I] Частоты найдены")

            print(f"[I] Расчёт Hk(T)/k от 1 до {k}")
            hktks.clear()
            for k in all_frequencies:
                frequencies = all_frequencies[k]
                hktks.append(enthropi.enthropi(frequencies, k))
            print("[I] Расчёт завершён\n")

            print("Hk(T)/k при:")
            for k in range(len(hktks)):
                print(f"k = {k + 1}: {hktks[k]}")

            input("\nНажмите Enter для продолжения...")

        elif action == '2':
            os.system('cls' if os.name == 'nt' else 'clear')

            print("-------|| Модель открытого текста ||-------")
            print("             Построить график\n")

            plt.plot(range(1, k + 1), hktks, marker='o')
            plt.title("Зависимость Hk(T)/k от k")
            plt.xlabel("k")
            plt.ylabel("Hk(T)/k")
            plt.grid(True)
            plt.show()

            input("Нажмите Enter для продолжения...")

        elif action == '8' or action == "":
            print("\n[I] Завершение работы программы")
            break


if __name__ == "__main__":
    main()
