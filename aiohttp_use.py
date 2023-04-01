# # asyncio模块内部实现了对于TCP，UDP, SSL协议的异步操作，但是对于HTTP请求需要用aiohttp

# # 基本介绍
# # 服务端 客户端

# # 基本实例
# import aiohttp
# import asyncio

# async def fetch(session, url):
#     async with session.get(url) as response:
#         return await response.text(), response.status
    
# async def main():
#     async with aiohttp.ClientSession() as session:
#         html, status = await fetch(session, 'http://cuiqingcai.com')
#         print(f'html: {html[:100]}...')
#         print(f'status: {status}')
    
# if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())


# # URL参数设置
# import aiohttp
# import asyncio

# async def main():
#     params = {'name': 'germey', 'age':25}
#     async with aiohttp.ClientSession() as session:
#         async with session.get('https://www.httpbin.org/get', params=params) as response:
#             print(await response.text())

# if __name__ == "__main__":
#     asyncio.get_event_loop().run_until_complete(main())


# # 其他请求类型
# async def main():
#     async with aiohttp.ClientSession() as session:
#         session.post('http://www.httpbin.org/post', data=b'data')
#         session.put('http://www.httpbin.org/put', data=b'data')
#         session.delete('http://www.httpbin.org/delete')
#         session.head('http://www.httpbin.org/get')
#         session.options('http://www.httpbin.org/get')
#         session.patch('http://www.httpbin.org/patch', data=b'data')

# # POST请求
# import aiohttp
# import asyncio


# async def main():
#     data = {'name': 'germey', 'age': 25}
#     async with aiohttp.ClientSession() as session:
#         async with session.post('https://www.httpbin.org/post', data=b'data') as response:
#             print(await response.text())

# if __name__ == "__main__":
#     asyncio.get_event_loop().run_until_complete(main())

# # 提交json字符串
# import aiohttp
# import asyncio


# async def main():
#     data = {'name': 'germey', 'age': 25}
#     async with aiohttp.ClientSession() as session:
#         async with session.post('https://www.httpbin.org/post', json=data) as response:
#             print(await response.text())

# if __name__ == "__main__":
#     asyncio.get_event_loop().run_until_complete(main())

# # 响应
# import aiohttp
# import asyncio


# async def main():
#     data = {'name': 'germey', 'age': 25}
#     async with aiohttp.ClientSession() as session:
#         async with session.post('https://www.httpbin.org/post', data=data) as response:
#             print('status:', response.status)
#             print('headers:', response.headers)
#             print('body:', await response.text())
#             print('bytes:', await response.read())
#             print('json:', await response.json())

# if __name__ == "__main__":
#     asyncio.get_event_loop().run_until_complete(main())


# # 超时设置
# # 设置ClientTimeout对象设置超时
# import aiohttp
# import asyncio

# async def main():
#     timeout = aiohttp.ClientTimeout(total=2)
#     # timeout = aiohttp.ClientTimeout(total=1)
#     async with aiohttp.ClientSession(timeout=timeout) as session:
#         async with session.get('https://www.httpbin.org/get') as response:
#             print('atstus:', response.status)
        
# if __name__ == "__main__":
#     asyncio.get_event_loop().run_until_complete(main())


# # 并发限制
# import aiohttp
# import asyncio

# CONCURRENCY = 5
# URL = 'https://www.baidu.com'

# semaphore = asyncio.Semaphore(CONCURRENCY)
# session = None

# async def scrape_api():
#     async with semaphore:
#         print('scraping', URL)
#         async with session.get(URL) as response:
#             await asyncio.sleep(1)
#             return await response.text()

# async def main():
#     global session
#     session = aiohttp.ClientSession()
#     scrape_index_tasks = [asyncio.ensure_future(scrape_api()) for _ in range(10000)]
#     await asyncio.gather(*scrape_index_tasks)

# if __name__ == "__main__":
#     asyncio.get_event_loop().run_until_complete(main())


# aiohttp异步爬取实战
import asyncio
import aiohttp
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

INDEX_URL = 'https://spa5.scrape.center/api/book/?limit=18&offset={offset}'
DETAL_URL = 'https://spa5.scarpe.center/api/book/{id}'
PAGE_SIZE = 18
PAGE_NUMBER = 100
CONCURRENCY = 5
FILE = "aiohttp.txt"

# 爬取列表页
semaphore = asyncio.Semaphore(CONCURRENCY)
session = None

async def scrape_api(url):
    async with semaphore:
        try:
            logging.info('scraping %s', url)
            async with session.get(url) as response:
                return await response.json()
        except aiohttp.ClientError:
            logging.error('error occurred while scraping %s', url, exc_info=True)


async def scrape_index(page):
    url = INDEX_URL.format(offset=PAGE_SIZE * (page - 1))
    return await scrape_api(url)

import json

async def main():
    global session
    session = aiohttp.ClientSession()
    scrape_index_tasks = [asyncio.ensure_future(scrape_index(page)) for page in range(1, PAGE_NUMBER + 1)]
    results = await asyncio.gather(*scrape_index_tasks)
    logging.info('result %s', json.dumps(results, ensure_ascii=False, indent=2))

    await session.close()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())


    
    
    


