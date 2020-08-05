import requests
if __name__=="__main__":
# 指定url
    url='https://www.sogou.com/'
# 发起请求
    response=requests.get(url=url)
# 获取响应对象
    x=response.text
# 持久化存储
    with open('./sogou.html','w',encoding='utf-8') as fp:
        fp.write(x)
    print('结束')