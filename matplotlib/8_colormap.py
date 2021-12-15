def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=100):
    import matplotlib.colors as colors
    import matplotlib.pyplot as plt
    import numpy as np

    new_camp = colors.LinearSegmentedColormap.from_list("trunc{n},{a:.2f},{b:.2f}".format(n=cmap.name, a=minval, b=maxval), cmap(np.linspace(minval, maxval, n)))
    return new_camp


def draw(data, x_name, y_name):
    import matplotlib.colors as colors
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd

    df = pd.read_csv(data, header=0)
    x_value = df[x_name]
    y_value = df[y_name]

    fig, ax = plt.subplots()
    ax.set(xlim=(x_value.min(), x_value.max()), ylim=(y_value.min(),y_value.max()), autoscale_on=False)

    a = np.array([[2, 2],
                [1, 1]])

    width = 0.4
    for x, y in zip(x_value, y_value):
        cmap = plt.cm.RdYlGn_r
        new_camp = truncate_colormap(cmap, minval=0.0, maxval=y/y_value.max(), n=100)
        #ax.xaxis.set_ticks_position('left')
        #ax.yaxis.set_ticks_position('bottom')
        #ax.clear()
        #ax.invert_yaxis()
        ax.imshow(a, interpolation='bicubic', extent=(x, x+width, 0, y), cmap=new_camp)

    ax.set_aspect('auto')
    plt.show()
    return

def main():
    data = r'C:\Users\Jayde\Desktop\test\data.csv'
    x_name = 'year'
    y_name = 'loss'
    draw(data, x_name, y_name)

    return

if __name__ == '__main__':
    main()
