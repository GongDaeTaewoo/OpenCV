import numpy as np
import cv2

src=cv2.imread('warp.jpg')
w,h=720,540
#색깔
purple=(255,0,255)
green=(0,255,0)
#점(원)의 갯수를 저장함
NumOfCir=0
#mode1 노말 mode2그래이스케일 mode3이진화mode4샤프닝

#클릭하는 원4개의 위치를 저장하는 array
save_point=np.zeros((4,2),dtype=np.float32)
mode=0
#콜백함수
def click(event,x,y,flags,img):
    global NumOfCir,mode

    # 클릭후 뗄시
    if (event==cv2.EVENT_LBUTTONUP and mode!=0):
        #원을그림
        cv2.circle(src,(x,y),4,(0,0,255),-1)
        cv2.imshow('image',src)
        #점(원) 좌표를 저장
        save_point[NumOfCir,:]=(x,y)
        #점과점사이 선그리기
        if(NumOfCir>=1):
            p1=tuple(save_point[NumOfCir-1,:])
            p2=tuple(save_point[NumOfCir,:])
            cv2.line(src, p1, p2, green, 2)
            #점4개되면 3개그리기
            if(NumOfCir==3):
                cv2.line(src, tuple(save_point[0, :]), tuple(save_point[3, :]), green, 2)
            cv2.imshow('image',src)
        NumOfCir+=1
        #점(원)이 4개일 경우
        if NumOfCir==4:
            #오리지날모드
            if(mode==1):
                #원근 투시변환
                dst_point = np.array([[0, 0], [w - 1, 0], [w - 1, h - 1], [0, h - 1]], dtype=np.float32)
                perspect = cv2.getPerspectiveTransform(save_point,dst_point)
                dst=cv2.warpPerspective(src, perspect, (w,h))
                cv2.imshow('image',dst)
                cv2.imwrite("original mode.jpg", dst)

            #그레이모드
            if(mode==2):
                dst_point = np.array([[0, 0], [w - 1, 0], [w - 1, h - 1], [0, h - 1]], dtype=np.float32)
                perspect = cv2.getPerspectiveTransform(save_point, dst_point)
                dst = cv2.warpPerspective(src, perspect, (w, h))
                dst = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
                cv2.imshow('image', dst)
                cv2.imwrite("gray mode.jpg", dst)
            #그레이모드 적응형이진화
            if (mode == 3):
                dst_point = np.array([[0, 0], [w - 1, 0], [w - 1, h - 1], [0, h - 1]], dtype=np.float32)
                perspect = cv2.getPerspectiveTransform(save_point, dst_point)
                dst = cv2.warpPerspective(src, perspect, (w, h))
                dst = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
                #이진화
                dst=cv2.adaptiveThreshold(dst, 255, cv2.ADAPTIVE_THRESH_MEAN_C  , cv2.THRESH_BINARY_INV, 9, -1)

                cv2.imshow('image', dst)
                cv2.imwrite("color mode.jpg", dst)
            if (mode == 4):
                dst_point = np.array([[0, 0], [w - 1, 0], [w - 1, h - 1], [0, h - 1]], dtype=np.float32)
                perspect = cv2.getPerspectiveTransform(save_point, dst_point)
                dst = cv2.warpPerspective(src, perspect, (w, h))
                dst = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
                dst = cv2.adaptiveThreshold(dst, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 9, -1)
                dst = cv2.medianBlur(dst, 11)
                cv2.imshow('image', dst)
                cv2.imwrite("color plus mode.jpg", dst)
        # 모드정하기
    if event == cv2.EVENT_LBUTTONUP:
        if (300 > x > 0 and 100 > y > 0):
            mode = 1
    if event == cv2.EVENT_LBUTTONUP:
        if (550 > x > 350 and 100 > y > 0):
            mode = 2
    if event == cv2.EVENT_LBUTTONUP:
        if (800 > x > 550 and 100 > y > 0):
            mode = 3
    if event == cv2.EVENT_LBUTTONUP:
        if (1040 > x > 800 and 100 > y > 0):
            mode = 4


cv2.namedWindow('image')
cv2.setMouseCallback('image',click)
# 버튼만들기
cv2.putText(src, "original", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, purple,2)
cv2.putText(src, "gray", (350, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, purple,2)
cv2.putText(src, "color", (600, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, purple,2)
cv2.putText(src, "color+", (840, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, purple,2)
cv2.rectangle(src, (0, 0), (300, 100), green, 3, cv2.LINE_4)
cv2.rectangle(src ,(300, 0), (550, 100) ,green, 3, cv2.LINE_4)
cv2.rectangle(src ,(550, 0), (800, 100) ,green, 3, cv2.LINE_4)
cv2.rectangle(src ,(800, 0), (1040, 100) ,green, 3, cv2.LINE_4)

cv2.imshow('image',src)
cv2.waitKey()