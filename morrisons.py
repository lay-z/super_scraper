from bs4 import BeautifulSoup
import requests
import csv


# import sys
# sys.stdout = open("outputMorrisons.txt", "w")


def writeToFile(filename, data, heading):
    """
    Writes data to the file using csv writer
    Writer appends to the file rather than writing over it

    :param filename: name of to be written too
    :param data: Dictionary to be written to file
    :param heading: *optional* heading to be passed in to file
    :return: None
    """

    headers = list(data.keys())  # Gets the dictionary keys, converts to a list
    products = data[headers[0]]
    prices = data[headers[1]]
    rows = []

    # Produces array in correct format to write out to csv
    for row in range(len(products)):
        rows.append([products[row], prices[row]])   # Adds the list for the product name and price to the "rows" list

    print(rows)

    # Good practice to open files using "with" keyword also using "a" to append to the file rather than write over it
    with open(filename, "a") as file:
        writer = csv.writer(file, delimiter=";")

        if heading:
            writer.writerow([heading])

        writer.writerow(headers)  # Writes the headers to file

        writer.writerows(rows)  # Write rows takes in a list of lists, each list will be the respective values for that row


def parseResponse(response):
    """
    Takes in a response object, converts it to soup and then parses response
        for product name and amount.

    :param response: requests response object
    :return: Dictionary object holding products and prices
    """
    # Just to see
    print(response.url)

    soup = BeautifulSoup(response.text, "html.parser")
    productFrames = soup.find_all("li", class_="productDetails")

    print("found {} products".format(len(productFrames)))

    products = []  # Initialise products Array
    prices = []  # Initialise prices Array

    if len(productFrames) is not 0:
        for product in productFrames:
            if product.h4.strong.abbr:
                products.append(product.h4.strong.abbr["title"])  # For titles that have ... for abreviation strings
            else:
                products.append(product.h4.strong.string)

            price = product.find("div", class_="typicalPrice")  # Find price section for product

            if price.span:  # Span tag only exist for "was" and "now" prices
                price = price.find("span", "wasPrice").string.strip()  # Strip removes whitespaces before and after
            else:
                price = price.h5.string.strip()
            prices.append(price)

        return {"prices": prices, "products": products, "prevResp": products[0]}
    else:
        raise Exception("Parse Error")  # Raising Exception good way to handle errors and shit


def morrisonsScraper(tags):
    """

    :param tags: Tags parameter in url for product type (i.e. tea, coffee etc)
    :return: Dictionary holding products and prices
    """

    ajaxUrl = "https://groceries.morrisons.com/webshop/getCategories.do"

    r = requests.Session()  # Because making ajax calls need to use a session (probs)
    returnDict = {"products": [], "prices": []}

    payload = {
        "ajax": "true",
        "index": 0,
        "tags": tags,
        "browse": "true"
    }
    response = r.get(ajaxUrl, params=payload)

    prevResp = ""  # Initialise empty string for prevResp Test
    parsedResponse = parseResponse(response)

    while (parsedResponse["prevResp"] != prevResp):
        prevResp = parsedResponse["prevResp"]  # Used for determining if all data been scraped
        payload["index"] += 1
        response = r.get(ajaxUrl, params=payload)
        parsedResponse = parseResponse(response)

        # Add it to giant list of products and prices
        returnDict["products"] += parsedResponse["products"]
        returnDict["prices"] += parsedResponse["prices"]

    return returnDict


filename = "outputMorrisons.txt"

morrisonsTeaTags = "|105651|103644|103986|103987"
teaData = morrisonsScraper(morrisonsTeaTags)
writeToFile(filename, teaData, heading="TEA")


morrisonsCoffeeTags = "|105651|103644|103986|154741"
coffeeData = morrisonsScraper(morrisonsCoffeeTags)
writeToFile(filename, coffeeData, heading="COFFEE")

# morrisonsUrlHotchoc =\
#     " https://groceries.morrisons.com/webshop/getCategories.do?tags=%7C105651%7C103644%7C103986%7C103996"
# print('HOT CHOCOLATE ETC:')
# morrisonsScraper(morrisonsUrlHotchoc)
#
# morrisonsUrlSugar = "https://groceries.morrisons.com/webshop/getCategories.do?tags=%7C102705%7C104867"
# print('SUGAR')
# morrisonsScraper(morrisonsUrlSugar)
