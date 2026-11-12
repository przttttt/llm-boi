import torch
from main.utils.seed import set_seed

def test_seed():
    set_seed(0)
    a = torch.rand(3)
    set_seed(0)
    assert torch.equal(a, torch.rand(3))