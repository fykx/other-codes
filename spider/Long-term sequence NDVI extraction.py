'''
@Descripttion: Long-term sequence NDVI extraction based on landsat data
@version: 0.1
@Author: Jianbang Wang
@Date: 2020-05-23 09:39:32
'''
import socket
socket.setdefaulttimeout(20)

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

def generate_url(pathin_data):
    list_data = readf(pathin_data)
    urls = {}
    for i in list_data:
        url = "https://tpts01.terrapulse.com:8090/_gee_ndvi?format=png&w=1040&h=220&agg=month&x={0}&y={1}".format(str(i[1]),str(i[2]))
        urls[i[0]] = url
    return urls

def Download_picture(pathin_data, pathout):
    from urllib import request
    import os
    import ssl

    ssl._create_default_https_context = ssl._create_unverified_context

    nn = pathout + '/'+'Failed_task'+'.txt'
    f = open(nn, 'w')
    
    urls_dict = generate_url(pathin_data)
    for i in urls_dict.keys():
        print("name_ID："+ str(i) + "开始下载！")
        src = urls_dict[i]
        image_name = str(i) + ".png"
        try:
            request.urlretrieve(src, os.path.join(pathout, image_name))
        except socket.timeout:
            count = 1
            while count <= 5:
                try:
                    print("第{}尝试重新下载name_ID：{}".format(count, str(i)))
                    request.urlretrieve(src, os.path.join(pathout, image_name))
                    print("第{}尝试重新下载name_ID：{}成功！".format(count, str(i)))
                    break
                except socket.timeout:
                    print("第{}尝试重新下载name_ID：{}失败！".format(count, str(i)))
                    count += 1
            if count > 5:
                print("name_ID：{}下载失败！".format(str(i)))
                f.write("{}\n".format(i))
    f.close()                
    return

if __name__ == "__main__":
    pathin_data = r'E:\forest_data\ne\forest_ne_n500_all.csv'
    pathout = r'E:\forest_data\ne\out'
    Download_picture(pathin_data, pathout)

