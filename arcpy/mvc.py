'''
File: mvc.py
Author: 王建邦
Version: 0.1
Create: 2017-05-01
Description: MODIS13Q1 NDVI最大值合成
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
        if i[-4:] == '.tif':
            fn_i = pathin + '/' + i
            a.append(fn_i)
    return a

def main(pathin, pathout):
    rn = [0,31,60,91,121,152,182,213,244,274,305,335,366]
    pn = [0,31,59,90,120,151,181,212,243,273,304,334,365]
    days = [rn,pn]
    a = listdatas(pathin)
    pr = 0
    if int(a[0].split('/')[-1].split('.')[1][1:5]) % 4 == 0:
        pr = 0
        print '今年是闰年'
    else:
        pr = 1
        print '今年是平年'
    b = []
    for i in a:
        a.remove(i)
        for j in a:
            m = 0
            while m < 12:
                if i != j and \
                   days[pr][m] < int(i.split('/')[-1].split('.')[1][-3:].lstrip('0')) <= days[pr][m+1] and \
                   days[pr][m] < int(j.split('/')[-1].split('.')[1][-3:].lstrip('0')) <= days[pr][m+1]:
                    print i.split('/')[-1].split('.')[1][-3:].lstrip('0'),j.split('/')[-1].split('.')[1][-3:].lstrip('0')
                    outCellStatistics = CellStatistics([i,j], "MAXIMUM", "NODATA")
                    outCellStatistics.save(pathout + '/' + i.split('/')[-1].split('.')[1][1:5] + str(m+1).rjust(2,'0'))
                    c = [i,j]
                    b = b + c  
                m = m + 1
    for q in listdatas(pathin):
        if q in b:
            pass
        else:
            print 'Mind!',q.split('/')[-1].split('.')[1],'is single!'
            m = 0
            while m < 12:
                if days[pr][m] < int(q.split('/')[-1].split('.')[1][-3:].lstrip('0')) <= days[pr][m+1]:
                    print 'Rename:',q.split('/')[-1].split('.')[1][1:5] + str(m+1).rjust(2,'0')
                    break
                m = m + 1
            outRaster = arcpy.Raster(q) * 1.0
            outRaster.save(pathout + '/' + q.split('/')[-1].split('.')[1][1:5] + str(m+1).rjust(2,'0'))
    return

if __name__ == '__main__':
    pathin = r'D:\MODIS\2017'
    pathout = r'D:\MODIS\2017\MVC'
    main(pathin, pathout)


        
    
    
    


