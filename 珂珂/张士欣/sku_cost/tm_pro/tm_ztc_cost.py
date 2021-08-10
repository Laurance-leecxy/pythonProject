# -*- coding: utf-8 -*-
# @Time    : 2021/1/20 11:02
# @Author  : Paul
import json
import os
import random
import tempfile
import time
import urllib
import zipfile
from configparser import ConfigParser
from datetime import datetime, timedelta
import numpy as np
import pandas as pd
import pymysql
import requests
from apscheduler.schedulers.blocking import BlockingScheduler
from jsonpath import jsonpath
from retrying import retry
from sqlalchemy import create_engine

from send_file import WeChatRobot
import config

class TmCost():
    def __init__(self):
        self.headers = {
                        'origin': 'https://subway.simba.taobao.com',
                        'referer': 'https://subway.simba.taobao.com/index.jsp',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
                        'x-requested-with': 'XMLHttpRequest',
                        # 'Cookie': 't=fcddc5667879a47b9bae8b531d6bf346; cna=XUWMF2VUoGsCAXTkvN6vlV6H; cookie2=11c0f65bc7ddd2c55d521eae8a7546c7; _tb_token_=30e987836e585; xlly_s=1; adv-tutorial-bar-1111=1; v=0; alimamapwag=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV09XNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS83OC4wLjM5MDQuMTA4IFNhZmFyaS81MzcuMzY%3D; cookie32=c83865c69cb216fb6cbb5d1973f72f27; alimamapw=QHMiHCRRECRRRHF6Rnt1QyRwQHNWHCcgECJTRHQARnwHQyN1QHJRHCcjPFZRBQEOAg8DVgABUglW%0AWgRSVlVTUgZaUg8FAFYFAVUG; cookie31=MTE1NjIzMDEwMSwlRTglQjElQTElRTUlQjglOUQlRTYlOTUlQjAlRTclQTAlODElRTQlQjglOTMlRTglOTAlQTUlRTUlQkElOTcseGlhbmdkaXNodW1hQG1vYjE2OC5jb20sVEI%3D; taokeisb2c=; taokeIsBoutiqueSeller=eQ%3D%3D; login=UIHiLt3xD8xYTw%3D%3D; rurl=aHR0cHM6Ly9hZC5hbGltYW1hLmNvbS9yZXBvcnQvb3ZlcnZpZXcvb3JkZXJzLmh0bT9zcG09YTIxYW4uNzY3NjAwNy4xOTk4NDczMTgyLmRhZGY1YTZhMC42ZTZlNjFkYnlzUzdEcyZzdGFydFRpbWU9MjAyMS0wMS0yMyZlbmRUaW1lPTIwMjEtMDEtMjMmcGFnZU5vPTEmanVtcFR5cGU9MCZwb3NpdGlvbkluZGV4PQ%3D%3D; tfstk=cnZVBmDsgiIVNmo1JmiwGAYtksMAZLe0I3kIoPEbpNSfz20ciORtETOtUAa3lqf..; l=eB_aJAteOV4w8JMhBO5CFurza77TrIRbzsPzaNbMiInca6Gd1FtkUNCI9H4pRdtjgtfEHetzYAkGMR3XWFUdgKLc1cAVASbkxxJw-; isg=BDEx5bDr9cxcs2YOfu55__QtQL3LHqWQXOaxyxNG4PgXOlOMW2x7YMEcXM5c8j3I',
                        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'
                    }
        # self.connect = create_engine('mysql+pymysql://root:nengliang2019@@47.103.114.251:3306/operating-management?charset=utf8mb4')
        self.connect = config.connect_info
        # self.connect_pro = create_engine('mysql+pymysql://opera_man_prod:nengliang2019@@rm-uf6h2s8g5xg6482r75o.mysql.rds.aliyuncs.com:3306/operating-management-20210107?charset=utf8mb4')
        self.connect_pro1 = create_engine('mysql+pymysql://opera_python:nenglianginfo2021@python@rm-uf698x9pde1ytqxe8ko.mysql.rds.aliyuncs.com:3306/operating-management?charset=utf8mb4')
        self.sql_sku_none = 'select sku_id,sku_cost,sku_code,create_date,create_time,sku_type,shop_type,shop_name from tm_ztc_sku_none where create_date ="%s"'
        self.sql_sku = 'select outer_id from goods_skus_info where num_iid ="%s"'
        self.get_sku_sql = 'select * from %s where sku_id ="%s" and create_date="%s" and sku_type="%s" and shop_name="%s"'
        self.save_sql = """insert into {} (sku_id,sku_cost,sku_code,create_date,create_time,sum_cost,sku_type,shop_type,shop_name,cost_money,total_amount,ROI) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        # self.config = {
        #     'host': 'rm-uf6h2s8g5xg6482r75o.mysql.rds.aliyuncs.com',
        #     'user': 'opera_man_prod',
        #     'password': 'nengliang2019@',
        #     'database': 'operating-management-20210107',
        #     'charset': 'utf8mb4',
        #     'port': 3306
        # }
        # self.config_test = {
        #     'host': '47.103.114.251',
        #     'user': 'root',
        #     'password': 'nengliang2019@',
        #     'database': 'operating-management',
        #     'charset': 'utf8mb4',
        #     'port': 3306
        # }
        self.config_test = config.config
    def cookies_load(self,shop_names):
        """处理cookies"""
        cookies_dict = dict()
        with open('./tool/tm/tm_ztc_cookies{}.json'.format(shop_names), 'r', encoding='utf-8') as f:
            listCookies = json.loads(f.read())
        for cookie in listCookies:
            cookies_dict[cookie['name']] = cookie['value']
        return cookies_dict

    @retry(stop_max_attempt_number=3)
    def get_content(self,url,data,shop_names):
        response = requests.post(url, data=data, headers=self.headers,cookies=self.cookies_load(shop_names))
        return response.json()

    @retry(stop_max_attempt_number=3)
    def get_contents(self, url,shop_name,data=None):
        response = requests.get(url, data=data, headers=self.headers,cookies=self.cookies_load(shop_name),stream=True)
        return response.content

    def get_token(self,shop_names):
        url = 'https://subway.simba.taobao.com/bpenv/getLoginUserInfo.htm'
        response = self.get_content(url,None,shop_names)
        shop_name = response['result']['nickName']
        token = response['result']['token']
        return token,shop_name

    def get_cost(self,token,yesterday_time,shop_name):
        """获取总额"""
        url = f'https://subway.simba.taobao.com/report/rptBpp4pCustomSum.htm?startDate={yesterday_time}&endDate={yesterday_time}&effect=-1'
        refer = f'/report/bpreport/index?start={yesterday_time}&end={yesterday_time}&page=1'
        data = {
            'sla': 'json',
            'isAjaxRequest': 'true',
            'token': token,
            '_referer': refer,
            'sessionId': '3742c665-a4f6-45ab-8270-74aab81b6940'
        }
        data_encode = urllib.parse.urlencode(data)
        response = self.get_content(url, data_encode, shop_name)
        code = response['code']
        if code == '200':
            sum_cost = float(jsonpath(response,'$..cost')[0]) / 100
            return sum_cost
        else:
            return None


    def get_ztc_cost(self,token,yesterday_time,shop_name):
        """添加快车前一天要生成的文件"""
        url = 'https://subway.simba.taobao.com/reportdownload/addtask.htm'
        refer = f'/report/bpreport/index?start={yesterday_time}&end={yesterday_time}&page=1'
        file_name = f'天猫直通车报表{yesterday_time}'

        item = {
            "fileName":file_name,
            "dimension":2,
            "startDate": yesterday_time,
            "endDate": yesterday_time,
            "sla": "json",
            "isAjaxRequest": "true",
            "token": token,
            "_referer": refer,
            "sessionId": "2d87e4f4-e086-41dd-93bd-e0fc81eb03b5"
        }
        data_encode = urllib.parse.urlencode(item)
        response = self.get_content(url,data_encode,shop_name)
        code = response['code']
        if code == '200':
            return file_name
        else:
            return None

    def down_file(self,token,file_name,shop_name,shop_type,sum_cost):
        time.sleep(5)
        url = 'https://subway.simba.taobao.com/reportdownload/getdownloadTasks.htm?pageSize=100&pageNumber=1'
        item = {
            "sla": "json",
            "isAjaxRequest": "true",
            "token": token,
            "_referer": '/report/bpreport/download',
            "sessionId": "d5450ae8-7332-4dc7-8160-18247caad3c8",
        }
        data_encode = urllib.parse.urlencode(item)
        response = self.get_content(url,data_encode,shop_name)

        for i in response['result']['items']:
            file_names = i['fileName']
            if file_name == file_names:
                cust_id = i['custId']
                id = i['id']
                url = f'https://download-subway.simba.taobao.com/download.do?spm=a2e2i.11816827.0.0.10c868f8695S29&custId={cust_id}&taskId={id}&token=abc77a1a'
                response_content = self.get_contents(url,shop_name)
                _tmp_file = tempfile.TemporaryFile()  # 创建临时文件
                _tmp_file.write(response_content)  # byte字节数据写入临时文件

                zf = zipfile.ZipFile(_tmp_file, mode='r')
                for names in zf.namelist():
                    f = zf.extract(names, './tool/')  # 解压到zip目录文件下 https://www.cnblogs.com/alexzu/p/9818837.html

                # 处理excel
                file_path = './tool/' + file_names + '.csv'
                if os.path.exists(file_path):
                    self.deal_file(file_path,shop_name,shop_type,sum_cost)
                    os.remove(file_path)

                time.sleep(5)

                self.delete_file(token,id,shop_name)

    def delete_file(self,token,task_id,shop_name):
        """删除文件"""
        # https://subway.simba.taobao.com/#!/report/bpreport/download
        url = 'https://subway.simba.taobao.com/reportdownload/deltask.htm'
        item = {
            "taskId": task_id,
            "sla": "json",
            "isAjaxRequest": "true",
            "token": token,
            "_referer": '/report/bpreport/download',
            "sessionId": "845378f3-7c8f-41e4-8448-c74f4be9c797",
        }
        data_encode = urllib.parse.urlencode(item)
        response = self.get_content(url, data_encode,shop_name)
        if response['result']:
            print('删除成功.')

    def get_sku_code(self,id):
        """
        sku编码
        :param id: sku的id
        :return: 编码
        """
        try:
            df = pd.read_sql_query(self.sql_sku % (id), self.connect_pro1)
            df.dropna(subset=['outer_id'], inplace=True)
            data = df.to_dict('records')[0]
            sku_code = data.get('outer_id')
            if sku_code:
                if len(sku_code) >= 18:
                    return sku_code[:18]
                else:
                    return None
            else:
                return None
        except Exception as e:
            return None

    def deal_file(self,file_path,shop_name,shop_type,cost_money):
        df = pd.read_csv(file_path)
        df.rename(columns = {'商品id':'sku_id','花费(分)':'sku_cost', '总成交金额(分)': 'total_amount', '投入产出比': 'ROI'},inplace=True)
        df1 = df.groupby('sku_id').sum().reset_index()[['sku_id','sku_cost','total_amount','ROI']]
        df1 = df1[df1.sku_cost != 0]
        df1['create_date'] = (datetime.now() + timedelta(days=-1)).strftime('%Y-%m-%d')
        df1['create_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        df1['sku_code'] = df1.sku_id.apply(self.get_sku_code)
        df1.sku_code.fillna(method='bfill', inplace=True)  # bfill:向前填充
        df1.sku_code.fillna(method='ffill', inplace=True)
        sum_cost = float(int(np.around(df1.sku_cost.sum(), 2)) / 100)
        df1['sum_cost'] = sum_cost
        df1['cost_money'] = cost_money
        df1['sku_cost'] = np.around(df1.sku_cost, 2) / 100
        df1['total_amount'] = np.around(df1.total_amount, 2) / 100
        df1['ROI'] = np.around(df1.ROI, 2)
        df1['shop_name'] = shop_name
        df1['shop_type'] = '天猫商城'
        df1['sku_type'] = shop_type
        df4 = df1[df1.sku_code.isna()]  # None
        df5 = df1[df1.sku_code.notna()]

        # 处理空值
        self.save_date(df4, 'tm_ztc_sku_none')

        # 处理正常值入库
        self.save_date(df5, 'tm_ztc_sku')

        # self.save_date(df1)
        # df1.to_sql(name='tm_ztc_sku', con=self.connect,if_exists='append',index=False)

    def super_reco(self,yesterday_time,shop_name,shop_type):
        """超级推荐数据处理"""
        df = pd.read_excel(r'./tool/tm/活动商品分日报表{}.xls'.format(shop_name))
        df.rename(columns={'宝贝id': 'sku_id', '消耗': 'sku_cost', '日期': 'date_time'}, inplace=True)
        # df['date_time'] = pd.to_datetime(df['date_time'])

        df.set_index('date_time', inplace=True)
        df = df.sort_index()
        df = df.loc[yesterday_time:yesterday_time]
        sku_size = df.size  # 元素的总个数

        if sku_size:
            df1 = df.groupby('sku_id').sum().reset_index()[['sku_id', 'sku_cost']]
            df1 = df1[df1.sku_cost != 0]
            df1['create_date'] = (datetime.now() + timedelta(days=-1)).strftime('%Y-%m-%d')
            df1['create_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            df1['sku_code'] = df1.sku_id.apply(self.get_sku_code)
            sum_cost = np.around(df1.sku_cost.sum(), 2)
            df1['sum_cost'] = sum_cost
            df1['sku_cost'] = np.around(df1.sku_cost, 2)
            df1['shop_name'] = shop_name
            df1['shop_type'] = '天猫商城'
            df1['sku_type'] = shop_type
            df1['total_amount'] = 0
            df1['ROI'] = 0
            # print(df1)
            df4 = df1[df1.sku_code.isna()]  # None
            df5 = df1[df1.sku_code.notna()]

            # 处理空值
            self.save_date(df4, 'tm_ztc_sku_none')

            # 处理正常值入库
            self.save_date(df5, 'tm_ztc_sku')
            # self.save_date(df1,'tm_ztc_sku')
            # df1.to_sql(name='tm_ztc_sku', con=self.connect, if_exists='append', index=False)
        else:
            print('超级推荐前一天数据为空')

    def save_date(self,df,db_name):
        '''数据入库'''
        # conn = pymysql.connect(**self.config)  # 有中文要存入数据库的话要加charset='utf8'
        conn = pymysql.connect(**self.config_test)  # 有中文要存入数据库的话要加charset='utf8'
        cursor = conn.cursor() # 创建游标

        yes_date = (datetime.now() + timedelta(days=-1)).strftime('%Y-%m-%d')

        for index, row in df.iterrows():
            sku_id = int(row['sku_id'])
            sku_cost = row['sku_cost']
            sku_code = row['sku_code']
            create_date = row['create_date']
            create_time = row['create_time']
            sum_cost = row['sum_cost']
            sku_type = row['sku_type']
            shop_type = row['shop_type']
            try:
                cost_money = row['cost_money']
            except BaseException as e:
                cost_money = 0 # 超级推荐没有此字段
            shop_name = row['shop_name']
            total_amount = row['total_amount']
            ROI = row['ROI']
            try:
                cursor.execute(self.get_sku_sql % (db_name,sku_id,yes_date,sku_type,shop_name))
                results = cursor.fetchall()
                if results:
                    pass
                else:
                    cursor.execute(self.save_sql.format(db_name),(sku_id,sku_cost,sku_code,create_date,create_time,sum_cost,sku_type,shop_type,shop_name,cost_money,total_amount,ROI))
                    conn.commit()
            except Exception as e:
                print(e)
                conn.rollback()

        cursor.close()
        conn.close()

    def get_none(self,yesterday_time):
        df = pd.read_sql_query(self.sql_sku_none % yesterday_time, self.connect)
        index_size = df.shape[0]

        # if index_size != 0:
        file_name = f'./tool/tm_sku_none_{yesterday_time}.xlsx'
        df.to_excel(file_name,index=False)
        wx = WeChatRobot()
        wx.send_msg()
        errmsg = wx.send_file(file_name)['errmsg']
        print('send_file:',errmsg)
        os.remove(file_name)

    def start_one(self,yesterday_time):
        config = ConfigParser()
        config.read("./tm_config.ini", encoding="utf-8")
        sections = config.sections()
        for i in sections:

            shop_names = i
            shop_name = shop_names
            # if len(shop_name) > 1:
            #     shop_name = shop_name[1]
            # else:
            #     shop_name =shop_name[0]

            try:
                token, sn = self.get_token(shop_name)
                print(shop_name)
                # 获取前一天花费总额
                sum_cost = self.get_cost(token,yesterday_time,shop_name)
                # 直通车
                file_name = self.get_ztc_cost(token, yesterday_time, shop_name)
                shop_type = 'ztc'
                if file_name:
                    print(file_name,'等待一分钟')
                    time.sleep(60)
                    print('开始下载')
                    self.down_file(token, file_name, shop_name, shop_type,sum_cost)
                # 超级推荐
                shop_type = 'reco'
                self.super_reco(yesterday_time, shop_name, shop_type)
            except Exception as e:
                print(shop_names,e)

    def start(self):
        now = datetime.now()

        date_yesterday = datetime.now() + timedelta(days=-1)
        yesterday_time = (date_yesterday).strftime('%Y-%m-%d')

        self.start_one(yesterday_time)

        # 查询non值发到群组
        self.get_none(yesterday_time)

        end_time = datetime.now()
        # self.connect.dispose()
        self.connect_pro1.dispose()
        print('结束时间：', end_time.strftime('%Y-%m-%d %H:%M:%S'))
        print('耗费时间:', end_time - now)


if __name__ == '__main__':
    tm = TmCost()
    tm.start()

    scheduler = BlockingScheduler()
    scheduler.add_job(tm.start, 'cron', hour=8, minute=30)
    scheduler.start()


# 01:28




















# https://www.cnblogs.com/SunshineKimi/p/12053914.html
# https://www.cnblogs.com/xdlzs/p/11346732.html
