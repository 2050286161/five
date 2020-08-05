import requests
import json
post_usl='https://fanyi.baidu.com/sug'
word=input('enter a word:')
data={
    'kw':word
}
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3766.400 QQBrowser/10.6.4163.400'
}
response=requests.post(url=post_usl,data=data,headers=headers)
dic_obj=response.json()
print(dic_obj)
fp=open('./dog.json','w',encoding='utf-8')
json.dump(dic_obj,fp=fp,ensure_ascii=False)
print('over')