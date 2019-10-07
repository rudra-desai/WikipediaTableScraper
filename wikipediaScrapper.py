import requests
import bs4
import re
r = requests.get('https://en.wikipedia.org/wiki/Thomas_Jefferson')
type(r)
soup = bs4.BeautifulSoup(r.text, 'html.parser')
table = soup.find('table', {'class': 'infobox vcard'}).tbody
line = str(table.text)
for word in line:
    for letter in word:
        if letter is int or letter.upper():
            print('\n')
print(line)
print("test")


