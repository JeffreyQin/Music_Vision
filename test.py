import cv2
from img_utils import rescale_image, remove_white_border

img = cv2.imread('./chord_data/images/2.png')
img = remove_white_border(img)
img = rescale_image(img,20,20)
cv2.imshow('img', img)
cv2.waitKey()