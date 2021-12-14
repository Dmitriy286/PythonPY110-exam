"""
Программа возвращает список книг
"""

import random
import json

from faker import Faker

from conf import MODEL


def title() -> str:
    """
    Эта функция возвращает название книги из файла books.txt
    :return:
    """

    file = "books.txt"
    with open(file, "r", encoding="UTF-8") as f:
        d = random.randint(0, 4)
        return f[d].rstrip()


def year_func(first_year: int = 1450, second_year: int = 2021) -> int:
    """
    Function...
    :param first_year:
    :param second_year:
    :return:
    """

    return random.randrange(first_year, second_year)


def page_func() -> int:
    """
    Эта функция возвращает количество страниц
    :return:
    """
    random_number_of_page = random.randint (1, 10000)
    return random_number_of_page


def isbn13(separator: str = '-') -> str:
    fake = Faker()
    isbn_number = fake.isbn13()
    return isbn_number


def rating_func() -> float:
    return random.uniform(0, 5)


def price_func() -> float:
    return random.uniform(0, 2000)


def author_func() -> list[str]:
    fake = Faker()
    random_number = random.randint(1, 3)
    return [fake.name() for _ in range(random_number)]


def gen(pk: int=1) -> dict:
    while True:
        yield {
            "model": MODEL,
            "pk": pk,
            "fields": {
                "title": title(),
                "year": year_func(),
                "pages": page_func(),
                "isbn13": isbn13(),
                "rating": rating_func(),
                "price": price_func(),
                "author": author_func()
            }
        }
        pk += 1

def main():
    book_gen = gen(1)
    list_ = [next(book_gen) for _ in range(10)]
    print(list_)
    output_file = "output_3.txt"
    with open(output_file, "w", encoding='utf-8') as f:
        json.dump(list_, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()
