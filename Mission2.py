import numpy as np
import re
import time

#On dispose d'une balance et de plusieurs sacs de fruit, on stock le poids et le contenu des sacs dans un dictionnaire
#Le challenge est de trouver le poids de chaque fruit sans ouvrir les sacs.(Hypothése : la masse de chaque fruit est constante) 

sacs = {"500g":["2 orange(s)","10 fraise(s)","1 banane(s)"],"210g":["1 orange(s)","6 fraise(s)","0 banane(s)"],"420g":["0 orange(s)","12 fraise(s)","3 banane(s)"]}

orange = r'.+\sorange.+'
fraise = r'.+\sfraise.+'
banane = r'.+\sbanane.+'

o = re.compile(orange)
f = re.compile(fraise)
b = re.compile(banane)
    
liste1 = []
liste2 = []
#On analyse le dictionnaire pour retirer les chiffres et on les stock dans une liste:
for key in sacs.keys():                                                         
    liste1.append(re.search(r'\d+', key).group())
    for n in range(len(sacs[key])):
        if o.match(sacs[key][n]) is not None:
            liste2.append(re.search(r'\d+', sacs[key][n]).group())
        if f.match(sacs[key][n]) is not None:
            liste2.append(re.search(r'\d+', sacs[key][n]).group()) 
        if b.match(sacs[key][n]) is not None:
            liste2.append(re.search(r'\d+', sacs[key][n]).group())
#On met les chiffres dans des tableaux en int:
liste1 = np.array(liste1).astype("int64")                                       
liste2 = np.reshape(np.array(liste2),(len(sacs.values()),3)).astype("int64")    
#Solution la plus rapide et la plus efficace, on obtient une liste avec les résultats dans l'ordre:
start1_time = time.time()                                                       
result1 = np.linalg.solve(liste2,liste1)         
print(result1,time.time() - start1_time)
#Bonne solution, on obtient une liste avec les résultats dans l'ordre:
start2_time = time.time()                                                       
result2 = np.linalg.inv(liste2).dot(liste1)
print(result2,time.time() - start2_time)
#Solution "plus longue" et moins efficace que les 2 autres, on obtient un tableau (1,3) avec les résultats dans l'ordre:
start3_time = time.time()                                                       
matrice = np.matrix(liste2)
result3 = np.dot(matrice.I,liste1)
print(result3,time.time() - start3_time)
 

