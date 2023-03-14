import requests

url = 'https://spa16.scrape.center/'
response = requests.get(url)
print(response.text)

import httpx

response = httpx.get('https://www.httpbin.org/get')
print(response.status_code)
print(response.headers)
print(response.text)


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}
response = httpx.get('https://www.httpbin.org/get', headers=headers)
print(response.text)

client = httpx.Client(http2=True)
response = client.get('https://spa16.scrape.center/')
print(response.text)
r = httpx.get('https://www.httpbin.org/get', params={'name': 'germey'})
print(r)
r = httpx.post('https://www.httpbin.org/post', data={'name': 'germey'})
print(r)
r = httpx.put('https://www.httpbin.org/put')
print(r)
r = httpx.delete('https://httpbin.org/delete')
print(r)
r = httpx.patch('https://httpbin.org/patch')
print(r)

# Client对象
with httpx.Client() as client:
    response = client.get('https://www.httpbin.org/get')
    print(response)

# 添加参数
url = 'https://httpbin.org/get'
headers = {'User-Agent': 'my-app/0.0.1'}
with httpx.Client(headers=headers) as client:
    r = client.get(url)
    print(r.json()['headers']['User-Agent'])

# 支持异步请求
import asyncio

async def fetch(url):
    async with httpx.AsyncClient(http2=True) as client:
        response = await client.get(url)
        print(response.text)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(fetch('https://www.httpbin.org/get'))