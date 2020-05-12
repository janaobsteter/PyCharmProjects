from collections import defaultdict
import requests
from bs4 import BeautifulSoup
import time
from modules.price import Price
from modules.database import Database
from pprint import pprint

# url = "http://www.dormeo.net/lezisca/"
#
# request = requests.get(url)
# content = request.content
#
# soup = BeautifulSoup(content, "html.parser")
# element = soup.find_all("a", href=True)
# #print(element)
# links = list(set([link["href"] for link in element if "lezisce" in link["href"]]))
# #print(links)
#
Database.initialize()
#
# for link in links:
#     reqLink = requests.get(link)
#     time.sleep(10)
#     contentLink = reqLink.content
#     soup = BeautifulSoup(contentLink, "html.parser")
#     name = soup.find("h1", {"itemprop": "name"}).text
#     price = soup.find_all("script", type="text/javascript")
#     #[l.split(",") for l in [x for x in str(price).split("{") if "label" in x]]
#     prod =  [x for x in str(price).split("{") if "label" in x]
#
#     DE = []
#     for pr in prod:
#         j = pr.split(",")
#         DE.append([x for x in j if "dataprice" in x or "label" in x])
#
#
#     for de in DE:
#         try:
#             prod = Price(productName = name,
#                          specs = de[0].split(":")[1].strip('"').strip(" cm"),
#                          price = de[1].split(":")[1].strip('"'))
#             prod.save_to_db(collection = "Dormeo")
#         except:
#             pass


pprint(Database.find(collection="Dormeo",
              query={"Specification": "160x200"}))

