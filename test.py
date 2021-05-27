import bs4
import requests

def getNeostorePrice(productUrl):
    response = requests.get(productUrl)
    response.raise_for_status()

    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    contents = soup.select('#product-13807 > div.single-product-wrapper > div.summary.entry-summary > p > span > ins > span > bdi')
    return contents[0].text.strip()

product_address = input("Enter the product site address:")
price = getNeostorePrice(product_address)

print("The price is" + price)
    