# # 例子一
# import asyncio
# from pyppeteer import launch
# from pyquery import PyQuery as pq

# async def main():
#     browser = await launch()
#     page = await browser.newPage()
#     await page.goto('https://spa2.scrape.center/')
#     await page.waitForSelector('.item .name')
#     doc = pq(await page.content())
#     names = [item.text() for item in doc('.item .name').items()]
#     print('Name:', names)
#     await browser.close()

# asyncio.get_event_loop().run_until_complete(main())


# # 例子二
# import asyncio
# from pyppeteer import launch

# width, height = 1366, 768

# async def main():
#     browser = await launch()
#     page = await browser.newPage()
#     await page.setViewport({'width': width, 'height': height})
#     await page.goto('https://spa2.scrape.center/')
#     await page.waitForSelector('.item .name')
#     await asyncio.sleep(2)
#     await page.screenshot(path='example.png')
#     dimensions = await page.evaluate('''() => {
#         return {
#             width: document.documentElement.clientWidth,
#             height: document.documentElement.clientHeight,
#             deviceScaleFactor: window.devicePixelRatio,
#         }
#     }''')
#     print(dimensions)
#     await browser.close()

# asyncio.get_event_loop().run_until_complete(main())

# launch方法


# # 无头模式
# import asyncio
# from pyppeteer import launch

# async def main():
#     await launch(headless=False)
#     await asyncio.sleep(100)

# asyncio.get_event_loop().run_until_complete(main())


# # 调试模式
# import asyncio
# from pyppeteer import launch

# async def main():
#     browser = await launch(devtools=True)
#     page = await browser.newPage()
#     await page.goto('https://www.baidu.com')
#     await asyncio.sleep(60)
# asyncio.get_event_loop().run_until_complete(main())


# # 禁用提示条
# import asyncio
# from pyppeteer import launch

# async def main():
#     browser = await launch(headless=False, args=['--disable-infobars'])
#     page = await browser.newPage()
#     await page.goto('https://www.baidu.com')
#     await asyncio.sleep(60)
# asyncio.get_event_loop().run_until_complete(main())


# 防止检测
# import asyncio
# from pyppeteer import launch

# async def main():
#     browser = await launch(headless=False, args=['--disable-infobars'])
#     page = await browser.newPage()
#     await page.goto('https://antispider1.scrape.center/')
#     await asyncio.sleep(5)

# asyncio.get_event_loop().run_until_complete(main())

# # 使用evaluateOnNewDocument方法
# import asyncio
# from pyppeteer import launch

# async def main():
#     browser = await launch(headless=False, args=['--disable-infobars'])
#     page = await browser.newPage()
#     await page.evaluateOnNewDocument('Object.defineProperty(navigator, "webdriver", {get: () => undefined})')
#     await page.goto('https://antispider1.scrape.center/')
#     await asyncio.sleep(20)

# asyncio.get_event_loop().run_until_complete(main())

# # 页面大小设置
# import asyncio
# from pyppeteer import launch

# width, height = 1366, 768

# async def main():
#     browser = await launch(headless=False, args=['--disable-infobars', f'--window-size={width},{height}'])
#     page = await browser.newPage()
#     # await page.setViewport({'width': width, 'height': height})
#     await page.evaluateOnNewDocument('Object.defineProperty(navigator, "webdriver", {get: () => undefined })')
#     await page.goto('https://antispider1.scrape.center/')
#     await asyncio.sleep(20)

# asyncio.get_event_loop().run_until_complete(main())


# # 用户数据持久化
# import asyncio
# from pyppeteer import launch

# async def main():
#     browser = await launch(headless=False, userDataDir='./userdata', args=['--disable-infobars'])
#     page = await browser.newPage()
#     await page.goto('https://www.taobao.com')
#     await asyncio.sleep(20)

# asyncio.get_event_loop().run_until_complete(main())


# # Browser

# # 开启无痕模式

# import asyncio
# from pyppeteer import launch

# width, height = 1366, 768

# async def main():
#     browser = await launch(headless=False, args=['--disable-infobars', f'--window-size={width},{height}'])
#     context = await browser.createIncognitoBrowserContext()
#     page = await context.newPage()
#     await page.setViewport({'width': width, 'height': height})
#     await page.goto('https://www.baidu.com')
#     await asyncio.sleep(20)

# asyncio.get_event_loop().run_until_complete(main())

# # 关闭

# import asyncio
# from pyppeteer import launch
# from pyquery import PyQuery as pq

# async def main():
#     browser = await launch()
#     page = await browser.newPage()
#     await page.goto('https://spa2.scrape.center/')
#     await browser.close()

# asyncio.get_event_loop().run_until_complete(main())

# # Page
# # 选择器
# import asyncio
# from pyppeteer import launch
# from pyquery import PyQuery as pq

# async def main():
#     browser = await launch()
#     page = await browser.newPage()
#     await page.goto('https://spa2.scrape.center/')
#     await page.waitForSelector('.item .name')
#     j_result1 = await page.J('.item .name')
#     j_result2 = await page.querySelector('.item .name')
#     jj_result1 = await page.JJ('.item .name')
#     jj_result2 = await page.querySelectorAll('.item .name')
#     print('J Result1:', j_result1)
#     print('J Result2:', j_result2)
#     print('JJ Result1:', jj_result1)
#     print('JJ Result2:', jj_result2)
#     await browser.close()

# asyncio.get_event_loop().run_until_complete(main())

# # 选项卡操作
# import asyncio
# from pyppeteer import launch

# async def main():
#     browser = await launch(headless=False)
#     page = await browser.newPage()
#     await page.goto('https://www.baidu.com')
#     page = await browser.newPage()
#     await page.goto('https://www.bing.com')
#     pages = await browser.pages()
#     print('Pages:', pages)
#     page1 = pages[1]
#     await page1.bringToFront()
#     await asyncio.sleep(20)

# asyncio.get_event_loop().run_until_complete(main())

# 页面操作
import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq

