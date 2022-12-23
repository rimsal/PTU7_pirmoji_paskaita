# Turime logo su peršviečiamu fonu, dydis 128*128.
# Atsisiųskite, ir perdarykite taip, kad nuo viršaus ir
# apačios nusiimtų po 28 eilutes pikselių. Išsisaugokite,
# nes naudosime sekančioms užduotims.

# 1 UZDUOTIS
# from PIL import Image
#
# im = Image.open("logo.png")
# region = im.crop(box=(0, 28, 128, 100))
# region.save('test_logo.png')


# 2 UZDUOTIS

# from PIL import Image, ImageEnhance
# import os
#
# def enhance_image(pic, contrast, color, sharpness, brightness, save=False):
#     im = Image.open(pic)
#     enh = ImageEnhance.Contrast(im)
#     im = enh.enhance(contrast)
#     enh = ImageEnhance.Color(im)
#     im = enh.enhance(color)
#     enh = ImageEnhance.Brightness(im)
#     im = enh.enhance(brightness)
#     enh = ImageEnhance.Sharpness(im)
#     im = enh.enhance(sharpness)
#     if save:
#         loc = os.path.splitext(pic)[0]
#         ext = os.path.splitext(pic)[1]
#         im.save(f'{loc}_modified{ext}')
#     im.show()
#
# enhance_image('dog.jpg', 2, 0, 5, 1, True)

# 3 UZDUOTIS

# from PIL import Image
# import os
#
# def get_list(folder):
#     files = os.listdir(folder)
#     images = []
#     for i in files:
#         if i.endswith(('.jpg', '.png')):
#            images.append(folder+'/'+i)
#     return images
#
# def pic_resize(pic, height):
#     im = Image.open(pic)
#     width = round(im.size[1]/im.size[0]*height)
#     im = im.resize((height, width))
#     return im
#
# def optimize_images(folder, height):
#     os.mkdir(f'{folder}/optimized')
#     logo = Image.open('test_logo.png')
#     pic_num = 0
#     for i in get_list(folder):
#         pic = Image.open(i)
#         pic = pic_resize(i, height)
#         logo_location = (
#             pic.size[0]-logo.size[0],
#             pic.size[1]-logo.size[1],
#             pic.size[0],
#             pic.size[1])
#         pic.paste(logo, logo_location, logo)
#         pic_num += 1
#         pic.save(f'{folder}/optimized/picture_{pic_num}.png')
#

