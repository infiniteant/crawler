import requests
import pcUserAgent


header = {
    'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel MAC OSX 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
}
response = requests.get('http://fanyi.youdao.com', headers=header)
print(response.text)

