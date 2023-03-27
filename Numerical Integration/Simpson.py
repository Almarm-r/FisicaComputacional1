#Simpson 

from scipy.optimize import fsolve 
import math
a=float(input('a \t')) # límite inferior
b=float(input('b \t')) #límite superior
n=int(input('half of n \t')) # # de subintervalos
if  a == 0:
  a = 0.00001  #Evintnado indeterminaciones 
def f(x):
  return(math.sin(x)/x) #función
dx=(b-a)/(n*2) #paso, normalmente vale n*2=6 l parecer
suma=f(a)+f(b) 
four=0
two=0


for i in range (n):
  four=four+4*f(a+(2*i+1)*dx)
for i in range ((n)-1):
  two=two+2*f(a+(2*i+2)*dx)
sn=(suma+two+four)*dx/3

print('S',n*2, "=" ,sn)
