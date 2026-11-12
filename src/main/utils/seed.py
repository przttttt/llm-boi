import torch

def set_seed(seed=1337):
    torch.manual_seed(seed)