import cv2
import numpy as np
from matplotlib import pyplot as plt


def calculate_perimeter(img):
    p = 0
    for i in range(1, img.shape[0] - 1, 1):
        for j in range(1, img.shape[1] - 1, 1):
            if img[i][j] == 0:
                number_white_pixels = 0
                for r in range(-1, 2, 1):
                    if r != 0:
                        if img[i][j + r] == 255:
                            number_white_pixels += 1
                for c in range(-1, 2, 1):
                    if c != 0:
                        if img[i + c][j] == 255:
                            number_white_pixels += 1
                p += number_white_pixels
    return p


def calculate_square(img):
    s = 0
    for i in range(1, img.shape[0] - 1, 1):
        for j in range(1, img.shape[1] - 1, 1):
            if img[i][j] == 0:
                s += 1
    return s


def count_number_corners(img):
    num_corners = 0
    i_ = []
    j_ = []
    for i in range(1, img.shape[0] - 1, 1):
        for j in range(1, img.shape[1] - 1, 1):
            if img[i][j] == 0:
                number_neighbors = 0

                for c in range(-1, 2, 1):
                    for r in range(-1, 2, 1):
                        if c != 0 or r != 0:
                            if img[i + c][j + r] == 0:
                                number_neighbors += 1

                if number_neighbors == 3:
                    flag = False
                    for k in range(len(i_)):
                        if (abs(i_[k] - i) <= 5) and (abs(j_[k] - j) <= 5):
                            flag = True
                            break
                    if not flag:
                        i_.append(i)
                        j_.append(j)
                        num_corners += 1

                if number_neighbors == 4:
                    number_neighbors = 0
                    for c in range(-2, 3, 1):
                        for r in range(-4, 5, 1):
                            if img[i + c][j + r] == 0:
                                number_neighbors += 1

                    if number_neighbors <= 22:
                        flag = False
                        for k in range(len(i_)):
                            if (abs(i_[k] - i) <= 5) and (abs(j_[k] - j) <= 5):
                                flag = True
                                break
                        if not flag:
                            i_.append(i)
                            j_.append(j)
                            num_corners += 1


    plt.subplot(1, 1, 1)
    plt.imshow(img, 'gray')
    plt.plot(j_, i_, 'ro')
    plt.xticks([]), plt.yticks([])
    plt.show()
    return num_corners


def calculate_roundness(img):
    p = calculate_perimeter(img)
    s = calculate_square(img)
    o = p ** 2 / (4 * 3.14 * s)
    return o


def recognize_figures(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    ret, thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)

    kernel = np.ones((5, 5), np.uint8)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel, iterations=1)

    closing = cv2.erode(closing, kernel)

    closing = cv2.dilate(closing, kernel)

    num_corners = count_number_corners(closing)

    if num_corners == 3:
        return 'Треугольник'
    elif num_corners == 4:
        return 'Прямоугольник'
    elif num_corners == 8:
        return 'Восьмиугольник'
    else:
        roundness = calculate_roundness(closing)
        print('Округлость = ', roundness)
        if 1 <= roundness < 1.66:
            return 'Круг'
        else:
            return 'Эллипс'


image_path = "C:\\Users\\romAn\\Documents\\GitHub\\ComputerVision\\labs\\img\\figures\\triangle.png"
print(recognize_figures(image_path))
