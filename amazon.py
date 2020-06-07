import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.com/Flexispot-EC1W-R4830W-Electric-Adjustable-Standing/dp/B07W42DSG8/ref=sr_1_9?dchild=1&keywords=stand%2Bup%2Bdesk&qid=1591398957&sr=8-9&th=1'


headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}

page = requests.get(URL, headers=headers)

# soup1 = BeautifulSoup(page.content, "lxml")
soup1 = BeautifulSoup(page.content, 'html.parser')
soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

# title = soup2.find(id= "title").get_text()
# print(title)
# price = soup2.find(id="priceblock_ourprice").get_text()
# print(price)
#  converted_price = float(price[0:5])

# print(converted_price)


page = requests.get(URL, headers=headers, stream=True)
for chunk in page.iter_lines():
    if chunk.find('id="priceblock_ourprice"') > -1:
        print(chunk)
