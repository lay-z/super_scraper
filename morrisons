from bs4 import BeautifulSoup
import requests
import sys
sys.stdout = open("C:\\Users\\megaw_000\\Desktop\\super_scraper-master\\outputMorrisons.txt", "w")



def morrisonsScraper(url):

    r = requests.get(url)
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
        print("{};{}".format(product_name[:-1], price[2:6]))

    print("")  # spacing between each scrape

morrisonsUrlTea =\
    "https://groceries.morrisons.com/webshop/getCategories.do?tags=%7C105651%7C103644%7C103986%7C103987"
print('TEA:')
morrisonsScraper(morrisonsUrlTea)

morrisonsUrlCoffee =\
    "https://groceries.morrisons.com/webshop/getCategories.do?tags=%7C105651%7C103644%7C103986%7C154741"
print('COFFEE:')
morrisonsScraper(morrisonsUrlCoffee)

morrisonsUrlHotchoc =\
    "https://groceries.morrisons.com/webshop/getCategories.do?tags=%7C105651%7C103644%7C103986%7C103996"
print('HOT CHOCOLATE ETC:')
morrisonsScraper(morrisonsUrlHotchoc)

morrisonsUrlSugar = "https://groceries.morrisons.com/webshop/getCategories.do?tags=%7C102705%7C104867"
print('SUGAR')
morrisonsScraper(morrisonsUrlSugar)
