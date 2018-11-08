import requests
from bs4 import BeautifulSoup


url = "https://www.johnlewis.com/house-by-john-lewis-fluent-chair/p2101407"
# request = requests.get("http://www.google.com")
request = requests.get(url)
content = request.content
soup = BeautifulSoup(content, "html.parser") #search through the data with an htl parser
element = soup.find("p", {"class": "price price--large"}) #span is the tag and {} are the attributes, recursive is True by default
#print(element.text.strip())
string_price = element.text.strip() #£39.0

#do slicing to remove £
price_without_symbol = float(string_price[1:]) #this is also £39.0, this is COPYING the string
budget = 100
print(price_without_symbol)
print(price_without_symbol < budget)

if price_without_symbol <= budget:
    print("Buy the chair.")
    print("Current price is {}".format(string_price))
else:
    print("Do not buy the chair.")

#<p class="price price--large">£39.00 </p>

#print(request.content) #this is a get request
#element = soup.find("div", {"class":"prices-container", "itemprop":"offers"}) #span is the tag and {} are the attributes, recursive is True by default
