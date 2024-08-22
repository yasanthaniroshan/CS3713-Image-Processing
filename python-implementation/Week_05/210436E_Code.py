#!/usr/bin/env python3

import cv2
import numpy as np
import matplotlib.pyplot as plt
import os,sys

INDEX = "210436E"
CURRENT_DIR = os.getcwd()
IMAGE_URL = CURRENT_DIR + f'/Inputs/{INDEX}_SrcImage.jpg'
OUTPUT = CURRENT_DIR + '/Outputs'
GREYSCALE_IMAGE_URL = OUTPUT + f'/{INDEX}_OPImage_{1}.jpg'
PLOT_OUTPUT = OUTPUT + f'/{INDEX}_SubPlot.jpg'

def get_negative_image(src_image:np.ndarray)->np.ndarray:
    return 255 - src_image

def increase_brigtness(src_image:np.ndarray,percentage:float)->np.ndarray:
    if percentage > 1:
        percentage = percentage/100
    percentage += 1
    return np.clip(src_image*percentage,0,255).astype(np.uint8)

def reduce_contrast(src_image: np.ndarray, low: int, high: int) -> np.ndarray:
    normalized_image = (src_image - np.min(src_image)) / (np.max(src_image) - np.min(src_image))
    scaled_image = normalized_image * (high - low) + low
    return np.clip(scaled_image, low, high).astype(np.uint8)

def reduce_grey_depth(src_image:np.ndarray,new_grey_depth)->np.ndarray:
    factor = 256//(2**new_grey_depth)
    return (src_image//factor)

def vertical_mirror(src_image:np.ndarray)->np.ndarray:
    return np.array([arr[::-1] for arr in src_image])

try:
    image = cv2.imread(IMAGE_URL,cv2.IMREAD_GRAYSCALE)
except:
    print("Error in loading Image")
    sys.exit()

try :
    cv2.imwrite(GREYSCALE_IMAGE_URL,image)
except:
    print("Error in Saving File")
    sys.exit()

neg_image = get_negative_image(image)
bright_image = increase_brigtness(image,20)
contrast_image = reduce_contrast(image,125,175)
grey_depth_reduced_image = reduce_grey_depth(image,2)
flipped_image = vertical_mirror(image)

plt.subplot(2, 3, 1)
plt.title("Original Image")
plt.imshow(image, cmap='gray')

plt.subplot(2, 3, 2)
plt.title("Negative Image")
plt.imshow(neg_image, cmap='gray')

plt.subplot(2, 3, 3)
plt.title("Bright Image")
plt.imshow(bright_image, cmap='gray')

plt.subplot(2, 3, 4)
plt.title("Contrasted Image")
plt.imshow(contrast_image, cmap='gray')

plt.subplot(2, 3, 5)
plt.title("Reduced Grey Image")
plt.imshow(grey_depth_reduced_image*16, cmap='gray')

plt.subplot(2, 3, 6)
plt.title("Flipped Image")
plt.imshow(flipped_image, cmap='gray')

plt.savefig(PLOT_OUTPUT, pad_inches=1)

plt.show()
