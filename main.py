import cv2 as cv 
print("1.Blur your image\n2.View HSV image\n3.View LAB image")
choice=int(input("Enter your choice:"))
path=input("Give your image path")
img=cv.imread(path)
cv.imshow('Original_image',img)
if choice==1:
    blur=cv.medianBlur(img,7)
    cv.imshow('Blur_image',blur)
if choice==2:
    hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
    cv.imshow('HSV_image',hsv)
if choice==3:
    lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
    cv.imshow("LAB_image",lab)
cv.waitKey(0)
