# pylint: disable=missing-docstring,invalid-name

from bs4 import BeautifulSoup
HTML = "pages/carrot.html"

with open(HTML, encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

for recipe in soup.find_all('p', {'class': 'recipe-name'}):
    print(recipe.text)
