def draw(input):
    '''使用pandas读取数据绘制折线图'''
    import pandas as pd
    import matplotlib.pyplot as plt

    f = pd.ExcelFile(input)
    for sheet_name in f.sheet_names:
        df = pd.read_excel(input, sheet_name = sheet_name)
        fig = plt.figure(figsize=(7, 5), dpi=300)
        ax = fig.add_subplot(111)
        ax.plot(df['year'], df['mean'],'co--', markersize=8, label='mean')
        ax.plot(df['year'], df['max'],'go--', markersize=8, label='max')
        ax.plot(df['year'], df['median'],'bo--', markersize=8, label='median')
        plt.legend()
        plt.title(sheet_name)

        plt.ylabel('NDVI') 
        plt.xlabel('year')
        #fig.autofmt_xdate()

        fig.savefig(sheet_name + '.png', dpi=300)
    return

def main():
    input = r'C:\Users\Jayde\Desktop\me\me.xlsx'
    draw(input)

if __name__ == "__main__":
    main()