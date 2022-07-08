import sys

sys.path.append(".")


# Usuarios registrados

PERSON_1 = "Fran1"
PERSON_2 = "Selu"
PERSON_3 = "Mario"
PERSON_4 = "Kike"
PERSON_5 = "Nani"
PERSON_6 = "Ouissan"

################################################


# AJUSTES FUNCION GENERAR FRAMES

# Caracteristicas imagen

WIDTH = 640

# espicador de la talla de imagen ajustando al rostro
SCALE_FACTOR = 1.4

# parametro cuantos frames detectac una misma cara
MIN_NEIGHBORS = 5 

# tamaño del frame capturado en pixeles
PIXEL = (150,150)

# Numero de frames que se capturan en el video
NUM_FRAMES = 300

#####################################################

# AJUSTES FUNCION PROCESADO FRAMES

