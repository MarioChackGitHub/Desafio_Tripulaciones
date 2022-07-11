import cv2
import os
import imutils

from config import PERSON, WIDTH, SCALE_FACTOR, MIN_NEIGHBORS, PIXEL, NUM_FRAMES


def generar_frames(PERSON):

    '''
    Función que recibe la ruta de un video, detecta rostros y captura un numero de frame de dicho rostro,
    Como configuración, se puede cambiar, la anchura de la foto, el ajuste del frame del rostro, el numero
    de frames detectados para generar una imagen, y el numero de pixeles de la imagenes generadas.


    '''
    # routing 
    person_name = PERSON
    data_path = './data'
    person_path = data_path +'/'+ person_name
    # comprobar que la carpeta existe
    if not os.path.exists(person_path):
        print('Carpeta creada: ', person_path)
        os.makedirs(person_path)
    # capturing from video
    cap = cv2.VideoCapture(f'videos/{person_name}.mp4')
    # classification
    face_classif = cv2.CascadeClassifier('frontalface_default.xml')  #cv2.data.haarcascades

    count = 0

    while True:
    # read the capture, flip the object, resizing the image and convert to gray     
        ret, im = cap.read()
        if ret == False:
            break
        im = cv2.flip(im,0)
        im = imutils.resize(im, width=WIDTH)
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        aux_frame = im.copy()
    # detection from image gray and scale square from the face, five frames from image 
        faces = face_classif.detectMultiScale(gray, SCALE_FACTOR, MIN_NEIGHBORS)
    # create a rectangle above the face
        for (x,y,w,h) in faces:
            cv2.rectangle(im, (x,y),(x+w,y+h),(0,255,0),2)
            rostro = aux_frame[y:y+h,x:x+w]
            rostro = cv2.resize(rostro,PIXEL, interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(person_path + '/cara_{}.jpg'.format(count),rostro)
            count = count + 1
        cv2.imshow('Imagen', im)

        k= cv2.waitKey(1)
        if k == 27 or count >= NUM_FRAMES:
            break
    
    
    cap.release()
    cv2.destroyAllWindows()


##############################################################    



def procesado_frames():
    '''
    Función que reconoce la ruta al banco de imagenes y las procesa al estado de numpy 
    array en escala de grises, devolviendolas normalizadas entre 0 y 1. Así transformamos las imagenes
    al estado optimo para ser entrenadas.
    IMPORTANTE: Verificar la ruta al banco de imagenes
    '''
# verify route 
    data_path = "./data/"
    people = os.listdir(data_path)

    print(people)

    labels = []
    caras = []

    
    # iteration in data sample, read the image and 
    for folder in people:
        person_path = data_path + '/' + folder
        print('Leyendo las imágenes de la carpeta...{}'.format(folder))

        label = folder

        for imagen in os.listdir(person_path):
            # print('Caras: ', folder + '/' + imagen)
            labels.append(label)
            caras.append(cv2.imread(person_path + '/' + imagen,0)) #el 0 es el que indica la escala de grises, que es el formato aceptado en el entrenamiento
    print('Imágenes pasadas a arrays')
    # add faces to array and divide to 255 for normalize 
    caras_norm = []
    for cara in caras:
        caras_norm.append(cara/255)

    print(caras_norm)

    return caras_norm