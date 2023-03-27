#Trapecio 

from scipy.optimize import fsolve 
import math
from sympy import *
import numpy as np
2
a=float(input('a \t'))
b=float(input('b \t'))
n=int(input('n \t'))
if  a == 0:
  a = 0.00001
def f(x):
    return(math.sin(x)/x) #aquí va la f(x)
dx=(b-a)/n
suma=f(a)+f(b)
for i in range(n-1): #vemos n-1 términos, el for para uno antes. realmente es un n-2 | termina en un n-1 términos.
    Pah=2*f(a+(i+1)*dx)
    suma=suma+Pah
#print(suma)
print( "Sn" , "=", dx/2*suma) 
