#Evolution du nombre de morts du Covid-19 en Belgique au cours du temps.
import urllib.request 
import json
import numpy as np
import matplotlib.pyplot as plt

#On va chercher les datas qu'on veut dessiner:

url = "https://epistat.sciensano.be/Data/COVID19BE_MORT.json"
response = urllib.request.urlopen(url)
data = json.loads(response.read())

men= {}
women= {}
unknown = {}
m = []
w = []
u = []
t = []

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
        m.append(sum(value))
    for value in women.values():
        w.append(sum(value))
    for value in unknown.values():
        u.append(sum(value))
    for n in range(len(m)):
        t.append(m[n]+w[n]+u[n]) 
    return(m,w,u,t,men,women,unknown)
    
analyse(data)
#On construit la figure :

legende_x = list(men.keys())
width = 0.9
x = np.arange(len(legende_x))
fig, axes = plt.subplots()

axes.bar(x - width/3 , m, width/3, label='Men', align='center',color="blue")
axes.bar(x , w, width/3, label='Women', align='center',color="pink")
axes.bar(x + width/3 , u, width/3, label='Unknown', align='center',color="yellow")
axes.plot(x , t, label='Total',color="red")
axes.set_ylabel('Deaths')
axes.set_xlabel('Date ')
axes.set_title("Victimes du Covid-19 en Belgique au cours du temps ")
axes.set_xticks(x)
axes.set_xticklabels(legende_x)
axes.legend(loc="best")
plt.xticks(rotation=90)
fig.set_size_inches(18, 9)

plt.show()
