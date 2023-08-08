# OpenCV
OpenCV를 이용한 모바일스캐너입니다.
# 1.프로젝트 설명
OpenCV를 이용해서 사진의 선택된 영역을 잘라 보정한다.
모바일의 스캐너를 보고 기능을 모방하였다.
## 1-2 프로젝트 기간

2021/6/16(추정)~2021/6/17
# 2.기술 스택
- Python
- OpenCV
# 3.기능 설명
사진에 모드를 선택한후 네점을 찍으면 원근투시변환,적응형 이진화,Median필터링등을 사용하여 사진을 잘라 보정한다.
# 4.실행 사진
![](https://velog.velcdn.com/images/yun68000/post/ab7ce272-085d-4d47-b4a3-a13d8750dd69/image.jpg)
![](https://velog.velcdn.com/images/yun68000/post/abcfd410-b979-423c-99f1-53810f367a42/image.jpg)
![](https://velog.velcdn.com/images/yun68000/post/63629c20-7b41-41f9-9a24-eaab6ce5c700/image.jpg)

# 5.핵심코드
```
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
                cv2.imwrite("color plu
```

# 6.아쉬운점
조잡한 color , color+ 등의 선택창이 아쉽다
