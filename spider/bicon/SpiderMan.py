from URLManager import URLManager
from HtmlDownloader import HtmlDownloader
from HtmlParser import HtmlParser
from DataOutput import DataOutput

class SpiderMan(object):
    def __init__(self):
        self.manager = URLManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = DataOutput()
        self.page = 0
    
    def crawl(self, root_url):
        #添加起始url
        while (self.page <= 5):
            self.manager.add_new_url(root_url+str(self.page))
            self.page += 1
            try:
                new_url = self.manager.get_new_url()
                html = self.downloader.download(new_url)
                new_urls = self.parser.parser(new_url, html)
                for url in new_urls:
                    self.manager.add_new_url(url)
                while(self.manager.has_new_url()):
                    new_url = self.manager.get_new_url()
                    self.output.store_url(new_url)
            except Exception as e:
                print('crawl failed : ' + str(e))

if __name__ == '__main__':
    spider_man = SpiderMan()
    print('1.插画\n2.cosplay\n3.私服')
    num = input('请选择要下载的图片类型\n')
    if num == '1':
        spider_man.crawl('https://api.vc.bilibili.com/link_draw/v2/Doc/list?category=illustration&type=hot&page_size=20&page_num=')
    elif num == '2':
        spider_man.crawl('https://api.vc.bilibili.com/link_draw/v2/Photo/list?category=cos&type=hot&page_size=20&page_num=')
    else:
        spider_man.crawl('https://api.vc.bilibili.com/link_draw/v2/Photo/list?category=sifu&type=hot&page_size=20&page_num=')