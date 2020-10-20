'''
File: 4_bzc.py
Author: 王建邦
Version: 0.1
Create: 2017-07-01
Description: 计算标准差
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
        if i[0:4] == 'czxl' or i[0:4] == 'jzxl':
            fn_i = pathin + '/' + i
            a.append(fn_i)
    return a
            
def bzc_5(pathin1,pathin2,pathout,para_fixed):
    datas1 = listdatas(pathin1)#czxl
    datas2 = listdatas(pathin2)#jzxl
    Ras_para = arcpy.Raster(para_fixed)
    q = 1
    while q <= len(datas1):
        print q
        para = Ras_para - Ras_para
        for i in datas1[0:q]:
            Ras_i = arcpy.Raster(i)
            for j in datas2:
                if j[-2:] == str(q).zfill(2):
                    Ras_j = arcpy.Raster(j)
                    para = para + Square((Ras_i - Ras_j))
                    #print datas1[0:q],q
                    print '(', i[-6:], '-', j[-6:], ')',  q
        para = SquareRoot(para/q)
        para.save(pathout+'/'+'bzc'+str(q).zfill(2))
        q = q + 1
    return
            
if __name__ == '__main__':
    pathin1 = r'D:\paper_2\Hurst\1_czxl'
    pathin2 = r'D:\paper_2\Hurst\2_jzxl'
    pathout = r'E:\paper\results\hurst\5_bzc'
    para_fixed = r'E:\paper\nodata\value_nodata'
    bzc_5(pathin1,pathin2,pathout,para_fixed)
