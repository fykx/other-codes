def draw(data, pathout):
    from matplotlib import pyplot as plt
    from matplotlib.pyplot import MultipleLocator
    import pandas as pd
    import numpy as np
    from scipy.interpolate import make_interp_spline

    df = pd.read_csv(data, header=0)
    columns = df.columns.values.tolist()# 读取列索引

    df_filter = df[(df[columns[1]] != -9999)]
    df_sort = df_filter.sort_values(by=columns[0])

    x = df_sort[columns[0]]
    y = df_sort[columns[1]]

    x_smooth = np.linspace(x.min(),x.max(),400)
    y_smooth = make_interp_spline(x,y)(x_smooth)

    fig, ax = plt.subplots(1,1,figsize=(3.14960629921,1.1811024), dpi=700, frameon=True)# 0.393700787402

    ax.plot(x_smooth, y_smooth, linewidth=0.5, label='', color='k', linestyle='-', marker='')

    '''设置边框样式'''
    ax.spines['top'].set_color('k')
    ax.spines['right'].set_color('k')
    ax.spines['bottom'].set_linewidth(0.5)
    ax.spines['left'].set_linewidth(0.5)
    ax.spines['top'].set_linewidth(0.5)
    ax.spines['right'].set_linewidth(0.5)

    '''设置tick样式'''
    ax.tick_params(axis='both', direction='out', length=1.5, width=0.5, color='k', pad=2)
    # https://blog.csdn.net/qq_35240640/article/details/89478662
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tick_params.html?highlight=tick_params#matplotlib.pyplot.tick_params

    '''设置grid'''
    #plt.grid( color = 'black',linestyle='-.',linewidth = 0.2)

    ax.set_xlabel('Elevation (m)', fontdict={'family': 'Arial', 'color': 'black', 'weight': 'normal', 'size':7.5})
    ax.set_ylabel('TCC mean (%)', fontdict={'family': 'Arial', 'color': 'black', 'weight': 'normal', 'size':7.5})

    ax.set_xticks(range(0, 3000, 500))
    ax.set_xticklabels(range(0, 3000, 500), family='Arial', fontsize=7.5, rotation=0)
    ax.set_yticks(range(0, 60, 10))
    ax.set_yticklabels(range(0, 60, 10), family='Arial', fontsize=7.5, rotation=0)   

    fig.savefig(pathout + '/' + columns[0] + '.png', dpi=700, bbox_inches='tight')

    plt.close()

    return


def main():
    data = r'C:\Users\Jayde\Desktop\paper\dem\2_stat\stat.csv'
    pathout = r'C:\Users\Jayde\Desktop\paper\dem\2_stat'
    draw(data, pathout)

    return

if __name__ == "__main__":
    main()
