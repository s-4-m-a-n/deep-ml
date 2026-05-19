import torch

def grad_of_quadratic(x_value: float) -> float:
    # TODO: build a tracked leaf for x, compute f(x), run backprop, return df/dx as a 
    x = torch.tensor(x_value, dtype=torch.float32, requires_grad=True)
    out = x**2 + 3*x + 2
    out.backward()
    return float(x.grad)
