import cv2
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
        # realiza a leitura da imagem
        img = cv2.imread(self.imageName)

        # converte a imagem para YUV
        yuvImg = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

        # aplica a equalização
        yuvImg[:, :, 0] = cv2.equalizeHist(yuvImg[:, :, 0])

        # converte para RGB
        histEqualization = cv2.cvtColor(yuvImg, cv2.COLOR_YUV2BGR)

        return histEqualization

    def __filename(self):
        """Método responsável por gerar o nome da imagem

        Returns:
            string: Nome da imagem
        """
        return 'images/eq-{}-{}.ppm'.format(
            self.imageName.split('.')[0], datetime.now()
        )

    def generate(self):
        """Método responsável por gerar a imagem

        Returns:
            string: Nome da imagem gerada
        """
        data = self.__generateData()

        cv2.imwrite(self.__filename(), data)
