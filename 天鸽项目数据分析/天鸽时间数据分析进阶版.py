# -*- coding: utf-8 -*-

import xlwt
import xlrd
from xlutils.copy import copy
import datetime

#把字符串转成时间
def string_toDatetime(st):
    return datetime.datetime.strptime(st,"%Y-%m-%d %H:%M:%S.%f")

#计算每个步骤所用的时间
def getfinaltime(start1_time,end1_time):
    if end1_time >= start1_time:
        time1 = (end1_time - start1_time)
        finaltime = str(time1.seconds) + "." + str(time1.microseconds)[:3]
    else:
        time1 = (start1_time - end1_time)
        finaltime = "-" + str(time1.seconds) + "." + str(time1.microseconds)[:3]
    return finaltime

#读取xls里的数据存储到列表里
def readfile(read_file):
    read_sheet = read_file.sheet_by_name("Sheet1")
    msgids= []
    endtimes = []
    starttimes = []
    types = []
    for row in range(1, read_sheet.nrows):
        msgids.append(read_sheet.cell(rowx=row, colx=1).value)
        types.append(read_sheet.cell(rowx=row, colx=0).value)
        endtimes.append(read_sheet.cell(rowx=row, colx=5).value)
        starttimes.append(read_sheet.cell(rowx=row, colx=4).value)
    return types,msgids,starttimes,endtimes

#把有效数据写入xls
def writefile(read_file,types,msgids,starttimes,endtimes):
    haveendtime = ['READWEIGHT-2', 'MOTIONDETECT', 'RECOG', 'READWEIGHT-1','SENDTOPOS']
    # noendtime = ['RE4SDK', 'SENDTOGUI', 'RE4POS', 'FINISH']
    title = ['TYPE','MSGID','STARTTIME','ENDTIME','USERTIME']
    count = 0
    row = 0
    write_file = copy(read_file)
    mySheets = read_file.sheet_names()
    if "Sheet2" in mySheets:
        write_sheet = write_file.get_sheet("Sheet2")
    else:
        write_sheet = write_file.add_sheet("Sheet2",cell_overwrite_ok=True)
    for clo in range(0, 5):
        write_sheet.write(0, clo,title[clo] )
    for msgid in msgids:
        if count+7<len(msgids):
            print(count)
            print(msgid)
            print(msgids[count + 7])
            if msgid == msgids[count+7]:
                for newcount in range(count,count+8):
                    newtype = types[newcount]
                    newmsgid = msgid
                    newstarttime = starttimes[newcount]
                    newendtime = endtimes[newcount]
                    finaltime=''
                    print(newcount)
                    if starttimes[newcount] == '':
                        finaltime = "no start time"
                    else:
                        if newtype in haveendtime:
                            finaltime = getfinaltime(string_toDatetime(newstarttime), string_toDatetime(newendtime))
                        elif newtype == 'RE4SDK':
                            finaltime = getfinaltime(string_toDatetime(starttimes[types.index( 'RE4SDK',count,count+8)]),
                                                     string_toDatetime(starttimes[types.index('SENDTOGUI', count, count + 8)]))
                        elif newtype == 'SENDTOGUI':
                            finaltime = getfinaltime(
                                string_toDatetime(starttimes[types.index('SENDTOGUI', count, count + 8)]),
                                string_toDatetime(starttimes[types.index('RE4POS', count, count + 8)]))
                        elif newtype == 'RE4POS':
                            finaltime = getfinaltime(
                                string_toDatetime(starttimes[types.index('RE4POS', count, count + 8)]),
                                string_toDatetime(starttimes[types.index('FINISH', count, count + 8)]))
                        else:
                            finaltime="no this type use time"
                        datas = [newtype, newmsgid, newstarttime, newendtime, finaltime]
                        for clo in range(0, 5):
                            write_sheet.write(row + 1, clo, datas[clo])
                        row += 1
        else:
            pass

        count += 1
    print(count)
    write_file.save(path)




path = "F:/work/天鸽/log/20181023.xls"
#python3输入
# path = input('请输入文件目录')
#python27输入
# print(u'请输入文件目录')
# path = raw_input()

read_file = xlrd.open_workbook(path)
types,msgids,starttimes,endtimes=readfile(read_file)

writefile(read_file,types,msgids,starttimes,endtimes)








