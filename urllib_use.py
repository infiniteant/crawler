''' 使用urllib库'''

# # urllib库有四个模块 
import urllib.request
# import urllib.error
# import urllib.parse
# import urllib.robotparser


# # 对于这个库最简单的使用
# response = urllib.request.urlopen('https://www.python.org')
# print(response.read().decode('utf-8'))
# print(type(response))


# # http.client.HTTPResponse对象，以及这些对象的方法和属性
# from http.client import HTTPResponse
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Server'))


# # urlopen()方法的参数
# '''
# def urlopen(url, data=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT,
#             *, cafile=None, capath=None, cadefault=False, context=None): ...
# '''
# # data 参数
# data = bytes(urllib.parse.urlencode({'name': 'germey'}), encoding='utf-8')
# response = urllib.request.urlopen('https://www.httpbin.org/post', data=data)
# print(response.read().decode('utf-8'))

# # timeout 参数
# response = urllib.request.urlopen('https://www.httpbin.org/get', timeout=0.1)
# print(response.read())

# # 处理异常
# import socket
# import urllib.response
# # 上面引入了该库
# # import urllib.error
# try:
#     response = urllib.request.urlopen('https://www.httpbin.org/get', timeout=0.1)
# except urllib.error.URLError as e:
#     if isinstance(e.reason, socket.timeout):
#         print('TIMEOUT')


# # Resquest
# request = urllib.request.Request('https://python.org')
# response = urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))

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
