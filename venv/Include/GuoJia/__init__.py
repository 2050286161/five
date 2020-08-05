import requests
import json

url='http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList'
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3766.400 QQBrowser/10.6.4163.400'
}
pram={
    'on':'true',
    'page':'1',
    'pageSize':'15',
    'productName':'',
    'conditionType':'1',
    'applyname':'',
}
reponse=requests.post(url=url,params=pram,headers=headers)
json_ids=reponse.json()
id_list=[]
json_data=[]
for idc in json_ids['list']:
    id_list.append(idc['ID'])
url1='http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById'
for data in id_list:
    datas={
    'id':data
    }
    reponse=requests.post(url=url1,data=datas,headers=headers)
    json_data.append(reponse.json())
fp=open('china.json','w',encoding='utf-8')
json.dump(json_data,fp=fp,ensure_ascii=False)
print('over')
