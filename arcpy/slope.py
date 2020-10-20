'''
@Descripttion: 
@version: 0.1
@Author: Jianbang Wang
@Date: 2020-07-30 13:59:11
'''

import arcpy,os,glob,time
from arcpy.sa import *
arcpy.CheckOutExtension("spatial")
arcpy.env.overwriteOutput = 1


def listdatas(pathin):
    a = []
    datas = os.listdir(pathin)
    for i in datas:
        if i[-4:] == '.tif':
            fn_i = pathin + '/' + i
            a.append(fn_i)
    return a
            

def hurst(pathin,pathout,para_fixed):
    datas = listdatas(pathin)#rs
    datas.sort()
    Ras_para = arcpy.Raster(para_fixed)
    para = Ras_para - Ras_para
    para1 = Ras_para - Ras_para
    q = 0
    w = 0
    for i in datas:
        Ras_i = arcpy.Raster(i)#1
        para = para + (Ras_i * float(i.split('/')[-1].split('.')[0].split('_')[1]))
        q = q + float(i.split('/')[-1].split('.')[0].split('_')[1])
        para1 = para1 + Ras_i
        w = w + Square(float(i.split('/')[-1].split('.')[0].split('_')[1]))
        print len(datas),float(i.split('/')[-1].split('.')[0].split('_')[1])
    para_0 = len(datas) * para
    para_1 = para1 * q
    para_2 = ((len(datas))) * w - Square(q)
    out_data = (para_0 - para_1) / para_2
    out_data.save(pathout + '/' + 'slope.tif')
    return

if __name__ == '__main__':
    pathin = r'E:\forest_data\tianshui\tcc\maps\tcc'
    pathout = r'E:\forest_data\tianshui\4_out'
    para_fixed = listdatas(pathin)[-1]
    hurst(pathin,pathout,para_fixed)
