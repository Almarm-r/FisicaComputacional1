from scipy.optimize import fsolve 
import math
def f(x):
  return (((x**(3))-2*(x**(2))+1))  #Colocar la función de la cual estamos buscando la raíz 
print(fsolve(f,5000)) #f, dato referencia, solución cercana a #
l=0 #left 
r=3 #rigth
m=2 #middle 
n= int(input("Escriba en número de interaciones"))
for i in range(n):
  if f(l)*f(m)>0:
    l=m
  else:
    r=m
  m=(l+r)/2
print('l=',l,'\t m=',m,'\t r=',r,)
print('f(l)=',f(l), 'f(m)=',f(m), 'f(r)=', f(r))

