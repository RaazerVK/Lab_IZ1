import cv2
import numpy as np

# Чтение изображения
img = cv2.imread("claymor_4.jpg")

# Конвертация изображения в оттенки серого
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Реализация алгоритма Канни
edges = cv2.Canny(gray, 125, 200)

# Реализация метода Собеля
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
edges_sobel = np.sqrt(np.power(sobelx, 2) + np.power(sobely, 2))
edges_sobel = edges_sobel / np.max(edges_sobel)
edges_sobel = np.uint8(edges_sobel * 255)

# Реализация метода Лапласа
laplacian = cv2.Laplacian(gray, cv2.CV_64F)
edges_laplacian = np.uint8(np.abs(laplacian) / np.max(np.abs(laplacian)) * 255)

# Отображение результатов
cv2.imshow("Canny", edges)
cv2.imshow("Sobel", edges_sobel)
cv2.imshow("Laplacian", edges_laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()
