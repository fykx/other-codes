def draw(data, pathout):
    from matplotlib import pyplot as plt
    from matplotlib.pyplot import MultipleLocator
    import matplotlib as mpl
    import matplotlib.gridspec as gridspec
    import pandas as pd
    import numpy as np
    from scipy.interpolate import make_interp_spline

    mpl.font_manager.fontManager.addfont('/public/home/mfeng/jwang/Fonts/arial.ttf')
    mpl.rcParams['font.sans-serif'] = ['Arial'] # 设置全局字体
    mpl.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    df = pd.read_csv(data, header=0)
    columns = df.columns.values.tolist()# 读取列索引

    fig = plt.figure(figsize=(5.64173228346, 1.57480314961), dpi=700, frameon=True, tight_layout=True)
    gs = gridspec.GridSpec(1, 3)

    ax_0 = fig.add_subplot(gs[0, 0])

    value_0_percentage = round(df.loc[0][1]/df[columns[1]].sum()*100, 2)
    value_others_percentage = 100 - value_0_percentage

    labels = ['TCC=0', 'TCC>0']
    values = [value_0_percentage, value_others_percentage]
    colors = [ 'orange','forestgreen',]
    explode = [0, 0.1]

    wedges, texts, autotexts = ax_0.pie(values, labels=labels, colors=colors, explode=explode, labeldistance=1.1, pctdistance=0.5, shadow=False, textprops=dict(color="k", fontsize=8), autopct='%1.1f%%', startangle=70, rotatelabels=0)
    '''
    x       :(每一块)的比例，如果sum(x) > 1会使用sum(x)归一化；
    labels  :(每一块)饼图外侧显示的说明文字；
    explode :(每一块)离开中心距离；
    startangle :起始绘制角度,默认图是从x轴正方向逆时针画起,如设定=90则从y轴正方向画起；
    shadow  :在饼图下面画一个阴影。默认值：False，即不画阴影；
    labeldistance :label标记的绘制位置,相对于半径的比例，默认值为1.1, 如<1则绘制在饼图内侧；
    autopct :控制饼图内百分比设置,可以使用format字符串或者format function
            '%1.1f'指小数点前后位数(没有用空格补齐)；
    pctdistance :类似于labeldistance,指定autopct的位置刻度,默认值为0.6；
    radius  :控制饼图半径，默认值为1；
    counterclock ：指定指针方向；布尔值，可选参数，默认为：True，即逆时针。将值改为False即可改为顺时针。
    wedgeprops ：字典类型，可选参数，默认值：None。参数字典传递给wedge对象用来画一个饼图。例如：wedgeprops={'linewidth':3}设置wedge线宽为3。
    textprops ：设置标签（labels）和比例文字的格式；字典类型，可选参数，默认值为：None。传递给text对象的字典参数。
    center ：浮点类型的列表，可选参数，默认值：(0,0)。图标中心位置。
    frame ：布尔类型，可选参数，默认值：False。如果是true，绘制带有表的轴框架。
    rotatelabels ：布尔类型，可选参数，默认为：False。如果为True，旋转每个label到指定的角度。
    '''

    ax_1 = fig.add_subplot(gs[0, 1:])

    df_filter = df[(df['value'] > 0)]

    x = df_filter[columns[0]]
    y = df_filter[columns[1]]

    ax_1.bar(x, y, align='center', color='forestgreen')

    '''设置边框样式'''
    ax_1.spines['top'].set_color('k')
    ax_1.spines['right'].set_color('k')
    ax_1.spines['bottom'].set_linewidth(0.5)
    ax_1.spines['left'].set_linewidth(0.5)
    ax_1.spines['top'].set_linewidth(0.5)
    ax_1.spines['right'].set_linewidth(0.5)

    '''设置tick样式'''
    ax_1.tick_params(axis='both', direction='out', length=1.5, width=0.5, color='k', pad=2)
    # https://blog.csdn.net/qq_35240640/article/details/89478662
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tick_params.html?highlight=tick_params#matplotlib.pyplot.tick_params

    '''设置grid'''
    #plt.grid( color = 'black',linestyle='-.',linewidth = 0.2)

    ax_1.set_xlabel('TCC (%)', fontdict={'color': 'black', 'weight': 'normal', 'size':8})
    ax_1.set_ylabel('Area (1000×ha)', fontdict={'color': 'black', 'weight': 'normal', 'size':8})

    ax_1.set_xticks(range(0, 110, 10))
    ax_1.set_xticklabels(range(0, 110, 10), fontsize=8, rotation=0)
    ax_1.set_yticks(range(0, 7000, 2000))
    ax_1.set_yticklabels(range(0, 7000, 2000), fontsize=8, rotation=0)   

    fig.savefig(pathout + '/' + columns[0] + '.png', dpi=700, bbox_inches='tight', transparent=True)

    plt.close()

    return


def main():
    data = r'/public/home/mfeng/jwang/paper/10_ne/result/1_Spatial_distribution/reslut/hist/2_stat/stat.csv'
    pathout = r'/public/home/mfeng/jwang/paper/10_ne/result/1_Spatial_distribution/reslut/hist/2_stat'
    draw(data, pathout)

    return

if __name__ == "__main__":
    main()
