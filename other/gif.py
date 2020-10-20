'''
@Descripttion: 
@version: 0.1
@Author: Jianbang Wang
@Date: 2020-07-27 16:25:20
'''

def listdatas(pathin):
    import os
    
    a = []
    datas = os.listdir(pathin)
    for i in datas:
        if i.endswith('.png'):
            fn_i = pathin + '/' + i
            a.append(fn_i)
    return a


def create_gif(image_list, gif_name, duration, pathout):
    import imageio

    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))

    imageio.mimsave(pathout + '/' + gif_name, frames, 'GIF', duration=duration)
    return

def main():
    pathin = r'E:\forest_data\tianshui\2_out'
    image_list = listdatas(pathin)
    image_list.sort()
    gif_name = 'new.gif'
    duration = 1.5
    pathout = r'E:\forest_data\tianshui\3_out'
    create_gif(image_list, gif_name, duration, pathout)

if __name__ == '__main__':
    main()