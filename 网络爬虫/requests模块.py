# import requests

# POST请求
# data = {'name': 'tom', 'pass': '123456'}
# url = 'https://www.iqianyue.com/mypost/'
# post = requests.post(url, data=data)
# print(post.text)  # 以文本格式返回结果

# GET请求
# url = 'https://www.taobao.com'
# response = requests.get(url)
# # print(response.text)  # 文本显示
# data = response.content  # content返回字节流
# print(data.decode('utf-8'))  # 转码

# headers头部反爬机制
# url = 'http://www.dianping.com/'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
# # response = requests.get(url)
# response = requests.get(url, headers=headers, timeout=0.1)
# data = response.content.decode('utf-8')
# # print(data)  # 不加headers只出现一部分数据
# print(data)

# 跳过登录得到登录后的数据信息
# 登录前
# data = requests.get('https://www.baidu.com').content.decode('utf-8')
# print(data)
# with open('百度登录前.html','w',encoding='utf-8') as f:
#     f.write(data)
# 登录后:创建表单数据cookies
# text = 'BIDUPSID=001B9A19F8B107BE2D216BA437F7CF1E; PSTM=1566784732; BD_UPN=12314353; BAIDUID=79DD0344AAA13834E85E28F8BC88C8AD:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; Hm_lvt_9f14aaa038bbba8b12ec2a4a3e51d254=1570520146; delPer=0; H_PS_PSSID=1425_21124_29721_29567_29220_26350; BD_CK_SAM=1; PSINO=5; shifen[48580593514_13628]=1570605363; shifen[110595446534_81398]=1570606075; BCLID=10491449518804526436; BDSFRCVID=L1LOJeC62w0PTx5ww8aYhURbCe6gK6jTH6aI_QR66Z7PKBX5H6gQEG0PeM8g0KubcYoEogKK0eOTHkCF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=JJP8_I0MfCvbfP0kMt5qMtK8hxtX5-RLfKJxVp7F5l8-hRRayx6T3b-Wea3japQNKe7-0DoJMxjxOKQphn6Sblky-JjM5bONJ27BKU5N3KJme4P9bT3v5Du_htTU2-biWbR-2Mbd2hOP_IoG2Mn8M4bb3qOpBtQmJeTxoUJ25DnJhhCGe6LbejO3jN0s-njKKKIX_Cj_ab__Hn7zePOPQbtpbtbmhU-e2DTPo-35fnjBMt5VyTrx2jkgqf54-Pv8Qb7ZVDD5fCtMMItr5b5H-PQHjHQB2-DXKKOLVMOD04OkeqOJ2Mt5M4LADpJfqPow5eTH0n4aMCncKJoH5-7B3TtpeGKqq6_8JRuJV-b-KROqKCKlM4nDq4tehHRrJx79WDTm_Do5tUJxJK565T7HWtkA0x5mK65MWbcB-pPKKlTrVf_CjlCb0MPYWao7ttbI3mkjbn5zfn02OP5P-proQt4syP4jKxRnWI3mKfA-b4ncjRcTehoM3xI8LNj405OTbIFO0KJzJCcjqR8Ze5tajf5; COOKIE_SESSION=664_1_7_7_5_27_0_4_7_5_68_5_72_1570605364_137_50_1570606163_1570606076_1570606026%7C9%23664_160_1570606026%7C9; BDUSS=EVrcVZFWVNPUEROYjhGdWRabWhFdkFTdmZBeDJGfm9wVFVQfkZWNy1FWklMOFZkSUFBQUFBJCQAAAAAAAAAAAEAAADt2SxgzfXn5ufmbAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEiinV1Iop1dO; BD_HOME=1'
# a = text.split('; ')  # 根据; 分割
# dict1 = {}
# # print(a)
# for i in a:
#     # print(i.split('=', 1))
#     b = i.split('=', 1)
#     dict1[b[0]] = b[1]
# # print(dict1)
# data = requests.get('http://www.baidu.com', cookies=dict1).content.decode('utf-8')
# print(data)
# with open('百度登录后.html', 'w', encoding='utf-8') as f:
#     f.write(data)

# 作业：抓取淘宝48个主体信息
url = 'https://www.taobao.com'
import urllib.request
import re

response = urllib.request.urlopen(url).read().decode('utf-8')
# print(response)
# 解析正则表达式
re1 = re.compile('<a href="(.*?)" data-cid="1" data-dataid=".*?">(.*?)</a>')
res1 = re.findall(re1, response)
for i in res1:
    # print(i[0])
    if 'https:' in i[0]:
        print(i[0], i[1])
    else:
        print('https:' + i[0], i[1])

print('-----------------------------------------------------------------------------------------------------------')

import requests

data = requests.get(url).content.decode('utf-8')
# print(data)
# 解析正则表达式
re2 = re.compile('<a href="(.*?)" data-cid="1".*?>(.*?)</a>')
res2 = re.findall(re2, data)
for i in res2:
    # print(i[0])
    if 'https:' in i[0]:
        print(i[0], i[1])
    else:
        print('https:' + i[0], i[1])
