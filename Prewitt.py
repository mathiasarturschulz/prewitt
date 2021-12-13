import cv2
import math
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

class Prewitt:
    """Classe responsável por gerar uma imagem utilizando o operador Prewitt

    :Authors:
        Mathias Artur Schulz <mathias@schulz.net.br>
    """


    def __init__(self, imageName) -> None:
        """Construtor da classe Prewitt

        Args:
            imageName (str): Nome da imagem base para geração da nova imagem
        """
        self.imageName = imageName


    def __generateData(self, img):
        """Método responsável pela geração do conteúdo da imagem

        Args:
            img (array): Imagem
        Returns:
            string: String com o conteúdo da imagem
        """
        # geração das duas máscaras
        # detecção das bordas verticais de uma imagem
        prewittx = [
            [-1,  0,  1],
            [-1,  0,  1],
            [-1,  0,  1]
        ]
        # detecção das bordas horizontais de uma imagem
        prewitty = [
            [-1, -1, -1],
            [ 0,  0,  0],
            [ 1,  1,  1]
        ]

        # busca a largura e altura da imagem
        width, height = img.shape

        # monta um array inicialmente com zeros
        pixels = np.zeros((int(width), int(height)))

        # percorre cada pixel da imagem
        for row in range(width - len(prewittx)):
            for col in range(height - len(prewittx)):
                Gx = 0
                Gy = 0
                # realiza os cálculos para cada pixel
                for i in range(len(prewittx)):
                    for j in range(len(prewitty)):
                        value = img[row + i, col + j]
                        Gx += prewittx[i][j] * value
                        Gy += prewitty[i][j] * value

                pixels[row + 1, col + 1] = int(math.sqrt(Gx * Gx + Gy * Gy))

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
        """
        # realiza a leitura da imagem já em tons de cinza
        img = cv2.imread(self.imageName, cv2.IMREAD_GRAYSCALE)

        data = self.__generateData(img)

        # realiza a geração do gráfico
        fig, axes = plt.subplots(
            ncols=2, sharex=True, sharey=True, figsize=(8, 4)
        )
        axes[0].imshow(img, cmap=plt.cm.gray)
        axes[0].set_title('Imagem Original')
        axes[1].imshow(data, cmap=plt.cm.gray)
        axes[1].set_title('Imagem com Operador Prewitt')
        for ax in axes:
            ax.axis('off')
        plt.tight_layout()
        plt.savefig(self.__filename())
