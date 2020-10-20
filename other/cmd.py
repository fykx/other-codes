'''
@Descripttion: 使用py调用cmd
@version: 0.1
@Author: Jianbang Wang
@Date: 2020-05-24 12:32:25
'''

def readf(pathin_data):
    import re

    a=[]
    f = open(pathin_data,'r')
    f.readline()
    for line in f.readlines():
        b = []
        b.append(float(re.split(',',line.strip())[0]))#name_ID
        b.append(float(re.split(',',line.strip())[3]))#lon
        b.append(float(re.split(',',line.strip())[4]))#lat
        a.append(b)
    f.close()
    return a

def main(pathin_data, pathout):
    import os

    list_data = readf(pathin_data)
    for i in list_data:
        os.system(r"python extract_tcc_records_tiles.py -i E:\forest_data\ne\tcc\maps -o {}\{}_.png -c {} {}"\
        .format(pathout, str(i[0]), str(i[2]), str(i[1])))
    return

if __name__ == "__main__":
    pathin_data = r'E:\forest_data\ne\forest_ne_n500_all.csv'
    pathout = r'C:\Users\fykx\Desktop\out'
    main(pathin_data, pathout)

