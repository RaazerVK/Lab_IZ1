import cv2
import numpy as np


def canny(image, threshold1, threshold2):
    # Преобразование в оттенки серого
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Фильтрация с помощью Гауссова ядра
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # Вычисление градиентов в каждом направлении
    gradient_x = cv2.Sobel(blurred_image, cv2.CV_64F, 1, 0, ksize=5)
    gradient_y = cv2.Sobel(blurred_image, cv2.CV_64F, 0, 1, ksize=5)

    # Вычисление модуля и направления градиента
    gradient_magnitude = np.sqrt(np.power(gradient_x, 2) + np.power(gradient_y, 2))
    gradient_angle = np.arctan2(gradient_y, gradient_x) * 180 / np.pi

    # Нормализация градиентов
    gradient_magnitude = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX)
    gradient_magnitude = gradient_magnitude.astype(np.uint8)

    # Применение пороговой операции
    edges = np.zeros_like(gradient_magnitude)
    edges[(gradient_magnitude >= threshold1) & (gradient_magnitude <= threshold2)] = 255

    # Удаление небольших кусочков и замыкание дырок
    edges = cv2.dilate(edges, np.ones((5, 5), np.uint8))
    edges = cv2.erode(edges, np.ones((5, 5), np.uint8))

    return edges
def canny_sig_3(image, threshold1, threshold2):
    # Преобразование в оттенки серого
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Фильтрация с помощью Гауссова ядра
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 11)

    # Вычисление градиентов в каждом направлении
    gradient_x = cv2.Sobel(blurred_image, cv2.CV_64F, 1, 0, ksize=5)
    gradient_y = cv2.Sobel(blurred_image, cv2.CV_64F, 0, 1, ksize=5)

    # Вычисление модуля и направления градиента
    gradient_magnitude = np.sqrt(np.power(gradient_x, 2) + np.power(gradient_y, 2))
    gradient_angle = np.arctan2(gradient_y, gradient_x) * 180 / np.pi

    # Нормализация градиентов
    gradient_magnitude = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX)
    gradient_magnitude = gradient_magnitude.astype(np.uint8)

    # Применение пороговой операции
    edges = np.zeros_like(gradient_magnitude)
    edges[(gradient_magnitude >= threshold1) & (gradient_magnitude <= threshold2)] = 255

    # Удаление небольших кусочков и замыкание дырок
    edges = cv2.dilate(edges, np.ones((5, 5), np.uint8))
    edges = cv2.erode(edges, np.ones((5, 5), np.uint8))

    return edges
def canny_raz(image, threshold1, threshold2):
    # Преобразование в оттенки серого
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Фильтрация с помощью Гауссова ядра
    blurred_image = cv2.GaussianBlur(gray_image, (9, 9), 0)

    # Вычисление градиентов в каждом направлении
    gradient_x = cv2.Sobel(blurred_image, cv2.CV_64F, 1, 0, ksize=5)
    gradient_y = cv2.Sobel(blurred_image, cv2.CV_64F, 0, 1, ksize=5)

    # Вычисление модуля и направления градиента
    gradient_magnitude = np.sqrt(np.power(gradient_x, 2) + np.power(gradient_y, 2))
    gradient_angle = np.arctan2(gradient_y, gradient_x) * 180 / np.pi

    # Нормализация градиентов
    gradient_magnitude = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX)
    gradient_magnitude = gradient_magnitude.astype(np.uint8)

    # Применение пороговой операции
    edges = np.zeros_like(gradient_magnitude)
    edges[(gradient_magnitude >= threshold1) & (gradient_magnitude <= threshold2)] = 255

    # Удаление небольших кусочков и замыкание дырок
    edges = cv2.dilate(edges, np.ones((5, 5), np.uint8))
    edges = cv2.erode(edges, np.ones((5, 5), np.uint8))

    return edges



# Загрузка изображения
image1 = cv2.imread('claymor_1.jpg')
# image2 = cv2.imread('claymor_2.jpg')
# image3 = cv2.imread('claymor_3.jpg')
# image4 = cv2.imread('claymor_4.jpg')

image1s = cv2.imread('claymor_1.jpg')
# image2s = cv2.imread('claymor_2.jpg')
# image3s = cv2.imread('claymor_3.jpg')
# image4s = cv2.imread('claymor_4.jpg')

image1r = cv2.imread('claymor_1.jpg')
# image2r = cv2.imread('claymor_2.jpg')
# image3r = cv2.imread('claymor_3.jpg')
# image4r = cv2.imread('claymor_4.jpg')

# Вызов функции
edges1 = canny(image1, 50, 100)
# edges2 = canny(image2, 100, 200)
# edges3 = canny(image3, 100, 200)
# edges4 = canny(image4, 100, 200)

edges2 = canny(image1, 100, 200)
# edges2s = canny(image2, 100, 200)
# edges3s = canny(image3, 100, 200)
# edges4s = canny(image4, 100, 200)

edges3 = canny(image1, 150, 300)
# edges2r = canny(image2, 100, 200)
# edges3r = canny(image3, 100, 200)
# edges4r = canny(image4, 100, 200)

edges1s = canny_sig_3(image1s, 50, 100)
edges2s = canny_sig_3(image1s, 100, 200)
edges3s = canny_sig_3(image1s, 200, 300)

edges1r = canny_raz(image1r, 50, 100)
edges2r = canny_raz(image1r, 100, 200)
edges3r = canny_raz(image1r, 200, 300)




cv2.imshow("Canny_original_50_100", edges1)
# cv2.imshow("Canny_2_original", edges2)
# cv2.imshow("Canny_3_original", edges3)
# cv2.imshow("Canny_4_original", edges4)

cv2.imshow("Canny_original_100_200", edges2)
# cv2.imshow("Canny_2_sigma", edges2s)
# cv2.imshow("Canny_3_sigma", edges3s)
# cv2.imshow("Canny_4_sigma", edges4s)

cv2.imshow("Canny_original_200_300", edges3)
# cv2.imshow("Canny_2_razmer", edges2r)
# cv2.imshow("Canny_3_razmer", edges3r)
# cv2.imshow("Canny_4_razmer", edges4r)

cv2.imshow("Canny_sigma3_50_100", edges1s)
cv2.imshow("Canny_sigma3_100_200", edges2s)
cv2.imshow("Canny_sigma3_200_300", edges3s)

cv2.imshow("Canny_razmer9_50_100", edges1r)
cv2.imshow("Canny_razmer9_100_200", edges2r)
cv2.imshow("Canny_razmer9_200_300", edges3r)

cv2.waitKey(0)
cv2.destroyAllWindows()