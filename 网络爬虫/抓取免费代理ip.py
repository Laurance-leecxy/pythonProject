# import requests
# from lxml import etree
# import pymysql
#
#
# # 请求一个单页内容拿到html
# def get_one_page(url):
#     response = requests.get(url).content.decode('utf-8')
#     # 返回页面的内容
#     # print(response)
#     return response
#
#
# # 解析htm1 (IP,PORT,匿名度,类型,位置,响应速度,最后验证时间)
# def parse_one_page(text):
#     html = etree.HTML(text)
#     # print(html)
#     length = len(html.xpath('//tbody/tr'))
#     # print(length)  # 一页15个数据
#     for i in range(length):
#         # IP
#         find_ip = html.xpath('//td[@data-title="IP"]/text()')
#         # print(find_ip[i])
#         a = find_ip[i]
#
#         # PORT
#         find_port = html.xpath('//td[@data-title="PORT"]/text()')
#         # print(find_port[i])
#         b = find_port[i]
#
#         # 匿名度
#         anonymity = html.xpath('//td[@data-title="匿名度"]/text()')
#         # print(anonymity[i])
#         c = anonymity[i]
#
#         # 类型
#         types = html.xpath('//td[@data-title="类型"]/text()')
#         # print(types[i])
#         d = types[i]
#
#         # 位置
#         place = html.xpath('//td[@data-title="位置"]/text()')
#         # print(place[i])
#         e = place[i]
#
#         # 响应速度
#         speed = html.xpath('//td[@data-title="响应速度"]/text()')
#         # print(speed[i])
#         f = speed[i]
#
#         # 最后验证时间
#         verification_time = html.xpath('//td[@data-title="最后验证时间"]/text()')
#         # print(verification_time[i])
#         g = verification_time[i]
#
#         yield a, b, c, d, e, f, g
#
#
# # 数据存储
# def write_to_mysql(content):
#     # 连接数据库
#     conn = pymysql.connect(host='localhost', user='root', password='123456', db='free_ip', port=3306, charset='utf8')
#
#     # 创建游标
#     cursor = conn.cursor()
#
#     # 创建数据表
#     # create_sql = 'create table if not exists `message`(`IP` varchar(255),`PORT` varchar(255),`匿名度` varchar(255),`类型` varchar(255),`位置` varchar(255),`响应速度` varchar(255),`最后验证时间` varchar(255))'
#
#     num = 1
#     for i in content:
#         # print(i)
#         find_ip = i[0]
#         find_port = i[1]
#         anonymity = i[2]
#         types = i[3]
#         place = i[4]
#         speed = i[5]
#         verification_time = i[6]
#
#         # 增加数据
#         insert_sql = "insert into `message` value (%s,%s,%s,%s,%s,%s,%s)"
#         parm_list = [(find_ip, find_port, anonymity, types, place, speed, verification_time)]
#         # print('保存 <%s> IP完成!' % find_ip)
#         print('保存第%s条IP完成!' % num)
#         num += 1
#
#         # 提交执行sql语句
#         cursor.executemany(insert_sql, parm_list)
#
#         # cursor.execute(create_sql)
#
#         # 向数据库提交操作
#         conn.commit()
#
#     # 关闭游标
#     cursor.close()
#
#     # 关闭连接
#     conn.close()
#
#
# # 函数回调
# def main():
#     count = 1
#     for i in range(1, 101):
#         url = 'https://www.kuaidaili.com/free/inha/{}/'.format(i)
#         a = get_one_page(url)
#         b = parse_one_page(a)
#         write_to_mysql(b)
#         print('\n第%d页IP已保存成功......\n' % count)
#         count += 1
#     print('免费代理ip前一百页已抓取完成')
#
#
# # 主函数
# if __name__ == '__main__':
#     main()


# {'协议': 'ip:端口号'}
import pymysql

# 连接数据库
conn = pymysql.connect(host='localhost', user='root', password='123456', db='free_ip', port=3306, charset='utf8')
# 创建游标
cursor = conn.cursor()
sql = 'select IP,PORT,类型 from message'
# 提交执行sql语句
cursor.execute(sql)
# 得到查询后的所有结果
data = cursor.fetchall()
# print(data)
dip = {}
for i in data:
    # print(i[0]+':'+i[1])
    # 以字典形式查询所有IP
    dip[i[2]] = i[0] + ':' + i[1]
    print(dip)
# 查询不需要向数据库提交
# 关闭游标
cursor.close()
# 关闭连接
conn.close()
