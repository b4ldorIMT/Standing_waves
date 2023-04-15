import matplotlib.pyplot as plt 
import numpy as np 
from mpl_toolkits.mplot3d import axes3d
import matplotlib.animation as animation 


t = np.linspace(0, np.pi, 50) 
x = np.linspace(-np.pi, np.pi, 300)

def f(x,t):
    f =1000
    l = 0.343
    w = 2 * np.pi * f
    k= (2*np.pi)/l
    return ((1* np.sin(k*x)) - (w *t))
    #return np.sin(x+t)
#Grafica 
fig=plt.figure()
ax = fig.gca()

#Actualizar
def animacion(i):
    #ax.clear()
    ax.plot(x,f(x,t[i]))
    plt.title(str(t[i]))
    plt.xlim(min(x), max(x))
    plt.ylim(-1.5, 1.5)
    
#animacion 
animan= animation.FuncAnimation(fig, animacion, range(len(x)), interval=10,repeat=False)
plt.show()