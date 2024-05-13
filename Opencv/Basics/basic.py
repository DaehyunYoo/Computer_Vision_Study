import cv2 as cv

img = cv.imread('Resources/Photos/cat.jpg')
cv.imshow('Cat', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
# 이미지에 존재하는 edge를 찾아줌
cany = cv.Canny(img, 125, 175) # 125~175 사이의 값은 edge로 판단
cv.imshow('Canny Edges', cany)

# Dilating the image
# 이미지의 edge를 두껍게 만들어줌
dilated = cv.dilate(cany, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

# Eroding
# 이미지의 edge를 얇게 만들어줌
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC) # interpolation는 원래 크기보다 작게 할 때 유용함
cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]

cv.watiKey(0)