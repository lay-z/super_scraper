from bs4 import BeautifulSoup
import requests
import sys
sys.stdout = open("C:\\Users\\megaw_000\\Desktop\\super_scraper-master\\outputTesco.txt", "w")

tescoUrlTea = "http://www.tesco.com/groceries/product/browse/default.aspx?N=4293863468&Ne=4294793660&Nao="
pagesListTea = ['0', '20', '40', '60', '80', '100', '120', '140', '160', '180', '200', '220', '240', '260', '280']
print('TEA:')

for page in pagesListTea:
    fullUrl = tescoUrlTea+page
    r = requests.get(fullUrl)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")

    # Find all elements that exist in product.clearfix class
    productsFrames = soup.find_all("li", class_="product")

    for product in productsFrames:
        product_name = product.img["title"].split('-')[0]
        price = product.find(class_="linePrice").string
        print("{};{}".format(product_name, price[2:6]))

tescoUrlCoffee = "http://www.tesco.com/groceries/product/browse/default.aspx?N=4294107884&Ne=4294793660&Nao="
pagesListCoffee = ['0', '20', '40', '60', '80', '100', '120', '140', '160', '180', '200', '220', '240', '260']
print('COFFEE:')

for page in pagesListCoffee:
    fullUrl = tescoUrlCoffee+page
    r = requests.get(fullUrl)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")

    # Find all elements that exist in product.clearfix class
    productsFrames = soup.find_all("li", class_="product")

    for product in productsFrames:
        product_name = product.img["title"].split('-')[0]
        price = product.find(class_="linePrice").string
        print("{};{}".format(product_name, price[2:6]))

tescoUrlSugar = "http://www.tesco.com/groceries/product/browse/default.aspx?N=4294792852&Ne=4294793660&Nao="
pagesListSugar = ['0', '20', '40', '60']
print('SUGAR')

for page in pagesListSugar:
    fullUrl = tescoUrlSugar+page
    r = requests.get(fullUrl)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")

    # Find all elements that exist in product.clearfix class
    productsFrames = soup.find_all("li", class_="product")

    for product in productsFrames:
        product_name = product.img["title"].split('-')[0]
        price = product.find(class_="linePrice").string
        print("{};{}".format(product_name, price[2:6]))
