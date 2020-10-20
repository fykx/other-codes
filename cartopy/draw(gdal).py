def listdatas(pathin):
    import os

    a = []
    datas = os.listdir(pathin)
    for i in datas:
        if i.endswith('.tif'):
            fn_i = pathin + '/' + i
            a.append(fn_i)
    return a

def get_geotiff_wkt(dataset):
    '''Get WKT projection information from geotiff'''
    from osgeo import osr

    proj = dataset.GetProjection()

    proj_wkt = osr.SpatialReference()
    proj_wkt.ImportFromWkt(proj)

    return proj_wkt


def get_cartopy_proj(proj_wkt):
    '''Extract EPSG code from WKT and get cartopy projection
       NOTE: code must be projected coordinate system, not geodetic coordinate
       system'''
    import cartopy.crs

    #projcs = proj_wkt.GetAuthorityCode('PROJCS')
    projcs = int(proj_wkt.GetAttrValue('Authority',1))

    #TODO make handle other geodetic projections
    if projcs==4326:
        projection = cartopy.crs.PlateCarree()
    else:
        projection = cartopy.crs.epsg(projcs)
    return projection


def plot_geotiff(file_path, pathout):
    from osgeo import gdal, osr
    import matplotlib.pyplot as plt
    import matplotlib as mpl
    from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
    import cartopy.feature as cfea
    import numpy as np

    # Read file, data, and geotransform
    gdal.UseExceptions()
    dataset = gdal.Open(file_path)

    data = dataset.ReadAsArray()
    geotransform = dataset.GetGeoTransform()

    ## http://geoinformaticstutorial.blogspot.no/2012/09/reading-raster-data-with-python-and-gdal.html
    ## Dataset parameters
    #cols = dataset.RasterXSize
    #rows = dataset.RasterYSize
    #bands = dataset.RasterCount
    #driver = dataset.GetDriver().LongName

    ## Geotransform parameters
    #origin_x     = geotransform[0] # top left x
    #pixel_width  = geotransform[1] # w-e pixwl resolution
    #x_rot        = geotransform[2] # rotation, 0 = "north up"
    #origin_y     = geotransform[3] # top left y
    #y_rot        = geotransform[4] # rotation, 0 = "north up"
    #pixel_height = geotransform[5] # n-s pixel resolution

    # Get projection for plotting
    proj_wkt = get_geotiff_wkt(dataset)
    projection = get_cartopy_proj(proj_wkt)

    # Create plot
    subplot_kw = dict(projection=projection)
    fig, ax = plt.subplots(figsize=(9, 4), dpi=300, linewidth=0.5, subplot_kw=subplot_kw)

    extent = (geotransform[0],
              geotransform[0] + dataset.RasterXSize * geotransform[1],
              geotransform[3] + dataset.RasterYSize * geotransform[5],
              geotransform[3])

    plot_data = np.ma.masked_where(data>100, data)

    cmap = plt.get_cmap('YlGn')#gist_rainbow_r,Spectral,RdYlBu,tab20c,tab10,Set2设置色带颜色
    norm = mpl.colors.Normalize(vmin=1, vmax=100)

    img = ax.imshow(plot_data, extent=extent, cmap=cmap, origin='upper')

    cbar1=fig.colorbar(img, ax=ax,orientation='vertical',pad=0.02,extendrect=False,\
                 fraction=0.04,extend='both')
    cbar1.ax.tick_params(labelsize=7,direction='in',pad=1.2,width=0.5,length=2,labelrotation=90)
    cbar1.set_label('TCC',fontsize=7,labelpad=1.5)

    pt = ax.gridlines(draw_labels=True,linestyle='--',alpha=0.8,linewidth=0.5)#显示经纬度必须得要虚线框
    pt.xlabel_style={'size':7}
    pt.ylabel_style={'size':7}
    pt.xlabels_top = False
    pt.ylabels_right = False
    pt.xformatter = LONGITUDE_FORMATTER
    pt.yformatter = LATITUDE_FORMATTER
    ax.set_title(file_path.split('/')[-1].split('.')[0])

    fig.savefig(pathout + '/' + file_path.split('/')[-1].split('.')[0] + '.png', dpi=300, bbox_inches='tight')
    plt.close()

    return None

def main():
    pathin = r'/home/forest/tianshui/tcc_c'
    pathout = r'/home/forest/tianshui/2_result/gif'

    datas = listdatas(pathin)
    for file_path in datas:
        print(file_path.split('/')[-1])
        plot_geotiff(file_path, pathout)
    return


if __name__ == '__main__':
    main()