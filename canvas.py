import numpy as np
from PIL import Image


class Canvas:

    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color

        # create a 3d numpy array of zeros
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        self.data[:] = self.color

    def make(self, image_path):
        """Converts the current array into an image file"""
        img = Image.fromarray(self.data, 'RGB')
        img.save(image_path)
