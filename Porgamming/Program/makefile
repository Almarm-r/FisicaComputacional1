
#Reutilizando el make file hecho en clase  :) --->
# este es un objetivo por defecto
# emplearemos make
.PHONY: all
all: program

# reglas para decirle a make que vamos a contruir desde el archivo cpp
hello: program.cpp
	g++ -o program program.cpp -lm 
#el lm vincula la libreria matematica limb.so

# esta regla le indica a make que debe copiar los archvos en algun subdirectorio
# es opcional

.PHONY: install
install:
	mkdir -p binaries
	cp -p program binaries

# esta regla le indica a make que borre hello y hello.o
.PHONY: clean
clean: 
	rm -f program 
