'''
File: mk.py
Author: 王建邦
Version: 0.1
Create: 2017-06-12
Description: 趋势显著性检验
'''

import arcpy,os,glob,time
from arcpy.sa import *
arcpy.CheckOutExtension("spatial")
arcpy.env.overwriteOutput = 1
arcpy.env.workspace = r'G:\test'

def listdatas(pathin):
    a = []
    datas = os.listdir(pathin)
    for i in datas:
        if i[0:2] == 'rw' or i[0:4] == 'ndvi':
            fn_i = pathin + '/' + i
            a.append(fn_i)
    return a
            
def MK(pathin, pathout, para_fixed):
    Ras_para = arcpy.Raster(para_fixed)
    para_1 = Ras_para - Ras_para 
    datas = listdatas(pathin)
    for i in range(0,len(datas)-1):
        for j in range(i+1,len(datas)):
            data = arcpy.Raster(datas[i]) - arcpy.Raster(datas[j])
            print datas[j][-8:],datas[i][-8:],i+1
            agn_data = Con((data > 0),1,Con((data < 0),-1,0.0))
            para_1+= agn_data
    para_1.save(pathout+'/'+'s')
    s_s = float((float(len(datas))*(float(len(datas))-1.0)*((2*float(len(datas)))+5.0))/18.0)
    z_value = Con((para_1 > 0),(para_1-1.0)/SquareRoot(s_s),Con((para_1 < 0),(para_1+1.0)/SquareRoot(s_s),0.0))
    z_value.save(pathout + '/' + 'z')
    return
            
def main():
    pathin = r'E:\paper\results\rw'
    pathout = r'D:\paper_2\MK'
    para_fixed = r'E:\paper\nodata\value_nodata'
    MK(pathin, pathout, para_fixed)
    
if __name__=='__main__':
    main()
