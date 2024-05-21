import cv2 as cv

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Simple Thresholding -> 픽셀 값이 threshold보다 크면 255로, 작으면 0으로 설정
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Thresholded Image', thresh)

# Simple Thresholding Inverse -> 픽셀 값이 threshold보다 크면 0으로, 작으면 255로 설정
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresholded Inverse Image', thresh_inv)

# Adaptive Thresholding -> 이미지의 작은 영역마다 threshold를 설정
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 9) # 11: block size, 9: constant
cv.imshow('Adaptive Thresholding', adaptive_thresh)


cv.waitKey(0)
