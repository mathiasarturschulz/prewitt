import cv2
import math
import numpy as np
from datetime import datetime

class Prewitt:
    """Classe responsável por gerar uma imagem utilizando o operador Prewitt
    """

    def __init__(self, imageName) -> None:
        """Construtor da classe Prewitt

        Args:
            imageName (str): Nome da imagem base para geração da nova imagem
        """
        self.imageName = imageName

    def __generateData(self):
        """Método responsável pela geração do conteúdo da imagem

        Returns:
            string: String com o conteúdo da imagem
        """
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

        # realiza a leitura da imagem já em tons de cinza
        img = cv2.imread(self.imageName, cv2.IMREAD_GRAYSCALE)

        # busca a largura e altura da imagem
        width, height = img.shape

        pixels = np.zeros((int(width), int(height)))
        print('pixels')
        print(pixels)

        linScale = .3

        #For each pixel in the image
        for row in range(width-len(prewittx)):
            for col in range(height-len(prewittx)):
                Gx = 0
                Gy = 0
                for i in range(len(prewittx)):
                    for j in range(len(prewitty)):
                        val = img[row+i, col+j] * linScale
                        Gx += prewittx[i][j] * val
                        Gy += prewitty[i][j] * val

                pixels[(row+1),(col+1)] = int(math.sqrt(Gx*Gx + Gy*Gy))

        print('pixels')
        print(pixels)
        return pixels

    def __filename(self):
        """Método responsável por gerar o nome da imagem

        Returns:
            string: Nome da imagem
        """
        return 'images/prewitt-{}-{}.jpg'.format(
            self.imageName.split('.')[0], datetime.now()
        )

    def generate(self):
        """Método responsável por gerar a imagem

        Returns:
            string: Nome da imagem gerada
        """
        data = self.__generateData()

        cv2.imwrite(self.__filename(), data)



prewitt = Prewitt('Fig2.ppm')
prewitt.generate()
