# # txt存储
# import requests
# from pyquery import PyQuery as pq
# import re

# url = "https://ssr1.scrape.center/"
# html = requests.get(url).text
# doc = pq(html)
# items = doc('.el-card').items()

# with open('movies.txt', 'w', encoding='utf-8') as file:
#     for item in items:
#         # 电影名称
#         name = item.find('a > h2').text()
#         file.write(f'名称：{name}\n')
#         # 类别
#         categories = [item.text() for item in item.find('.categories button span').items()]
#         file.write(f'类别：{categories}')
#         # 上映时间
#         published_at = item.find('.info:contains(上映)').text()
#         published_at = re.search('(\d{4}-\d{2}-\d{2})', published_at).group(1) \
#         if published_at and re.search('\d{4}-\d{2}-\d{2}', published_at) else None
#         file.write(f'上映时间：{published_at}\n')
#         # 评分
#         score = item.find('p.score').text()
#         file.write(f'评分：{score}\n')
#         file.write(f'{"=" * 50}\n')

# # json格式
# import json
# str = '''
# [{
#     "name": "Bob",
#     "gender": "male",
#     "birthday": "1992-10-18"
# },{
#     "name": "Selina",
#     "gender": "female",
#     "birthday": "1995-10-18"
# }]
# '''
# print(type(str))
# data = json.loads(str)
# print(data)
# print(type(data))

# print(data[0]['name'])
# print(data[0].get('name'))

# print(data[0].get('age'))
# print(data[0].get('age', 25))

# # JSON需要使用双引号包围，不能使用单引号
# try:
#     str = '''
#     [{
#         'name': 'Bob',
#         'gender': 'male'
#     }]
#     '''
#     data = json.loads(str)
# except Exception as e:
#     print(e)

# with open('data.json', encoding='utf-8') as fp:
#     data_str = fp.read()
#     data = json.loads(data_str)
#     print(data)


# data = json.load(open('data.json', encoding='utf-8'))
# print(data)

# # 输出json

# data = [{
#     'name': 'Bob',
#     'gender': 'male',
#     'birthday': '1992-10-18'
# }]
# with open('data.json', 'w', encoding='utf-8') as fp:
#     fp.write(json.dumps(data))


# # indent缩进格式
# data = [{
#     'name': '王伟',
#     'gender': '男',
#     'birthday': '1992-10-18'
# }]
# with open('data.json', 'w', encoding='utf-8') as fp:
#     fp.write(json.dumps(data, indent=2))

# # 显示中文
# import json
# data = [{
#     'name': '王伟',
#     'gender': '男',
#     'birthday': '1992-10-18'
# }]
# with open('data.json', 'w', encoding='utf-8') as fp:
#     fp.write(json.dumps(data, indent=2, ensure_ascii=False))

# json.dump(data, open('data.json', 'w', encoding='utf-8'), indent=2, ensure_ascii=False)

# csv文件存储
import csv

# with open('data.csv', 'w') as fp:
#     writer = csv.writer(fp, delimiter=' ')
#     writer.writerow(['id', 'name', 'age'])
#     writer.writerow(['10001', 'Mike', 20])
#     writer.writerow(['10002', 'Bob', 22])
#     writer.writerow(['10003', 'Jordan', 21])

# with open('data.csv', 'w') as fp:
#     writer = csv.writer(fp)
#     writer.writerows([['id', 'name', 'age'],['10001', 'Mike', 20], ['10002', 'Bob', 22], ['10003', 'Jordan', 21]])

# # 追加
# with open('data.csv', 'a') as fp:
#     fieldnames = ['id', 'name', 'age']
#     writer = csv.DictWriter(fp, fieldnames=fieldnames)
#     writer.writerow({'id': 10004, 'name': 'Durant', 'age': 22})


# import csv

# with open('data.csv', 'a', encoding='utf-8') as fp:
#     fieldnames = ['id', 'name', 'age']
#     writer = csv.DictWriter(fp, fieldnames=fieldnames)
#     writer.writerow({'id': 10004, 'name': '王伟', 'age': 22})

# import pandas as pd

# data = [
#     {'id': '10001', 'name': 'Mike', 'age': 20},
#     {'id': '10002', 'name': 'Bob', 'age': 21},
#     {'id': '10003', 'name': 'Jordan', 'age': 22},
# ]
# df  = pd.DataFrame(data)
# df.to_csv('data.csv', index=False)

# # 读取
# import csv

# with open('data.csv', 'r', encoding='utf-8') as fp:
#     reader = csv.reader(fp)
#     for row in reader:
#         print(row)


# import pandas as pd
# df = pd.read_csv('data.csv')
# print(df)

# import pandas as pd

# df = pd.read_csv('data.csv')
# data = df.values.tolist()
# print(data)

# df = pd.read_csv('data.csv')
# for index, row in df.iterrows():
#     print(row.tolist())


