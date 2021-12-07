# pip install scikit-image
import cv2
import matplotlib.pyplot as plt
from skimage import filters

# realiza a leitura da imagem
image = cv2.imread('Fig2.ppm', cv2.IMREAD_GRAYSCALE)

prewitt = filters.prewitt(image)
# prewitt = filters.prewitt_h(image)
# prewitt = filters.prewitt_v(image)

fig, axes = plt.subplots(
    ncols=2, sharex=True, sharey=True, figsize=(8, 4)
)

axes[0].imshow(image, cmap=plt.cm.gray)
axes[0].set_title('Imagem Original')

axes[1].imshow(prewitt, cmap=plt.cm.gray)
axes[1].set_title('Filtro Prewitt')

for ax in axes:
    ax.axis('off')

plt.tight_layout()
# plt.show()
plt.savefig('images/Fig2.jpg')
