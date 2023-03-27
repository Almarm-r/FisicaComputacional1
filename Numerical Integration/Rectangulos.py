#Rectangulos 

from scipy.optimize import fsolve 
import math
from sympy import *
import numpy as np

a=float(input('a \t')) # límite inferior
b=float(input('b \t')) #límite superior
n=int(input('half of n \t')) # de subintervalos
if  a == 0:
  a = 0.00001

def f(x): 
  return(math.sin(x)/x)
dx= (b-a)/n
suma=0
for i in range(n):
  suma=suma+f(a+(2*i+1)*dx/2)

print("Sn =",suma*dx)
