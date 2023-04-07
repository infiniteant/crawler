# 调用
import requests

url = 'http://localhost:8050/render.html?url=https://www.baidu.com'
response = requests.get(url)
print(response.text)

# wait

import requests
url = 'http://localhost:8050/render.html?url=https://www.taobao.com&amp;wait=5'
response = requests.get(url)
print(response.text)


# render.png

import requests

url = 'http://localhost:8050/render.png?url=https://www.jd.com&wait=5&width=1000&height=700'
response = requests.get(url)
with open('jd.png', 'wb') as fp:
    fp.write(response.content)


# render.jpeg
# 比render.png多一个参数quality，该参数可以用来设置图片质量

# render.har
# 里面包含了页面加载过程中的HAR数据

# render.json


# execute
import requests
from urllib.parse import quote

lua = '''
function main(splash)
    return 'hello'
end
'''

url = 'http://localhost:8050/execute?lua_source=' + quote(lua)
response = requests.get(url)
print(response.text)


import requests
from urllib.parse import quote

lua = '''
function main(splash, args)
    local treat = require("treat")
    local response = splash:http_get("http://www.httpbin.org/get")
    return {html=treat.as_string(response.body),
        url=response.url,
        status=response.status
    }
end
'''

url = 'http://localhost:8050/execute?lua_source=' + quote(lua)
response = requests.get(url)
print(response.text)

# 负载均衡
# 配置负载均衡器Splash提供的API

# render.html

