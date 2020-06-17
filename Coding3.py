import urllib.request 
import json
import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy.interpolate import interp1d

#Select a dataset from an Open Data source and draw it as a scatter plot : 

#On récupère les data
url = "https://epistat.sciensano.be/Data/COVID19BE_tests.json"
response = urllib.request.urlopen(url)
data = json.loads(response.read())
#Choisir le degré(réglé)
n = int(sys.argv[1])               
#On crée les listes qu'on va utilisé pour faire nos tableaux
date = []
tests = []
o = 1
#On remplie les listes avec les valeurs de tests et le comptage des jours
for j in data:
    date.append(o)
    tests.append(j['TESTS'])
    o += 1
#On transforme ces listes en tableaux à 1 dimension
x = np.array(date)
y = np.array(tests)
#On trouve la courbe correspondante, c'est un tableau à n dimensions
curve = np.polyfit(x,y,n)
#On transforme la courbe en une fonction polynomial de degré n
polynomial = np.poly1d(curve)
#Maintenant on cherche les nouveaux point sur la courbe transfomé
fit_x = []
fit_y = []
#On prend des points de x[1-->len(data)] et on les remplaces dans la formule du polynomial trouvé  
for i in range(len(data)) :
    fit_x.append(i+1)
    c = polynomial(i+1)
    fit_y.append(c)
#On utilise la technique d'interpolations
interpolations= interp1d(x, y)
#On dessine le tout
plt.figure(figsize=(15,5))
plt.plot(fit_x, interpolations(fit_x), '--',color = 'black')
plt.scatter(x,y,color="red")
plt.plot(fit_x,fit_y,color= "blue")
plt.legend(['Interpolations','Polyfit','Data'], loc='best')
plt.title("Total number of tests performed by days from 2020-03-01 for the Covid-19 in Belgium")
plt.xlabel("Jours")
plt.ylabel("Tests")
plt.show()
