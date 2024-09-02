"""
Работа с датой и временем
Задание №4
Пользователь с клавиатуры вводит названия файлов, до тех пор, пока он не введет слово quit. После завершения ввода программа должна записать в итоговый файл символы, которые есть во всех перечисленных файлах (символы должны быть в каждом файле)
"""


def find_common_characters(filenames):
    if not filenames:
        return set()

    common_chars = set()
    first_file = True

    for filename in filenames:
        try:
            with open(filename, "r", encoding="utf-8") as file:
                file_content = set(file.read())

                if first_file:
                    common_chars = file_content
                    first_file = False
                else:
                    common_chars = common_chars.intersection(file_content)

                if not common_chars:
                    break  # Если нет общих символов, дальнейший поиск не имеет смысла
        except FileNotFoundError:
            print(f"Файл '{filename}' не найден.")
        except Exception as e:
            print(f"Ошибка при чтении файла '{filename}': {e}")

    return common_chars


def main():
    filenames = []

    while True:
        filename = input("Введите название файла (или 'quit' для завершения)\n(используй названия ag.txt, df.txt, sd.txt): ")

        if filename.lower() == "quit":
            break

        filenames.append(filename)

    common_chars = find_common_characters(filenames)

    if common_chars:
        # Записываем общие символы в файл
        output_filename = "common_characters.txt"
        with open(output_filename, "w", encoding="utf-8") as outfile:
            outfile.write("".join(common_chars))

        print(f"Общие символы успешно записаны в файл '{output_filename}'.")
    else:
        print("В указанных файлах нет общих символов или файлы не были найдены.")


if __name__ == "__main__":
    main()
