def test(input, output):
    import pandas as pd
    import scipy.stats as stats

    nn_1 = output + '/' + 'result_1' + '.csv'
    f_csv_1 = open(nn_1,'w')

    nn_2 = output + '/' + 'result_2' + '.csv'
    f_csv_2 = open(nn_2,'w')

    f = pd.ExcelFile(input)
    for sheet_name in f.sheet_names:
        df = pd.read_excel(input, sheet_name = sheet_name)
        station_names = list(df['站点名称'].drop_duplicates())# 获取站点名称
        plant_names = list(df['植物中文名'].drop_duplicates())# 获取植物中文名称
        column_names = df.columns.values[4:13]# 获取列名称

        for station_name in station_names:
            df_station_name = df[df['站点名称'] == station_name]
            beginning_of_flowering = df_station_name['开花始期']
            for column_name in column_names:
                values = df_station_name[column_name]
                r, p = stats.pearsonr(beginning_of_flowering, values)
                f_csv_1.write('{},{},{},{}\n'.format(station_name, column_name, r, p))

                values_1 = df_station_name[column_name]
                values_2 = df_station_name[column_name+'_']
                r_2, p_2 = stats.pearsonr(values_1, values_2)
                f_csv_2.write('{},{},{},{}\n'.format(station_name, column_name, r_2, p_2))
        
        for plant_name in plant_names:
            df_plant_name = df[df['植物中文名'] == plant_name]
            beginning_of_flowering = df_plant_name['开花始期']
            for column_name in column_names:
                values = df_plant_name[column_name]
                r, p = stats.pearsonr(beginning_of_flowering, values)
                f_csv_1.write('{},{},{},{}\n'.format(plant_name, column_name, r, p))

                values_1 = df_plant_name[column_name]
                values_2 = df_plant_name[column_name+'_']
                r_2, p_2 = stats.pearsonr(values_1, values_2)
                f_csv_2.write('{},{},{},{}\n'.format(plant_name, column_name, r_2, p_2))

        beginning_of_flowering = df['开花始期']
        for column_name in column_names:
            values = df[column_name]
            r, p = stats.pearsonr(beginning_of_flowering, values)
            f_csv_1.write('{},{},{}\n'.format(column_name, r, p))

            values_1 = df[column_name]
            values_2 = df[column_name+'_']
            r_2, p_2 = stats.pearsonr(values_1, values_2)
            f_csv_2.write('{},{},{}\n'.format(column_name, r_2, p_2))
    f_csv_1.close()
    f_csv_2.close()
    return

def main():
    input = r'D:\test\data\data.xlsx'
    output = r'D:\test\out'
    test(input, output)

if __name__ == "__main__":
    main()