'''
@Descripttion: 
@version: 0.1
@Author: Jianbang Wang
@Date: 2020-06-18 11:28:30
'''

#计算机提取
def readf_pred(name):
    import re
    a=[]
    f = open(name,'r')
    f.readline()
    for line in f.readlines():
        if re.split(',',line.strip())[9] != "None":
            a.append(re.split(',',line.strip())[9])
        else:
            a.append('false')
    f.close()
    #print(a)
    return a

#人工解译
def readf_true(name):
    import re
    a=[]
    f = open(name,'r')
    f.readline()
    for line in f.readlines():
        if re.split(',',line.strip())[12] != "None":
            a.append(re.split(',',line.strip())[12])
        else:
            a.append('false')
    f.close()
    #print(a)
    return a

def main(pathin):
    import math
    from math import sqrt
    from sklearn.metrics import mean_absolute_error
    from sklearn.metrics import mean_squared_error
    from sklearn.metrics import r2_score

    y_pred = readf_pred(pathin)#计算机提取
    y_rg = readf_true(pathin)#人工解译
    
    y_predict = []#计算机提取
    y_test = []#计算机提取

    for i in range(len(y_pred)):
        if y_pred[i] == 'false' or y_rg[i] == 'false':
            pass
        else:
            y_predict.append(float(y_pred[i]) + 1970.0)
            y_test.append(float(y_rg[i]))

    print("mean_absolute_error:", mean_absolute_error(y_test, y_predict))
    print("mean_squared_error:", mean_squared_error(y_test, y_predict))
    print("rmse:", sqrt(mean_squared_error(y_test, y_predict)))
    print("r2 score:", r2_score(y_test, y_predict))

if __name__ == '__main__':
    pathin = r'E:\forest_data\ne\result_1\6_5__forest_ne_n500_all.csv'
    main(pathin)
    




    
    
