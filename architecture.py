import torch
from torch import utils, nn

CLASSIFIER_MODEL_PATH = './models/classifier_model.pth'
LOCALIZER_MODEL_PATH = './models/localizer_model.pth'

class LocalizerModel(nn.Module):
    def __init__(self):
        super(LocalizerModel, self).__init__()
    
    def forward(input):
        return


class ClassifierModel(nn.Module):
    def __init__(self):
        super(ClassifierModel, self).__init__()

    def forward(input):
        return