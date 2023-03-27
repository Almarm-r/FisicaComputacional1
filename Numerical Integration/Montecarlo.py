# Montecarlo 
from scipy.optimize import fsolve 
import math
import numpy as np
from sympy import *
from numpy.random import uniform as unif
import random


a=float(input('a \t'))
b=float(input('b \t'))
n=int(input('n \t'))
sum = 0 
if  a == 0:
  a = 0.00001
def f(x):
    return(math.sin(x)/x)
for i in range (n):
  p= float(random.uniform(a, b)) #Genera numeros aleatorios en el intervalo 
  sum =+ f(p) # Suma las funcion evaluada en los números generados. 



fprom = (1/n) * sum 
mont = (b-a)*fprom

#print("Suma", "=",sum)
print( "Sn" , "=",  mont  )
