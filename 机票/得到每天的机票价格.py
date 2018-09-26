import requests,datetime,json
from operator import itemgetter

startdate='20180923'
enddate='20180924'
startDate=datetime.datetime.strptime(startdate,'%Y%m%d')
endDate=datetime.datetime.strptime(enddate,'%Y%m%d')
dcity = {"ZUH": "珠海", "CAN": "广州", "SZX": "深圳"}
# acity = {"SHA": "上海", "HGH": "杭州", "NGB": "宁波"}
acity = {"KHN": "南昌"}
url = "http://flights.ctrip.com/itinerary/api/12808/lowestPrice"
def getprice(url,dcity,acity,startDate,endDate):
    finalldata = {}
    for fromcode, fromcity in sorted(dcity.items(), key=itemgetter(0)):
        for tocode, tocity in sorted(acity.items(), key=itemgetter(0)):
            json1 = {"flightWay": "Oneway", "dcity": fromcode, "acity": tocode}
            # print(json1)
            if fromcode != tocode:
                text = requests.post(url,json=json1)
                data = json.loads(text.text)
                data1 = data['data']['oneWayPrice'][0]
                for date, price in data1.items():
                    newdate = datetime.datetime.strptime(date, '%Y%m%d')
                    if newdate <= endDate and newdate >= startDate:
                        city = fromcity + "-->" + tocity + " : " + str(newdate)
                        finalldata[city] = price
    finallprice = sorted(finalldata.items(), key=itemgetter(1))
    filename = "price.txt"
    with open(filename,'a') as writefile :
        writefile.write(str(finallprice[0])+"\n")
    with open(filename,'r') as writefile :
        print(writefile.readlines()[-1])

getprice(url,acity,dcity,startDate,endDate)



