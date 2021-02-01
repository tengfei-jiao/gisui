# coding=utf-8
import os
import xlrd
from Common.function import project_path

'''
函数read_excel:读excel操作，所有数据存放在字典中
    filename为文件名
    index为sheet的索引值
'''


def read_excel(filename,index):
    xls = xlrd.open_workbook(filename)
    sheet = xls.sheet_by_index(index)
    print(sheet.nrows)
    print(sheet.ncols)  # 列:column
    dic={}
    for j in range(sheet.ncols):
        data = []
        for i in range(sheet.nrows):
            data.append(sheet.row_values(i)[j])
        dic[j]=data
    return dic


if __name__ == "__main__":
    # 读取excel操作，并返回字典
    date = read_excel(project_path()+"TestDatas\\testdata.xls",0)
    print(date)
    print(date.get(1))