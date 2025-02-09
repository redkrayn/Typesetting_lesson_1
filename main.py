import datetime
import os
import pandas
from collections import defaultdict
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from dotenv import load_dotenv


def add_year(how_long):
    return {
        how_long % 10 == 0: 'лет',
        how_long % 10 == 1: 'год',
        1 < how_long % 10 < 5: 'года',
        how_long % 10 > 4: 'лет',
        10 < how_long % 100 < 20: 'лет',
        how_long < 0: 'ошибка'
    }[True]


def main():
    load_dotenv()

    today = datetime.date.today()
    past_year = datetime.datetime(year=1920, month=10, day=10)
    how_long = today.year - past_year.year

    excel_file_path = os.getenv("EXCEL_WITH_WINES", "wine.xlsx")
    excel_data_wine = pandas.read_excel(excel_file_path, na_values=['N/A', 'NA'], keep_default_na=False)
    wines = excel_data_wine.to_dict(orient="records")

    wine_dictionary = defaultdict(list)
    default_category = "Без категории"
    for wine in wines:
        category = wine.get("Категория", default_category)
        wine_dictionary[category].append(wine)

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template("template.html")
    rendered_page = template.render(
        how_long=f"Уже {how_long} {add_year(how_long)} с нами",
        wine_categories=wine_dictionary,
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)
    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()