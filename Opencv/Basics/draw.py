import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8') # 500 x 500의 검은색 이미지 생성
cv.imshow('Blank', blank)

# 1. Paint the image a certain color
blank[:] = 0, 255, 0
cv.imshow('Grenn', blank)

blank[:] = 0, 0, 255
cv.imshow('Red', blank)

blank[:] = 255, 0, 0
cv.imshow('Blue', blank)

# 2. Draw a rectangle
# cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=2)
cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=cv.FILLED)
cv.imshow('Rectangle', blank)

# 3. Draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 0, 255), thickness=3)
cv.imshow('Circle', blank)

# 4. Draw a line
cv.line(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 255), thickness=3)
cv.imshow('Line', blank)

# 5. Write text
cv.putText(blank, 'Hello', (255, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2)
cv.imshow('Text', blank)

cv.watiKey(0)
