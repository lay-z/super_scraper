from bs4 import BeautifulSoup
import requests
import csv
tescoSearchUrl = "http://www.tesco.com/groceries/product/search/default.aspx?searchBox=tea&newSort=true&search="
item = "tea"
r = requests.get(tescoSearchUrl+item)
data = r.text
soup = BeautifulSoup(data, "html.parser")

# find all elements that exist in product.clearfix class
productsFrames = soup.find_all("li", class_="product")

with open("output.csv", "w") as csvfile:

    for product in productsFrames:
        print(product)
        product_name = product.img["title"].split('-')[0]
        price = product.find(class_="linePriceAbbr").string
        print("{}: {}".format(product_name,price[2:-1]))
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow([product_name, price[2:-1]])


# print(len(productsFrames))