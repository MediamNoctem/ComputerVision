import cv2
from matplotlib import pyplot as plt


image = cv2.imread("C:\\Users\\romAn\\Documents\\GitHub\\ComputerVision\\labs\\img\\balmoral.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

top, bottom, left, right = 10, 10, 10, 10

replicated_image = cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_REPLICATE)

titles = ['Исходное изображение', 'Изображение с применением флага BORDER_REPLICATE']
images = [image, replicated_image]

for i in range(2):
    plt.subplot(1, 2, i + 1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
