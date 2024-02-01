import cv2
from img_utils import enhance_image, remove_white_border

img = cv2.imread('./music_score/images/2.png')

img = enhance_image(img)

cv2.imshow('img',img)
cv2.waitKey()

img = remove_white_border(img)

cv2.imshow('img',img)
cv2.waitKey()
