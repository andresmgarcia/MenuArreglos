__author__ = 'examen'
from Clase.Inscriptos import *
import random
import pickle
import os.path
cadena = ["andres","mariano","silvio","valerio","zoe","buffa","jeremias","jimenez","juli"]


#punto 1
def cargar_Arreglo(n):
    lista = []*n
    for i in range(n):
        dni = random.randint(40000,50000)
        nom = random.choice(cadena)
        cur = random.randint(0,29)
        form = random.randint(0,4)
        monto = random.randint(0,300)
        reg=Inscriptos(dni,nom,cur,form,monto)
        add_in_order(reg,lista)

    return lista

def add_in_order(reg,lista):
    n=len(lista)
    izq,der=0,n-1
    pos=n

    while izq<=der:

        c = (izq+der)//2

        if reg.dni == lista[c].dni:
            pos = c
            break
        if reg.dni < lista[c].dni:
            der = c-1
        else:
            izq = c+1

    if izq > der:
        pos = izq

    lista[pos:pos] = [reg]

#Punto 2
def mostrar_Arreglo(lista):
    print(encabeza())
    for i in range(len(lista)):
        reg=lista[i]
        print(toString(reg))

#Punto3
def crear_archivo(ruta,lista,x):
    m=open(ruta,"wb")
    for i in range(len(lista)):
        reg=lista[i]
        if reg.monto < x :
            pickle.dump(reg,m)

    m.flush()
    m.close()

#Punto 4
def mostrar_archi(ruta):
    m=open(ruta,"rb")
    tam = os.path.getsize(ruta)
    print(encabeza())
    while m.tell() < tam:
        reg=pickle.load(m)
        print(toString_archi(reg))
    m.close()

#Punto 5
def buscar_nom(lista,x):
    for i in range(len(lista)):
        if x ==lista[i].nom:
            return lista[i]
    return False

#Punto 6
def generar_matriz(lista):
    matriz = [[0]*30 for i in range(5)]
    for i in range(len(lista)):
        matriz[lista[i].forma][lista[i].curso]+=1
    return matriz

def mostrar_matriz(matris):
    for i in range(len(matris)):
        for j in range(len(matris[i])):
            if matris[i][j] != 0 :
                print("Inscriptos",matris[i][j],"tipo:",i,"forma de pago:",j)

#punto 7
def segundo_archi(ruta,lista):
    m=open(ruta,"wb")
    for i in range(len(lista)):
        reg=lista[i]
        if reg.forma !=4:
            pickle._dump(reg,m)
    m.flush()
    m.close()
def mostrar_archi2(ruta):
    m=open(ruta,"rb")
    tam = os.path.getsize(ruta)
    print(encabeza())
    while m.tell() < tam:
        reg=pickle.load(m)
        print(toString(reg))
    m.close()


def temporizador(n):
    while n!=0:
        print("hola gay",n)
        return temporizador(n-1)


def main():

    temporizador(30)

if __name__ == '__main__':

    main()