import requests,datetime,json
from operator import itemgetter

startdate='20181007'
enddate='20181009'
startDate=datetime.datetime.strptime(startdate,'%Y%m%d')
endDate=datetime.datetime.strptime(enddate,'%Y%m%d')
print(startDate)
print(endDate)
dcity = {"ZUH": "珠海", "CAN": "广州", "SZX": "深圳"}
acity = {"SHA": "上海", "HGH": "杭州", "NGB": "宁波"}
url = "http://flights.ctrip.com/itinerary/api/12808/lowestPrice"
for fromcode, fromcity in sorted(dcity.items(), key=itemgetter(0)):
    for tocode, tocity in sorted(acity.items(), key=itemgetter(0)):
        json1 = {"flightWay": "Oneway", "dcity": fromcode, "acity": tocode}
        # print(json1)
        if fromcode != tocode:
            text = requests.post(url,json=json1)
            data = json.loads(text.text)
            cost = data['data']['oneWayPrice'][0]['20180901']



