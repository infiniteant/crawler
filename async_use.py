# import requests
# import logging
# import time

# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s : %(message)s')
# TOTAL_NUMBER = 100
# BASIC_URL = 'https://www.httpbin.org/delay/5'

# start_time = time.time()
# for _ in range(1, TOTAL_NUMBER + 1):
#     logging.info('scraping %s', BASIC_URL)
#     response = requests.get(BASIC_URL)
# end_time = time.time()
# logging.info('total time %s seconds', end_time - start_time)


# 使用协程
# import asyncio

# async def execute(x):
#     print('Number:', x)

# coroutine = execute(1)
# print('Coroutine:', coroutine)
# print('After calling execute')

# loop = asyncio.get_event_loop()
# loop.run_until_complete(coroutine)
# print('After calling loop')

# import asyncio

# async def execute(x):
#     print('Number:', x)
#     return x

# coroutine = execute(1)
# print('Coroutine:', coroutine)
# print('After calling execute')

# loop = asyncio.get_event_loop()
# task = loop.create_task(coroutine)
# print('Task:', task)
# loop.run_until_complete(task)
# print('Task:', task)
# print('After calling loop')


# # 调用asyncio包的ensure_future
# import asyncio

# async def execute(x):
#     print('Number:', x)
#     return x

# coroutine = execute(1)
# print('Coroutine:', coroutine)
# print('After calling execute')

# task = asyncio.ensure_future(coroutine)
# print('Task:', task)
# loop = asyncio.get_event_loop()
# loop.run_until_complete(task)
# print('Task:', task)
# print('After calling loop')

# # 绑定回调
# import asyncio
# import requests

# async def request():
#     url = 'http://www.baidu.com'
#     status = requests.get(url)
#     return status

# def callback(task):
#     print('Status:', task.result())

# coroutine = request()
# task = asyncio.ensure_future(coroutine)
# task.add_done_callback(callback)
# print('Task:', task)

# loop = asyncio.get_event_loop()
# loop.run_until_complete(task)
# print('Task:', task)


# # 调用result()方法
# import asyncio
# import requests


# async def request():
#     url = 'http://www.baidu.com'
#     status = requests.get(url)
#     return status

# coroutine = request()
# task = asyncio.ensure_future(coroutine)
# print('Task:', task)

# loop = asyncio.get_event_loop()
# loop.run_until_complete(task)
# print('Task:', task)
# print('Task result:', task.result())

# # 多任务协程
# import asyncio
# import requests

# async def request():
#     url = 'https://www.baidu.com'
#     status = requests.get(url)
#     return status

# tasks = [asyncio.ensure_future(request()) for _ in range(5)]
# print('Task:', tasks)

# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))

# for task in tasks:
#     print('Task result:', task.result())

# # 协程实现
# import asyncio
# import requests
# import time

# start = time.time()

# async def request():
#     url = 'https://www.httpbin.org/delay/5'
#     print('Waiting for', url)
#     response = requests.get(url)
#     print('Get response from', url, 'response', response)

# tasks = [asyncio.ensure_future(request()) for _ in range(10)]
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))

# end = time.time()
# print('Cost time:', end - start)

# # 增加挂起
# import asyncio
# import requests
# import time

# start = time.time()

# async def request():
#     url = 'https://www.httpbin.org/delay/5'
#     print('Waiting for', url)
#     response = await requests.get(url)
#     print('Get response from', url, 'response', response)

# tasks = [asyncio.ensure_future(request()) for _ in range(10)]
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))

# end = time.time()
# print('Cost time:', end - start)

# 报错

# # 使用aiohttp库
# import asyncio
# import aiohttp
# import time

# start = time.time()

# async def get(url):
#     session = aiohttp.ClientSession()
#     response = await session.get(url)
#     await response.text()
#     await session.close()
#     return response

# async def request():
#     url = 'https://www.httpbin.org/delay/5'
#     print('Waiting for', url)
#     response = await get(url)
#     print('Get response from', url, 'response', response)

# tasks = [asyncio.ensure_future(request()) for _ in range(10)]
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))

# end = time.time()
# print('Cost time:', end - start)


# 测试并发
import asyncio
import aiohttp
import time

def test(number):
    start = time.time()

    async def get(url):
        session = aiohttp.ClientSession()
        response = await session.get(url)
        await response.text()
        await session.close()
        return response
    
    async def request():
        url = 'https://www.baidu.com'
        await get(url)

    tasks = [asyncio.ensure_future(request()) for _ in range(number)]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))

    end = time.time()

    print('Number:', number, 'Cost time:', end - start)

for number in [1, 3, 5, 10, 15, 30, 50, 75, 100, 200, 500]:
    test(number)