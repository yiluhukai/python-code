from urllib import request
from urllib import parse

# 1.
resp = request.urlopen("http://www.baidu.com")


print(resp.read())

print(resp.readline())


# 2.保存到本地

# request.urlretrieve('http://www.baidu.com', 'baidu.html')


# 3.编码和解码
# data = {"name": "bruce"}

# print(data)
# encodeData = parse.urlencode(data)

# print(encodeData)

# decodeData = parse.parse_qs(encodeData)
# print(decodeData['name'])


# 4.解析url

# url = parse.urlparse("http://www.baidu.com/s;hello?username=zhiliao")


# print(url.scheme, url.netloc, url.params, url.path, url.query, url.fragment)

# urlsplit和url.parse类似，urlsplit解析出来字典不包含params,params被当最为path的一部分
# url1 = parse.urlsplit("http://www.baidu.com/s;hello?username=zhiliao")


# print(url1.scheme, url1.netloc,
#       url1.path, url1.query, url1.fragment)
