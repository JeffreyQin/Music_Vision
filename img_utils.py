import os
import cv2
import numpy as np 


# remove white borders at top and bottom of image
def remove_white_border(img):
    y_top, y_bottom = 0, len(img) - 1
    border_removed = False
    for y in range(len(img)):
        for x in range(len(img[0])):
            if img[y,x] != 0:
                y_top = y
                border_removed = True
                break
        if border_removed:
            break
    border_removed = False
    for y in reversed(range(len(img))):
        for x in range(len(img[0])):
            if img[y,x] != 0:
                y_bottom = y
                border_removed = True
                break
        if border_removed:
            break
    return img[y_top : y_bottom + 1, :]

# rescale image (distorts aspect ratio)
def rescale_image(img, width, height):
    return cv2.resize(img, (width, height), interpolation=cv2.INTER_LINEAR)


# other processes
def enhance_image(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # grayscaling
    img = cv2.GaussianBlur(img, (3,3), 0) # gaussian bluring
    _, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU) # otsu thresholding
    img = cv2.bitwise_not(img) # inverse color for better feature extraction

    img = np.array(img).astype('float32')
    img /= 255.0 # pixel normalization
    return img