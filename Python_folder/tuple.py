import torch
def instance_check(tensors):
    tensors = (tensors,)  if isinstance(tensors, torch.Tensor) else print(tuple(tensors))
    """ notice torch.Tensor is a type not a function  
    lets say, 
    y = torch.randn(1,2)
    t = tuple(y)
    v = (y,)
    t: It is a tuple where each element of the tensor y becomes an element in the tuple, so t will have the same number of elements as y.
    v: It is a tuple containing the tensor y as its single element. So, v will always have one element regardless of the shape or size of y.
    """
    print(2*2)
    

x = torch.randn(1,2)    
instance_check(x)

