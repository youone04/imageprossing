from PIL import Image
im = Image.open('colourfull_ab.jpg', 'r')
width, height = im.size
pixel_values = list(im.getdata())
print('pixel_values',pixel_values)
# print('length pixel',len(pixel_values))
# print('width' ,width)
# print('height' ,height)
# for x in pixel_values:
#   print(x)
