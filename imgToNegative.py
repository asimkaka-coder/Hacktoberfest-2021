from PIL import Image
import numpy as np

opened_img = Image.open('lena_color.gif')
grey_scale_img = opened_img.convert('L')
array_of_image = np.array(grey_scale_img)
l=256

for i in range(len(array_of_image)):
    for j in range(len(array_of_image[i])):
        r=array_of_image[i,j]
        s=l-1-r
        array_of_image[i,j]=s

neg_img = Image.fromarray(array_of_image)
