'''
File: 2_jzxl.py
Author: 王建邦
Version: 0.1
Create: 2017-07-01
Description: 计算均值序列
'''

import arcpy
import os
from arcpy.sa import *
arcpy.CheckOutExtension("spatial")
arcpy.env.overwriteOutput = 1

def jzxl_1(pathin,pathout):
    arcpy.env.workspace = pathin
    datas = arcpy.ListRasters()
    for i in datas:
        if i[0:4] != 'czxl':
            datas.remove(i)
    j = 1
    while j <= len(datas):
        out_1 = CellStatistics(datas[0:j], "MEAN", "NODATA")
        print datas[0:j],j
        out_1.save(pathout+'/'+'jzxl'+str(j).zfill(2))
        j = j + 1  
    return

if __name__ == '__main__':
    pathin = r'D:\paper_2\Hurst\1_czxl'
    pathout = r'D:\paper_2\Hurst\2_jzxl'
    jzxl_1(pathin,pathout)
