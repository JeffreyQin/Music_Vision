
import torch
from torch import utils
import pandas as pd 
import numpy as np
import cv2

from torchvision import transforms
from img_utils import ChordTransform

class ChordDataset(utils.data.Dataset):
    def __init__(self, validation=False):
        super(ChordDataset, self).__init__()

        self.label_df = pd.read_csv('./chord_data/label.csv')
        self.num_samples = len(self.label_df)
        self.labels = [self.label_df.iloc[idx, 1:] for idx in range(self.num_samples)]

        self.transform = transforms.Compose([ChordTransform])


    def __len__(self):
        return self.num_samples
    
    def __getitem__(self, index):

        img = cv2.imread(f'./chord_data/images/{index}.png')
        img = self.transform(img)
        label = np.array(self.labels[index], dtype=float)
        return {'image': img, 'label': label}
    

class MeasureDataset(utils.data.Dataset):
    def __init__(self, validation=False);
        super(ChordDataset, self).__init__()
    
    def __len__(self):
    
    def __getitem__(self, index):