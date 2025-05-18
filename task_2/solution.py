import requests
from bs4 import BeautifulSoup
import time
import csv
from collections import defaultdict
from urllib.parse import urljoin


BASE_URL = "https://ru.wikipedia.org"
START_URL = f"{BASE_URL}/wiki/Категория:Животные_по_алфавиту"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}


def get_animals_count_by_letter():
    counts = defaultdict(int)
    url = START_URL

    while url:
        print(f"Парсим: {url}")
        try:
            response = requests.get(url, headers=HEADERS)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Ошибка запроса: {e}")
            break

        soup = BeautifulSoup(response.text, "html.parser")

        div = soup.find("div", {"id": "mw-pages"})
        if not div:
            print("Блок 'mw-pages' не найден")
            break

        items = div.select("div.mw-category-group ul li a")
        for item in items:
            name = item.text.strip()
            if name:
                first_letter = name[0].upper()
                counts[first_letter] += 1

        time.sleep(1)

        next_page_link = soup.find("a", string="Следующая страница")
        if next_page_link:
            url = urljoin(BASE_URL, next_page_link["href"])
        else:
            break

    return dict(counts)


def save_counts_to_csv(counts, filename="beasts.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Буква", "Количество животных"])
        for letter in sorted(counts.keys()):
            writer.writerow([letter, counts[letter]])
    print(f"Результаты сохранены в файл: {filename}")


if __name__ == "__main__":
    counts = get_animals_count_by_letter()
    save_counts_to_csv(counts)
