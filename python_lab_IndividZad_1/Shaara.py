import cv2
import numpy as np

def custom_canny(img, sigma=0.33):
    # Преобразование в градации серого
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2)

# Чтение изображения
img = cv2.imread("image.jpg")
# Применение функции custom_canny
canny = custom_canny(img)
# Отображение результата
cv2.imshow("Canny", canny)
cv2.waitKey(0)
cv2.destroyAllWindows()