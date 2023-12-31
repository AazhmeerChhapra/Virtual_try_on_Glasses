import numpy as np
import cv2
from django.shortcuts import render, get_object_or_404, HttpResponse
from store.models.product import Products
from django.urls import path
import math
import os


def try_on_glasses(request, product_id):
    # Absolute paths to required files
    product = get_object_or_404(Products, id=product_id)
    script_directory = os.path.dirname(os.path.abspath(__file__))

# Navigate to the 'store/uploads/products' directory
    current_directory = os.path.join(script_directory, 'uploads', 'products')
    cascade_face_path = os.path.join(script_directory, 'haarcascade_frontalface_default.xml')
    cascade_eye_path = os.path.join(script_directory, 'haarcascade_eye.xml')

# https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml

# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml

    face_cascade = cv2.CascadeClassifier(cascade_face_path)
    eye_cascade = cv2.CascadeClassifier(cascade_eye_path)

    glasses = os.path.join(current_directory,os.path.basename(product.image.url))
    image = cv2.imread(glasses,cv2.IMREAD_COLOR)


    row, col , channels = image.shape

    cap = cv2.VideoCapture(0) 

    flag = 0

    eyes=[]

    while 1:
        print("hellllooo")
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    
        for (x,y,w,h) in faces:  ## we only look for eyes inside faces
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
        
            eyes = eye_cascade.detectMultiScale(roi_gray)

        
    
    

        if (len(eyes) == 2):   ## if two eyes are found... sometimes objects are misidentified as eyes, and sometimes eyes are not identified 

            flag = 1

            fx = eyes[0,0]+eyes[1,0] 
            fx= int(fx/2 + x)
            fy = eyes[0,1]+eyes[1,1] 
            fy= int(fy/2 + y)

            dis = abs(eyes[0,0]-eyes[1,0])
            print(fx,' ',fy,' ',dis)

        
            dis_default = 65 # default distance for the scale of glasses
            dx = 50 # rows offset
            dy = 20 # columns offset
        


            ratio = dis/dis_default

            dx = int(dx*ratio)  # shifting offsets to distance
            dy = int(dy*ratio)

            size = (int(col*ratio) , int(row*ratio) )

            print(ratio,' ',size)

            img3 = cv2.resize(image,size) 

            rows, cols , channels = img3.shape


        

            img3gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
            ret, mask = cv2.threshold(img3gray, 10, 255, cv2.THRESH_BINARY)
            mask_inv = cv2.bitwise_not(mask)


        if flag == 1: # flag is used to wiat for initial position of glasses to be set
            roi = img[fy+0-dy:fy+rows-dy,fx+0-dx:fx+cols-dx]  
            img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
            img3_fg = cv2.bitwise_and(img3,img3,mask = mask)
            dst = cv2.add(img1_bg,img3_fg)
            img[fy+0-dy:fy+rows-dy, fx+0-dx:fx+cols-dx] = dst

        cv2.imshow('img',img)


        k = cv2.waitKey(30) & 0xff 
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

    _, buffer = cv2.imencode('.jpg', image)
    response = HttpResponse(buffer.tobytes(), content_type='image/jpeg')
    return response
    

