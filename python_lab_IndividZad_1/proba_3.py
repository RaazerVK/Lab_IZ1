import cv2
import numpy as np

def canny_edge_detection(image):
# Конвертация изображения в оттенки серого
 gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Реализация алгоритма Канни
 edges = cv2.Canny(gray, 50, 150)

 return edges

def sobel_edge_detection(image):
# Конвертация изображения в оттенки серого
 gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Реализация метода Собеля
 sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
 sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
 edges_sobel = np.sqrt(np.power(sobelx, 2) + np.power(sobely, 2))
 edges_sobel = edges_sobel / np.max(edges_sobel)
 edges_sobel = np.uint8(edges_sobel * 255)

 return edges_sobel

def laplacian_edge_detection(image):
# Конвертация изображения в оттенки серого
 gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Реализация метода Лапласа
 laplacian = cv2.Laplacian(gray, cv2.CV_64F)
 edges_laplacian = np.uint8(np.abs(laplacian) / np.max(np.abs(laplacian)) * 255)

 return edges_laplacian

#Чтение изображения

img = cv2.imread("claymor_1.jpg")

blu1 = cv2.GaussianBlur(img, (5, 5), 0)
blu2 = cv2.GaussianBlur(img, (5, 5), 5)
blu3 = cv2.GaussianBlur(img, (5, 5), 10)
#Вызов функций

edges_canny = canny_edge_detection(blu1)
edges_sobel = sobel_edge_detection(blu1)
edges_laplacian = laplacian_edge_detection(blu1)

edges_canny = canny_edge_detection(blu2)
edges_sobel = sobel_edge_detection(blu2)
edges_laplacian = laplacian_edge_detection(blu2)

edges_canny = canny_edge_detection(blu3)
edges_sobel = sobel_edge_detection(blu3)
edges_laplacian = laplacian_edge_detection(blu3)

#Отображение результатов

cv2.imshow("Canny", edges_canny)
cv2.imshow("Sobel", edges_sobel)
cv2.imshow("Laplacian", edges_laplacian)

cv2.imshow("Canny", edges_canny)
cv2.imshow("Sobel", edges_sobel)
cv2.imshow("Laplacian", edges_laplacian)

cv2.imshow("Canny", edges_canny)
cv2.imshow("Sobel", edges_sobel)
cv2.imshow("Laplacian", edges_laplacian)


cv2.waitKey(0)
cv2.destroyAllWindows()