"""This file contains the code necessary to make predictions on an input image of size 28x28"""

import torch
import torch.nn as nn
import torch.utils.data

import numpy as np

INPUT_VECTOR_SIZE = 784
NUM_CLASSES = 2


def setup():
    class Net(nn.Module):
        def __init__(self):
            super().__init__()
            self.conv1 = nn.Conv2d(1, 16, kernel_size=(3, 3), stride=1,
                                    padding=1)  # 1 input channel since the image is in black and white format.
            self.act1 = nn.ReLU()
            self.drop1 = nn.Dropout(0.3)

            self.conv2 = nn.Conv2d(16, 16, kernel_size=(3, 3), stride=1, padding=1)
            self.act2 = nn.ReLU()
            self.pool2 = nn.MaxPool2d(kernel_size=(2, 2))

            self.flat = nn.Flatten()

            self.fc3 = nn.Linear(3136, 512)
            self.act3 = nn.ReLU()
            self.drop3 = nn.Dropout(0.5)

            self.fc4 = nn.Linear(512, 10)

        def forward(self, x):
            # input 1x28x28, output 8x28x28
            x = self.act1(self.conv1(x))
            x = self.drop1(x)
            # input 8x28x28, output 8x28x28
            x = self.act2(self.conv2(x))
            # input 8x28x28, output 8x14x14
            x = self.pool2(x)
            # input 8x14x14, output 1568
            x = self.flat(x)
            # input 1568, output 512
            x = self.act3(self.fc3(x))
            x = self.drop3(x)
            # input 512, output 10
            x = self.fc4(x)
            return x

    device = torch.device('cpu')
    global MODEL
    MODEL = Net()
    MODEL.load_state_dict(
        torch.load('model_module/Model.pt',
                   map_location=device))


def make_prediction(data: np.ndarray, convolutional=False):
    if convolutional:
        data = data.reshape(1, 1, 28, 28)

    x = torch.Tensor(data)

    MODEL.eval()
    with torch.no_grad():
        output = MODEL(x)
        S = nn.Softmax(dim=0)

        if convolutional:
            data = output.data[0]
        else:
            data = output.data

        probabilities = S(data)
    _, pred = torch.max(data, 0)

    MODEL.train()
    return pred, probabilities
