def func(x, a, b):
    return a * x + b


def draw(data, pathout):
    from matplotlib import pyplot as plt
    from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
    import matplotlib as mpl
    import pandas as pd
    import numpy as np
    from scipy.interpolate import make_interp_spline
    import scipy.stats as stats
    from scipy.optimize import curve_fit

    mpl.font_manager.fontManager.addfont('/public/home/mfeng/jwang/Fonts/arial.ttf')
    mpl.rcParams['font.sans-serif'] = ['Arial'] # 设置全局字体
    mpl.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    df = pd.read_csv(data, header=0)
    columns = df.columns.values.tolist()# 读取列索引

    df_filter = df[(df[columns[1]] != -9999)]
    df_sort = df_filter.sort_values(by=columns[0])

    df_filter = df_sort[(df_sort[columns[0]] > 1985) & (df_sort[columns[0]] < 2018)]
    x = df_filter[columns[0]]
    y = df_filter[columns[1]]
    

    df_filter_b = df_sort[(df_sort[columns[0]] > 1985) & (df_sort[columns[0]] < 2000)]
    df_filter_a = df_sort[(df_sort[columns[0]] > 1999) & (df_sort[columns[0]] < 2018)]

    x_b = df_filter_b[columns[0]]
    y_b = df_filter_b[columns[1]]

    x_a = df_filter_a[columns[0]]
    y_a = df_filter_a[columns[1]]

    fig, ax = plt.subplots(1,1,figsize=(5.64173228346, 1.5), dpi=700, frameon=True)# 0.393700787402

    ax.plot(x, y, linewidth=0.5, label='', color='k', linestyle='-', marker='.', markersize=2, markerfacecolor='r', markeredgecolor='forestgreen')

    popt_b, pcov_b = curve_fit(func, x_b, y_b)
    a_b = popt_b[0]
    b_b = popt_b[1]
    slope, intercept, r_value_b, p_value, std_err = stats.linregress(x_b, y_b)

    ax.plot(x_b, func(x_b, a_b, b_b), color='r', linestyle='-', linewidth=0.5)
    ax.text(1987, 24, 'y = %.2fx - %.2f \nR$^{2}$ = %.2f'%(round(a_b,2), round(b_b,2)*(-1), round(r_value_b*r_value_b,2)),fontdict={'size':'8','color':'k'})

    popt_a, pcov_a = curve_fit(func, x_a, y_a)
    a_a = popt_a[0]
    b_a = popt_a[1]
    slope, intercept, r_value_a, p_value, std_err = stats.linregress(x_a, y_a)

    ax.plot(x_a, func(x_a, a_a, b_a), color='r', linestyle='-', linewidth=0.5)
    ax.text(2010, 21, 'y = %.2fx - %.2f \nR$^{2}$ = %.2f'%(round(a_a,2), round(b_a,2)*(-1), round(r_value_a*r_value_a,2)),fontdict={'size':'8','color':'k'})

    '''设置边框样式'''
    ax.spines['top'].set_color('k')
    ax.spines['right'].set_color('k')
    ax.spines['bottom'].set_linewidth(0.5)
    ax.spines['left'].set_linewidth(0.5)
    ax.spines['top'].set_linewidth(0.5)
    ax.spines['right'].set_linewidth(0.5)


    '''设置grid'''
    #plt.grid( color = 'black',linestyle='-.',linewidth = 0.2)

    ax.set_xlabel('Year', fontdict={'color': 'black', 'weight': 'normal', 'size':8})
    ax.set_ylabel('TCC mean (%)', fontdict={'color': 'black', 'weight': 'normal', 'size':8})

    ax.set_xticks(range(1986, 2019, 3))
    ax.set_xticklabels(range(1986, 2019, 3), fontsize=8, rotation=0)
    ax.set_yticks(range(20, 28, 2))
    ax.set_yticklabels(range(20, 28, 2), fontsize=8, rotation=0)

    ax.xaxis.set_major_locator(MultipleLocator(3))
    ax.xaxis.set_major_formatter('{x:.0f}')
    ax.xaxis.set_minor_locator(MultipleLocator(1))

    ax.yaxis.set_major_locator(MultipleLocator(2))
    ax.yaxis.set_major_formatter('{x:.0f}')
    ax.yaxis.set_minor_locator(MultipleLocator(1))

    ax.tick_params(which='both', direction='out', width=0.5, color='k')# axis:可选{'x', 'y', 'both'}，选择对哪个轴操作，默认是'both'
    ax.tick_params(which='major', length=3)
    ax.tick_params(which='minor', length=1.5)
    # https://blog.csdn.net/qq_35240640/article/details/89478662
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tick_params.html?highlight=tick_params#matplotlib.pyplot.tick_params

    fig.savefig(pathout + '/' + columns[0] + '.png', dpi=700, bbox_inches='tight', transparent=True)

    plt.close()

    return


def main():
    data = r'/public/home/mfeng/jwang/paper/10_ne/data/data_albers_tiles/result/1_mosaic/1_tcc/result/mean_median_stat.csv'
    pathout = r'/public/home/mfeng/jwang/paper/10_ne/data/data_albers_tiles/result/1_mosaic/1_tcc/result'
    draw(data, pathout)

    return

if __name__ == "__main__":
    main()