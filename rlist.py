import csv
import pandas as pd
from termcolor import colored, cprint
from tabulate import tabulate
from datetime import date

reading_list = []

from datetime import datetime

now = datetime.now()
current = now.strftime("%Y%m%-d")


def add_book():
    date = input("Дата:").strip() or current.strip()
    title = input("Назва: ").strip() or "?"
    author = input("Автор: ").strip() or "?"
    year = input("Рік публікації: ").strip() or "?"
    rating = input("Рейтинг (1/5 -> 5/5): ").strip() or "☆☆☆☆☆"

    book = f"{date},{title},{author},{year},{rating}\n"

    with open("books.csv", "a") as reading_list:
        reading_list.write(book)


def get_all_books():
    books = []

    with open("books.csv", "r") as reading_list:
        for book in reading_list:
            date, title, author, year, rating = book.strip().split(",")

            books.append(
                {
                    "date": date,
                    "title": title,
                    "author": author,
                    "year": year,
                    "rating": rating,
                }
            )

    return books


def show_books(books):
    for book in books:
        print(
            f" ~ {book['date']}, {book['title']}, {book['author']}, ({book['year']}), {book['rating']}"
        )


menu_prompt = """
Будь ласка, оберіть один з варіантів:

- 'a' - додати до списку  нову книжку 
- 'l' - переглянути список читання
- 's' - зберегти список читання до текстового файлу
- 'q' - завершити роботу з програмою
"""

selected_option = input(menu_prompt).strip().lower()


def save_books():
    with open("rlist.txt", "w") as f:
        f.write(allbooks)


headers = ["ДАТА", "НАЗВА", "АВТОР(и)", "РІК", "РЕЙТИНГ"]
readinglist = pd.read_csv("books.csv")
allbooks = tabulate(readinglist, headers, tablefmt="simple_grid")

while selected_option != "q":
    if selected_option == "a":
        add_book()
    elif selected_option == "l":
        reading_list = get_all_books()
        print("")
        show_books(reading_list)
        print("")
    elif selected_option == "s":
        save_books()
        cprint("    Saved ..", "light_green")
    else:
        print("")
        print(f"Sorry, '{selected_option}' is not a valid option.")

    selected_option = input(menu_prompt).strip().lower()
