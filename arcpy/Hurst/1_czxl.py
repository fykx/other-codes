'''
File: 1_czxl.py
Author: 王建邦
Version: 0.1
Create: 2017-07-01
Description: 计算差值序列
'''

import arcpy
import os
from arcpy.sa import *
arcpy.CheckOutExtension("spatial")
arcpy.env.overwriteOutput = 1

def listdatas(pathin):
    a = []
    datas = os.listdir(pathin)
    for i in datas:
        if i[0:2] == 'rw' or i[0:4] == 'jzxl':
            fn_i = pathin + '/' + i
            a.append(fn_i)
    return a
            
def czxl_1(pathin,pathout):
    datas = listdatas(pathin)
    q = 0
    while q < len(datas)-1:
        out_data = arcpy.Raster(datas[q+1]) - arcpy.Raster(datas[q])
        print datas[q+1][-6:],datas[q][-6:],q+1
        out_data.save(pathout+'/'+'czxl'+str(q+1).zfill(2))
        q = q + 1
    return
            
if __name__ == '__main__':
    pathin = r'E:\paper\results\rw'
    pathout = r'D:\paper_2\Hurst\1_czxl'
    czxl_1(pathin,pathout)
