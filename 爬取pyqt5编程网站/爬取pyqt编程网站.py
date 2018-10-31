import os
import random
import re
import requests
from bs4 import BeautifulSoup


def get():
    url = "http://www.xdbcb8.com/pyqt5/"
    text = requests.get(url)
    soup = BeautifulSoup(text.text, 'html.parser')
    #设置消息头的User-Agent
    my_headers = [
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0"
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
        "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"
        ]

    #获取每节课的内容
    # for item in soup.find_all("a", text="阅读全文"):
    if True:
        #获取一节课的url
        # newurl = item.get('href')
        newurl = 'http://www.xdbcb8.com/archives/1529.html'
        #设置消息头
        header = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip,deflate",
            "Connection": "keep-alive",
            "User-Agent": random.choice(my_headers),
            "Referer":  newurl
        }
        #获取一节课的内容
        itemtext = requests.get(newurl)
        print(itemtext)
        newsoup = BeautifulSoup(itemtext.text,'html.parser')
        #获取这节课的课名
        title = newsoup.find_all('h1',class_ = 'entry-title')
        print(title[0].text)
        # urls= []
        # #设置图片的保存地址
        # path = 'F:\\pythonwork\\xiaogongju\\爬取pyqt5编程网站\\imgs'
        # if not os.path.exists(path):
        #     os.mkdir(path)
        # #获取这节课中用到的图片的url
        # for doc in newsoup.find_all(href=re.compile('upload'),class_='fancybox'):
        #     urls.append(doc['href'])
        # #下载图片并保存到本地
        # for url in urls:
        #     print(url)
        #     imgname = url.split('/')[-1]
        #     filename = os.path.join(path, imgname)
        #     if url.endswith('.png') or url.endswith('jpg') or url.endswith('gif'):
        #         r = requests.get(url,headers=header)
        #         print(r.status_code)
        #         fw = open(filename, 'wb')  # 指定绝对路径
        #         fw.write(r.content)  # 保存图片到本地指定目录
        for newitem in newsoup.find_all(['p','d','h4']):
            print(newitem.text)














get()

