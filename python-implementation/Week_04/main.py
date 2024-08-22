import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image = cv.imread('rgb.jpg', cv.IMREAD_COLOR)
print(image.shape)