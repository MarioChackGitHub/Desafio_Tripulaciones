import cv2
import os
import imutils
import image_Augmentation as datagen

person_name = 'Fran'
data_path = 'C:/Users/Usuario/workspace/GitHub/TheBridge/DESAFIO/Desafio_Tripulaciones/data'
person_path = data_path +'/'+ person_name

if not os.path.exists(person_path):
    print('Carpeta creada: ', person_path)
    os.makedirs(person_path)

cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture('C:/Users/Usuario/workspace/GitHub/TheBridge/DESAFIO/Desafio_Tripulaciones/videos/FranRuizGuerra.mp4')

# face_classif = cv2.CascadeClassifier('frontalface_default.xml')  #cv2.data.haarcascades
face_classif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')


num_face = len(os.listdir(person_path))

if num_face == 0:
    count = 0
else :
    count = num_face

#count = 0

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

        #Añadimos imagenes con desplazamiento horizontal
        rostro2 = datagen.horizontal_shift(rostro, 0.7)
        cv2.imwrite(person_path + '/cara2_{}.jpg'.format(count),rostro)

        #Añadimos imagenes con desplazamiento vertical
        rostro2 = datagen.vertical_shift(rostro, 0.7)
        cv2.imwrite(person_path + '/cara3_{}.jpg'.format(count),rostro)

        #Añadimos imagenes cambiando el brillo
        rostro2 = datagen.brightness(rostro, 0.5, 3)
        cv2.imwrite(person_path + '/cara4_{}.jpg'.format(count),rostro)

        #Añadimos imagenes aumentando el Zoom
        rostro2 = datagen.zoom(rostro, 0.5)
        cv2.imwrite(person_path + '/cara5_{}.jpg'.format(count),rostro)

        #Añadimos imagenes con la función espejo
        rostro2 = datagen.horizontal_flip(rostro, True)
        cv2.imwrite(person_path + '/cara6_{}.jpg'.format(count),rostro)

        #Añadimos imagenes rotadas
        rostro2 = datagen.rotation(rostro, 30)
        cv2.imwrite(person_path + '/cara7_{}.jpg'.format(count),rostro)

        count = count + 1
    cv2.imshow('Imagen', im)
    k= cv2.waitKey(1)
    if k == 27 or count >= num_face + 300:
        break


cap.release()
cv2.destroyAllWindows()