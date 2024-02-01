import os
import cv2

# rename all image data files to indices
def rename_img_files():
    img_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), './music_score/images/')
    
    for idx, img in enumerate(os.listdir(img_folder)):
        os.rename(img_folder + img, img_folder + f'{idx}.png')


# remove white borders at top and bottom of image
def remove_white_border(img):
    y_top, y_bottom = 0, len(img) - 1
    border_removed = False
    for y in range(len(img)):
        for x in range(len(img[0])):
            if not all(el == 255 for el in img[y][x]):
                y_top = y
                border_removed = True
                break
        if border_removed:
            break
    border_removed = False
    for y in reversed(range(len(img))):
        for x in range(len(img[0])):
            if not all (el == 255 for el in img[y][x]):
                y_bottom = y
                border_removed = True
                break
        if border_removed:
            break
    return img[y_top : y_bottom + 1]

# rescale image (distorts aspect ratio)
def rescale_image(img, width, height):
    return cv2.resize(img, (width, height), interpolation=cv2.INTER_LINEAR)

# other processes
def enhance_image(img):
    return img

