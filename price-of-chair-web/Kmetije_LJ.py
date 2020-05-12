# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
import pandas as pd


url = "https://www.ljubljana.si/sl/moja-ljubljana/podezelje/samooskrba-v-ljubljani/ponudniki-ljubljanskega-podezelja-in-regije/"

request = requests.get(url)
content = request.content
soup = BeautifulSoup(content, "html.parser")
kmetije = soup.findAll("div", {"class": "content-inner"})

kmetije_links = []
kmetije_ime = dict()
kmetije_info = dict()
kmetije_ponudba = dict()
kmetije_prodaja = dict()
ID = 0
for kmetija in kmetije:
    #kmetije_links.append('ljubljana.si/' + kmetija.h2.a['href'])
    ID += 1
    id = "ID" + str(ID)
    print(id)
    kmetija_url = 'https://www.ljubljana.si/' + kmetija.h2.a['href']
    content_kmetija = urlopen(kmetija_url)
    content_kmetija = content_kmetija.read()
    #request_kmetija = requests.get(kmetija_url)
    #content_kmetija = request_kmetija.content
    content_kmetija = content_kmetija.replace(b'<br/>', b'|br|')
    soup_kmetija = BeautifulSoup(content_kmetija, "html.parser")
    ponudba_kmetija = [x.text for x in soup_kmetija.findAll("div", {"class": "content-toggle"})[1].findAll("p")]
    ponudba = [x for x in ponudba_kmetija if 'PONUDBA' in x]
    prodaja = [x for x in ponudba_kmetija if 'PRODAJA' in x]
    kontakt = soup_kmetija.findAll("div", {"class": "content-toggle"})[-1].findAll("p")[0]
    for br_tag in kontakt.findAll('br'):
        br_tag.replace_with('|')
    kontakt = kontakt.text.split('|')
    ime = kontakt[0]
    print(ime)
    naslov = kontakt[1:]
    kmetije_ime[id] = ime
    kmetije_info[id] = naslov
    kmetije_ponudba[id] = ponudba
    kmetije_prodaja[id] = prodaja


kmetijeImeDF = pd.DataFrame.from_dict(kmetije_ime, orient='index')
kmetijeImeDF = kmetijeImeDF.rename(columns = {0:'ID'})
kmetijeInfoDF = pd.DataFrame.from_dict(kmetije_info, orient='index')
kmetijeInfoDF = kmetijeInfoDF.rename(columns = {0:'ID'})
kmetijePonudbaDF = pd.DataFrame.from_dict(kmetije_ponudba, orient='index')
kmetijePonudbaDF = kmetijePonudbaDF.rename(columns = {0:'ID'})
kmetijeProdajaDF = pd.DataFrame.from_dict(kmetije_prodaja, orient='index')
kmetijeProdajaDF = kmetijeProdajaDF.rename(columns = {0:'ID'})


kmetijeDF = pd.merge(kmetijeImeDF, kmetijeInfoDF, how="outer", left_index=True, right_index=True)
kmetijeDF = pd.merge(kmetijeDF, kmetijePonudbaDF, how="outer", left_index=True, right_index=True)
kmetijeDF = pd.merge(kmetijeDF, kmetijeProdajaDF, how="outer", left_index=True, right_index=True)

kmetijeDF.to_csv("/home/jana/Documents/KmetijeLJ.csv")


