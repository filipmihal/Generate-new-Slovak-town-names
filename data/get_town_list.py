# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests


# PARAMETERS
SOURCE_URL = 'http://www.e-obce.sk/zoznam_vsetkych_obci.html?strana='
TOWNS_PER_PAGE = 500
PAGES = 6

DATA_FILE = "Slovak_towns.csv"
CSV = open(DATA_FILE, "w")


def get_url(url, param):
    return url + str(param)


def get_table(content):
    body = content.find("div", {"id": "telo"})
    table = body.findAll('table')
    return table[0].find('table').findAll('table')[-1]


for num in range(0, PAGES):
    towns_num = 0
    url = get_url(SOURCE_URL, num * TOWNS_PER_PAGE)
    source = requests.get(url, verify=False)
    source.encoding = 'windows-1250'
    html = source.text
    content = BeautifulSoup(html)
    table = get_table(content)
    rows = table.findAll('tr')
    links = table.findAll('a')
    for link in links:
        towns_num += 1
        CSV.write(link.contents[0] + "\n")
