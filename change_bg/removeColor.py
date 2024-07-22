import os
from PIL import Image
root_path = 'change_bg\\'

def calc_diff(pixel, bg_color):
    return (pixel[0] - bg_color[0]) ** 2 + (pixel[1] - bg_color[1]) ** 2 + (pixel[2] - bg_color[2]) ** 2

# 采用pillow库
def remove_one_color_pillow(image_path):  
    delete_color = [237, 237, 237]
    threshold = 300
    img = Image.open(image_path)
    img = img.convert('RGBA')
    pixdata = img.load()
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            if calc_diff(pixdata[x, y], delete_color) < threshold:
                pixdata[x, y] = (255, 255, 255, 0)

    img.save(root_path + '\\output1.png')

# 合成两张图片
def combine():
    bg = Image.open(root_path + '\\bg.jpg')  # 背景图1
    fg = Image.open(root_path + '\\output1.png')  # 前景图
    bg.paste(fg, mask=fg)  # 以自身透明区域作为掩膜
    result_img = root_path + '\\result1.png'
    bg.save(result_img)  # 保存
    if os.path.exists(root_path + '\\output1.png'):
        os.remove(root_path + '\\output1.png')

remove_one_color_pillow(root_path + '\\fg.png')
combine()


