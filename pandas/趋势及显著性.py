def listdatas(pathin):
    import os

    a = []
    datas = os.listdir(pathin)
    for i in datas:
        if i.endswith('.csv'):
            fn_i = pathin + '/' + i
            a.append(fn_i)
    return a

'''定义拟合函数'''
def func(x, a, b):
    return a * x + b

def test(input):
    import pandas as pd
    import numpy as np
    from scipy.optimize import curve_fit
    import scipy.stats as stats
    import math

    df = pd.read_csv(input, header=0)
    df_filter = df[(df['start'] != -9999) & (df['end'] != -9999)]

    result_dict = {}

    if len(df_filter) >= 2:
        for i in df_filter.columns:
            if i != 'year':
                popt, pcov = curve_fit(func, np.array(range(len(df_filter))), df_filter[i])
                result_dict[i+'_k'] = popt[0]

                r,p = stats.pearsonr(np.array(range(len(df_filter))),df_filter[i])
                result_dict[i+'_p'] = p
                result_dict[i+'_r'] = r
                

                if len(df_filter) > 2 and result_dict[i+'_r'] != None and result_dict[i+'_r'] != 1 and result_dict[i+'_k'] != None and result_dict[i+'_k'] != 0 and (1-result_dict[i+'_r']*result_dict[i+'_r'])/(len(df_filter)-1-1) > 0:
                    t = result_dict[i+'_r']/math.sqrt((1-result_dict[i+'_r']*result_dict[i+'_r'])/(len(df_filter)-1-1))
                    
                    s = t / result_dict[i+'_k']
                    result_dict[i+'_s'] = s
                else:
                    result_dict[i+'_s'] = None
                
                
    else:
        for i in df_filter.columns:
            if i != 'year':
                result_dict[i+'_k'] = None
                result_dict[i+'_p'] = None
                result_dict[i+'_r'] = None
                result_dict[i+'_s'] = None

    return result_dict

def main():
    import numpy as np
    import pandas as pd
    pathin = r'C:\Users\Jayde\Desktop\test\out'
    pathout = r'C:\Users\Jayde\Desktop\test\out_1'
    datas = listdatas(pathin)

    out_csv = {}
    for input in datas:
        print(input)
        result_dict = test(input)
        out_csv[input.split('/')[-1].split('_')[0]] = result_dict
    
    frame = pd.DataFrame(out_csv).T
    frame.index.name = 'zd'
    frame.to_csv(pathout + '/' + 'k_p_r_s.csv')

if __name__ == "__main__":
    main()