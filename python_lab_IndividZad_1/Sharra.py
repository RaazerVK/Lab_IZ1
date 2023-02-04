import cv2
import numpy as np

def canny(image, threshold1, threshold2):
# Преобразование в оттенки серого
 gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Фильтрация с помощью Гаусса
 blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Вычисление градиентов в каждом направлении
 gradient_x = cv2.Scharr(blurred_image, cv2.CV_64F, 1, 0)
 gradient_y = cv2.Scharr(blurred_image, cv2.CV_64F, 0, 1)

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

#Загрузка изображения
image = cv2.imread('claymor_1.jpg')

#Вызов функции canny
edges = canny(image, 100, 200)
cv2.imshow("Canny", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()