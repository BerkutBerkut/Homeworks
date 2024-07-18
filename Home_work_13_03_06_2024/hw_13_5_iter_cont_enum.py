"""
Домашнее задание №09: Итераторы, контейнеры и перечисления.
Выполните следующее задание:
На вход подается последовательность символов (символы могут быть любыми, в том 
числе и не буквенными, могут повторяться). Выведите все слова, которые можно составить из букв данной последовательности и их количество. 
Воспользуйтесь средствами модуля itertools.
"""


import itertools


def generate_words(sequence) -> list[str]:
    """
    Функция генерирует слова из букв входной последовательности.

    Args:
        sequence (str): Входная последовательность символов.

    Returns:
        List[str]: Список уникальных отсортированных слов.
    """
    # Извлекаем буквы из последовательности
    letters = [char for char in sequence if char.isalpha()]

    # Создаем множество для уникальных слов
    unique_words = set()

    # Генерируем все возможные комбинации букв и их перестановки
    for length in range(1, len(letters) + 1):
        for combination in itertools.combinations(letters, length):
            for permutation in itertools.permutations(combination):
                word = "".join(permutation)
                unique_words.add(word)

    # Преобразуем множество в отсортированный список 
    sorted_words = sorted(unique_words, key=lambda x: (len(x), x))

    return sorted_words


if __name__ == "__main__":
    input_sequence = input("Введите последовательность символов: ")
    words = generate_words(input_sequence)

    # Выводим количество слов
    print(len(words))

    # Выводим все слова
    for word in words:
        print(word)
