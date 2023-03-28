from traitlets.traitlets import Float
"""import os
os.chdir("C:\\Datos")
os.getcwd()"""
#Extraer los datos en arreglos. 
import csv
f= open("xy.csv")
reader = csv.reader(f)
xdat =[ ]
ydat = [ ]

for row in reader:

    # Row 1 es el dato y y row 0 es el dato x 
  xdat.append( row[0])
  ydat.append(row[1])

#Falta cambiar el tipo de dato. 
xdat.pop(0)
ydat.pop(0)

x=[ ]
y = [ ]
for dat in xdat:
  x.append(float(dat))

for dats in ydat:
  y.append(float(dats))



#Para calcular los gradientes 

v=[]
a=[]

for i in range(len(x)-1):   
    velocidad = (y[i+1] - y[i]) / (x[i+1] - x[i])
    v.append(velocidad) 

for i in range(len(v)-1):
    aceleracion = (v[i+1] - v[i]) / (x[i+2] - x[i])
    a.append(aceleracion) 

with open("values.txt", "w") as archivo: # Prepara mediante write la creacion de un write de extension txt
    archivo.write("Tiempo\tPosicion\tVelocidad\tAceleracion\n") # Este es el encabezado de mi write txt
    for i in range(len(y)): # Este bucle depende del numero de valores del vector posicion
        archivo.write(f"{y[i]}\t{y[i]}\t") # Esta linea imprime en el write los tiempos (ubicados en el vector tiempos) y las posiciones (ubicadas en el vector posiciones)
        if i < len(v): # Esta estructura de control va guardando las velocidades obtenidas en el vector velocidades, en el write txt
            archivo.write(f"{v[i]}\t") # Almacena las velocidade al write
        else:
            archivo.write("\t") # cuando no encuentra velocidades, pasa a guardar las aceleraciones
        if i < len(a): # Esta estructura de control va guardando las aceleraciones obtenidas en el vector aceleraciones, en el write txt
            archivo.write(f"{a[i]}") # Guarda todas la aceleraciones calculadas en el write
        archivo.write("\n") # Instruccion que indica fin de la linea
