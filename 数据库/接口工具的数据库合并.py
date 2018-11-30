#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#
import pymysql

# 原始数据的数据连接
db1 = pymysql.connect('127.0.0.1', 'root', '123456', 'test')
cursor1 = db1.cursor()
# 定义查询语句
len1 = cursor1.execute('select id,CAST(createtime AS CHAR) AS createtime,paycount from admin_payinfo limit 100')

# 迁移库的数据连接
db2 = pymysql.connect('192.168.0.110', 'root', '1234', 'test1')
cursor2 = db2.cursor()
# 批量插入语句
sql = 'insert into admin_payinfo(id,createtime,paycount) value(%s, %s, %s)'

# 每次循环导入的数据量
num = 11

for i in range(int(len1/num)):
    print(i)
    data1 = cursor1.fetchmany(num)
    cursor2.executemany(sql, data1)

# 把剩下的数据一次性导入
data2 = cursor1.fetchall()
cursor2.executemany(sql, data2)

# 这种可以全部导入
# data2 = cursor1.fetchall()
# cursor2.executemany(sql, data2)

# 提交到数据库
db2.commit()

# 关闭数据库连接
db1.close()
db2.close()