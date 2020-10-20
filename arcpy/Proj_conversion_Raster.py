'''
File: Proj_conversion_Raster.py
Author: 王建邦
Version: 0.1
Description: 栅格投影转换
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
        if i[-4:] == '.tif' and i[0:2] == '20':
            fn_i = pathin + '/' + i
            a.append(fn_i)
    return a

def c_project(para, pathin, pathout):
    outcs = arcpy.Describe(para).spatialReference
    for i in listdatas(pathin):
        print i.split('/')[-1]
        arcpy.ProjectRaster_management (i, pathout + '/' + i.split('/')[-1].split('.')[0], outcs)
    return

if __name__ == '__main__':
    para = r'C:\Users\hupengfei\Desktop\test\200401.tif'
    pathin = r'E:\graceread'
    pathout = r'E:\grace'
    c_project(para, pathin, pathout)

