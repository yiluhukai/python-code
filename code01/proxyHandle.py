'''
@Author: yiluhuakai
@LastEditors: yiluhuakai
@Date: 2020-07-26 15:32:30
@LastEditTime: 2020-07-26 16:14:40
@FilePath: /python_code/code01/proxyHandle.py
'''

# 通过代理的方式访问目标服务器


from urllib import request


url = 'http://httpbin.org/ip'


# 创建代理handle

handle = request.ProxyHandler({
    'http': '61.163.32.88:3128'
})

opener = request.build_opener(handle)

requestUrl = request.Request(url)

resp = opener.open(requestUrl)

print(resp.getcode())

print(resp.read())
