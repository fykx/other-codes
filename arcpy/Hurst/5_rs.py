'''
File: 5_rs.py
Author: 王建邦
Version: 0.1
Create: 2017-07-01
Description: 计算R/S
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
        if i[0:3] == 'bzc' or i[0:2] == 'jc':
            fn_i = pathin + '/' + i
            a.append(fn_i)
    return a
            
def rs_6(pathin1,pathin2,pathout):
    datas1 = listdatas(pathin1)
    datas2 = listdatas(pathin2)
    for i in datas1:
        if i[-2:] != '01':
            Ras_i = arcpy.Raster(i)
            for j in datas2:
                if j[-2:] == i[-2:]:
                    Ras_j = arcpy.Raster(j)
                    print i[-4:],j[-5:]
                    out_data = Ras_i / Ras_j
                    out_data.save(pathout+'/'+'rs'+i[-2:])
    return
                    
if __name__ == '__main__':
    pathin1 = r'E:\paper\results\hurst\4_jc'
    pathin2 = r'E:\paper\results\hurst\5_bzc'
    pathout = r'E:\paper\results\hurst\6_Rs'
    rs_6(pathin1,pathin2,pathout)
