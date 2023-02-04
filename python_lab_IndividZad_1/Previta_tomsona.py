import cv2
import numpy as np

def canny(img, sigma=11.33):
    # Преобразование в градации серого
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred_image = cv2.GaussianBlur(gray, (5, 5), 0)
    # Вычисление градиента используя оператор Превита-Томаса
    gradient_x = cv2.Sobel(blurred_image, cv2.CV_64F, 1, 0, ksize=3, scale=sigma)
    gradient_y = cv2.Sobel(blurred_image, cv2.CV_64F, 0, 1, ksize=3, scale=sigma)
    gradient = np.hypot(gradient_x, gradient_y)
    gradient = gradient / gradient.max() * 255
    return gradient

# Чтение изображения
img = cv2.imread("claymor_1.jpg")
# Применение функции custom_canny
canny = canny(img)
# Отображение результата
cv2.imshow("Canny", canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
