# spiderLagou
>## 1.环境&工具
###### Python 3.6.4
###### PyCharm 2018.1 EAP
###### MySQL 5.7.21

>## 2.第三方的库
###### requests
###### json
###### csv
###### pymysql
###### random
###### time

>## 3.需求
 ##### 1)爬取拉勾平台的全国各地的python职业信息，包含的字段：公司名、职业名称、工作经验、学历要求、薪酬、融资阶段、企业优势、规模；
 ##### 2)有用数据提取做数据分析：公司名、职位名称、薪酬、职位描述、城市，初步分析python职位的在全国各地需求分布情况，薪酬情况，所需技能总结，然后再逐步对比其他语言职业需求。

>## 4.功能流程图

```
graph LR
开始-->输入拉钩url
输入拉钩url-->输入爬取的页码
输入爬取的页码-->发送post请求
发送post请求-->返回json数据

```

```
graph LR
返回json数据-->提取当前页的职业列表内容
提取当前页的职业列表内容-->去重
去重-->爬取职业详情页
爬取职业详情页-->下一页

```

```
graph LR
循环爬取所有的页职业列表-->将列表的字典内容入库
将列表的字典内容入库-->结束
```


<html>
<!--拉钩url->输入爬取的页码（不输默认全部）->发送post请求->返回json数据->提取当前页的职业列表内容->去重->爬取职业详情页->下一页，循环爬取所有的页职业列表->将列表的字典内容入库->关闭数据库，结束容-->
</html>


>## 5.关键代码-函数-参数-返回值
- [x] parse_url--爬取当前页的内容/ 参数--url,page/ 返回值--response，post data
- [x] get_content_list--拿到列表内容/ 参数--返回的response/ 返回值--入库的数据
- [x] saveByMysql--爬取的数据入库/ 参数--入库的数据/ 返回值--无,直接写到库中

```
response = requests.post(url, data=post_data, headers=self.headers).text
        return response, post_data
        
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
    list_data.append(res)           
 return list_data

 for each in data_list:
    table = 'lg_demo'
    keys = ', '.join(each.keys())
    values = ', '.join(['%s'] * len(each))
    sql_insert_data = 'INSERT INTO {table} ({keys}) VALUES
    ({values})'.format(table=table, keys=keys, values=values)
    try:
        self.cursor.execute(sql_insert_data, tuple(each.values()))
    # connect.commit()
    #配置了autocommit为True
    except:
        self.db.rollback()
```


>6.参考

>7.总结
