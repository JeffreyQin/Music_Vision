import os

# rename all image data files
def rename_img_files():
    chord_img_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), './chord_data/images/')
    measure_img_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), './measure_data/images/')
    
    for idx, img in enumerate(os.listdir(chord_img_path)):
        os.rename(chord_img_path + img, chord_img_path + f'{idx}.png')
    for idx, img in enumerate(os.listdir(measure_img_path)):
        os.rename(measure_img_path + img, measure_img_path + f'{idx}.png')


rename_img_files()