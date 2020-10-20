'''
File: 3_jllc_jc.py
Author: 王建邦
Version: 0.1
Create: 2017-07-01
Description: 计算积累离差和极差
'''

import arcpy
import os
from arcpy.sa import *
arcpy.CheckOutExtension("spatial")
arcpy.gp.overwriteOutput = 1
arcpy.env.workspace = r'F:\test_2'

def listdatas(pathin):
    a = []
    datas = os.listdir(pathin)
    for i in datas:
        if i[0:4] == 'czxl' or i[0:4] == 'jzxl':
            fn_i = pathin + '/' + i
            a.append(fn_i)
    return a
            
def jllc_3(pathin1, pathin2, pathout1, pathout2, para_fixed):
    datas1 = listdatas(pathin1)
    datas2 = listdatas(pathin2)
    Ras_para = arcpy.Raster(para_fixed)
    q = 1
    while q <= len(datas1):
        para = Ras_para - Ras_para
        a = []
        for i in datas1[0:q]:
            Ras_i = arcpy.Raster(i)
            for j in datas2:
                if j[-2:] == str(q).zfill(2):
                    #print i,j
                    Ras_j = arcpy.Raster(j)
                    jc = Ras_i - Ras_j
                    para = para + jc
                    a.append(para)
                    print datas1[0:q],q
                    print i[-6:],j[-6:]
        print a
        outdata = CellStatistics(a, "MAXIMUM", "NODATA") - CellStatistics(a, "MINIMUM", "NODATA")
        outdata.save(pathout2+'/'+'jc'+str(q).zfill(2))
        para.save(pathout1+'/'+'jllc'+str(q).zfill(2))
        q = q + 1
    return
            
if __name__ == '__main__':
    pathin1 = r'F:\hurst\1_czxl'
    pathin2 = r'F:\hurst\2_jzxl'
    pathout1 = r'F:\hurst\3_jllc'
    pathout2 = r'F:\hurst\4_jc'
    para_fixed = r'F:\528\nodata\value_nodata'
    jllc_3(pathin1, pathin2, pathout1, pathout2, para_fixed)
