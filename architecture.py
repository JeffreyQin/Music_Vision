import torch
from torch import utils, nn

MODEL_PATH = './model/kimchi.pt'

class Kimchi(nn.Module):
    def __init__(self, config):
        super(Kimchi, self).__init__()

        self.img_height, self.img_width = 128, 256 
        self.chord_idx_range = config['max_chord_num'] + 1

        self.feature_extraction_layers = nn.Sequential(
            nn.Conv2d(in_channels=1, out_channels=4, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(num_features=4),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),

            nn.Conv2d(in_channels=4, out_channels=8, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(num_features=8),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )

        self.border_embedding = nn.Embedding(num_embeddings=self.img_width, embedding_dim=128)
        
        self.linear_layers = nn.Sequential(
            nn.Linear(in_features=8 * 32 * 128 + 128, out_features=256),
            nn.ReLU(inplace=True),
            nn.Linear(in_features=256, out_features=64),
            nn.ReLU(inplace=True),
            nn.Linear(in_features=64, out_features=11)
        )


    def forward(self, img, idx):
        x_img = self.feature_extraction_layers(img)
        x_img = x_img.view(-1, 8 * 32 * 128)
        x_idx = self.border_embedding(idx)
        
        x = torch.cat((x_img, x_idx), dim=1)
        x = self.linear_layers(x)
        return x
