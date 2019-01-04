import requests
from bs4 import BeautifulSoup
import re

links = []
names = []
proxy = '127.0.0.1:25378'   #自己设置代理服务器地址
localPath = r'E:\pictures\P站\\'  #图片保存的路径
start_url = 'https://www.pixiv.net/bookmark.php'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
    'cookie': '', #填上自己的cookie，这里我就不放自己的cookie了
    'referer': 'https://www.pixiv.net/ranking.php?mode=daily&content=illust'
}
proxies = {
    'https': proxy
}
def download(url):
    res = requests.get(url,headers = headers,proxies = proxies)
    soup = BeautifulSoup(res.text,'html.parser')
    linkList = soup.select('._layout-thumbnail .ui-scroll-view')
    titleList = soup.select('.image-item .title') 

    for link in linkList:
        link = link['data-src'].replace('c/150x150/','')
        links.append(link)

    for t in titleList:
        t = t['title'].replace('\\','')
        names.append(t)
    
    next_link = soup.select('.pager-container span.next ._button')
    if(next_link):
        next_link = next_link[0]
        url = url + next_link['href']
        download(url)
    
def savePicture():
    for (pic,name) in zip(links,names):
        res = requests.get(url = pic,headers = headers,proxies = proxies)
        with open(localPath+name+'.jpg','wb') as f:
            f.write(res.content)
            print(name+'下载完毕')
    
download(start_url)
savePicture()
