'''
File: MosaicToNewRaster.py
Author: 王建邦
Version: 0.1
Description: 镶嵌至新栅格
'''

import arcpy,os,glob,time
from arcpy.sa import *
arcpy.CheckOutExtension("spatial")
arcpy.env.overwriteOutput = 1

def listdatas(pathin):
    a = []
    datas = os.listdir(pathin)
    for i in datas:
        if i[-4:] == '.shp' or i[0:2] == 'rw':
            fn_i = pathin + '/' + i
            a.append(fn_i)
    return a

def mosaic(pathin,pathout):
    try:
        arcpy.MosaicToNewRaster_management(listdatas(pathin),pathout, "lat", "",\
                                       "", "250", "1", "","")
    except:
        print "Mosaic To New Raster example failed."
        print arcpy.GetMessages()
    return

if __name__ == '__main__':   
    pathin = r'G:\point\wd'
    pathout = r'G:\point\lon_lat'
    mosaic(pathin,pathout)
