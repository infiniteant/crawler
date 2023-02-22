'''
requests.exceptions.SSLError: HTTPSConnectionPool(host='ssr1.scrape.center', port=443): Max retries exceeded with url: 
/ (Caused by SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1122)')))
代理问题
'''

import requests

response = requests.get('http://www.baidu.com')
print(type(response))
print(response.status_code)
print(type(response.text))
print(response.text[:100])
print(response.cookies)

response = requests.get('http://www.httpbin.org/get')
response = requests.post('http://www.httpbin.org/post')
response = requests.put('http://www.httpbin.org/put')
response = requests.delete('http://www.httpbin.org/delete')
response = requests.patch('http://www.httpbin.org/patch')

GET请求
response = requests.get('http://www.httpbin.org/get')
print(response.text)


data = {
    'name': 'germey',
    'age': 25
}
response = requests.get('http://www.httpbin.org/get', params=data)
print(response.text)
print(response.json())
print(type(response.json()))


# 抓取网页
import re

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}
response = requests.get('https://ssr1.scrape.center/', headers=headers)
pattern = re.compile('<h2.*?>(.*?)</h2>', re.S)
title = re.findall(pattern, response.text)
print(title)

# 抓取二进制数据
response = requests.get('https://scrape.center/favicon.ico')
print(response.text)
print(response.content)

response = requests.get('https://scrape.center/favicon.ico')
with open('favicon.ico', 'wb') as f:
    f.write(response.content)

# 添加请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}
response = requests.get('https://scrape.center/', headers=headers)
print(response.text)


POST请求

data = {'name': 'germey', 'age': '25'}
response = requests.post('https://www.httpbin.org/post', data=data)
print(response.text)


# 响应
response = requests.get('https://ssr1.scrape.center/')
print(type(response.status_code), response.status_code)
print(type(response.headers), response.headers)
print(type(response.cookies), response.cookies)
print(type(response.url), response.url)
print(type(response.history), response.history)

状态码
response = requests.get('https://ssr1.scrape.center/')
exit() if not response.status_code == requests.codes.ok else print('Resquest Successfully')

# 文件上传
files = {'file': open('favicon.ico', 'rb')}
response = requests.post('https://www.httpbin.org/post', files=files)
print(response.text)


# Cookie设置
response = requests.get('https://www.baidu.com')
print(response.cookies)
for key, value in response.cookies.items():
    print(key + '=' + value)

headers = {
    'cookie': '_octo=GH1.1.756088770.1670570324; _device_id=f771e5da596b343d6deb643eebc120cb; user_session=6-a0i3nW0d3xjRK5S-VqibL34XOGbpS_7mq3mg4EKVWpC--R; __Host-user_session_same_site=6-a0i3nW0d3xjRK5S-VqibL34XOGbpS_7mq3mg4EKVWpC--R; logged_in=yes; dotcom_user=infiniteant; has_recent_activity=1; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; preferred_color_mode=dark; tz=Asia%2FShanghai; _gh_sess=1Sy6Vdx5HDUyDAfnRhgLGTm91JsDQfg%2Fh3PKXigVKk5y8EB8YB3aRLBhmP3xD85xcMKutZwhnddyF5NfsW3Ac4XMLwEBlDY%2BbazK25a%2FGLg%2FJO%2Bj88dGTXUZPsdyjPxY67zHa7ePEPpP4QuCNPn4CZQfr4G5u0izRaRIDqfFPXNQaF7p2hHnKn9Cjfh4On1KuaC1wkgw0efVHN0otfY68nAK9OJEFQr9Z19qnPTGnpIoTJvRonsMU1gtUyp2KXUHvWlPlf9rpYlQP4PprSuUFhRO0DOtUFrcVZAbL8loMAfyvfjljJLrgcU%3D--2hXqkr3otUIfH9pr--9cpYCXBQx4H0lKk3zwZwwA%3D%3D'
}

response = requests.get('https://github.com/', headers=headers)
print(response.text)

cookies = '_octo=GH1.1.756088770.1670570324; _device_id=f771e5da596b343d6deb643eebc120cb; user_session=6-a0i3nW0d3xjRK5S-VqibL34XOGbpS_7mq3mg4EKVWpC--R; __Host-user_session_same_site=6-a0i3nW0d3xjRK5S-VqibL34XOGbpS_7mq3mg4EKVWpC--R; logged_in=yes; dotcom_user=infiniteant; has_recent_activity=1; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; preferred_color_mode=dark; tz=Asia%2FShanghai; _gh_sess=1Sy6Vdx5HDUyDAfnRhgLGTm91JsDQfg%2Fh3PKXigVKk5y8EB8YB3aRLBhmP3xD85xcMKutZwhnddyF5NfsW3Ac4XMLwEBlDY%2BbazK25a%2FGLg%2FJO%2Bj88dGTXUZPsdyjPxY67zHa7ePEPpP4QuCNPn4CZQfr4G5u0izRaRIDqfFPXNQaF7p2hHnKn9Cjfh4On1KuaC1wkgw0efVHN0otfY68nAK9OJEFQr9Z19qnPTGnpIoTJvRonsMU1gtUyp2KXUHvWlPlf9rpYlQP4PprSuUFhRO0DOtUFrcVZAbL8loMAfyvfjljJLrgcU%3D--2hXqkr3otUIfH9pr--9cpYCXBQx4H0lKk3zwZwwA%3D%3D'
jar = requests.cookies.RequestsCookieJar()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}
for cookie in cookies.split(';'):
    key, value = cookie.split('=', 1)
    jar.set(key, value)
response = requests.get('https://github.com/', cookies=jar, headers=headers)
print(response.text)


Session
requests.get('https://www.httpbin.org/cookies/set/number/123456789')
response = requests.get('https://www.httpbin.org/cookies')
print(response.text)


s = requests.Session()
s.get('https://www.httpbin.org/cookies/set/number/123456789')
response = s.get('https://www.httpbin.org/cookies')
print(response.text)


# SSL证书验证
response = requests.get('https://ssr2.scrape.center/', verify=False)
print(response.status_code)

from requests.packages import urllib3

urllib3.disable_warnings()
response = requests.get('https://ssr2.scrape.center/', verify=False)
print(response.status_code)


import logging
logging.captureWarnings(True)
response = requests.get('https://ssr2.scrape.center/', verify=False)
print(response.status_code)

# 可以指定本地证书作为客户端证书，可以是单个文件(包括密钥和证书)或一个包含两个文件路径的元组
response = requests.get('https://ssr2.scrape.center/', cert=('/path/server.crt', 'path/server.key'))
print(response.status_code)

# 超时设置
# connect and read总和
response = requests.get('https://www.httpbin.org/get', timeout=1)
print(response.status_code)

# 分别设置
response = requests.get('https://www.httpbin.org/get', timeout=(5,30))
print(response.status_code)

永久等待设置为None或者不设置
response = requests.get('https://www.httpbin.org/get', timeout=None)
response = requests.get('https://www.httpbin.org/get')


# 身份认证
from requests.auth import HTTPBasicAuth

response =requests.get('https://ssr3.scrape.center/', auth=HTTPBasicAuth('admin', 'admin'))
print(response.status_code)


# 简单写法
response =requests.get('https://ssr3.scrape.center/', auth=('admin', 'admin'))
print(response.status_code)


# OAuth认证
from requests_oauthlib import OAuth1

url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET', 'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
response = requests.get(url, auth=auth)
print(response.text)


# 代理设置
proxies = {
    'http': 'http://10.10.10.10:1080',
    'https': 'https://10.10.10.10:1080',
}

# 若代理需要用户认证可以这样设置
proxies = {'https': 'http://user:password@10.10.10.10:1080/',}
requests.get('https://www.httpbin.org/get', proxies=proxies)

# 除了HTTP代理，还支持SOCKS协议的代理
proxies = {
    'http': 'socks5://user:password@host:port',
    'https': 'socks5://user:password@host:port',
}
requests.get('https://www.httpbin.org/get', proxies=proxies)

# Resquest对象
url = 'https://www.httpbin.org/post'
data = {'name': 'germey'}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}
s = requests.Session()
req = requests.Request('POST', url, data=data, headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)