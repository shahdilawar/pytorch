'''
A tensor is an array of numerical values that can be multidimensional. 
*   A one-dimensional tensor is called a vector.
*   a two-dimensional tensor is called a matrix. and for 
*   higher dimensions, it is referred to as an n-order tensor.
'''

import torch
#import torchvision
import logging as log

# set log level to INFO
log.basicConfig(level=log.INFO)

class TensorDemo:
    
    def __init__(self, range_val : int) -> None:
        self.range_val = range_val

    # Create a Vector
    def tensor_as_vector(self) -> torch.Tensor:
        return torch.arange(self.range_val)
    
    # Create a two dimensional tensor
    def tensor_2d(self, range_val, row : int, col : int) -> torch.Tensor:
        self.range_val = range_val
        #create a 2D Tensor
        tensor_2d_obj = torch.arange(self.range_val).reshape(row, col)
        return tensor_2d_obj
    # initialize tensor with zeros
    def initialize_tensor_with_zeroes(self, no_of_axes : int, 
                                      row : int, 
                                      col : int) -> torch.Tensor:
        return torch.zeros(no_of_axes, row, col)
    # initialize tensor with ones
    def initialize_tensor_with_ones(self, no_of_axes : int, 
                                    row : int, 
                                    col : int) -> torch.Tensor:
        return torch.ones(no_of_axes, row, col)
    def initialize_tensor_with_random_num(self, no_of_axes : int, 
                                          row : int, 
                                          col : int) -> torch.Tensor:
        return torch.randn(no_of_axes, row, col)

    #create a tensor initialized
    #   1. initialize with zeroes, ones or rand int
    #   2. no of axes - 2D or 3D
    def initialize_tensor(self, inititialize_with : str,
                           no_of_axes : int, 
                           row : int, 
                           col : int) -> torch.Tensor:
        if (inititialize_with == "0"):
            tensor_obj = self.initialize_tensor_with_zeroes(no_of_axes,
                                                             row, col)
        elif (inititialize_with == "1"):
            tensor_obj = self.initialize_tensor_with_ones(no_of_axes,
                                                           row, col)
        else:
            tensor_obj = self.initialize_tensor_with_random_num(no_of_axes,
                                                                 row, col)
        return tensor_obj

# Test method
def test_classes():
    # initialize TensorDemo class
    tensor_demo = TensorDemo(12)
    # create a vector.
    tensor_obj = tensor_demo.tensor_as_vector()
    log.info(f" Type is { type(tensor_obj) } ")
    log.info(f"Vector is : {tensor_obj}")
    #dimension
    log.info(f"dimesnsion is : {tensor_obj.dim()}")
    #size
    log.info(f"Size is : {tensor_obj.numel()}")

    ##############################################
    # create a 2D Tensor 
    #seek shape tuple
    row = int( input ("Enter no of rows : "))  
    col = int( input ("Enter no of cols : "))  

    #call the tensor2 method
    tensor_2d_obj = tensor_demo.tensor_2d(12, row, col)
    log.info(f"tensor_2d is : {tensor_2d_obj}")

    ##############################################

    #call the initialize tensor obj
    # seek type, axes, row and columns
    initialized_type = input ("Enter initialization type <0, 1 or random: ")
    no_of_axes = int (input ("Enter no of axes : ") )
    row = int( input ("Enter no of rows : "))  
    col = int( input ("Enter no of cols : "))  

    tensor_initialized_obj = tensor_demo.initialize_tensor( initialized_type, 
                                                           no_of_axes, 
                                                           row, 
                                                           col )
    log.info( f"initialized tensor : \n {tensor_initialized_obj}" )

if __name__ == "__main__":
    test_classes()



