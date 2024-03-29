import torch
import torch.nn as nn


class ConfidNet(nn.Module):
    def __init__(self, small=False, input_size=128,):
        super(ConfidNet, self).__init__()
        self.small = small
        self.input_size = input_size

        if small:
            self.uncertainty = nn.Linear(input_size, 1)
        else:
            self.uncertainty = nn.Sequential(
                nn.Linear(input_size, 400),
                nn.ReLU(inplace=True),
                nn.Linear(400, 400),
                nn.ReLU(inplace=True),
                nn.Linear(400, 400),
                nn.ReLU(inplace=True),
                nn.Linear(400, 400),
                nn.ReLU(inplace=True),
                nn.Linear(400, 1),
            )

    def forward(self, x):
        return torch.sigmoid(self.uncertainty(x))
