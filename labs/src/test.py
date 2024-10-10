import cv2
import numpy as np
from matplotlib import pyplot as plt


def recognize_triangle(image_path):
    """
    Распознает треугольник на изображении с помощью морфологических операций
    без нахождения контуров и аппроксимации.

    Args:
        image_path: Путь к изображению.

    Returns:
        True, если треугольник найден, иначе False.
    """

    # Загрузка изображения
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Бинаризация изображения
    ret, thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)

    # Создание структурного элемента для эрозии и дилатации
    kernel = np.ones((5, 5), np.uint8)

    # Морфологическое открытие для удаления шума
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

    # Морфологическое закрытие для заполнения пробелов
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel, iterations=2)

    print(closing.shape[0])

    # Поиск пикселей с тремя соседними пикселями (углы треугольника)
    triangle_pixels = 0
    for i in range(closing.shape[0] - 2):
        for j in range(closing.shape[1] - 2):
            if 
                triangle_pixels += 1
    print(triangle_pixels)

    # Проверка на наличие треугольников
    # return len(triangle_pixels[0]) > 0
    return


# Пример использования
image_path = "C:\\Users\\romAn\\Documents\\GitHub\\ComputerVision\\labs\\img\\figures.png"

if recognize_triangle(image_path):
    print("Треугольник найден!")
else:
    print("Треугольник не найден.")
