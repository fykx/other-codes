'''
File: sen.py
Author: 王建邦
Version: 0.1
Create: 2017-06-12
Description: 计算Sen趋势
'''

import arcpy
import os
from arcpy.sa import *
arcpy.CheckOutExtension("spatial")
arcpy.env.overwriteOutput = 1
arcpy.env.workspace = r'G:\test_2'
arcpy.env.scratchWorkspace = r'G:\test_2'

def sen(pathin, pathout):
    a = []
    datas = os.listdir(pathin)
    for i in datas:
        if i[0:4] == 'ndvi':
            for j in datas:
                if j[0:4] == 'ndvi':
                    if int(j[-4:]) < int(i[-4:]):
                        print i,j
                        fn_i = pathin + '/' + i
                        fn_j = pathin + '/' + j
                        Ras_i = arcpy.Raster(fn_i)
                        Ras_j = arcpy.Raster(fn_j)
                        out_data = (Ras_i - Ras_j)/(int(i[-4:])-int(j[-4:]))
                        a.append(out_data)
    print len(a)
    outCellStatistics = CellStatistics(a, "MEDIAN", "NODATA")
    outCellStatistics.save(pathout + '/' + 'sen')
    return

if __name__ == '__main__':
    pathin = r'G:\528\re_ndvi\year_setnull'
    pathout = r'G:\1_sen'
    sen(pathin, pathout)
