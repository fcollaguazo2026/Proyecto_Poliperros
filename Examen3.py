import random
import os
import stdiomask
import random
import subprocess
import random
import os
import stdiomask
import random
import subprocess

datos = {
"nombre":[],
"apellido":[],
"telefono":[],
"direccion":[],
"pedido":[],
"paquete":[],
"total":[]
}

def Menu():
    print("\n ====== TECHWORLD S.A ====== \n")
    print(" ***** Bienvenido(a) ***** \n")
    print("""
    ¿Que acción desea realizar?
    * 1) Registrar Pedidos
    * 2) Mostrar Pedidos
    * 3) Mostrar detalle de un pedido
    * 4) Eliminar un pedido
    * 5) Salir del sistema""")
    opcion = int(input("Ingrese la opción: "))
    return opcion

def RegistrarPedidos():
    print(" ----- Nuevo Pedido ----- \n")
    print("\t Ingrese los datos del cliente \n")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    telefono = input("Teléfono: ")
    direccion = input("Dirección: ")
    pedido = random.randint(1000,9999)
       

    print("\t Seleccione el paquete ofimatico a contratar\n")
    print("""
    * 1) Opcion 1: PC + Monitor = $500
    * 2) Opcion 2: PC + Monitor 4k = $2000
    * 3) Opcion 3: Laptop UltraProIA = $1500
    * 4) Opcion 4: Workstation servidor = $3000""")
    opcion = int(input("Ingrese la opción: "))

  
    datos['nombre'].append(nombre)
    datos['apellido'].append(apellido)
    datos['telefono'].append(telefono)
    datos['direccion'].append(direccion)
    datos['pedido'].append(pedido)
    datos['paquete'].append(opcion)
    datos['total'].append(total)

def MostrarPedidos():

    if len(datos['nombre']) == 0:
        print("\n No hay pedidos registrados \n")
    else:
        print("\n ----- Detalle de los pedidos ----- \n")
        print("-----------------------------------")
for i in range(len(datos['nombre'])):
    print("\nDetalle del pedido", i+1)
    print("\n")
    print("Datos del cliente")
    print("\t* Nombre:", datos['nombre'][i])
    print("\t* Apellido:", datos['apellido'][i])
    print("\t* Teléfono:", datos['telefono'][i])
    print("\t* Dirección:", datos['direccion'][i])
    print("\t* Pedido:", datos['pedido'][i])
    print("\t* Total: $", datos['total'][i])

def MostrarDetalle():
    print(" ----- Detalle de un pedido ----- \n")
    print("-----------------------------------")
    pedido = int(input("Ingrese el codigo del pedido: "))

    if pedido in datos['pedido']:
        indice = datos['pedido'].index(pedido)
        print("Detalle del pedido", indice+1)
        print("\n")
        print("Datos del cliente")
        print("\t* Nombre:", datos['nombre'][indice])
        print("\t* Apellido:", datos['apellido'][indice])
        print("\t* Teléfono:", datos['telefono'][indice])
        print("\t* Dirección:", datos['direccion'][indice])
        print("\t* Pedido:", datos['pedido'][indice])
        print("\t* Paquete:", datos['paquete'][indice])
        print("\t* Total:", datos['total'][indice])

    else:
        print(" ******* ERROR *******")
        print("El pedido no existe")

    def EliminarPedido():
        print(" ----- Eliminar un pedido ----- \n")
        print("-----------------------------------")
    pedido = int(input("Ingrese el número de pedido: "))

    if pedido in datos['pedido']:
        indice = datos['pedido'].index(pedido)
        datos['nombre'].pop(indice)
        datos['apellido'].pop(indice)
        datos['telefono'].pop(indice)
        datos['direccion'].pop(indice)
        datos['pedido'].pop(indice)
        datos['paquete'].pop(indice)
        datos['total'].pop(indice)
        print("El pedido ha sido eliminado")

    else:
      print(" ******* ERROR *******")
      print("El pedido no existe")

def main():
    opcion = Menu()
    while opcion != 5:
     if opcion == 1:
        RegistrarPedidos()
     elif opcion == 2:
         MostrarPedidos()
     elif opcion == 3:
        MostrarDetalle()
     elif opcion == 4:
        EliminarPedido()
    opcion = Menu()
    print("Gracias por usar el sistema")

main()