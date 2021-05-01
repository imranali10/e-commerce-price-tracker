import requests
import lxml
from bs4 import BeautifulSoup


def getLinkData(url):
    
    headers = {
        "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
        'Accept-Language': 'en',
    }

    content = requests.get(url, headers=headers)
    soup = BeautifulSoup(content.text, 'lxml')

    title = soup.select_one(selector="#productTitle").get_text(strip=True)
    try:
        price = soup.select_one(selector="#priceblock_ourprice").get_text()

    except:
        price = soup.select_one(selector="#priceblock_dealprice").get_text()

    price = price[2:]
    price = float(price.replace(",", ""))
    # price = float(re.sub('[\₹,]', '', price)[1:])

    return title, price