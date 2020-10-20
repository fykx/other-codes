'''
File: Resample.py
Author: 王建邦
Version: 0.1
Description: 栅格重采样
'''

import arcpy
from arcpy import env
arcpy.CheckOutExtension("Spatial")
from arcpy.sa import *
arcpy.env.overwriteOutput = 1

def resample(pathin,pathout):
    arcpy.env.workspace = pathin
    datas = arcpy.ListRasters()
    for i in datas:
        if i[0:2] == 'rw':
            print i
            arcpy.Resample_management(i, pathout+'/'+i[:], "1000", "NEAREST")   
    return
    
if __name__ == "__main__":
    pathin = r'D:\paper_2\results\datas\rw_f'
    pathout = r'G:\123\Resample\rw_f'
    resample(pathin,pathout)
