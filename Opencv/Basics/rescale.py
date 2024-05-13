import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * sclae)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# changeRes: Live video만 가능
def changeRes(width, height):
    capture.set(3, width) 
    capture.set(4, height) 

# Reading videos
capture = cv.VideoCapture('/home/work/daehyun/Computer_Vision_Study/Opencv/opencv-course/Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read() # 비디오를 프레임별로 읽어옴
    
    frame_resize = rescaleFrame(frame)
    
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resize)
    
    if cv.watiKey(20) & 0xFF==ord('d'):
        break # d를 누르면 종료

capture.release() # 비디오 캡쳐를 종료
cv.destoryAllWindows() # 모든 창을 닫음