import requests
import json

url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'
}
kw=input('enter a word')

para={
    'cname':'',
    'pid':'',
    'keyword':kw,
    'pageIndex':'1',
    'pageSize':'30',
}
reponse=requests.post(url=url,params=para,headers=headers)
list_data=reponse.json()
fp=open('./kfc.json','w',encoding='utf-8')
json.dump(list_data,fp=fp,ensure_ascii=False)
print('over')
