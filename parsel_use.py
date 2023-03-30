html = '''
<div>
    <ul>
        <li class="item-0">first item</li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-0 activate"><a href="link3.html"><span class="bold">third item</span></a></li>
        <li class="item-1 activate"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a></li>
    </ul>
</div>
'''

# 初始化
from parsel import Selector
selector = Selector(text=html)
items = selector.css('.item-0')
print(len(items), type(items), items)
items2 = selector.xpath('//li[contains(@class, "item-0")]')
print(len(items2), type(items2), items2)

# 提取文本
from parsel import Selector
selector = Selector(text=html)
items = selector.css('.item-0')
for item in items:
    text = item.xpath('.//text()').get()
    print(text)

result = selector.xpath('//li[contains(@class, "item-0")]//text()').get()
print(result)

result = selector.xpath('//li[contains(@class, "item-0")]//text()').getall()
print(result)

result = selector.css('.item-0 *::text').getall()
print(result)

# 提取属性
from parsel import Selector
selector = Selector(text=html)
result = selector.css('.item-0.activate a::attr(href)').get()
print(result)
result = selector.xpath('//li[contains(@class, "item-0") and contains(@class, "activate")]/a/@href').get()
print(result)

# 正则提取
from parsel import Selector
selector = Selector(text=html)
result = selector.css('.item-0').re('link.*')
print(result)

from parsel import Selector
selector = Selector(text=html)
result = selector.css('.item-0 *::text').re('.*item')
print(result)


from parsel import Selector
selector = Selector(text=html)
result = selector.css('.item-0').re_first('<span class="bold">(.*?)</span>')
print(result)