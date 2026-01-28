import random
import os
from PIL import Image

datosPoliperros={
    "nombre":[],
    "huellaDactilar":[],
    "foto":[]
}

numPerros=0

def menu():
    print("\n\t\t *** Bienvenido(a) ***\n")
    print("Que accion desea realizar?")
    print('* 1)Registrar poliperros')
    print('* 2)Mostrar poliperros')
    print('* 3)Imprimir BDD')
    print('* 4)Salir del Sistema')
    opcion=int(input('Ingrese la opcion: '))
    return opcion

def registararPoliperros(numPerros):
    os.makedirs("BDDPERROS",exist_ok=True)
    archivo=open("poliperros.txt","a") 

    for i in range(numPerros):
        print(f"Ingrese los datos del poliperro {i+1}")
        nombre=input("Nombre: ")
        huellaDactilar=input("Huella dactilar: ")
        
        print("El poliperro dispone de foto?")
        tieneFoto=input("Ingrese si o no: ")
        if tieneFoto=="si":
            rutaOriginal=input("Ingrese la ruta de la foto: ")
            imagen=Image.open(rutaOriginal)
        else:
            imagen=Image.open("dog.png")
        rutaGuardada=f"BDDPERROS/poliperro_{random.randint(1,1000)}.png"
        imagen.save(rutaGuardada)

        datosPoliperros["nombre"].append(nombre)
        datosPoliperros["huellaDactilar"].append(huellaDactilar)
        datosPoliperros["foto"].append(rutaGuardada)

        archivo.write("BDD POLIPERROS \n")
        archivo.write(f"{nombre} -- {huellaDactilar} -- {rutaGuardada}\n")
    archivo.close()


def mostrarPoliperros():
    for i in range(len(datosPoliperros["nombre"])):
        print("-------------------------------")
        print(f"Mostrar los datos del poliperro {i+1}")
        print("* Nombre",datosPoliperros["nombre"][i])
        print("* huellaDactilar",datosPoliperros["huellaDactilar"][i])
        imagen=Image.open(datosPoliperros["foto"][i])
        imagen.show()

def mostrarPoliperrosPorHuella():
    huella_buscar = input("Ingrese la huella dactilar")
    encontrado=False
    for i in range(len(datosPoliperros["nombre"])):
        if huella_buscar==datosPoliperros["huellaDactilar"]:
            print("* Nombre",datosPoliperros["nombre"][i])
            print("* huellaDactilar",datosPoliperros["huellaDactilar"][i])
            imagen=Image.open(datosPoliperros["foto"][i])
            imagen.show()
            encontrado=True
            break
        if not encontrado:
            print("No se ha encontrado la huella dactilar")




def imprimirArchivo():
    archivo=open("poliperros.txt","r")
    lineas=archivo.readlines()
    for l in lineas:
        print(l,end="")
    archivo.close()

def main():
    print("----------POLIPERROS----------")
    opcion=menu()
    while opcion !=4:
        if opcion==1:
            numPerros=int(input("Ingrese el numero de poliperros a regitrar: "))
            registararPoliperros(numPerros)
        elif opcion==2:
            mostrarPoliperros()
        elif opcion==3:
            imprimirArchivo()
        opcion=menu()
    print("Gracias por usar el sistema")


main() 