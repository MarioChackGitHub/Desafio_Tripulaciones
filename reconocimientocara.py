import cv2
import os
import imutils


person_name = 'Mario'
data_path = 'C:/Users/usuario/Documents/GitHub/Desafio_Tripulaciones/Reconocimiento_Facial'
person_path = data_path +'/'+ person_name

if not os.path.exists(person_path):
    print('Carpeta creada: ', person_path)
    os.makedirs(person_path)

cap = cv2.VideoCapture(0)
face_classif = cv2.CascadeClassifier('frontalface_default.xml')  #cv2.data.haarcascades

count = 0

while True:
    ret, im = cap.read()
    if ret == False:
        break
    im = imutils.resize(im, width=640)
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    aux_frame = im.copy()

    faces = face_classif.detectMultiScale(gray, 1.3,5)

    for (x,y,w,h) in faces:
        cv2.rectangle(im, (x,y),(x+w,y+h),(0,255,0),2)
        rostro = aux_frame[y:y+h,x:x+w]
        rostro = cv2.resize(rostro,(150,150), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(person_path + '/cara_{}.jpg'.format(count),rostro)
        count = count + 1
    cv2.imshow('Imagen', im)

    k= cv2.waitKey(1)
    if k == 27 or count >= 300:
        break

cap.release()
cv2.destroyAllWindows()