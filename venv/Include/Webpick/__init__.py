import requests
#数据搜索原始网页爬取
url='https://www.sogou.com/web'
kw=input('enter a word:')
param={
    'query':kw
}
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3766.400 QQBrowser/10.6.4163.400'
}
response=requests.get(url=url,params=param,headers=headers)
page_text=response.text
filename=kw+'.html'
with open(filename,'w',encoding='utf-8') as fp:
    fp.write(page_text)
print(filename,'保存成功')