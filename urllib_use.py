''' 使用urllib库'''

# urllib库有四个模块 
import urllib.request
import urllib.error
import urllib.parse
import urllib.robotparser


# 对于这个库最简单的使用
response = urllib.request.urlopen('https://www.python.org')
print(response.read().decode('utf-8'))
print(type(response))


# http.client.HTTPResponse对象，以及这些对象的方法和属性
from http.client import HTTPResponse
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))


# urlopen()方法的参数
'''
def urlopen(url, data=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT,
            *, cafile=None, capath=None, cadefault=False, context=None): ...
'''
# data 参数
data = bytes(urllib.parse.urlencode({'name': 'germey'}), encoding='utf-8')
response = urllib.request.urlopen('https://www.httpbin.org/post', data=data)
print(response.read().decode('utf-8'))

# timeout 参数
response = urllib.request.urlopen('https://www.httpbin.org/get', timeout=0.1)
print(response.read())

# 处理异常
import socket
import urllib.response
# 上面引入了该库
# import urllib.error
try:
    response = urllib.request.urlopen('https://www.httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIMEOUT')


# Resquest
request = urllib.request.Request('https://python.org')
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))

# 测试参数
url = 'https://www.httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'Host': 'www.httpbin.org'
}
dict = {'name': 'germey'}
data = bytes(urllib.parse.urlencode(dict), encoding='utf-8')
request = urllib.request.Request(url=url, data=data, headers=headers, method='POST')
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))


# Handler
username = 'admin'
password = 'admin'
url = 'https://ssr3.scrape.center/'

p = urllib.request.HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)
auth_handler = urllib.request.HTTPBasicAuthHandler(p)
opener = urllib.request.build_opener(auth_handler)
try:
    result = opener.open(url)
    html = result.read().decode('utf-8')
    print(html)
except urllib.error.URLError as e:
    print(e)

# 代理
proxy_handler = urllib.request.ProxyHandler({
    'http': 'http://127.0.0.1:8080',
    'https': 'https://127.0.0.1:8080'
})
opener = urllib.request.build_opener(proxy_handler)
try:
    response = opener.open('https://www.baidu.com')
    print(response.read().decode('utf-8'))
except urllib.error.URLError as e:
    print(e.reason)

# Cookie
import http.cookiejar
# 因为上面已导入该库
# import urllib.request
cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('https://www.baidu.com')
for item in cookie:
    print(item.name + "=" + item.value)

# 将cookie导入文件中
# filename = 'mozilla_cookie.txt'
# cookie = http.cookiejar.MozillaCookieJar(filename)
# LWP格式文件
filename = 'lwp_cookie.txt'
cookie = http.cookiejar.LWPCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('https://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)

# 读取cookie文件
cookie = http.cookiejar.LWPCookieJar()
cookie.load('lwp_cookie.txt', ignore_discard=True, ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('https://www.baidu.com')
print(response.read().decode('utf-8'))


# 处理异常
# URLError
try:
    response = urllib.request.urlopen('https://cuiqingcai.com/404')
except urllib.error.URLError as e:
    print(e.reason)

# HTTPError
try:
    response = urllib.request.urlopen('https://cuiqingcai.com/404')
except urllib.error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')


# 先处理子类，再处理父类
try:
    response = urllib.request.urlopen('https://cuiqingcai.com/404')
except urllib.error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
except urllib.error.URLError as e:
    print(e.reason)
else:
    print('Request Successfully')

import socket
try:
    response = urllib.request.urlopen('https://www.baidu.com', timeout=0.01)
except urllib.error.URLError as e:
    print(e.reason)
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')


# 解析链接

# urlparse
result = urllib.parse.urlparse('https://www.baidu.com/index.html;user?id=5#comment')
print(type(result))
print(result)

result = urllib.parse.urlparse('www.baidu.com/index.html;user?id=5#comment', scheme='https')
print(result)

result = urllib.parse.urlparse('http://www.baidu.com/index.html;user?id=5#comment', scheme='https')
print(result)

result = urllib.parse.urlparse('https://www.baidu.com/index.html;user?id=5#comment', allow_fragments=False)
print(result)

result = urllib.parse.urlparse('https://www.baidu.com/index.html#comment', allow_fragments=False)
print(result)

result = urllib.parse.urlparse('https://www.baidu.com/index.html#comment', allow_fragments=False)
print(result.scheme, result[0], result.netloc, result[1], sep='\n')

# urlunparse
# 必须传入六个参数
data = ['https', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
print(urllib.parse.urlunparse(data))

# urlsplit
result = urllib.parse.urlsplit('https://www.baidu.com/index.html;user?id=5#comment')
print(result)

# 该方法得到的结果也是一个元组
result = urllib.parse.urlsplit('https://www.baidu.com/index.html;user?id=5#comment')
print(result[0])


# urlunsplit
# 同理该方法传入的参数必须为5
data = ['https', 'www.baidu.com', 'index.html', 'a=6', 'comment']
print(urllib.parse.urlunsplit(data))

# urljoin
from urllib.parse import urljoin
print(urljoin('https://www.baidu.com', 'FAQ.html'))
print(urljoin('https://www.baidu.com', 'https://cuiqingcai.com/FAQ.html'))
print(urljoin('https://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html'))
print(urljoin('https://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html?question=2'))
print(urljoin('https://www.baidu.com?wd=abc', 'https://cuiqingcai.com/index.php'))
print(urljoin('https://www.baidu.com', '?category=2#comment'))
print(urljoin('www.baidu.com', '?category=2#comment'))
print(urljoin('www.baidu.com#comment', '?category=2'))

# urlencode
from urllib.parse import urlencode

params = {
    'name': 'germey',
    'age': 25
}
base_url = 'https://www.baidu.com?'
url = base_url + urlencode(params)
print(url)

# parse_qs
from urllib.parse import parse_qs

query = 'name=germey&age=25'
print(parse_qs(query))

from urllib.parse import parse_qsl
query = 'name=germey&age=25'
print(parse_qsl(query))

# quote
from urllib.parse import quote

keyword = '壁纸'
url = 'https://www.baidu.com/s?wd=' + quote(keyword)
print(url)

# unquote
from urllib.parse import unquote
url = 'https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
print(unquote(url))


# Robots协议

from urllib.robotparser import RobotFileParser

rp = RobotFileParser()
rp.set_url('https://www.baidu.com/robots.txt')
rp.read()
print(rp.can_fetch('Baiduspider', 'https://www.baidu.com'))
print(rp.can_fetch('BaiduSpider', 'https://www.baidu.com/homepage/'))
print(rp.can_fetch('Googlebot', 'https://www.baidu.com/homepage/'))

# 也可以使用parse方法对robots.txt文件读取和分析
from urllib.request import urlopen
from urllib.robotparser import RobotFileParser

rp = RobotFileParser()
rp.parse(urlopen('https://www.baidu.com/robots.txt').read().decode('utf-8').split('\n'))
print(rp.can_fetch('Baiduspider', 'https://www.baidu.com'))
print(rp.can_fetch('BaiduSpider', 'https://www.baidu.com/homepage/'))
print(rp.can_fetch('Googlebot', 'https://www.baidu.com/homepage/'))
