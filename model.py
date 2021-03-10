import torch.nn as nn
import torch.nn.functional as F
import torch


class ConvNet(nn.Module):
    def __init__(self):
        super(ConvNet, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=10, kernel_size=5)
        self.pool1 = nn.MaxPool2d(kernel_size=2)
        self.conv2 = nn.Conv2d(in_channels=10, out_channels=20, kernel_size=3)
        self.pool2 = nn.MaxPool2d(kernel_size=2)
        self.fc = nn.Linear(5 * 5 * 20, 10)

    def forward(self, x):
        x = F.relu(self.pool1(self.conv1(x)))
        x = F.relu(self.pool2(self.conv2(x)))
        # print(x.size())
        x = torch.flatten(x, 1)
        x = self.fc(x)

        return x

    def summary(self):
        return sum(p.numel() for p in self.parameters())

net = ConvNet()
net.load_state_dict(torch.load('state_dict_model.pt'))
