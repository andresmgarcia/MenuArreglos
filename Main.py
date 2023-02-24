from Clase.Inscriptos import *
from Funciones import *


op=0
hay_arreglo =False
hay_arhi = False
while op!=9:

    print("\nBIENVENIDO AL PROGRAMA FINAL")
    print("*"*50)
    print("1-Cargar arreglo.")
    print("2-Mostrar arreglo.")
    print("3-Crear arrchivo. ")
    print("4-Mostrar archivo1")
    print("5-Buscar nombre en el arreglo.")
    print("6-Generar Matriz contadora")
    print("7-Mostrar archivo2 ")
    print("8-Salir.\n")

    op=int(input("\tIngrese la opcion que desea:"))

    if not hay_arreglo and op!=1:
        print("\tDebe crear el arrelgo (ingrese 1) ")
    elif op==1:
        n=int(input("\tCantidad de registros a cargar : "))
        lista = cargar_Arreglo(n)
        hay_arreglo=True
    elif op==2:
        mostrar_Arreglo(lista)

    elif op==3:
        if hay_arreglo:
            ruta = "ExamenFinal.dat"
            x = int(input("\tIngrese un monto : "))
            crear_archivo(ruta,lista,x)
            hay_arhi = True
        else:
            print("\tCrear el arreglo primero.")

    elif op==4:
        if hay_arhi:
            mostrar_archi(ruta)
        else:
            print("debe crear el archivo para poder mostrarlo")
    elif op==5:
        nom=input("ingrese el nombre que busca")
        lista2 = buscar_nom(lista,nom)
        if lista2:
            print(toString(lista2))
        else:
            print("\tNo se encontro el nombre buscado")
    elif op==6:
        matriz = generar_matriz(lista)
        mostrar_matriz(matriz)

    elif op==7:
        ruta2 = "SegundoFile.dat"
        segundo_archi(ruta2,lista)
        mostrar_archi2(ruta2)
    elif op==8:
        exit("**USTED HA SALIDO , ADIOS**")
    else:
        print("\tOpcion invalida.")