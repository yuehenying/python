# coding:utf-8
'''
import requests
r = requests.get('https://www.baidu.com')
print r.content
print r.text
print r.encoding
r.encoding = 'utf-8'
print r.text
'''

'''
# 使用chardet检测编码
import requests
import chardet
r = requests.get('https://www.baidu.com')
print chardet.detect(r.content)
r.encoding = chardet.detect(r.content)['encoding']
print r.text
'''

import requests
r = requests.get('https://www.baidu.com', stream = True)
print r.raw.read(10)
