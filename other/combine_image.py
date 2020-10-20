'''
@Descripttion: 将两张图片合并在一起，输出新的图片并完成标注
@version: 0.1
@Author: Jianbang Wang
@Date: 2020-05-24 13:20:08
'''

def listdatas(pathin):
    import os
    
    a = []
    datas = os.listdir(pathin)
    for i in datas:
        if i[-4:] == '.png':
            fn_i = pathin + '/' + i
            a.append(fn_i)
    return a

def Create_list(pathin_1, pathin_2):
    images_1 = listdatas(pathin_1)
    images_2 = listdatas(pathin_2)
    a = []
    for i in images_1:
        for j in images_2:
            if i.split("/")[-1].split(".")[0].replace('_','') == j.split("/")[-1].split(".")[0].replace('_',''):
                b = []
                b.append(i)
                b.append(j)
                a.append(b)
    return a

def combine_image(image_list, pathout, left_or_right):
    from PIL import Image, ImageDraw, ImageFont

    img1 = Image.open(image_list[0])
    img2 = Image.open(image_list[1])
    #arr是一个列表，里面是两个图片的路径，例如["p1.png", 'p2.png']
    toImage = Image.new('RGB', (max(img1.size[0], img2.size[0]), img1.size[1] + img2.size[1]),(255,255,255))
    
    toImage.paste(img1, (0, 0))
    toImage.paste(img2, (left_or_right, img1.size[1]))#参数100用来调整下面一副图像的左右位置
    #函数描述：toImage:背景图片,paste()函数四个变量分别为：起始横轴坐标，起始纵轴坐标，横轴结束坐标，纵轴结束坐标；

    draw = ImageDraw.Draw(toImage)
    fnt = ImageFont.truetype(r'C:\Windows\Fonts\timesbd.ttf', 20)#设置字体
    draw.text((70, 0), 'name_ID = ' + image_list[0].split("/")[-1].split(".")[0].replace('_',''), fill='black', font = fnt)

    toImage.save(pathout + '/' +  image_list[0].split("/")[-1].split(".")[0].replace('_','') + '.png')
    
    print(image_list[0].split("/")[-1].split(".")[0].replace('_',''))
    return

def main(pathin_1, pathin_2, pathout, left_or_right):
    image_lists  =Create_list(pathin_1, pathin_2)
    for image_list in image_lists:
        combine_image(image_list, pathout, left_or_right)
    return

if __name__ == "__main__":
    pathin_1 = r'E:\forest_data\ne\ys'
    pathin_2 = r'E:\forest_data\ne\rg'
    pathout = r'E:\forest_data\ne\out'
    left_or_right = 100
    main(pathin_1, pathin_2, pathout, left_or_right)