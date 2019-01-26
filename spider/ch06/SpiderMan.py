from URLManager import UrlManager
from HtmlDownloader import HtmlDownloader
from HtmlParser import HtmlParser
from DataOutput import DataOutput

class SpiderMan(object):
    def __init__(self):
        self.manager = UrlManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = DataOutput()
    def crawl(self, root_url):
        #添加入口url
        self.manager.add_new_url(root_url)
        #判断url管理器中是否有新的url，同时判断抓取了多少个url
        while(self.manager.has_new_url() and self.manager.old_url_size() < 100):
            try:
                #从url管理器获取新的url
                new_url = self.manager.get_new_url()
                #html下载器下载网页
                html = self.downloader.download(new_url)
                #html解析器抽取网页数据
                new_urls, data = self.parser.parser(new_url, html)
                #将抽取的url添加到url管理器中
                # self.manager.add_new_url(new_urls)    出现set不可hash问题，因为可迭代的数据是无法hash的
                for new_url in new_urls:
                    self.manager.add_new_url(new_url)
                #数据存储器存储文件
                self.output.store_data(data)
                print('已经抓取%s个链接' % self.manager.old_url_size())
            except Exception as e:
                print('crawl failed with' + str(e))
            #数据存储器将文件输出成指定格式

if __name__ == '__main__':
    spider_man = SpiderMan()
    spider_man.crawl("http://baike.baidu.com/view/284853.htm")