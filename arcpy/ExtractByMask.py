'''
File: ExtractByMask.py
Author: 王建邦
Version: 0.1
Description: 影像批量裁剪
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
        if i[0:2] == 'rw' or i[0:4] == 'ndvi':
            fn_i = pathin + '/' + i
            a.append(fn_i)
    return a
            
def Extract(pathin, pathout, mask):
    datas = listdatas(pathin)
    for i in datas:
        outExtractByMask = ExtractByMask(i, mask)
        outExtractByMask.save(pathout + '/' + i[-4:])  
    return
            
if __name__=='__main__':
    pathin = r'E:\paper\datas\re_ndvi\year_setnull'
    pathout = r'C:\Users\Administrator\Desktop\test'
    mask = r'C:\Users\Administrator\Desktop\SYH\syh_albers.shp'
    Extract(pathin, pathout, mask)
