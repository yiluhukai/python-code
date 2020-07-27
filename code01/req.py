from urllib import request, parse


urlStr = 'https://music.163.com/weapi/search/suggest/web?csrf_token='
headers = {
    'user-agent': 'Mozilla/5.0 (Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Mobile Safari/537.36'
}

formData = {
    'params': 'bN2mAgjFdFwIGppcorF2DrMtkAypKKoCyupZp2/ZrEDL8tFbxZ3N6xO4795cfGmw/LANGUg459mDw2WXpWeHq9lp6f0zQQdL9714Dz6gkU4=',
    'encSecKey':  '3abaa6841821a09fde326ded7e7d8ab395aa2b78598de00998181c87af7bb85de5bb2305a5651567d7ba3fe8e5f4131f184ade7fa17977609929419c4e3f8e24cf23f7426665d6f6b1e5d9a29384b5541ed1b0d04277619b4b9e3ba2eb27ebf7d20e0d4d58e5d98f52201586e8ea89b105695419d5adabb305c685dd12b1db51'
}
# 对data进行编码并转成ascill
# string -> byte encode()
# byte -> string decode()

url = request.Request(urlStr, data=parse.urlencode(
    formData).encode("utf-8"), headers=headers, method='POST')
resp = request.urlopen(url)

print(resp.read())
