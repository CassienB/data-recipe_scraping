# pylint: disable=missing-docstring,invalid-name

from bs4 import BeautifulSoup

soup = BeautifulSoup(open("pages/carrot.html"), "html.parser")

for recipe in soup.find_all('p', {'class': 'recipe-name'}):
    print(recipe.text)
