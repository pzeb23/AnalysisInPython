import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from datetime import datetime
import json
from pymongo import MongoClient

my_url = 'https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48'

# opening up connection
uClient = uReq(my_url)
# grabbing the page
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

#containers = page_soup.findAll("div", {"class": "item-container"})
# grab each product
containers = page_soup.findAll("div", {"class": "item-info"})

#myMongoClient = MongoClient()
myMongoClient = MongoClient('mongodb://localhost:27017')

myDatabase = myMongoClient['PiotrZ_web']

myData = myDatabase.posts

#len(containers)
#container = containers[0]
for container in containers:
    brand = container.a.img["title"]

    title_container = container.findAll("a", {"class": "item-title"})
    product_name = title_container[0].text

    features_container = container.findAll("ul", {"class": "item-features"})
    features = features_container[0].text.strip()

    shipping_container = container.findAll("li", {"class" : "price-ship"})
    shipping = shipping_container[0].text.strip()

    #rating_container = container.findAll("span", {"class" : "item-rating-num"})
    #ratings = rating_container[0].text

    #### printing to console ####
    print("brand: " + brand)
    print("product_name: " + product_name)
    print("shipping: " + shipping)
    print("features: " + features)
    #print("ratings: " + ratings)
    ##############################

for i in range(len(containers)):
    dane = {
        'brand':''+brand+'',
        'product_name':''+product_name+'',
        'shipping':''+shipping+'',
        'features':''+features+'',
        'time':''+str(datetime.now())+''
    }

    rezultat = myData.insert_one(dane)
    print('Inserted: {0}'.format(rezultat.inserted_id))

    #with open('plikPiotrZ'+str(i)+'.json',"w") as plik:
        #json.dump(dane, plik)

collections = myData.find({})
print(collections)

for k in collections:
    print(k)
