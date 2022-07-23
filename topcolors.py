import numpy as np
import matplotlib.pyplot as plt
from PIL import Image # for reading image files
import imageio
from colormap import rgb2hex
import pandas as pd

def get_colors(filename):

    my_img = Image.open('./static/images/'+filename)
    img_arr = np.array(my_img) 

    color_list = []

    for x in img_arr:
        for y in x:
            color_list.append(rgb2hex(y[0],y[1],y[2]))

    colors = pd.value_counts(np.array(color_list))
    top = colors.head(10)

    top_colors = top.to_dict()
    # bw = 255 - img_arr
    # # Save image as .png
    # #imageio.imsave('bw.png', bw)

    # plt.imshow(bw)
    # plt.show()

    return top_colors

# print(get_colors())
