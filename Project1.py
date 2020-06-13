#Find the vector of the cross product of 2 vectors and draw them in a 3D view : 
import sys
from math import sqrt
import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

o = np.zeros(3,dtype ="int64")
v1 = np.array([4,4,7])
v2 = np.array([1,3,4])
v3 = np.cross(v1,v2)

u,v,w = o         #Origine
x1, y1, z1 = v1
x2, y2, z2 = v2
x3, y3, z3 = v3

mini = np.minimum(v1,v2,v3)
maxi = np.maximum(v1,v2,v3)

axes = plt.subplot(projection='3d')
axes.quiver(u,v,w, x1, y1, z1, length=np.linalg.norm(v1), normalize=True,color = "blue")
axes.quiver(u,v,w, x2, y2, z2, length=np.linalg.norm(v2), normalize=True,color = "green")
axes.quiver(u,v,w, x3, y3, z3, length=np.linalg.norm(v3), normalize=True,color = "red")
axes.set_xlabel('X axis')
axes.set_ylabel('Y axis')
axes.set_zlabel('Z axis')
axes.set_xlim([-2*mini[0],2*maxi[0]])
axes.set_ylim([-2*mini[1],2*maxi[1]])
axes.set_zlim([-2*mini[2],2*maxi[2]])

plt.show()