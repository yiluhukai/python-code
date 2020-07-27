'''
@Author: yiluhuakai
@LastEditors: yiluhuakai
@Date: 2020-07-26 17:11:40
@LastEditTime: 2020-07-26 17:51:36
@FilePath: /python_code/code01/autoLogin.py
'''
# 通过密码登陆回去cookies


from urllib import request, parse
from http.cookiejar import CookieJar


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}


def get_opener():

    cookie = CookieJar()

    opener = request.build_opener(request.HTTPCookieProcessor(cookie))

    return opener


def go_login(opener):

    data = {
        "email": "17789108460", "password": "4655123411@@"
    }
    url = request.Request('http://www.renren.com/PLogin.do',
                          data=parse.urlencode(data).encode(), headers=headers)
    opener.open(url)


def go_personal_page(opener):

    url = request.Request(
        'http://www.renren.com/880151247/profile', headers=headers)
    resp = opener.open(url)
    with open('renren.html', 'w') as fp:
        fp.write(resp.read().decode("utf-8"))


if __name__ == '__main__':
    opener = get_opener()
    go_login(opener)
    go_personal_page(opener)
