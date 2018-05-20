# coding = utf-8
import csv,pymysql

class StoreData(object):
    '''
    USER test_demo;
    DROP TABLE IF EXISTS `lg_demo`;
    CREATE TABLE `lg_demo`(
    `ID` INT(11) NOT NULL AUTO_INCREMENT COMMENT '自增ID',
    `COMPANY` VARCHAR(50) DEFAULT NULL COMMENT '公司名',
    `POSITION` VARCHAR(20) DEFAULT NULL COMMENT '职位名称',
    `WORKYEAR` VARCHAR(20) DEFAULT NULL COMMENT '工作年限',
    `EADUCATION` VARCHAR(20) DEFAULT NULL COMMENT '学历',
    `CITY` VARCHAR(20) DEFAULT NULL COMMENT '城市',
    `SALARY` VARCHAR(20) DEFAULT NULL COMMENT '薪水',
    `FINANCESTAGE` VARCHAR(20) DEFAULT NULL COMMENT '融资情况',
    `POSITIONADVANTAGE` VARCHAR(20) DEFAULT NULL COMMENT '企业优势',
    `COMPANYSIZE` VARCHAR(200) DEFAULT NULL COMMENT '规模',
    PRIMARY KEY (`ID`)
    )AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT '拉钩网数据存储表'
    '''
    def __init__(self):
        self.config = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'password': '123456',
            'db': 'test_demo',
            'charset': 'utf8',
            'cursorclass': pymysql.cursors.DictCursor,
            'autocommit': True
        }

        # self.db = pymysql.connect(**config)
        # self.cursor = self.db.cursor()

    '''
    目前的存储方式有csv跟mysql
    '''
    def saveByCsv(self, list_data):
        with open('lagou.csv', 'a', encoding='utf-8') as f:
            f.write('公司,职称,年限,学历,城市,薪酬,融资,企业优势,公司规模' + '\n')
        for each in list_data:
            data_temp = [each['COMPANY'],each['POSITION'], each['WORKYEAR'], each['EADUCATION'], each['CITY'],each['SALARY'], each['FINANCESTAGE'],each['POSITIONADVANTAGE'], each['COMPANYSIZE']]
            with open('lagou.csv', 'a', encoding='utf-8') as f:
                temp_str = ','.join([str(i) for i in data_temp]) + '\n'
                f.write(temp_str)

    def saveByMysql(self, data_list):
        self.db = pymysql.connect(**self.config)
        self.cursor = self.db.cursor()
        for each in data_list:
            table = 'lg_demo'
            keys = ', '.join(each.keys())
            values = ', '.join(['%s'] * len(each))
            sql_insert_data = 'INSERT INTO {table} ({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
            try:
                self.cursor.execute(sql_insert_data, tuple(each.values()))
        # connect.commit() #配置了autocommit为True
            except:
                self.db.rollback()
        self.cursor.execute('select * from `lg_demo`')  # 执行sql语句
        # data = cursor.fetchone()  # 查一个
        data = self.cursor.fetchall() # 查所有
        # data = cursor.fetchmany(size=10)  # 指定查找size大小的数据量
        print(data)
        self.db.close()