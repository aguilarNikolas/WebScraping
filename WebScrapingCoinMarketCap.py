# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 16:15:16 2021

@author: Aguilar
"""

import requests
import pandas as pd
# from bs4 import BeautifulSoup

# Downloading contents of the web page
composite_list = []
results = []

#I found this number in the coinmarketcap website
coins_number = 6012      
url = f'https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?start=1&limit={coins_number}&sortBy=market_cap&sortType=desc&convert=USD&cryptoType=all&tagType=all&audited=false'
print(url)
data = requests.get(url,headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'})
data.status_code
lista_json = data.json()
df = pd.DataFrame(lista_json['data']['cryptoCurrencyList'])

df.to_csv('Cryptos_tickers.csv')
