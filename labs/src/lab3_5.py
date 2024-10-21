import cv2
import numpy as np
import random
from matplotlib import pyplot as plt


def find_sides_rectangle(perimeter):
    if perimeter % 2 != 0:
        print("Ошибка: неверное значение периметра.")
        return
    a_plus_b = perimeter // 2
    a = random.randint(1, a_plus_b)
    b = a_plus_b - a

    print('a = ', a)
    print('b = ', b)

    return a, b


def generate_random_shape(perimeter):
    if perimeter % 2 == 0:
        image = np.zeros((500, 800), dtype=np.uint8)
        x = 200
        y = 200
        a, b = find_sides_rectangle(perimeter)
        cv2.rectangle(image, (x, y), (x + a, y + b), (255, 255, 255), -1)
        return image
    else:
        print("Ошибка: неверное значение периметра.")
        return None


perimeter = int(input("Введите желаемый периметр: "))

image = generate_random_shape(perimeter)

plt.imshow(image, 'gray')
plt.show()
