from bs4 import BeautifulSoup
import requests

res = requests.get('https://www.baidu.com')
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.a.string)
