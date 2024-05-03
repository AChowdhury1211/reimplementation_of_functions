import torch
import torch.nn as nn
import numpy as np
from torchvision.utils import save_image, make_grid
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import os
import torchvision.transforms as transforms
from torch.utils.data import Dataset
from PIL import Image

def change_dim(in_filter , out_filter, x: torch.tensor):
    conv1 = nn.Conv2d(in_filter,out_filter,3,1,1)
    conv2 = nn.Conv2d(out_filter, out_filter,3,1,1)
    x1 = conv1(x)
    x2 = conv2(x1)

    if in_filter==out_filter:
        out = x + x2
    
    else:
        conv3 = nn.Conv2d(x.shape[1], x2.shape[1],3,1,1 ) # no of channels
        out = conv3(x) + x2
    
    return out

x = torch.randn(1,3,4,3)
res = change_dim(3, 1, x)
print(res)