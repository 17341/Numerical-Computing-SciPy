import numpy as np

a = np.arange(1,7).reshape(2,3) # [[1 2 3] [4 5 6]]

b = np.ones(3) # [1. 1. 1.]
b = b.ndim # 1 

c = np.linspace(1,7,3, endpoint = False) # [1. 3. 5.]
c = c[c%3 == 0] # [3]

d = np.vdot(a[0],a[1]) # 32(produit scalaire)
d = d/8 # 4 

e = np.array([7,c[0],d]) # [7,3,4]
e = np.insert(e,0,b) # [1,7,3,4]

f = np.append(e,d.size) # [1,7,3,4,1]

m = np.diag(f) # matrice diagonal avec les valeurs de f en diag le reste = 0
n  = np.identity(5) # matrice identité (1 en diagonal le reste = 0)

print(m*n)

