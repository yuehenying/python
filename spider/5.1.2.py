import csv
'''
# csv文件的写入
headers = ['ID','UserName','Password','Age','Country']
rows = [(1001,"qiye","qiye_pass",24,"China"),
         (1002,"Mary","Mary_pass",20,"USA"),
         (1003,"Jack","Jack_pass",20,"USA"),
       ]

with open('qiye.csv', 'w', newline = '') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)
'''

'''
with open('qiye.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    print(headers)
    for row in f_csv:
        print(row)
'''

'''
# 使用命名分组
from collections import namedtuple
import csv
with open('qiye.csv') as f:
    f_csv = csv.reader(f)
    headings = next(f_csv)
    Row = namedtuple('Row', headings)
    for r in f_csv:
        row = Row(*r)
        print(row.UserName, row.Password)
        print(row)
'''

'''
# 读取到字典中
with open('qiye.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        print(row.get('UserName'), row.get('Password'))
'''

import requests
import re
from lxml import etree

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'
headers = {
    'User-Agent': user_agent
}
res = requests.get('http://seputu.com/', headers = headers)
# 使用lxml解析
html = etree.HTML(res.text)
div_mulus = html.xpath('.//div[@class="mulu"]')
rows = []
for div_mulu in div_mulus:
    div_h2 = div_mulu.xpath('./div[@class="mulu-title"]/center/h2/text()')
    if len(div_h2) > 0:
        # 加上utf-8是为了统一数据格式
        h2_title = div_h2[0].encode('utf-8')
        a_s = div_mulu.xpath('./div[@class="box"]/ul/li/a')
        for a in a_s:
            href = a.xpath('./@href')[0].encode('utf-8')
            box_title = a.xpath('./@title')[0]
            pattern = re.compile(r'\[(.*)\]\s+(.*)')
            match = pattern.search(box_title)
            if match != None:
                date = match.group(1).encode('utf-8') 
                real_title = match.group(2).encode('utf-8')
                content = (h2_title, real_title, href, date)
                rows.append(content)
headers = ['title', 'realtitle', 'href', 'date']
with open('qiye.csv', 'w') as f:
    f_csv = csv.writer(f,)
    f_csv.writerow(headers)
    f_csv.writerows(rows)
    
            

