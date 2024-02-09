import torch
from torch import utils
import pandas as pd 
import numpy as np
import cv2
import random, json

from torchvision import transforms
from img_utils import *

def dataset_split(val_split, test_split):
    label_df = pd.read_csv('./music_score/label.csv')
    id = label_df.iloc[:,0].tolist()
    val_test_id = random.sample(id, int(len(id) * (val_split + test_split)))
    train_id = [idx for idx in id if idx not in val_test_id]
    val_id = random.sample(val_test_id, int(len(val_test_id) * val_split / (val_split + test_split)))
    test_id = [idx for idx in val_test_id if idx not in val_id]
    with open('./music_score/dataset_split.json', 'w') as f:
        json.dump({
            'train': train_id,
            'val': val_id,
            'test': test_id
        }, f)


class ScoreTransform(object):
    def __init__(self):
        self.height = 128
        self.width = 512
        
    def __call__(self, img):
        img = enhance_image(img)
        img = rescale_image(img, self.width, self.height) 
        return img
    
    
class ScoreDataset(utils.data.Dataset):
    def __init__(self, val=False, test=False):
        super(ScoreDataset, self).__init__()

        self.label_df = pd.read_csv('./music_score/label.csv')
        with open('music_score/dataset_split.json', 'r') as f:
            split = json.load(f)
            if val:
                self.id = split['val']
            elif test:
                self.id = split['test']
            else:
                self.id = split['train']
        self.num_examples = len(self.id)
        self.max_chord_num = max(self.label_df.iloc[:, 2].tolist())
        
        self.images = {idx: self.label_df.iloc[idx, 1] for idx in self.id}
        self.chord_indices = {idx: self.label_df.iloc[idx, 2] for idx in self.id}
        self.labels = {idx: self.label_df.iloc[idx, 3:] for idx in self.id}

        self.transform = transforms.Compose([ScoreTransform()])

    def __len__(self):
        return self.num_examples
    
    def __getitem__(self, index):
        img = cv2.imread(f'./music_score/labelled_images/{self.images[index]}.png')
        img = self.transform(img)
        label = self.labels[index]
        
        example = {"image": img, "chord_idx": self.chord_indices[index], "label": label}
        return example
    
    def collate_fn(batch):
        images = torch.tensor([ex['image'] for ex in batch]).float()
        images = images.view(images.size(0), -1, images.size(1), images.size(2))
        chord_indices = torch.tensor([ex['chord_idx'] for ex in batch])
        labels = torch.tensor([ex['label'] for ex in batch]).float()
        return {'images': images, 'chord_indices': chord_indices, 'labels': labels}

