'''
@Descripttion: 
@version: 0.1
@Author: Jianbang Wang
@Date: 2020-05-30 22:15:25
'''
#权重
def readf_qz(name):
    import re
    a=[]
    f = open(name,'r')
    f.readline()
    for line in f.readlines():
        a.append(float(re.split(',',line.strip())[1]))
    f.close()
    #print(a)
    return a

#计算机提取
def readf_jq(name):
    import re
    a=[]
    f = open(name,'r')
    f.readline()
    for line in f.readlines():
        #print(re.split(',',line.strip()))
        if re.split(',',line.strip())[9] != "None":
            a.append('true')
        else:
            a.append('false')
    f.close()
    #print(a)
    return a

#人工解译
def readf_rg(name):
    import re
    a=[]
    f = open(name,'r')
    f.readline()
    for line in f.readlines():
        if re.split(',',line.strip())[12] != "None":
            a.append('true')
        else:
            a.append('false')
    f.close()
    #print(a)
    return a

def main(pathin):
    from sklearn import metrics
    from sklearn.metrics import confusion_matrix
    from sklearn.metrics import classification_report
    import numpy as np

    y_jq = readf_jq(pathin)#计算机提取
    y_rg = readf_rg(pathin)#人工解译
    qz = readf_qz(pathin)#权重
    C = confusion_matrix(y_rg, y_jq, labels = ['true', 'false'], sample_weight = qz)
    print(C)
    print('overall accuracy:',np.sum(np.diag(C))/np.sum(C))
    print('Producer’s Accuracy(true):',C[0,0]/np.sum(C[0,:]))
    print('Producer’s Accuracy(false):',C[1,1]/np.sum(C[1,:]))
    print('User’s Accuracy(true):',C[0,0]/np.sum(C[:,0]))
    print('User’s Accuracy(false):',C[1,1]/np.sum(C[:,1]))
    return

if __name__ == '__main__':
    pathin = r'E:\forest_data\ne\result\new__forest_ne_n500_all.csv'
    main(pathin)
    




    
    
