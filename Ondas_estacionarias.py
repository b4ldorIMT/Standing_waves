import matplotlib.pyplot as plt 
import numpy as np 
import matplotlib.animation as animation 


t = np.linspace(0, 1, 300) 
x = np.linspace(-np.pi, np.pi, 300)

def onda_1(x,t):
    f =4000
    l = 0.343
    w = 2 * np.pi * f
    k= (2*np.pi)/l
    return (1* np.sin((k*x) - (w *t)))

def onda_2(x,t):
    f =4000
    l = 0.343
    w = 2 * np.pi * f
    k= (2*np.pi)/l
    return (1* np.sin((k*x) + (w *t)))

def onda_r(x,t):
    f =4000
    l = 0.343
    w = 2 * np.pi * f
    k= (2*np.pi)/l
    return ((1* np.sin((k*x) + (w *t)))) + ((1* np.sin((k*x) - (w *t))))

#Grafica 
fig=plt.figure()
ax = fig.gca()

  
#Actualizar
def animacion(i):
    ax.clear()
    ax.plot(x, onda_1(x,t[i]))
    ax.plot(x, onda_2(x,t[i]))
    ax.plot(x, onda_r(x,t[i]))  
    plt.title(str(t[i]))
    plt.xlim(min(x), max(x))
    plt.ylim(-5, 5)
    
#animacion 
animan= animation.FuncAnimation(fig, animacion, range(len(x)), interval=10,repeat=False)
plt.show()