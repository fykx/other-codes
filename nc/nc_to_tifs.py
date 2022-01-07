def nc_to_tifs(data, pathout):
    import netCDF4 as nc
    from osgeo import gdal
    import numpy as np

    nc_data = nc.Dataset(data)
    lon = nc_data.variables['lon'][:]
    lat = nc_data.variables['lat'][:]
    year = nc_data.variables['year'][:]
    tcc = nc_data.variables['tcc'][:]


    projection = nc_data.variables['tcc'].coordinates
    nodata = nc_data.variables['tcc'].missing_value
    
    lon_min, lat_max, lon_max, lat_min = [lon.min(), lat.max(), lon.max(), lat.min()]
    n_lon = len(lon)
    n_lat = len(lat)
    lon_res = (lon_max - lon_min) /(float(n_lon)-1)
    lat_res = (lat_max - lat_min) / (float(n_lat)-1)
    geotransform = (lon_min, lon_res, 0, lat_max, 0, -lat_res)


    for i in range(len(year)):
        year_value = year[i]
        tcc_value_array = tcc[i]

        #print(year_value)

        gtiff_driver = gdal.GetDriverByName('MEM')
        out_ds = gtiff_driver.Create('', n_lon, n_lat, 1, gdal.GDT_Float32)
        out_ds.SetProjection(projection)
        out_ds.SetGeoTransform(geotransform)

        out_band = out_ds.GetRasterBand(1)
        out_band.FlushCache()
        out_band.WriteArray(tcc_value_array)
        out_band.SetNoDataValue(float(nodata))
        out_band.ComputeStatistics(False)

        driver = gdal.GetDriverByName('GTiff')
        out_tif = pathout + '/' + str(year_value) + '_tcc.tif'
        driver.CreateCopy(out_tif, out_ds, strict=1, options=["TILED=YES", "COMPRESS=LZW"])

        del out_ds

    return



def main():
    data = r'C:\Users\Jayde\Desktop\nc\test.nc'
    pathout = r'C:\Users\Jayde\Desktop\nc\out_tifs'
    nc_to_tifs(data, pathout)

    return


if __name__ == "__main__":
    main()

    
