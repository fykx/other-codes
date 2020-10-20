'''
@Descripttion: 
@version: 0.1
@Author: Jianbang Wang
@Date: 2020-05-24 11:38:39
'''

import arcpy
import os
from arcpy.sa import *
arcpy.CheckOutExtension("spatial")
arcpy.env.overwriteOutput = 1

def listdatas_B3(pathin):
    a = []
    datas = os.listdir(pathin)
    for i in datas:
        if i[-4:] == '.TIF' and i.split(".")[0][-2:] == 'B3':
            fn_i = pathin + '/' + i
            a.append(fn_i)
    return a

def listdatas_B4(pathin):
    a = []
    datas = os.listdir(pathin)
    for i in datas:
        if i[-4:] == '.TIF' and i.split(".")[0][-2:] == 'B4':
            fn_i = pathin + '/' + i
            a.append(fn_i)
    return a

def main(pathin, pathout):
    ras_B3 = listdatas_B3(pathin)
    ras_B4 = listdatas_B4(pathin)

    for i in ras_B3:
        for j in ras_B4:
            if i.split("/")[-1].split(".")[0][:-1] == j.split("/")[-1].split(".")[0][:-1]:
                print i.split("/")[-1], "    ", j.split("/")[-1] 
                NDVI = (arcpy.Raster(j)*1.0 - arcpy.Raster(i)*1.0) / (arcpy.Raster(j)*1.0 + arcpy.Raster(i)*1.0)
                NDVI.save(pathout + '/' + i.split("/")[-1].split(".")[0][:-2] + 'NDVI' + '.TIF')

if __name__ == '__main__':   
    pathin = r'C:\Users\fykx\Desktop\data\data'
    pathout = r'C:\Users\fykx\Desktop\data\result'
    main(pathin,pathout)
