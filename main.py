from bs4 import BeautifulSoup
import requests
import csv
tescoUrl = "http://www.tesco.com/groceries/product/browse/default.aspx?N=4293863468&Ne=4294793660&icid=DRI_LHN_Tea&Nao="

pagesList = ['0', '40', '80', '120', '160', '200', '240', '280']

# something like for x = 0:len(pagesList):
    # fullUrl= tescoUrl+pagesList[x]

fullUrl = tescoUrl+pagesList[0]
r = requests.get(fullUrl)
data = r.text
soup = BeautifulSoup(data, "html.parser")

# Find all elements that exist in product.clearfix class
productsFrames = soup.find_all("li", class_="product")

with open("tesco.csv", "w") as csvfile:

    for product in productsFrames:
        product_name = product.img["title"].split('-')[0]
        price = product.find(class_="linePrice").string
        print("{}: {}".format(product_name, price[2:6]))
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow([product_name, price[2:6]])

# print(len(productsFrames))
