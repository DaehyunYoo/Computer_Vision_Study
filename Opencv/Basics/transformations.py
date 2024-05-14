import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/park.jpg')

cv.imshow('Park', img)

# Translation
def translate(img, x, y): # x, y: number of pixels to move in x and y direction
    transMat = np.float32([[1, 0, x], [0, 1, y]]) # 이미지를 이동시키기 위한 행렬
    dimensions = (img.shape[1], img.shape[0]) # 이미지의 너비와 높이
    
    return cv.warpAffine(img, transMat, dimensions) # 이미지 이동

# -x -> Left
# -y -> Up
# x -> Right
# y -> Down

translated = translate(img, 100, 100)
cv.imshow('Translated', translated)

# Rotation
def rotate(img, angle, rotPoint=None): # rotPoint: 회전 중심
    (height, width) = img.shape[:2] # 이미지의 너비와 높이
    if rotPoint is None:
        rotPoint = (width//2, height//2) # 이미지의 중심을 회전 중심으로 설정

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0) # 이미지를 회전시키기 위한 행렬
    dimensions = (width, height)
    
    return cv.warpAffine(img, rotMat, dimensions) # 이미지 회전

rotated = rotate(img, 45)

# Resizing
resize = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC) # 이미지 크기 조정
cv.imshow('Resized', resize)

# Flipping
flip = cv.flip(img, 0) # 0: x축 기준으로 상하 반전, 1: y축 기준으로 좌우 반전, -1: x, y축 기준으로 상하, 좌우 반전
cv.imshow('Flipped', flip)

# Cropping
cropped = img[200:400, 300:400] # 이미지의 일부분을 잘라냄
cv.imshow('Cropped', cropped)

cv.waitKey(0)