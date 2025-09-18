from cezar import CaesarCipher
import os


def main(fraze: str):
    os.system('cls' if os.name == 'nt' else 'clear')

    while True:
        print("---|| Шифр Цезаря ||---\n")
        action = input(
            "1. Шифрование\n2. Дешифрование\n3. Перебор\n4. Ответ\n5. Выход\n")
        if action == "1":
            cipher = CaesarCipher()
            text = input("Введите текст: ")
            key = int(input("Введите ключ: "))

            print("[I] Начало шифрования")
            shifr_text = cipher.shifrover(text, key)
            print("[I] Шифрование завершено")

            # print(shifr_text)
            with open("shifr-text.txt", "w", encoding="utf-8") as f:
                f.write(f"{key}\n")
                f.write(f"{shifr_text}\n")
            print("[I] Шифр текст сохранён в файл shifr-text.txt")

            input("Нажмите Enter для продолжения...")

        elif action == "2":
            cipher = CaesarCipher()
            text = input("Введите текст: ")
            open("deshifr-text.txt", "w").close()

            while True:
                key = int(input("Введите ключ: "))

                print("[I] Начало дешифрования")
                deshifr_text = cipher.shifrover(text, key, True)
                print("[I] Дешифрование завершено")

                # print(deshifr_text)
                with open("deshifr-text.txt", "a", encoding="utf-8") as f:
                    f.write(f"{key}\n")
                    f.write(f"{deshifr_text}\n")
                print("[I] Дешифрованный текст сохранён в файл deshifr-text.txt\n")

                text = input("Нажмите Enter для выхода или новый текст: ")
                if text == "":
                    break

        elif action == "3":
            cipher = CaesarCipher()
            results = cipher.brute_deshifrover(fraze)

            best_texts = {}
            for key in results:
                print(f"[I] key: {key}")
                print(f"[I] text: {results[key]}\n")
                count_of_words = cipher.word_funder(results[key])
                if count_of_words in best_texts:
                    best_texts[count_of_words].append([key, results[key]])
                else:
                    best_texts[count_of_words] = [[key, results[key]]]

            print("Самые вероятные расшифровки:")
            out_count = 0
            i = 0
            counts = sorted(best_texts.keys(), reverse=True)
            while i < 3:
                pairs = best_texts[counts[out_count]]
                i += len(pairs)
                out_count += 1
                for pair in pairs:
                    print(f"\nКлюч: {pair[0]}")
                    print(pair[1])

            input("Нажмите Enter для продолжения...")

        elif action == "4":
            cipher = CaesarCipher()

            print(f"Шифр-текст (ШТ): {fraze}")
            print("Расшифрованный текст (ОТ): всесчастливыесемьипохожидругнадругакаждаянесчастливаясемьянесчастливапосвоему")
            print("Ключ: 28")
            print("Автор и произведение (ОТ): Лев Николаевич Толстой «Анна Каренина»")

            shifr_text = cipher.shifrover("Лев Николаевич Толстой «Анна Каренина»", 28)
            print(f"Зашифрованные фамилия и название (ШТ): {shifr_text}")

            input("Нажмите Enter для продолжения...")

        elif action == "5" or action == "":
            break

        os.system('cls' if os.name == 'nt' else 'clear')

    print("[I] Программа завершила работу")


if __name__ == "__main__":
    fraze = "юнбнуьноздючбнбишдлксквдампяйьампяьжьваьыйбнуьноздюьынбишыйбнуьноздюьлкнюкбип"

    main(fraze)
