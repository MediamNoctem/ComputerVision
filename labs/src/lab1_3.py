import cv2
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog, messagebox


def gui_image_binarization():
    r = Tk()
    r.title("Бинаризация изображения")
    r.geometry("400x300")

    image_path = filedialog.askopenfilename(
        initialdir="/",
        title="Выберите изображение",
        filetypes=(("Image files", "*.jpg *.jpeg *.png *.bmp"), ("all files", "*.*"))
    )

    if not image_path:
        messagebox.showerror("Ошибка", "Не выбрано изображение")
        r.destroy()
        return

    label1 = Label(r, text='')
    label1.config(text=f"Выбрано изображение: {image_path}")
    label1.pack()

    label2 = Label(r, text='Выберите метод бинаризации.')
    label2.pack()

    types_of_binarization = ["Глобальная бинаризация", "Адаптивная бинаризация"]
    combobox = Combobox(values=types_of_binarization, width=25)
    combobox.pack()

    def update_parameters():
        selection = combobox.get()

        if selection == types_of_binarization[0]:
            global_params_frame = LabelFrame(r, text="Параметры глобальной бинаризации")
            global_params_frame.pack()

            label4 = Label(global_params_frame, text="Пороговое значение")
            label4.pack()

            entry1 = Entry(global_params_frame, width=10)
            entry1.pack()

            label5 = Label(global_params_frame, text="Максимальное значение пикселей")
            label5.pack()

            entry2 = Entry(global_params_frame, width=10)
            entry2.pack()

            label6 = Label(global_params_frame, text="Тип порогового значения")
            label6.pack()

            thresh = ["THRESH_BINARY",
                      "THRESH_BINARY_INV",
                      "THRESH_TRUNC",
                      "THRESH_TOZERO",
                      "THRESH_TOZERO_INV"]

            combobox2 = Combobox(global_params_frame, values=thresh, width=25)
            combobox2.pack()

            def gl_binarized():
                try:
                    threshold = int(entry1.get())
                    max_value = int(entry2.get())
                    thresh_type = {
                        "THRESH_BINARY": cv2.THRESH_BINARY,
                        "THRESH_BINARY_INV": cv2.THRESH_BINARY_INV,
                        "THRESH_TRUNC": cv2.THRESH_TRUNC,
                        "THRESH_TOZERO": cv2.THRESH_TOZERO,
                        "THRESH_TOZERO_INV": cv2.THRESH_TOZERO_INV
                    }[combobox2.get()]

                    img = cv2.imread(image_path)
                    ret, binarized_img = cv2.threshold(img, threshold, max_value, thresh_type)

                    cv2.imshow("Draw", binarized_img)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                except ValueError:
                    messagebox.showerror("Ошибка", "Некорректные значения параметров")

            button_gl_binarized = Button(r, text='Выполнить', width=15, command=gl_binarized)
            button_gl_binarized.pack()

        elif selection == types_of_binarization[1]:
            for widget in r.winfo_children():
                widget.destroy()

            global_params_frame = LabelFrame(r, text="Параметры глобальной бинаризации")
            global_params_frame.pack()

            label7 = Label(global_params_frame, text="Максимальное значение пикселей")
            label7.pack()

            entry3 = Entry(global_params_frame, width=10)
            entry3.pack()

            label8 = Label(global_params_frame, text="Выберите тип порогового значения")
            label8.pack()

            thresh = ["ADAPTIVE_THRESH_MEAN_C", "ADAPTIVE_THRESH_GAUSSIAN_C"]
            combobox3 = Combobox(values=thresh, width=25)
            combobox3.pack()

            label9 = Label(global_params_frame, text="Размер блока")
            label9.pack()

            entry4 = Entry(global_params_frame, width=10)
            entry4.pack()

            label10 = Label(global_params_frame, text="Константа C")
            label10.pack()

            entry5 = Entry(global_params_frame, width=10)
            entry5.pack()

            def adap_binarized():
                try:
                    max_value = int(entry3.get())

                    thresh_type = {
                        "ADAPTIVE_THRESH_MEAN_C": cv2.ADAPTIVE_THRESH_MEAN_C,
                        "ADAPTIVE_THRESH_GAUSSIAN_C": cv2.ADAPTIVE_THRESH_GAUSSIAN_C
                    }[combobox3.get()]

                    block_size = int(entry4.get())
                    c = int(entry5.get())

                    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
                    binarized_img = cv2.adaptiveThreshold(img, max_value, thresh_type, cv2.THRESH_BINARY, block_size, c)

                    cv2.imshow("Draw", binarized_img)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                except ValueError:
                    messagebox.showerror("Ошибка", "Некорректные значения параметров")

            button_adap_binarized = Button(r, text='Выполнить', width=15, command=adap_binarized)
            button_adap_binarized.pack()

    combobox.bind("<<ComboboxSelected>>", lambda event: update_parameters())

    r.mainloop()


gui_image_binarization()
