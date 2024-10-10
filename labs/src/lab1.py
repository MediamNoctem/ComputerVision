import cv2
from matplotlib import pyplot as plt
from tkinter import *
from tkinter.ttk import *


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


# def gui_image_binarization():
#     r = Tk()
#     r.title("Бинаризация изображения")
#     r.geometry("400x500")
#     label1 = Label(r, text='1. Выберите изображение.')
#     button = Button(r, text='Выбрать', width=10, command=r.destroy)
#     label2 = Label(r, text='2. Выберите метод бинаризации.')
#     var = StringVar()
#     type = ["Глобальная бинаризация", "Адаптивная бинаризация"]
#     combobox = Combobox(values=type, width=25)
#
#     label1.pack()
#     button.pack()
#     label2.pack()
#     combobox.pack()
#
#     if combobox.get() == type[0]:
#         label3 = Label(r, text="3. Введите параметры метода бинаризации.")
#
#         label4 = Label(r, text="Пороговое значение = ")
#         entry1 = Entry(r, width=10)
#
#         label5 = Label(r, text="Максимальное значение пикселей = ")
#         entry2 = Entry(r, width=10)
#
#         label6 = Label(r, text="Выберите тип порогового значения")
#         thresh = ["cv.THRESH_BINARY", "cv.THRESH_BINARY_INV", "cv.THRESH_TRUNC", "cv.THRESH_TOZERO", "cv.THRESH_TOZERO_INV"]
#         combobox2 = Combobox(values=thresh, width=25)
#
#         label3.pack()
#         label4.pack()
#         entry1.pack()
#         label5.pack()
#         entry2.pack()
#         label6.pack()
#         combobox2.pack()
#     if combobox.get() == type[1]:
#         label7 = Label(r, text="Максимальное значение пикселей = ")
#         entry3 = Entry(r, width=10)
#
#         label8 = Label(r, text="Выберите тип порогового значения")
#         thresh = ["cv.ADAPTIVE_THRESH_MEAN_C", "cv.ADAPTIVE_THRESH_GAUSSIAN_C"]
#         combobox3 = Combobox(values=thresh, width=25)
#
#         label9 = Label(r, text="Размер блока = ")
#         entry4 = Entry(r, width=10)
#
#         label10 = Label(r, text="Константа С = ")
#         entry5 = Entry(r, width=10)
#
#         label7.pack()
#         entry3.pack()
#         label8.pack()
#         combobox3.pack()
#         label9.pack()
#         entry4.pack()
#         label10.pack()
#         entry5.pack()
#
#     button_enter = Button(r, text='Выполнить', width=15)
#     button_enter.pack()
#
#     r.mainloop()

# f()
image_binarization("C:\\Users\\romAn\\Documents\\GitHub\\ComputerVision\\labs\\img\\rabbit.jpg", 77)
