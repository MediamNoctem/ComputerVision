import cv2
import numpy as np
from matplotlib import pyplot as plt


def increase_brightness(image, value=30):
    kernel = np.ones((1, 1), np.uint8) * value
    brightened_image = cv2.filter2D(image, -1, kernel)

    return brightened_image


image = cv2.imread("C:\\Users\\romAn\\Documents\\GitHub\\ComputerVision\\labs\\img\\balmoral.jpg")

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

brightened_image = increase_brightness(image, value=2)

titles = ['Исходное изображение', 'Увеличенная яркость']
images = [image, brightened_image]

for i in range(2):
    plt.subplot(1, 2, i + 1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
