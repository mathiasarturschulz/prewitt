from PIL import Image
import math
from skimage.data import camera
image = camera()

class Prewitt(object):

    def __init__(self, imPath):

        im = Image.open(imPath).convert('L')
        self.width, self.height = im.size
        mat = im.load()

        prewittx = [
            [-1, 0, 1],
            [-1, 0, 1],
            [-1, 0, 1]
        ]
        prewitty = [
            [1, 1, 1],
            [0, 0, 0],
            [-1, -1, -1]
        ]

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

inName = 'Fig2.ppm'
outName = 'Fig2-prewitt.jpg'
prewitt = Prewitt(inName)
prewitt.saveIm(outName)
