'''
File: 6_hurst.py
Author: 王建邦
Version: 0.1
Create: 2017-07-01
Description: 计算Hurst指数
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
        if i[0:2] == 'rs' or i[0:4] == 'jzxl':
            fn_i = pathin + '/' + i
            a.append(fn_i)
    return a
            
def hurst(pathin,pathout,para_fixed):
    datas = listdatas(pathin)
    Ras_para = arcpy.Raster(para_fixed)
    para = Ras_para - Ras_para
    para1 = Ras_para - Ras_para
    q = 0
    w = 0
    for i in datas:
        Ras_i = arcpy.Raster(i)
        para = para + (Ln(Ras_i) * Ln(float(i[-2:].lstrip('0'))))
        q = q + Ln(float(i[-2:].lstrip('0')))
        para1 = para1 + Ln(Ras_i)
        w = w + Square(Ln(float(i[-2:].lstrip('0'))))
        print len(datas),float(i[-2:].lstrip('0'))
    para_0 = len(datas) * para
    para_1 = para1 * q
    para_2 = ((len(datas))) * w - Square(q)
    out_data = (para_0 - para_1) / para_2
    out_data.save(pathout + '/' + 'hurst')
    return

if __name__ == '__main__':
    pathin = r'E:\paper\results\hurst\6_Rs'
    pathout = r'E:\paper\results\hurst\hurst'
    para_fixed = r'E:\paper\nodata\value_nodata'
    hurst(pathin,pathout,para_fixed)