# contours란
# 이미지에서 객체의 외곽선을 찾는 방법

import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/cats.jpg')

cv.imshow('Cats', img)

blank = np.zeros(img.shape, dtype='uint8') # 빈 이미지 생성

# gray 이미지 생성
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

# ret, thresh: 임계값과 임계값을 적용한 이미지를 반환
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (0, 0, 255), 1) # drawContours: 이미지에 외곽선을 그림
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)