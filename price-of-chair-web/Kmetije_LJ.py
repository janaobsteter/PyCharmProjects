
import requests
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen


url = "https://www.ljubljana.si/sl/moja-ljubljana/podezelje/samooskrba-v-ljubljani/ponudniki-ljubljanskega-podezelja-in-regije/"

request = requests.get(url)
content = request.content
soup = BeautifulSoup(content, "html.parser")
kmetije = soup.findAll("div", {"class": "content-inner"})

kmetije_links = []
kmetije_info = dict()
id = 0
for kmetija in kmetije:
    #kmetije_links.append('ljubljana.si/' + kmetija.h2.a['href'])
    id =+ id
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
    naslov = kontakt
    kmetije_info[id] = [naslov, ponudba, prodaja]

