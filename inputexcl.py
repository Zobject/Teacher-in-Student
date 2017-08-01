#coding:utf8
import xlrd


import  pymongo

try:
    conn=pymongo.MongoClient()
    print  'success'
except:
    print  'fail'

db=conn['Teacher']
#链接一个表准备导入
collections=db.test
#excl导入
def inputexcl(filename):
    fname=filename
    #打开excl 文件
    bk = xlrd.open_workbook(fname)
    shxrange = range(bk.nsheets)
    try:
        sh = bk.sheet_by_name("Sheet1")
    except:
        print "no sheet in %s named Sheet1" % fname
    nrows = sh.ncols

    #存入数据 四个数据项分别对应不同的字段
    for i in range(1, nrows+1):
           collections.insert({'name':sh.row_values(i)[0],'studentid':int(sh.row_values(i)[1]),'xi':sh.row_values(i)[2],'kemu':sh.row_values(i)[3]})


#需要导入的文件名字
filename='aaaaa.xlsx'
inputexcl(filename)