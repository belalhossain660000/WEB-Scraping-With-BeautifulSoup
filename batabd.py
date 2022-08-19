import requests
from bs4 import BeautifulSoup
import time

all_link = []
for i in range(1,31):
    url = "https://www.________.com/collections/men?page="+ str(i)
    response = requests.get(url)
    cont_ent = response.content
    soup = BeautifulSoup(cont_ent, 'html.parser')
    product = soup.find_all('a', attrs={"class":"product-grid-image"})
    for get_url in product:
        product_url = "https://www.batabd.com" + get_url.get('href')
        all_link.append(product_url)

for url2 in all_link:
    response2 = requests.get(url2)
    cont_ent2 = response2.content
    soup2 = BeautifulSoup(cont_ent2, 'html.parser')
    title = soup2.find('div', attrs={'class': "col-md-6 product-shop"})
    title_text = title.find('span').get_text().strip()
    price_tag = soup2.find('span', attrs={"class": "price on-sale"})
    price = price_tag.get_text().strip()
    all_list = [url2, title_text, price]
    print(all_list)
    file = open('batabdfile.txt', 'a', encoding='utf-8')
    file.write(str(all_list) + "\n")
    file.close()
    time.sleep(1)
