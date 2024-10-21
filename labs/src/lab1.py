import cv2
from matplotlib import pyplot as plt


# 1
def f():
    img = cv2.imread("C:\\Users\\romAn\\Documents\\GitHub\\ComputerVision\\labs\\img\\rabbit.jpg", 0)

    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, th1 = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
    print(ret)
    th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 10)

    titles = ['Оригинал', 'Бинаризация Оцу', 'Адаптивная бинаризация']
    images = [img, th1, th2]

    for i in range(3):
        plt.subplot(2, 2, i + 1)
        plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()


# 2
def image_binarization(path, thresh):
    img = cv2.imread(path, 0)
    height, width = img.shape[:2]
    for i in range(height):
        for j in range(width):
            if img[i][j] < thresh:
                img[i][j] = 0
            else:
                img[i][j] = 255
    path_new = path[:path.rfind("\\") + 1]
    cv2.imwrite(path_new + "output_lab1.jpg", img)


f()
image_binarization("C:\\Users\\romAn\\Documents\\GitHub\\ComputerVision\\labs\\img\\rabbit.jpg", 77)
