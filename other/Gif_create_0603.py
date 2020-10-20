# -*- coding: utf-8 -*-
"""
Created on Fri May 29 10:53:22 2020

@author: zkyxby
"""

'''
以下这段代码的作用主要是用来制作Gif动态图，通过这种方法做出的图像是对静态图片没有限制。
'''

import imageio
import os

def listdatas(pathin):
    a = []
    datas = os.listdir(pathin)
    for i in datas:
        if i[-4:] == '.jpg' :
            fn_i = pathin + '/' + i
            a.append(fn_i)
    return a

def create_gif(image_list,gif_name,duration = 1.0):
    '''
    :param image_list :这个列表用于存放生成动图的原始图片
    :param gif_name: 字符串，所生成gif文件名，带.gif后缀
    :param  duration: 图像间隔时间
    :return 
    '''
    
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))
    
    imageio.mimsave(gif_name,frames,'GIF',duration = duration)
    
    return

def main(pathin,pathout,name,duration):
    '''
    这里放上自己需要合成的图片
    '''
    
    '''
    这里需要得到一个list,list里面的每个文件需要带上文件名后缀，然后将这个list
    作为create_gif()函数的image_list
    '''
    image_list = listdatas(pathin)
    gif_name = pathout + '/' + name
    create_gif(image_list,gif_name,duration)
    
    #image_list = ['1.jpg','2.jpg','3.jpg']
    #gif_name = 'new0603.gif'
    #create_gif(image_list,gif_name,duration)

if __name__ == "__main__":
    name = "a.gif"
    pathin = r"C:\Users\zkyxby\Desktop\input_picture"
    pathout = r"C:\Users\zkyxby\Desktop\out_picture"
    duration = 0.5
    main(pathin,pathout,name,duration)
