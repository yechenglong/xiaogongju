# -*- coding: utf-8 -*-

import xlrd
from xlutils.copy import copy
import datetime

def string_toDatetime(st):
    return datetime.datetime.strptime(st,"%Y-%m-%d %H:%M:%S.%f")

path = "F:/work/天鸽/log/20181023.xls"
#python3输入
# path = input('请输入文件目录')
#python27输入
# print(u'请输入文件目录')
# path = raw_input()
xls_file = xlrd.open_workbook(path)
xls_sheet = xls_file.sheet_by_name("Sheet1")
write_file = copy(xls_file)
write_sheet = write_file.get_sheet("Sheet2")

for row in range(1, xls_sheet.nrows):
    print("row : "+ str(row) )
    end1 = xls_sheet.cell(rowx=row,colx=5).value
    start1 =xls_sheet.cell(rowx=row,colx=4).value
    # print("end1  "+end1+"start1 "+start1)
    if start1 == '':
        finaltime = "no start time"
        write_sheet.write(row,6,finaltime)
    elif row == xls_sheet.nrows-1:
        pass
    else:
        if end1 == '':
            end1_time = string_toDatetime(xls_sheet.cell(rowx=row+1,colx=4).value)
            start1_time = string_toDatetime(xls_sheet.cell(rowx=row,colx=4).value)
            if end1_time>=start1_time:
                time1 = (end1_time - start1_time)
                finaltime = str(time1.seconds) + "." + str(time1.microseconds)[:3]
            else:
                time1 = (start1_time-end1_time)
                finaltime = "-"+str(time1.seconds) + "." + str(time1.microseconds)[:3]
        else:
            end1_time = string_toDatetime(xls_sheet.cell(rowx=row,colx=5).value)
            start1_time = string_toDatetime(xls_sheet.cell(rowx=row,colx=4).value)
            if end1_time>start1_time:
                time1 = (end1_time - start1_time)
                finaltime = str(time1.seconds) + "." + str(time1.microseconds)[:3]
            else:
                time1 = (start1_time-end1_time)
                finaltime = "-"+str(time1.seconds) + "." + str(time1.microseconds)[:3]
    print(finaltime)
    write_sheet.write(row, 6, finaltime)
write_file.save(path)





