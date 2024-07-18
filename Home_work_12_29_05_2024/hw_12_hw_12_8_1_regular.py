"""
Домашнее задание №8: Сортировка, поиск, регулярные выражения.
Регулярные выражения.
Задание №1
Напишите программу, в которой возвращаются домены из списка e-mail адресов.
"""

import re
from typing import List

def extract_domains(emails: List[str]) -> List[str]:
    """
    Функция извлекает домены из списка e-mail адресов.
    
    Args:
        emails (List[str]): Список e-mail адресов.
    
    Returns:
        List[str]: Список доменов.
    """
    domains = []
    for email in emails:
        match = re.search(r'@([a-zA-Z0-9.-]+)', email)
        if match:
            domains.append(match.group(1))
    return domains

if __name__ == "__main__":
    # Пример использования:
    email_list = [
        "user1@example.com",
        "user2@test.org",
        "user3@sub.domain.net",
        "user4@another-domain.com"
    ]
    
    result = extract_domains(email_list)
    print("Домены из списка e-mail адресов: ", result)

