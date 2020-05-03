import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2, sys

# Transforme l'image en grayscale:

picture = sys.argv[2]
im1 = mpimg.imread(picture)
img1 = np.copy(im1)                                 #On fait une copie de l'original
print(img1.shape)                                   #Donne le nbr de pixel de l'image , le troisieme nombre est le nombre de couleur 3(rouge,vert,bleu).
print(img1)                                         #Donne un tableau avec les valeurs rgb de chaque pixel, img1[ligne][colonne]

#With matplotlib

def color_matplot():
    c =  sys.argv[3]    
    rgb= np.array([0.2989, 0.5870, 0.1140])         #Les constantes utilisé pour l'intensité effectif de luminosité d'un pixel.
    color_image = np.dot(img1, rgb)                 #On fait un produit scalaire de l'array de l'image avec l'intensité effectif, 
    print(color_image)                              #on obtient alors un tableau à 2 dimensions, 
    plt.imshow(color_image, cmap=plt.get_cmap(c))   #Finalement on fait une image de ça avec la couleur gris.
    plt.show()

def darker_matplot():
    b =  sys.argv[3]
    for i in range(img1.shape[0]):
        for j in range(img1.shape[1]):
            img1[i,j] = np.divide(img1[i,j],int(b)) #On divise chaque valeur rgb de chaque pixel par 2.                               
    plt.imshow(img1)       
    plt.show()
    
def invers_matplot():
    fig, axes = plt.subplots(2) 
    axes[0].imshow(img1)
    axes[1].imshow(np.flipud(img1))                 #Flipud , flip verticalement
    fig.set_size_inches(10, 7)                                  
    plt.show()

"""
#With Pillow

def gray_pillow():
    im2 = np.array(Image.open('Picture.jpg').convert('L'))
    img2 = Image.fromarray(im2)
    img2.show()
if sys.argv[1] == "gray-pillow" :
    gray_pillow()

#With OpenCV

def gray_cv2():
    image = cv2.imread('Picture.jpg')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray image', gray)
    cv2.waitKey(0)
if sys.argv[1] == "gray-cv2":
    gray_cv2()
"""

if sys.argv[1] == "color-matplot" :
    color_matplot()
if sys.argv[1] == "darker-matplot" :
    darker_matplot()
if sys.argv[1] == "invers-matplot":
    invers_matplot()

