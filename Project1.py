#Find the vector of the cross product of 2 vectors and draw them in a 3D view : 

import sys
from math import sqrt
import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

v1 = [2,1,2]
v2 = [1,3,4]
x1, y1, z1 = np.array(v1)
x2, y2, z2 = np.array(v2)
x3, y3, z3 = np.cross(v1,v2)
u,v,w = 0,0,0


axes = plt.subplot(111,projection='3d')
axes.quiver(u,v,w, x1, y1, z1, length=np.linalg.norm(v1), normalize=True,color = "blue")
axes.quiver(u,v,w, x2, y2, z2, length=np.linalg.norm(v2), normalize=True,color = "green")
axes.quiver(u,v,w, x3, y3, z3, length=np.linalg.norm(np.cross(v1,v2)), normalize=True,color = "red")
axes.set_xlabel('X axis')
axes.set_ylabel('Y axis')
axes.set_zlabel('Z axis')
axes.set_xlim([-5, 5])
axes.set_ylim([-5, 5])
axes.set_zlim([-5, 5])
plt.show()