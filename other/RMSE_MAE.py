'''
@Descripttion: 
@version: 0.1
@Author: Jianbang Wang
@Date: 2020-05-30 22:14:04
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
    y_pred = readf_pred(pathin)#计算机提取
    y_true = readf_true(pathin)#人工解译
    fykx = []
    for i in range(len(y_pred)):
        if y_pred[i] == 'false' or y_true[i] == 'false':
            pass
        else:
            fykx.append(float(y_pred[i]) - float(y_true[i]) + 1970.0)
    a = 0
    b = 0
    for j in fykx:
        a = a + j**2
    b = math.sqrt(a/len(fykx))
    print('RMSE:', b)
    c = 0
    d = 0
    for x in fykx:
        c = c + abs(x)
    d = c/len(fykx)
    print('MAE:', d)
    return

if __name__ == '__main__':
    pathin = r'E:\forest_data\ne\result\new__forest_ne_n500_all.csv'
    main(pathin)
    




    
    
