import requests
import csv

odpowiedz = requests.get("https://quotes.toscrape.com")
print(odpowiedz.status_code)
print(len(odpowiedz.text))

from bs4 import BeautifulSoup

soup = BeautifulSoup(odpowiedz.text, "html.parser")   
cytaty = soup.find_all("div", class_="quote")
#print(cytaty)

with open("cytaty.csv", "w", newline="", encoding="utf-8") as plik:
    writer = csv.writer(plik)
    writer.writerow(["cytat", "autor"])

    for cytat in cytaty:
        tekst = cytat.find("span", class_="text").text
        autor = cytat.find("small", class_="author").text
        #print(tekst, autor)
        writer.writerow([tekst, autor])              