import requests
import json
url='https://movie.douban.com/j/chart/top_list'
para={
    'type': '24',
    'interval_id':'100:90',
    'action':'',
    'start':'140',
    'limit':'20',
}
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3766.400 QQBrowser/10.6.4163.400'
}
reponse=requests.get(url=url,params=para,headers=headers)
list_data=reponse.json()
fp=open('./douban.json','w',encoding='utf-8')
json.dump(list_data,fp=fp,ensure_ascii=False)
print('over')