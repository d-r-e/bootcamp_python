from matplotlib import image as mpimg
import matplotlib.pyplot as plt
import numpy as np

class ScrapBooker(object):
    
    def crop(self, array, dimensions, position=(0, 0)):
        if dimensions[0] > array.shape[0] or dimensions[1] > array.shape[1]:
            print("Cropping out of range")
            return array
        return np.array(array[position[0]:position[0] + dimensions[0], position[1]:position[1] + dimensions[1]])
    
    def thin(self, array, n, axis):
        array = np.delete(array, np.s_[::n], axis)
        return array
    
    def juxtapose(self, array, n, axis):
        if axis == 1 and n > 0:
            data = np.tile(array, (1, n))
            return np.array(data)
        elif axis == 0 and n > 0:
            data = np.tile(array, (n, 1))
            return np.array(data)
        else:
            return array
    
    def mosaic(self, array, n):
        return np.tile(array, (n,n))
