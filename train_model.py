import torch
from torch import utils, optim, nn
from tqdm import tqdm
from absl import flags
import logging, os, sys

import numpy as np 
from dataset import ScoreDataset
from architecture import Kimchi, MODEL_PATH
from dataset import dataset_split

# mode
FLAGS = flags.FLAGS
flags.DEFINE_boolean('debug', False, '')
flags.DEFINE_boolean('evaluate_saved', False, '')
flags.DEFINE_boolean('generate_dataset_split', False, '')

# hyperparams
HP = flags.FLAGS
flags.DEFINE_integer('batch_size', 16, '')
flags.DEFINE_float('learning_rate', 1e-3, '')
flags.DEFINE_integer('train_epochs', 200, '')
flags.DEFINE_float('val_split', 0.1, '')
flags.DEFINE_float('test_split', 0.1, '')


# test/validation
def evaluate(model, device, evalset):
    eval_dataloader = utils.data.DataLoader(evalset, batch_size=1)

    model.to(device)
    model.eval()
    with torch.no_grad():
        for example_idx, example in tqdm(enumerate(eval_dataloader)):
            x_img, x_idx = example['image'].to(device), example['chord_idx'].to(device)
            y = example['label'].to(device)

            prediction = model(x_img, x_idx)
        
    model.train()
    return accuracy

# training
def train(trainset, valset):
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model_config = {"max_chord_num": trainset.max_chord_num}
    model = Kimchi(model_config).to(device)
    optimizer = optim.Adam(model.parameters(), lr=HP.learning_rate)
    loss_fn = nn.MSELoss()

    train_dataloader = utils.data.DataLoader(trainset, collate_fn=ScoreDataset.collate_fn, batch_size=HP.batch_size, pin_memory=(device=='cuda'), num_workers=0)

    best_loss = float('inf')
    model.train()
    for epoch_idx in enumerate(range(HP.train_epochs)):
        batch_losses = []
        for batch_idx, batch in tqdm(enumerate(train_dataloader)):
            x_img, x_idx = batch['images'].to(device), batch['chord_indices'].to(device)
            y = batch['labels'].to(device)
            print(y.shape)

            prediction = model(x_img, x_idx)
            print('dasdadasa')
            loss = loss_fn(prediction, y)
            
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            batch_losses.append(loss)

        epoch_loss = np.mean(batch_losses)
        epoch_acc = evaluate(model, device, valset)
        logging.info(f'epoch: {epoch_idx}, average loss: {epoch_loss}, accuracy: {epoch_acc}')
        if epoch_loss < best_loss:
            best_loss = epoch_loss
            torch.save(model.state_dict, MODEL_PATH)



def main():
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    logging.info('process started')

    if FLAGS.generate_dataset_split:
        dataset_split(HP.val_split, HP.test_split)
        choice = input('Dataset split generated. Continue? (y/n): ')
        if choice.lower() == 'n':
            exit()
    if FLAGS.evaluate_saved:
        testset = ScoreDataset(test=True)
        evaluate(testset)
        logging.info('evaluation complete')
    else:
        trainset = ScoreDataset()
        valset = ScoreDataset(val=True)
        train(trainset, valset)
        logging.info('training complete')


if __name__ == '__main__':
    FLAGS(sys.argv)
    HP(sys.argv)
    main()



