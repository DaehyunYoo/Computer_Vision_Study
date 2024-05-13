import cv2 as cv

img = cv.imread('/home/work/daehyun/Computer_Vision_Study/Opencv/opencv-course/Resources/Photos/cat.jpg')

cv.imshow('Cat', img)

cv.watiKey(0) # keyboard binding function

# 이미지 크기가 큰 경우에는 이미지가 뜨지 않을 수 있음
# 프레임 크기 조정 및 크기 조정을 통해 이미지를 확인할 수 있음

# Video
capture = cv.VideoCapture('/home/work/daehyun/Computer_Vision_Study/Opencv/opencv-course/Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read() # 비디오를 프레임별로 읽어옴
    cv.imshow('Video', frame)
    
    if cv.watiKey(20) & 0xFF==ord('d'):
        break # d를 누르면 종료

capture.release() # 비디오 캡쳐를 종료
cv.destoryAllWindows() # 모든 창을 닫음