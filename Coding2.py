#Evolution du nombre de morts du Covid-19 en Belgique au cours du temps.
import urllib.request 
import json
import numpy as np
import matplotlib.pyplot as plt

#On va chercher les datas qu'on veut dessiner:

url = "https://epistat.sciensano.be/Data/COVID19BE_MORT.json"
response = urllib.request.urlopen(url)
data = json.loads(response.read())

men= {}                 #Dictionnaire avec date comme clé et les diff déces par régions
women= {}               
unknown = {}
liste_m = []            #Liste des décès totaux par jour dans le bonne ordre
liste_w = []
liste_u = []

#On analyse le data qu'on a récuperé pour en sortir 3 dictionnaires qui ont comme clés les 
#dates et comme valeurs une liste de liste des déces en fct du sex on passe d'un dict à un 
#autre, on aura aussi 3 listes qui ont comme valeur la somme des déces par jour par sex.
def analyse(data):
    
    for deces in data :
        men[(deces['DATE'])] = []
        women[(deces['DATE'])] = []
        unknown[(deces['DATE'])] = []

    for n in range(len(data)) : 
        if "SEX" in data[n] and data[n]["SEX"] == "M":
            for date in men.keys() :
                if data[n]["DATE"] == date :
                    men[date].append(data[n]["DEATHS"])
        if "SEX" in data[n] and data[n]["SEX"] == "F":
            for date in women.keys() :
                if data[n]["DATE"] == date :
                    women[date].append(data[n]["DEATHS"])
        if "SEX" not in data[n] :
            for date in unknown.keys() :
                if data[n]["DATE"] == date :
                    unknown[date].append(data[n]["DEATHS"])

    for value in men.values():
        liste_m.append(sum(value))
    for value in women.values():
        liste_w.append(sum(value))
    for value in unknown.values():
        liste_u.append(sum(value))
    
    return(liste_m,liste_w,liste_u,men,women,unknown)

analyse(data)
#On construit la figure :
m = np.array(liste_m)                 #On transforme les listes en tableaux à 1 dimension.
w = np.array(liste_w)
u = np.array(liste_u)
t = np.array(m+w+u)                   #On ajoute les 3 "vecteurs" ensemble pour avoir le total.

legende_x = list(men.keys()) 
for n in range(len(legende_x)):
    legende_x[n] = legende_x[n][5:]        #Met toutes les dates dans une nouvelle liste dans l'ordre.
width = 0.9                     #On prédefini l'épaisseur de chaque bar.
x = np.arange(len(legende_x))   #On stock les locations des labels pour l'axe X dans un tableau à 1 dimension.
fig, axes = plt.subplots(2)     #On crée 2 figures et 2 axes associées à celle-ci

axes[0].bar(x - width/3 , m, width/3, label='Men', align='center',color="blue")           #On dessine l'evolution des nombres de décès de chaque genre sous forme d'histogramme.
axes[0].bar(x , w, width/3, label='Women', align='center',color="pink")               
axes[0].bar(x + width/3 , u, width/3, label='Unknown', align='center',color="yellow")    
axes[0].set_ylabel('Deaths')                                                           
axes[0].set_xlabel('Date ') 
axes[0].set_title("Victimes du Covid-19 en Belgique par rapport à leur sexe " ,fontsize=14, fontweight='bold') #On met le titre avec couleur et taille.
axes[0].set_xticks(x)                                                                     #On met les points sur l'axes x au nombre des dates.
axes[0].set_xticklabels(legende_x, rotation = "90")                                       #On nomme les points de l'axes x par les dates. 
axes[0].legend(loc="best")                                                                #On met les legendes au meilleur endroits.

axes[1].plot(x , t, label='Total',color="red")                                            #On dessine l'evolution des nombres de décès total sous forme de courbe.
axes[1].set_ylabel('Deaths')
axes[1].set_xlabel('Date ') 
axes[1].set_title("Evolution du nombre total de morts du Covid-19 en Belgique " ,fontsize=14, fontweight='bold') 
axes[1].set_xticks(x)
axes[1].set_xticklabels(legende_x, rotation = "90")
axes[1].legend(loc="best")

fig.set_size_inches(18, 9)                                                                 #On prédefini la taille de la fenetre qui va afficher la figure.
plt.subplots_adjust(left=None, bottom=0.14, right=None, top=None, wspace=None, hspace=0.7) #On espace les 2 graphes verticalement pour caler les dates.
plt.show()                                                                                 #On affiche la figure dans une fenêtre.
