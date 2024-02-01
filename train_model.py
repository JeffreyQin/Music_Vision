import torch
from torch import utils, optim
from sklearn.model_selection import train_test_split
from tqdm import tqdm

import numpy as np 
from dataset import ScoreDataset

d = ScoreDataset()
print(d.__getitem__(1))




def main():
    return


if __name__ == '__main__':
    main()