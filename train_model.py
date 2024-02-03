import torch
from torch import utils, optim, nn
from sklearn.model_selection import train_test_split
from tqdm import tqdm
from absl import flags

import numpy as np 
from dataset import ScoreDataset
from architecture import Kimchi, MODEL_PATH

# hyperparameters
HP = flags.FLAGS
flags.DEFINE_boolean('debug', False, '')
flags.DEFINE_integer('batch_size', 16, '')
flags.DEFINE_float('learning_rate', 1e-3, '')
flags.DEFINE_integer('train_epochs', 200, '')
flags.DEFINE_boolean('train_saved', False, '')



def validate():
    return


def train(trainset, testset):
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model = Kimchi().to(device)
    optimizer = optim.Adam(model.parameters(), lr=HP.learning_rate)
    loss_fn = nn.MSELoss()

    train_dataloader = utils.data.DataLoader(trainset, pin_memory=(device=='cuda'), num_workers=0, batch_size=HP.batch, shuffle=False)

    for epoch_idx, epoch in enumerate(range(HP.epochs)):
        
        for batch_idx, (imgs, labels) in tqdm(enumerate(train_dataloader)):
            
            
        




def main():
    trainset = ScoreDataset(validation=False)
    testset = ScoreDataset(validation=True)
    
    choice = input('Image data processed. Continue? (y/n): ')
    if choice.lower() == 'n':
        exit()

    model = train(trainset, testset)

    choice = input('Model trained. Save? (y/n): ')
    if choice.lower() == 'n':
        exit()

    torch.save(model.state_dict(), PATH)



if __name__ == '__main__':
    main()



