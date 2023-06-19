import easyocr
import matplotlib.pyplot as plt
import cv2
image = cv2.imread('./img/car1.png')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#이미지 이진화
binary = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
contours, _=cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for counter in contours:
    #너비 높이
    x, y, w, h = cv2.boundingRect(counter)
    #너비와 높이의 비율이 일정 범위에 들어가는 컨투어만 선택
    aspect_ratio = w / h
    if 2< aspect_ratio < 4:
        #선택 박스 이미지에 그림
        license_plate = cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,0),2)
        #번호판 영역추출
        lp_region = image[y:y+h, x:x+w]
        #OCR wjrdyd
        reader = easyocr.Reader(['en','ko'])
        result = reader.readtext(lp_region)
        # 결과 출력
        print(result)
img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()