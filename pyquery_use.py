# 字符串初始化
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
from pyquery import PyQuery as pq
doc = pq(html)
print(doc('li'))

# url初始化
from pyquery import PyQuery as pq
doc = pq(url="https://www.baidu.com")
# doc = pq(url="https://cuiqingcai.com")
print(doc('title'))

# 文件初始化
doc = pq(filename="demo.html")
print(doc('li'))

# 基本CSS选择器
from pyquery import PyQuery as pq

html = '''
<div id="container">
    <ul class="list">
        <li class="item-0">first item</li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-0 activate"><a href="link3.html"><span class="bold">third item</span></a></li>
        <li class="item-1 activate"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a></li>
    </ul>
</div>
'''
doc = pq(html)
print(doc('#container .list li'))
print(type(doc("#container .list li")))

for item in doc('#container .list li').items():
    print(item.text())

# 查找节点
# 子孙节点
doc = pq(html)
items = doc('.list')
print(type(items))
print(items)
lis = items.find('li')
print(type(lis))
print(lis)

# 只找子节点
lis = items.children()
print(type(lis))
print(lis)

lis = items.children('.activate')
print(lis)

# 父节点
html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
            <li class="item-0">first item</li>
            <li class="item-1"><a href="link2.html">second item</a></li>
            <li class="item-0 activate"><a href="link3.html"><span class="bold">third item</span></a></li>
            <li class="item-1 activate"><a href="link4.html">fourth item</a></li>
            <li class="item-0"><a href="link5.html">fifth item</a></li>
        </ul>
    </div>
</div>
'''
from pyquery import PyQuery as pq

doc = pq(html)
items = doc('.list')
container = items.parent()
print(type(container))
print(container)

# 祖先节点
from pyquery import PyQuery as pq

doc = pq(html)
items = doc('.list')
parents = items.parents()
print(type(parents))
print(parents)

parent = items.parents('.wrap')
print(parent)

# 兄弟节点
li = doc('.list .item-0.activate')
print(li.siblings())

print(li.siblings('.activate'))

# 遍历节点
from pyquery import PyQuery as pq
doc = pq(html)
li = doc('.item-0.activate')
print(li)
print(str(li))

lis = doc('li').items()
for li in lis:
    print(li, type(li))

# 获取信息
# 获取属性
html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
            <li class="item-0">first item</li>
            <li class="item-1"><a href="link2.html">second item</a></li>
            <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
            <li class="item-1 active"><a href="link4.html">fourth item</a></li>
            <li class="item-0"><a href="link5.html">fifth item</a></li>
        </ul>
    </div>
</div>
'''
from pyquery import PyQuery as pq
doc = pq(html)
a = doc('.item-0.active a')
print(a, type(a))
print(a.attr("href"))
print(a.attr.href)

# 获取文本
print(a.text())

from pyquery import PyQuery as pq
doc = pq(html)
li = doc('.item-0.active')
print(li)
print(li.html())

lis = doc('li')
print(lis.html())
print(lis.text())
print(type(lis.text()))

# 节点操作
from pyquery import PyQuery as pq
doc = pq(html)
li = doc('.item-0.active')
print(li)
li.removeClass('active')
print(li)
li.addClass('active')
print(li)

# attr text html
html = '''
<ul class="list">
    <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
</ul>
'''
from pyquery import PyQuery as pq
doc = pq(html)
li = doc('.item-0.active')
print(li)
li.attr('name', 'link')
print(li)
li.text('changed item')
print(li)
li.html('<span>changed item</span>')
print(li)

# remove 
html = '''
<div class="wrap">
    Hello, World
    <p>This is a paragraph.</p>
</div>
'''
from pyquery import PyQuery as pq

doc = pq(html)
wrap = doc('.wrap')
print(wrap.text())

wrap_remove = wrap.find('p').remove()
print(wrap.text())

# 伪类选择器
html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
            <li class="item-0">first item</li>
            <li class="item-1"><a href="link2.html">second item</a></li>
            <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
            <li class="item-1 active"><a href="link4.html">fourth item</a></li>
            <li class="item-0"><a href="link5.html">fifth item</a></li>
        </ul>
    </div>
</div>
'''
from pyquery import PyQuery as pq
doc = pq(html)
li = doc('li:first-child')
print(li)
li = doc('li:last-child')
print(li)
li = doc('li:nth-child(2)')
print(li)
li = doc('li:gt(2)')
print(li)
li = doc('li:nth-child(2n)')
print(li)
li = doc('li:contains(second)')
print(li)