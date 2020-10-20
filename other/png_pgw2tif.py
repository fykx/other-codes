# -*- coding: utf-8 -*-
import os
import imageio
from osgeo import gdal
from osgeo import osr


pngPath = r'G:\GIS\Test'
savePath = r'G:\GIS\Test'

for fulname in os.listdir(pngPath):
    name, suffix = fulname.split('.')
    if not (suffix == 'png' and os.path.exists(os.path.join(pngPath, name + '.pgw'))):
        continue
    img = imageio.imread(os.path.join(pngPath, fulname))

    pgwvals = []
    with open(os.path.join(pngPath, name + '.pgw'), 'r') as f:
        pgwval = f.readline()
        while pgwval:
            pgwvals.append(float(pgwval))
            pgwval = f.readline()

    geotransform = (pgwvals[4], pgwvals[0], pgwvals[1], pgwvals[5], pgwvals[2], pgwvals[3])

    driver = gdal.GetDriverByName('GTiff')
    clipraster = driver.Create(os.path.join(savePath, name + '.tif'), img.shape[1], img.shape[0], 3, gdal.GDT_Byte)
    clipraster.SetGeoTransform(geotransform)

    clipband = clipraster.GetRasterBand(1)
    clipband.WriteArray(img[:, :, 0])
    clipband = clipraster.GetRasterBand(2)
    clipband.WriteArray(img[:, :, 1])
    clipband = clipraster.GetRasterBand(3)
    clipband.WriteArray(img[:, :, 2])

    cliprasterSRS = osr.SpatialReference()
    cliprasterSRS.ImportFromEPSG(3857)
    clipraster.SetProjection(cliprasterSRS.ExportToWkt())
    clipband.FlushCache()
