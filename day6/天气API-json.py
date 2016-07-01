import requests
import json
response = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=北京')
response.encoding = 'utf-8'
print(response.text,type(response.text))

dic = json.loads(response.text)
print(dic,type(dic))
json.dump(dic,open('db','w'))


s1 = json.load(open('db','r'))
print(s1,type(s1))
'''
{"desc":"OK","status":1000,"data":{"wendu":"27","ganmao":"各项气象条件适宜，发生感冒机率较低。但请避免长期处于空调房间中，以防感冒。","forecast":[{"fengxiang":"无持续风向","fengli":"微风级","high":"高温 31℃","type":"雷阵雨","low":"低温 22℃","date":"30日星期四"},{"fengxiang":"无持续风向","fengli":"微风级","high":"高温 29℃","type":"阴","low":"低温 22℃","date":"1日星期五"},{"fengxiang":"无持续风向","fengli":"微风级","high":"高温 31℃","type":"多云","low":"低温 22℃","date":"2日星期六"},{"fengxiang":"无持续风向","fengli":"微风级","high":"高温 32℃","type":"阴","low":"低温 22℃","date":"3日星期天"},{"fengxiang":"无持续风向","fengli":"微风级","high":"高温 33℃","type":"晴","low":"低温 23℃","date":"4日星期一"}],"yesterday":{"fl":"微风","fx":"无持续风向","high":"高温 29℃","type":"雷阵雨","low":"低温 22℃","date":"29日星期三"},"aqi":"91","city":"北京"}} <class 'str'>
{'desc': 'OK', 'data': {'wendu': '27', 'yesterday': {'type': '雷阵雨', 'fx': '无持续风向', 'date': '29日星期三', 'high': '高温 29℃', 'low': '低温 22℃', 'fl': '微风'}, 'aqi': '91', 'city': '北京', 'ganmao': '各项气象条件适宜，发生感冒机率较低。但请避免长期处于空调房间中，以防感冒。', 'forecast': [{'date': '30日星期四', 'type': '雷阵雨', 'fengxiang': '无持续风向', 'fengli': '微风级', 'high': '高温 31℃', 'low': '低温 22℃'}, {'date': '1日星期五', 'type': '阴', 'fengxiang': '无持续风向', 'fengli': '微风级', 'high': '高温 29℃', 'low': '低温 22℃'}, {'date': '2日星期六', 'type': '多云', 'fengxiang': '无持续风向', 'fengli': '微风级', 'high': '高温 31℃', 'low': '低温 22℃'}, {'date': '3日星期天', 'type': '阴', 'fengxiang': '无持续风向', 'fengli': '微风级', 'high': '高温 32℃', 'low': '低温 22℃'}, {'date': '4日星期一', 'type': '晴', 'fengxiang': '无持续风向', 'fengli': '微风级', 'high': '高温 33℃', 'low': '低温 23℃'}]}, 'status': 1000} <class 'dict'>
'''

