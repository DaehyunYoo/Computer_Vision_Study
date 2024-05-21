import cv2 as cv

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

# 각 blurring 방법에 대한 설명
# 1. Averaging: 이미지의 픽셀을 주변 픽셀의 평균값으로 대체
# 2. Gaussian: 이미지의 픽셀을 주변 픽셀의 가중치 평균값으로 대체
# 3. Median: 이미지의 픽셀을 주변 픽셀의 중간값으로 대체


# Averaging
average = cv.blur(img, (7,7))
cv.imshow('Average Blur', average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur
median = cv.medianBlur(img, 7)
cv.imshow('Median Blur', median)

# Bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)
