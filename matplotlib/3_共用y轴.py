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

    fig = plt.figure(figsize=(5.64173228346, 1.96850393701), dpi=700, frameon=True, tight_layout=True)
    gs = gridspec.GridSpec(1, 2)

    ax_0 = fig.add_subplot(gs[0, 0]) # loss

    x_0 = df[columns[0]]
    y_0 = df[columns[-1]]

    ax_0.bar(x_0, y_0, align='center', color='c')

    '''设置边框样式'''
    ax_0.spines['top'].set_color('k')
    ax_0.spines['right'].set_color('k')
    ax_0.spines['bottom'].set_linewidth(0.5)
    ax_0.spines['left'].set_linewidth(0.5)
    ax_0.spines['top'].set_linewidth(0.5)
    ax_0.spines['right'].set_linewidth(0.5)

    ax_0.tick_params(axis='both', direction='out', length=1.5, width=0.5, color='k', pad=2)

    ax_0.set_xlabel('Year', fontdict={'color': 'black', 'weight': 'normal', 'size':8})
    ax_0.set_ylabel('Area (1000×ha)', fontdict={'color': 'black', 'weight': 'normal', 'size':8})

    ax_0.set_xticks(range(1985, 2025, 5))
    ax_0.set_xticklabels(range(1985, 2025, 5), fontsize=8, rotation=0)
    ax_0.set_yticks(range(0, 900, 200))
    ax_0.set_yticklabels(range(0, 900, 200), fontsize=8, rotation=0)



    ax_1 = fig.add_subplot(gs[0, 1], sharey=ax_0)
    plt.setp(ax_1.get_yticklabels(), visible=False)
    # http://www.dovov.com/gridspecpython.html

    x_1 = df[columns[0]]
    y_1 = df[columns[1]]

    ax_1.bar(x_1, y_1, align='center', color='forestgreen')

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

    ax_1.set_xlabel('Year', fontdict={'color': 'black', 'weight': 'normal', 'size':8})
    #ax_1.set_ylabel('Area (1000×ha)', fontdict={'color': 'black', 'weight': 'normal', 'size':8})

    ax_1.set_xticks(range(1985, 2025, 5))
    ax_1.set_xticklabels(range(1985, 2025, 5), fontsize=8, rotation=0)
    #ax_1.set_yticks(range(0, 1000, 200))
    #ax_1.set_yticklabels(range(0, 1000, 200), fontsize=8, rotation=0)  

    fig.savefig(pathout + '/' + columns[0] + '.png', dpi=700, bbox_inches='tight', transparent=True)

    plt.close()

    return


def main():
    data = r'/public/home/mfeng/jwang/paper/10_ne/result/2_loss_gain/4_result/result.csv'
    pathout = r'/public/home/mfeng/jwang/paper/10_ne/result/2_loss_gain/4_result'
    draw(data, pathout)

    return

if __name__ == "__main__":
    main()
