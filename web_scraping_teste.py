# -*- coding: utf-8 -*-
"""Web Scraping teste

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/175IeCSmibcfT586yA7Sktct7CrBt9lV4
"""

import requests
from bs4 import BeautifulSoup

url = 'https://www.cvc.com.br/'

page = requests.get(url)
print(page)

bs1 = BeautifulSoup(page.content, 'html.parser')

bs2 = BeautifulSoup(page.text, 'html.parser')

print(type(bs2))

#aqui parece que ele assume uma forma de vetor.
precos = []
precos = bs2.find_all('span')
listaPrecos = []

print(precos)

for i in len(precos):
  if precos[i].is_digit():
    listaPrecos.append(i.get_text())
print(listaPrecos)

link = bs2.find_all('a')
print('Link: ',link)

link = [link[i].get_text() for i in range(0,10)]
print('Link: ',link)

urls = []
for i in bs2.find_all('a'):
    urls.append(i.get('href'))

print(urls)

texto = ' '.join([link for link in link])

print(texto)

!pip install --upgrade gspread

from google.colab import auth
auth.authenticate_user()

import gspread
from oauth2client.client import GoogleCredentials

from google.oauth2.service_account import Credentials

credentials = Credentials.from_service_account_file(
    "/path/to/service_account_file.json"
)

gc = gspread.authorize(credentials)

sh = gc.create('teste') #cria a planilha