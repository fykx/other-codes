def listdatas(pathin):
    import os

    a = []
    datas = os.listdir(pathin)
    for i in datas:
        if i.endswith('.xls'):
            fn_i = pathin + '/' + i
            a.append(fn_i)
    return a

def test(input, pathout):
    import pandas as pd

    df = pd.read_excel(input, sheet_name=0, header=0)
    years = df['Year'].unique()

    out_csv = {}

    for year in years:
        df_year = df[(df['Year'] == year) & (df['depth'] > 0) & (df['depth'] < 100)]

        result = {}

        if len(df_year) < 5:
            result['start'] = -9999
            result['end'] = -9999
            result['Dl'] = -9999
            result['Ds'] = -9999
            result['Db'] = -9999
        else:
            a = 0
            for i in range(0, len(df_year)):
                if i+4 <= len(df_year)-1:
                    if df_year.iloc[i+4]['DOY'] == df_year.iloc[i]['DOY'] + 4:
                        a = 1
                        break
            if a == 1:
                result['start'] = df_year.iloc[i]['DOY']
            else:
                result['start'] = -9999

            b = 0
            for j in range(len(df_year),0,-1):
                j = j - 1
                if j-4 >= 0:
                    if df_year.iloc[j]['DOY'] == df_year.iloc[j-4]['DOY'] + 4:
                        b = 1
                        break
            if b == 1:
                result['end'] = df_year.iloc[j]['DOY']
            else:
                result['end'] = -9999

            if a == 1 and b == 1:
                result['Dl'] = result['end'] - result['start'] + 1

                df_Ds = df_year[(df_year['DOY'] >= result['start']) & (df_year['DOY'] <= result['end'])]
                result['Ds'] = len(df_Ds)

                result['Db'] = result['Dl'] - result['Ds']
            else:
                result['Dl'] = -9999
                result['Ds'] = -9999
                result['Db'] = -9999


        out_csv[year] = result
    
    frame = pd.DataFrame(out_csv).T
    frame.index.name = 'year'
    frame.to_csv(pathout + '/' + input.split('/')[-1].split('.')[0] + '_out.csv')
    return

def main():
    pathin = r'C:\Users\Jayde\Desktop\test\data'
    pathout = r'C:\Users\Jayde\Desktop\test\out'
    datas = listdatas(pathin)
    for input in datas:
        try:
            print(input,'开始处理！')
            test(input, pathout)
        except:
            print(input,'数据格式有误！')


if __name__ == "__main__":
    main()