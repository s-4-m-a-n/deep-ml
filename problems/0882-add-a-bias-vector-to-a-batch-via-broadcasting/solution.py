import torch

def add_bias(x: torch.Tensor, b: torch.Tensor) -> torch.Tensor:
    # TODO: add b to every row of x using broadcasting
    x_shape = x.shape
    b_like_x = b.broadcast_to(x_shape)
    return x + b_like_x

