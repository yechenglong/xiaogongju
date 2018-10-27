import requests
from bs4 import BeautifulSoup

url = "http://www.xdbcb8.com/pyqt5/"
text = requests.get(url)
soup = BeautifulSoup(text.text,'html.parser')

for item in soup.find_all("a", text="阅读全文"):
    # print(item.get('href'))
    itemtext = requests.get(item.get('href'))
    newsoup = BeautifulSoup(itemtext.text,'html.parser')
    newsoup1 = newsoup.find_all(class_="single-content")
    print(newsoup1.div.text.replace('\xa0',''))
    # for newitem in newsoup.find_all('div'):
    #     print(newitem)



