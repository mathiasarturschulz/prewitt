
#
#
#
# 1
#
#
#

# import numpy as np
# import cv2
# import matplotlib.pyplot as plt
# import matplotlib.image as mpig

# #define kernal convolution function
# # with image X and filter F
# def convolve(X, F):
#     # height and width of the image
#     X_height = X.shape[0]
#     X_width = X.shape[1]

#     # height and width of the filter
#     F_height = F.shape[0]
#     F_width = F.shape[1]

#     H = (F_height - 1) // 2
#     W = (F_width - 1) // 2

#     #output numpy matrix with height and width
#     out = np.zeros((X_height, X_width))
#     #iterate over all the pixel of image X
#     for i in np.arange(H, X_height-H):
#         for j in np.arange(W, X_width-W):
#             sum = 0
#             #iterate over the filter
#             for k in np.arange(-H, H+1):
#                 for l in np.arange(-W, W+1):
#                     #get the corresponding value from image and filter
#                     a = X[i+k, j+l]
#                     w = F[H+k, W+l]
#                     sum += (w * a)
#             out[i,j] = sum
#     #return convolution
#     return out

# # Using prewitt operator
# # Prewitt operator is similar to the Sobel operator and is used for detecting vertical and horizontal edges in images.
# # It provides us two masks one for detecting edges in horizontal direction and another for detecting edges in an vertical direction.

# # read the image in gray scale
# img = cv2.imread('output/knife.jpg',cv2.IMREAD_GRAYSCALE)
# plt.imshow(img,cmap='gray')

# # define horizontal and Vertical sobel kernels
# Hx = np.array([[-1, 0, 1],[-1, 0, 1],[-1, 0, 1]])
# Hy = np.array([[-1, -1, -1],[0, 0, 0],[1, 1, 1]])

# # normalizing the vectors
# pre_x = convolve(img, Hx) / 6.0
# pre_y = convolve(img, Hy) / 6.0

# # calculate the gradient magnitude of vectors
# pre_out = np.sqrt(np.power(pre_x, 2) + np.power(pre_y, 2))
# # mapping values from 0 to 255
# pre_out = (pre_out / np.max(pre_out)) * 255

# # output images
# cv2.imwrite('output/prewitt_knife.jpg', pre_out)
# plt.imshow(pre_out, cmap = 'gray', interpolation = 'bicubic')
# plt.show()



#
#
#
# 2
#
#
#
"""
Written in Python 2.7!
This module takes an image and converts it to grayscale, then applies a
Prewitt operator.
"""

__author__ = "Kevin Gay"

from PIL import Image
import math
from skimage.data import camera
image = camera()

class Prewitt(object):

    def __init__(self, imPath):

        im = Image.open(imPath).convert('L')
        self.width, self.height = im.size
        mat = im.load()

        prewittx = [[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]
        prewitty = [[1, 1, 1], [0, 0, 0], [-1, -1, -1]]

        self.prewittIm = Image.new('L', (self.width, self.height))
        pixels = self.prewittIm.load()

        linScale = .3

        #For each pixel in the image
        for row in range(self.width-len(prewittx)):
            for col in range(self.height-len(prewittx)):
                Gx = 0
                Gy = 0
                for i in range(len(prewittx)):
                    for j in range(len(prewitty)):
                        val = mat[row+i, col+j] * linScale
                        Gx += prewittx[i][j] * val
                        Gy += prewitty[i][j] * val

                pixels[row+1,col+1] = int(math.sqrt(Gx*Gx + Gy*Gy))

    def saveIm(self, name):
        self.prewittIm.save(name)

def test():
    im = 'jaguar'
    inName = im + '.jpg'
    outName = im + '-prewitt.jpg'
    prewitt = Prewitt(inName)
    prewitt.saveIm(outName)
