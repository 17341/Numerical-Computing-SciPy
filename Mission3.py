import time
import random  
import numpy as np
import sys 
import matplotlib.pyplot as plt

f = sys.argv[1]
ax1 = []
ax2 = []
ax3 = []
ax4 = []

for n in range(int(f)):
    result1 = [[0 for i in range(n)] for j in range(n)]
    m1 = [[random.randint(1,100) for i in range(n)] for j in range(n)]
    m2 = [[random.randint(1,100) for i in range(n)] for j in range(n)]
    m3 = (np.array(m1)).astype("int64")
    m4 = (np.array(m2)).astype("int64")

    def bas_matr_mult():
        start1_time = time.time()
        for i in range(len(m1)):
            for j in range(len(m1[0])):
                for k in range(len(m1)):
                    result1[i][j] += m1[i][k] * m2[k][j]
        t1 = time.time() - start1_time
        ax1.append(t1)

    def num_matr_mult():
        start2_time = time.time()
        m3.dot(m4)
        t2 = time.time() - start2_time
        ax2.append(t2)
    
    def bas_matr_add():
        start3_time = time.time()
        for i in range(len(m1)):
            for j in range(len(m1[0])):
                result1[i][j] = m1[i][j] + m2[i][j]
        t3 = time.time() - start3_time
        ax3.append(t3)

    def num_matr_add():
        start4_time = time.time()
        np.add(m3,m4)
        t4 = time.time() - start4_time
        ax4.append(t4)

    bas_matr_mult()  
    num_matr_mult()
    bas_matr_add()
    num_matr_add()
   
fig, axes = plt.subplots(2)

axes[0].plot(ax1,color = "red",label="With Lists")
axes[0].plot(ax2,color = "blue",label="With Numpy")
axes[0].set_title("Evolution of the execution time to multiply two square matrices")
axes[0].set_ylabel('Time[s]')
axes[0].set_xlabel('Dimensions[n]')
axes[0].legend(loc='best')

axes[1].plot(ax3,color = "red",label="With Lists")
axes[1].plot(ax4,color = "blue",label="With Numpy")
axes[1].set_title("Evolution of the execution time to add two square matrices")
axes[1].set_ylabel('Time[s]')
axes[1].set_xlabel('Dimensions[n]')
axes[1].legend(loc='best')


fig.set_size_inches(9, 6)
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.5)
plt.show()
