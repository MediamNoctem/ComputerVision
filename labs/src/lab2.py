import cv2
import matplotlib.pyplot as plt


def calculate_brightness_histogram(image_path):

    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    histogram = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
    histogram = histogram.flatten()

    return histogram


image_path = "C:\\Users\\romAn\\Documents\\GitHub\\ComputerVision\\labs\\img\\balmoral.jpg"
histogram = calculate_brightness_histogram(image_path)

# print("Гистограмма яркости:")
# for i, count in enumerate(histogram):
#     print(f"Яркость {i}: {count}")

x = [i for i in range(256)]

plt.hist(x=x, weights=histogram, bins=255, color="green")
plt.xlabel("Яркость")
plt.ylabel("Количество пикселей")
plt.show()
