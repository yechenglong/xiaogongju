import requests,datetime,random,time
from operator import itemgetter
dcity ={"ZUH":"珠海","CAN":"广州","SZX":"深圳"}
acity ={"SHA":"上海","HGH":"杭州","NGB":"宁波"}
UserAgent = [
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
    "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0) Gecko/16.0 Firefox/16.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1500.55 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17"
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
]
url = "http://flights.ctrip.com/itinerary/oneway/zuh-sha?date=2018-09-22&portingToken=20a425e051094256a546d3f8cfc793fa"
headers = {
    "Host": "flights.ctrip.com",
    "User-Agent":random.choice(UserAgent),
    "Referer": "http://flights.ctrip.com/booking/SHA-BJS-day-1.html?DDate1=2017-10-22",
    "Connection": "keep-alive",
}
def set_url_headers(url,startdate,enddate):
    startDate=datetime.datetime.strptime(startdate,'%Y-%m-%d')
    endDate=datetime.datetime.strptime(enddate,'%Y-%m-%d')
    while startDate<=endDate:
        today = startDate.strftime('%Y-%m-%d')
        for fromcode, fromcity in sorted(dcity.items(), key=itemgetter(0)):
            for tocode, tocity in sorted(acity.items(), key=itemgetter(0)):
                if fromcode != tocode:
                    requests.get(url)

            print("%s : %s(%s) ==> %s(%s) " % (today,fromcity,fromcode,tocity,tocode))

        time.sleep(10)
        startDate+=datetime.timedelta(days=1)

