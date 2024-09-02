"""
Работа с датой и временем
Задание №3
Пользователь с клавиатуры вводит названия файлов, до тех пор, пока он не введет слово quit. После завершения ввода программа должна объединить содержимое всех перечисленных пользователем файлов в один.
"""

def merge_files_content():
    files_content = []

    while True:
        filename = input("Введите название файла (или 'quit' для завершения)\n(используй названия ag.txt, df.txt, sd.txt): ")

        if filename.lower() == "quit":
            break

        try:
            with open(filename, "r", encoding="utf-8") as file:
                files_content.append(file.read())
        except FileNotFoundError:
            print(f"Файл '{filename}' не найден.")
        except Exception as e:
            print(f"Ошибка при чтении файла '{filename}': {e}")

    if files_content:
        merged_content = "\n".join(files_content)
        return merged_content
    else:
        return None


def main():
    merged_content = merge_files_content()

    if merged_content:
        # Выводим объединенное содержимое на экран
        print("\nОбъединенное содержимое файлов:")
        print(merged_content)

        # Записываем объединенное содержимое в файл
        output_filename = "merged_output.txt"
        with open(output_filename, "w", encoding="utf-8") as outfile:
            outfile.write(merged_content)

        print(f"\nРезультат объединения сохранен в файл '{output_filename}'.")
    else:
        print("Не удалось объединить содержимое файлов.")


if __name__ == "__main__":
    main()
