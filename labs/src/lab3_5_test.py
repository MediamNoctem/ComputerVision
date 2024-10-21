import cv2
import numpy as np
import random


def calculate_perimeter(img):
    p = 0
    for i in range(1, img.shape[0] - 1, 1):
        for j in range(1, img.shape[1] - 1, 1):
            if img[i][j] == 255:
                number_white_pixels = 0
                for r in range(-1, 2, 1):
                    if r != 0:
                        if img[i][j + r] == 0:
                            number_white_pixels += 1
                for c in range(-1, 2, 1):
                    if c != 0:
                        if img[i + c][j] == 0:
                            number_white_pixels += 1
                p += number_white_pixels
    return p


def find_sides_rectangle(perimeter):
    if perimeter % 2 != 0:
        print("Ошибка: неверное значение периметра.")
        return None
    a_plus_b = perimeter // 2
    a = random.randint(1, a_plus_b)
    b = a_plus_b - a

    print('a = ', a)
    print('b = ', b)

    return a, b


def generate_random_shape(perimeter):
    if perimeter > 0:
        image = np.zeros((500, 800), dtype=np.uint8)
        x = 200
        y = 200

        if perimeter % 2 == 0:
            a, b = find_sides_rectangle(perimeter)
            cv2.rectangle(image, (x, y), (x + a, y + b), (255, 255, 255), -1)
        else:
            p = 0
            for i in range(perimeter, 2, -1):
                if (i % 2 == 0) and (perimeter - i >= 2):
                    p = i
                    break
            if p == 0:
                print("Ошибка: не удалось построить фигуру.")
                return None

            print('p = ', p)

            a, b = find_sides_rectangle(p)
            cv2.rectangle(image, (x, y), (x + a, y + b), (255, 255, 255), -1)

            while perimeter - p >= 2:
                num_white = 0
                num_black = 0
                c = random.randint(0, 798)
                r = random.randint(0, 498)

                if image[r][c - 1] == 255:
                    num_white += 1
                else:
                    num_black += 1

                if image[r - 1][c] == 255:
                    num_white += 1
                else:
                    num_black += 1

                if image[r + 1][c] == 255:
                    num_white += 1
                else:
                    num_black += 1

                if image[r][c + 1] == 255:
                    num_white += 1
                else:
                    num_black += 1

                if (num_white != 0) and (num_black != 0):
                    image[r][c] = 255
                    p = calculate_perimeter(image)
                    print('p = ', p)

            while perimeter - p == 1:
                num_white = 0
                num_black = 0
                c = random.randint(0, 798)
                r = random.randint(0, 498)

                if image[r][c - 1] == 255:
                    num_white += 1
                else:
                    num_black += 1

                if image[r - 1][c] == 255:
                    num_white += 1
                else:
                    num_black += 1

                if image[r + 1][c] == 255:
                    num_white += 1
                else:
                    num_black += 1

                if image[r][c + 1] == 255:
                    num_white += 1
                else:
                    num_black += 1

                if num_white == 2:
                    image[r][c] = 255
                    p = calculate_perimeter(image)
                    print('p = ', p)

        return image
    else:
        print("Ошибка: неверное значение периметра.")


perimeter = int(input("Введите желаемый периметр: "))

image = generate_random_shape(perimeter)

cv2.imshow("Случайная фигура без отверстий", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# img = cv2.imread('C:\\Users\\romAn\\Documents\\GitHub\\ComputerVision\\labs\\img\\e.png', 0)
# print(img.shape)
# print(calculate_perimeter(img))
