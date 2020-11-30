import matplotlib.pyplot as plt
import numpy as np

def Logaritmic_spiral(b = 1,fi = 1, title = 'Logaritmic spiral'):
    fi = np.arange(0,8**np.pi,0.1)
    x= np.e**(b*fi)*np.cos(fi)
    y= np.e**(b*fi)*np.sin(fi)
    
    plt.plot(x,y,'c', label = 'graph')
    
    plt.title(title)
    plt.axis('equal')
    
    plt.show()

def Archimedean_spiral(k = 1 , title = 'Archimedean spiral'):
    fi = np.arange(0,8*np.pi,0.1)
    expr = k*fi
    
    x = expr * np.cos(fi)
    y = expr*np.sin(fi)
    
    plt.plot(x,y,'c', label = 'graph')
    plt.title(title)
    plt.legend()
    plt.axis('equal')
    
    plt.show()
 
def Spiral_staff(k = 1, title = 'Spiral staff'):
    fi = np.arange(0.1,8*np.pi,0.1)
    expr = k/np.sqrt(fi)
    x = expr * np.cos(fi)
    y = expr*np.sin(fi)
    
    plt.plot(x,y,'c', label = 'graph')
    plt.title(title)
    plt.legend()
    plt.axis('equal')
    
    plt.show()
    
def Rose(k = 1, title = 'Rose'):
    fi = np.arange(0,8*np.pi,0.001)
    expr = np.sin(k*fi)
    
    x = expr * np.cos(fi)
    y = expr*np.sin(fi)
    
    plt.plot(x,y,'s', label = 'graph')
    
    plt.title(title)
    plt.legend()
    plt.axis('equal')
    
    plt.show()


Logaritmic_spiral(0.1)
Archimedean_spiral(1)
Spiral_staff()
Rose(7)