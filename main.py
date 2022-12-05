import collections
from datetime import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler

import pandas
from jinja2 import Environment, FileSystemLoader, select_autoescape

from environs import Env


def get_year_ending(digit):
    for exception_digit in range(5, 20):
        if str(digit).endswith(str(exception_digit)):
            return "лет"
    if digit == 1 or str(digit).endswith("1"):
        return "год"
    if (
        (digit > 1 or digit < 5)
        or str(digit).endswith("2")
        or str(digit).endswith("3")
        or str(digit).endswith("4")
    ):
        return "года"
    else:
        return "лет"


def main():
    env_vars = Env()
    env_vars.read_env()
    catalog_file = env_vars.str("CATALOG_FILE", "")

    env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape(["html"]))
    template = env.get_template("template.html")

    current_year = datetime.today().year
    winery_since_year = 1920
    foundation_year = current_year - winery_since_year

    excel_data_df = pandas.read_excel(
        catalog_file, sheet_name="Лист1", keep_default_na=False
    )

    drinks = excel_data_df.to_dict(orient="records")

    drinks_by_categories = collections.defaultdict(list)
    for drink_row in drinks:
        drinks_by_categories[drink_row["Категория"]].append(drink_row)

    rendered_page = template.render(
        foundation=foundation_year,
        year_ending=get_year_ending(foundation_year),
        drinks_by_categories=drinks_by_categories,
    )

    with open("index.html", "w", encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(("0.0.0.0", 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
