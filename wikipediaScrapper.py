import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import re

f = open("text.txt", "w")
link = ("https://en.wikipedia.org/wiki/Thomas_Jefferson")
uClient = uReq(link)
page = uClient.read()
soup = BeautifulSoup(page, 'html.parser')
table = soup.find('table', class_='infobox vcard')
full = ""
for tr in table.find_all('tr') :
    temp = tr.text
    for i in range(0,len(temp)):
        if i < len(temp)-1:
            if temp[i].islower() and temp[i+1].isupper():
                full+= temp[i] + ": "
                continue
        if i == (len(temp)-1):
            full+= temp[i] + "\n"
        else:
            full+= temp[i]

print(full)