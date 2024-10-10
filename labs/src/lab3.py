import cv2
from matplotlib import pyplot as plt
import numpy as np


def find_coins_1_2_5(img_path):
    Dp = 116
    Dd = 132
    Dq = 142

    img = cv2.imread(img_path, 0)

    ret, th1 = cv2.threshold(img, 250, 255, cv2.THRESH_BINARY_INV)
    kernel = np.ones((3, 3), np.uint8)
    th2 = cv2.morphologyEx(th1, cv2.MORPH_OPEN, kernel)
    B = cv2.morphologyEx(th2, cv2.MORPH_CLOSE, kernel)

    mask1 = np.zeros((Dp, Dp), dtype=np.uint8)
    cv2.circle(mask1, (int(Dp / 2), int(Dp / 2)), int(Dp / 2), 255, -1)

    mask2 = np.zeros((Dd, Dd), dtype=np.uint8)
    cv2.circle(mask2, (int(Dd / 2), int(Dd / 2)), int(Dd / 2), 255, -1)

    mask5 = np.zeros((Dq, Dq), dtype=np.uint8)
    cv2.circle(mask5, (int(Dq / 2), int(Dq / 2)), int(Dq / 2), 255, -1)

    Q = cv2.erode(B, mask2, iterations=1)
    Q = cv2.dilate(Q, mask2, iterations=1)

    B1 = cv2.bitwise_xor(B, Q)
    B1 = cv2.morphologyEx(B1, cv2.MORPH_OPEN, kernel)

    D = cv2.erode(B1, mask1, iterations=1)
    D = cv2.dilate(D, mask1, iterations=1)

    B2 = cv2.bitwise_xor(B1, D)
    P = cv2.morphologyEx(B2, cv2.MORPH_OPEN, kernel)

    titles = ['Оригинал', 'Инвертированная бинаризация', 'Обработанное (открытие)', ' Обработанное (закрытие)', '1 рубль', '2 рубля', '5 рублей']
    images = [img, th1, th2, B, P, D, Q]

    for i in range(7):
        plt.subplot(2, 4, i + 1)
        plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()


def recognize_shapes(img_path):
    pass


# img_path = 'C:\\Users\\romAn\\Documents\\GitHub\\ComputerVision\\labs\\img\\coins.jpg'
# find_coins_1_2_5(img_path)
