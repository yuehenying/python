import requests
import re
from bs4 import BeautifulSoup
import json

pattern = re.compile(r'\[((\d+)-){2}\d+ ((\d+):){2}\d+\]\s+')
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'
headers = {
    'User-Agent': user_agent
}
res = requests.get('http://seputu.com/', headers = headers)
soup = BeautifulSoup(res.text, 'html.parser', from_encoding = 'utf-8')
content = []
for mulu in soup.find_all(class_ = "mulu"):
    h2 = mulu.find('h2')
    if h2 != None:
        h2_title = h2.string
    box = mulu.find(class_ = 'box')
    list = []
    if box != None:
        for a in box.find_all('a'):
            href = a.get('href')
            # 将时间替换为空
            box_title = re.sub(pattern, '', a.get('title'))
            list.append({'href': href, 'box_title': box_title})
        content.append({'title': h2_title, 'content': list})
        with open('qiye.json', 'w') as fp:
            json.dump(content, fp = fp, indent = 4)