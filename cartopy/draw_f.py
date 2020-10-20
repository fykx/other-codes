'''
Descripttion: 
version: 0.1
Author: Jianbang Wang
Date: 2020-08-05 12:24:40
'''
import os
import matplotlib.pyplot as plt
import matplotlib as mpl
import cartopy.crs as ccrs
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import cartopy.feature as cfea
import numpy as np
from osgeo import gdal
import geopandas as gpd
import xarray as xr

'''列出数据'''
def listdatas(pathin):
    import os

    a = []
    datas = os.listdir(pathin)
    for i in datas:
        if i.endswith('.tif'):
            fn_i = pathin + '/' + i
            a.append(fn_i)
    return a

def draw(img, pathout):
    da = xr.open_rasterio(img)
    da_= da.values[0].astype(float)
    da_[np.where(da_>100.0)] = np.nan
    da.values=np.array([da_])

    fig = plt.figure(figsize=(9,4),dpi=300,linewidth=0.5) #设置画布
    ax = fig.add_subplot(1,1,1,projection=ccrs.PlateCarree()) #添加子图

    cmap = plt.get_cmap('YlGn')#gist_rainbow_r,Spectral,RdYlBu,tab20c,tab10,Set2设置色带颜色
    norm = mpl.colors.Normalize(vmin=1, vmax=100)

    img_out = da.plot(ax=ax,transform=ccrs.PlateCarree(),cmap=cmap,add_colorbar=False,extend='both',norm=norm)

    cbar1=fig.colorbar(img_out, ax=ax,orientation='vertical',pad=0.02,extendrect=False,\
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
    #ax.set_ylim(33.5,40)
    #ax.set_xlim(72,79)
    ax.set_title(img.split('/')[-1].split('.')[0])

    fig.savefig(pathout + '/' + img.split('/')[-1].split('.')[0] + '.png', dpi=300, bbox_inches='tight')
    plt.close()
    return

def main():
    pathin = r'E:\forest_data\805\dxal\tcc\maps\1234a'
    pathout = r'C:\Users\fykx\Desktop\test_code\out'
    imgs = listdatas(pathin)
    for img in imgs:
        print(img.split('/')[-1])
        draw(img, pathout)
    return

if __name__ == "__main__":
    main()


