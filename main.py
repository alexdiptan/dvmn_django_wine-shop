from datetime import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler

import pandas
from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape(["html"]))
template = env.get_template("template.html")

current_year = datetime.today().year
years_since_foundation = current_year - 1920


def get_year_ending(digit):
    exception_digits = [i for i in range(11, 20)]
    for exception_digit in exception_digits:
        if str(digit).endswith(str(exception_digit)):
            return "лет"
    if (
            (digit > 1 or digit < 5)
            or str(digit).endswith("2")
            or str(digit).endswith("3")
            or str(digit).endswith("4")
    ):
        return "года"
    if digit == 1 or str(digit).endswith("1"):
        return "год"
    else:
        return "лет"


excel_data_df = pandas.read_excel(
    "wine.xlsx",
    sheet_name="Лист1",
)

rendered_page = template.render(
    foundation=years_since_foundation,
    year_ending=get_year_ending(years_since_foundation),
    wines=excel_data_df.to_dict(orient='records'),
)

with open("index.html", "w", encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(("0.0.0.0", 8000), SimpleHTTPRequestHandler)
server.serve_forever()
