from bs4 import BeautifulSoup
import requests
import sys
sys.stdout = open("outputTesco.txt", "w")



def tescoScraper(url, end):
    increment = 20
    start = 0
    pagesList = range(start, end+increment, increment)  # range produces a list start (inclusive) - end (exclusive) with increment seperation

    for page in pagesList:
        fullUrl = url+str(page)  # have to convert int to string to concatinate the two together
        r = requests.get(fullUrl)
        data = r.text
        soup = BeautifulSoup(data, "html.parser")

        # Find all elements that exist in product.clearfix class
        productsFrames = soup.find_all("li", class_="product")

        for product in productsFrames:
            product_name = product.img["title"].split('-')[0]
            price = product.find(class_="linePrice")
            if price is not None:
                price = price.string
            else:
                price = "NA"  # not available currently
            print("{};{}".format(product_name[:-1], price[2:6]))  # added the '-1' to remove space at the end of product description

    print("")  # spacing betwen each scrape

tescoUrlTea = "http://www.tesco.com/groceries/product/browse/default.aspx?N=4293863468&Ne=4294793660&Nao="
print('TEA:')
tescoScraper(tescoUrlTea, 280)

tescoUrlCoffee = "http://www.tesco.com/groceries/product/browse/default.aspx?N=4294107884&Ne=4294793660&Nao="
print('COFFEE:')
tescoScraper(tescoUrlCoffee, 260)

tescoUrlSugar = "http://www.tesco.com/groceries/product/browse/default.aspx?N=4294792852&Ne=4294793660&Nao="
print('SUGAR')
tescoScraper(tescoUrlSugar, 60)


