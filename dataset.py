
import torch
from torch import utils
import pandas as pd 
import numpy as np
import cv2

from torchvision import transforms
from img_utils import *


class ScoreTransform(object):
    def __init__(self):

        self.height = 100
        self.width = 30
        
    def __call__(self, img):
        img = remove_white_border(img)
        img = rescale_image(img, self.width, self.height)
        
        return img
    
    

class ScoreDataset(utils.data.Dataset):
    def __init__(self, validation=False):
        super(ScoreDataset, self).__init__()

        self.label_df = pd.read_csv('./music_score/label.csv')
        self.num_samples = len(self.label_df)
        self.labels = [self.label_df.iloc[idx, 1:] for idx in range(self.num_samples)]

        self.transform = transforms.Compose([ScoreTransform])


    def __len__(self):
        return self.num_samples
    
    def __getitem__(self, index):

        img = cv2.imread(f'./music_score/images/{index}.png')
        img = self.transform(img)
        label = np.array(self.labels[index], dtype=float)
        return {'image': img, 'label': label}
    