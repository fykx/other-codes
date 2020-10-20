'''
@Descripttion: 
@version: 0.1
@Author: Jianbang Wang
@Date: 2020-07-04 19:41:49
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
        if i[-3:] == '.nc':
            fn_i = pathin + '/' + i
            a.append(fn_i)
    return a

def main(pathin, pathout):
    datas = listdatas(pathin)
    for i in datas:
        print i.split('/')[-1]
        arcpy.MakeNetCDFRasterLayer_md(i,"GPP","longitude","latitude",i.split('/')[-1].split('.')[2],"","","BY_VALUE")
        arcpy.CopyRaster_management(i.split('/')[-1].split('.')[2], pathout + '/' + i.split('/')[-1].split('.')[2] + '.tif')
    return

if __name__ == '__main__':
    pathin = r'C:\Users\Jayde\Desktop\1991'
    pathout = r'C:\Users\Jayde\Desktop\1991\out'
    main(pathin, pathout)