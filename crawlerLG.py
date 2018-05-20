# coding = utf-8

import requests
import json
from lxml import etree
import csv
from crawler.lagou.storeData import StoreData
import pymysql
import random
import time

class CrawlerLaGou():
    '''
    爬取拉钩网的python职位
    '''

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
            'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=false&suginput=',
            'Cookie':'_ga=GA1.2.1399487501.1520475515; user_trace_token=20180308102020-3fe78cd4-2277-11e8-a098-525400f775ce; LGUID=20180308102020-3fe790ac-2277-11e8-a098-525400f775ce; JSESSIONID=ABAAABAAADEAAFI56226E6740F3159A4397A17B7195AEA5; _gid=GA1.2.1881942229.1526445622; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1526445622; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=index_search; _gat=1; LGSID=20180517090510-58a11d50-596e-11e8-86c4-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1526519085; LGRID=20180517090517-5cfba99d-596e-11e8-b18d-525400f775ce; SEARCH_ID=ab9eaae4a3c544d4af77b5cfb5292829',
            'Host': 'www.lagou.com'
        }

        # '''
        # 建表格存储
        # with open('lagou.csv', 'a', encoding='utf-8') as f:
        #     f.write('公司,职称,年限,学历,城市,薪酬,融资,企业优势,公司规模' + '\n')
        # '''

        # config = {
        #     'host': '127.0.0.1',
        #     'port': 3306,
        #     'user': 'root',
        #     'password': '123456',
        #     'db': 'test_demo',
        #     'charset': 'utf8',
        #     'cursorclass': pymysql.cursors.DictCursor,
        #     'autocommit': True
        # }
        #
        # self.db = pymysql.connect(**config)
        # self.cursor = self.db.cursor()
        self.start_page = 1
        # self.end_page = 0
        # self.page_size = 15

    def parse_url(self, url, page):
        post_data = {
            'first': 'false',
            'pn': page,
            'kd': 'python'
        }
        response = requests.post(url, data=post_data, headers=self.headers).text
        return response, post_data

    def get_content_list(self, json_data):
        dict_res = json.loads(json_data)
        result_list = dict_res['content']['positionResult']['result']
        # self.result_size = int(dict_res['content']['positionResult']['resultSize'])
        # self.totleCount = int(dict_res['content']['positionResult']['totalCount'])
        list_data = []
        for result in result_list:
            res = {}
            res['COMPANY'] = result['companyShortName']
            res['POSITION'] = result['positionName']
            res['WORKYEAR'] = result['workYear']
            res['EADUCATION'] = result['education']
            res['CITY'] = result['city']
            res['SALARY'] = result['salary']
            res['FINANCESTAGE'] = result['financeStage']
            res['POSITIONADVANTAGE'] = result['positionAdvantage']
            res['COMPANYSIZE'] = result['companySize']
            print(res)
            list_data.append(res)
        return list_data

    def run(self, end_page):
        cityList = ['深圳', '上海', '北京']
        for city in cityList:
            print('正在打印%s' % city)
            myurl = 'https://www.lagou.com/jobs/positionAjax.json?city={}&needAddtionalResult=false&isSchoolJob=0'.format(
                city)
            # self.end_page = self.totleCount / self.page_size + 1
            for current_page in range(self.start_page, end_page):
                # 缺陷，如果当前爬取的总页码小于end_page，会有问题，下次优化
                if current_page % 5 == 0:
                    time.sleep(random.randint(5, 10))
                json_res, post_data = self.parse_url(myurl, current_page)
                print('*' * 20 + '正在打印第%s页' % (post_data['pn']) + '*' * 20)
                list_content = self.get_content_list(json_res)
                # StoreData.saveByCsv(list_content)
                st = StoreData()
                st.saveByMysql(list_content)
                st.saveByCsv(list_content)







