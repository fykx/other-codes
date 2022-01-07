def listdatas(pathin):
    import os

    a = []
    datas = os.listdir(pathin)
    for i in datas:
        if i.endswith('.tif'):
            fn_i = pathin + '/' + i
            a.append(fn_i)
    a.sort()

    return a


def create_nc(datas):
    from datetime import datetime
    import numpy as np
    import pandas as pd
    import netCDF4 as nc
    from osgeo import gdal

    in_ds = gdal.Open(datas[0])
    in_band = in_ds.GetRasterBand(1)#波段索引从1开始
    nodata = in_band.GetNoDataValue()
    in_data = in_band.ReadAsArray()
    xsize = in_band.XSize#列
    ysize = in_band.YSize#行
    projection = in_ds.GetProjection()
    geotransform = in_ds.GetGeoTransform()
    del in_ds


    ## create NetCDF file
    newfile = nc.Dataset('test.nc', 'w', format='NETCDF4')

    ## define dimesions
    newfile.createDimension('lon', size=xsize)
    newfile.createDimension('lat', size=ysize)
    newfile.createDimension('year', size=len(datas))

    ## define variables for storing data
    lon = newfile.createVariable('lon', np.float64, dimensions='lon')
    lon.long_name = "longitude"  # 该变量的名称
    lon.units = "meters"  # 该变量的单位

    lat = newfile.createVariable('lat', np.float64, dimensions='lat')
    lat.long_name = "latitude"  # 该变量的名称
    lat.units = "meters"  # 该变量的单位

    year = newfile.createVariable('year', np.int16, dimensions='year')
    year.long_name = "year"  # 该变量的名称
    year.units = "year"  # 该变量的单位

    tcc = newfile.createVariable('tcc', np.float64, dimensions=('year','lat','lon'), zlib=True, complevel=3)
    tcc.long_name = "tree-canopy cover"  # 该变量的名称
    tcc.units = "%"  # 该变量的单位
    tcc.coordinates = projection
    tcc.missing_value = nodata


    years = []
    tccs = []
    for data in datas:
        year = int(data.split('/')[-1].split('_')[1][-4:])

        ds = gdal.Open(data)
        band = ds.GetRasterBand(1)
        data = band.ReadAsArray()
        del ds

        years.append(year)
        tccs.append(data)

    years_array = np.array(years)
    tccs_narray = np.array(tccs)


    newfile.variables['lon'][:] = np.array([geotransform[0] + i*geotransform[1] for i in range(xsize)])
    newfile.variables['lat'][:] = np.array([geotransform[-3] - i*geotransform[1] for i in range(ysize)])
    newfile.variables['year'][:] = years_array
    newfile.variables['tcc'][...] = tccs_narray

    newfile.author = 'fykx'  # 创建文件作者
    newfile.createdate = '%s' % datetime.now().strftime('%Y-%m-%d %H:%M') # 创建文件时间
    
    return


def main():
    pathin = r'C:\Users\Jayde\Desktop\nc\h000v019'
    datas = listdatas(pathin)
    create_nc(datas)


if __name__ == "__main__":
    main()

    
