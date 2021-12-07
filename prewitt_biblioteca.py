# pip install scikit-image
import matplotlib.pyplot as plt
from skimage import filters
from skimage.data import camera

image = camera()
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
plt.savefig('images/prewitt_biblioteca.jpg')