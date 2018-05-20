# coding = utf-8

from crawler.lagou.crawlerLG import CrawlerLaGou

if __name__ == '__main__':
    lg = CrawlerLaGou()
    print('开始爬取...')
    lg.run(10)
    print('爬取结束')