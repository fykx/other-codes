def func(x, a, b):
    return a * x + b


def draw(data, pathout):
    from matplotlib import pyplot as plt
    from matplotlib.pyplot import MultipleLocator
    import matplotlib as mpl
    import matplotlib.gridspec as gridspec
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

    df_filter = df[(df[columns[0]] > 1985) & (df[columns[0]] < 2018)]
    df_before = df_filter[(df_filter[columns[0]] < 2000)]
    df_after = df_filter[(df_filter[columns[0]] >= 2000)]

    fig = plt.figure(figsize=(5.64173228346, 2.16535433071), dpi=700, frameon=True, tight_layout=True)
    gs = gridspec.GridSpec(1, 2)

    ax_0 = fig.add_subplot(gs[0, 0]) # loss

    x_0 = df_filter[columns[0]]
    y_0 = df_filter[columns[-1]]

    ax_0.bar(x_0, y_0, align='center', label='Loss', color='teal')
    ax_0.legend(fontsize=8, ncol=1, frameon=False, loc=2, bbox_to_anchor=(0,1.12), borderaxespad=0)# https://www.jb51.net/article/191933.htm
    


    popt_0_b, pcov_0_b = curve_fit(func, df_before[columns[0]], df_before[columns[-1]])
    a_0_b = popt_0_b[0]
    b_0_b = popt_0_b[1]
    slope, intercept, r_value_0_b, p_value, std_err = stats.linregress(df_before[columns[0]], df_before[columns[-1]])

    ax_0.plot(df_before[columns[0]], func(df_before[columns[0]], a_0_b, b_0_b), color='r', linestyle='-', linewidth=0.5)
    ax_0.text(1987, 500, "Slope = %.2f\nR$^{2}$ = %.2f"%(round(a_0_b,2), round(r_value_0_b*r_value_0_b,2)),fontdict={'size':'8','color':'k'})


    popt_0_a, pcov_0_a = curve_fit(func, df_after[columns[0]], df_after[columns[-1]])
    a_0_a = popt_0_a[0]
    b_0_a = popt_0_a[1]
    slope, intercept, r_value_0_a, p_value, std_err = stats.linregress(df_after[columns[0]], df_after[columns[-1]])

    ax_0.plot(df_after[columns[0]], func(df_after[columns[0]], a_0_a, b_0_a), color='r', linestyle='-', linewidth=0.5)
    ax_0.text(2007, 310, "Slope = %.2f\nR$^{2}$ = %.2f"%(round(a_0_a,2), round(r_value_0_a*r_value_0_a,2)),fontdict={'size':'8','color':'k'})


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

    ax_0.set_xticks(range(1985, 2020, 5))
    ax_0.set_xticklabels(range(1985, 2020, 5), fontsize=8, rotation=0)
    ax_0.set_yticks(range(0, 900, 200))
    ax_0.set_yticklabels(range(0, 900, 200), fontsize=8, rotation=0)

    ax_1 = fig.add_subplot(gs[0, 1], sharey=ax_0)
    plt.setp(ax_1.get_yticklabels(), visible=False)

    x_1 = df_filter[columns[0]]
    y_1_new = df_filter[columns[3]]
    y_1_reg = df_filter[columns[2]]

    ax_1.bar(x_1, y_1_reg, align = 'center', label='Regeneration', color='darkgreen')
    ax_1.bar(x_1, y_1_new, align = 'center', bottom = y_1_reg, label='Newborn', color='forestgreen')
    plt.legend(fontsize=8, ncol=2, frameon=False, loc=2, bbox_to_anchor=(0,1.12), borderaxespad=0)# https://www.jb51.net/article/191933.htm


    popt_1_b, pcov_1_b = curve_fit(func, df_before[columns[0]], df_before[columns[1]])
    a_1_b = popt_1_b[0]
    b_1_b = popt_1_b[1]
    slope, intercept, r_value_1_b, p_value, std_err = stats.linregress(df_before[columns[0]], df_before[columns[1]])

    ax_1.plot(df_before[columns[0]], func(df_before[columns[0]], a_1_b, b_1_b), color='r', linestyle='-', linewidth=0.5)
    ax_1.text(1987.5, 470, "Slope = %.2f\nR$^{2}$ = %.2f"%(round(a_1_b,2), round(r_value_1_b*r_value_1_b,2)),fontdict={'size':'8','color':'k'})


    popt_1_a, pcov_1_a = curve_fit(func, df_after[columns[0]], df_after[columns[1]])
    a_1_a = popt_1_a[0]
    b_1_a = popt_1_a[1]
    slope, intercept, r_value_1_a, p_value, std_err = stats.linregress(df_after[columns[0]], df_after[columns[1]])

    ax_1.plot(df_after[columns[0]], func(df_after[columns[0]], a_1_a, b_1_a), color='r', linestyle='-', linewidth=0.5)
    ax_1.text(2000, 520, "Slope = %.2f\nR$^{2}$ = %.2f"%(round(a_1_a,2), round(r_value_1_a*r_value_1_a,2)),fontdict={'size':'8','color':'k'})

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

    ax_1.set_xticks(range(1985, 2020, 5))
    ax_1.set_xticklabels(range(1985, 2020, 5), fontsize=8, rotation=0)
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
