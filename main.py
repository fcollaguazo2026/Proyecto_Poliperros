import stdiomask
import random
import subprocess
from prettytable import PrettyTable

# Debe tener 8 listas (índices 0 a 7)
detallaComprasTupla = ([], [], [], [], [], [], [], [])
detalleCompras = list(detallaComprasTupla)

def menu():
    print("¿Qué acción se desea realizar?")
    print('* 1) Registrar pedidos')
    print('* 2) Mostrar pedidos')
    print('* 3) Actualizar pedido')
    print('* 4) Eliminar pedido')
    print('* 5) Salir del sistema')
    return int(input("Ingrese la opción: "))

def registrarPedidos():
    print("Ingresar los datos del cliente")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    telefono = input("Teléfono: ")

    print("Ingresar los datos del Destinatario")
    nombreDestinatario = input("Nombre: ")
    lugarDestinatario = input("Lugar: ")
    celularDestinatario = input("Celular: ")

    detalleCompras[0].append(nombre)
    detalleCompras[1].append(apellido)
    detalleCompras[2].append(telefono)
    detalleCompras[3].append(nombreDestinatario)
    detalleCompras[4].append(lugarDestinatario)
    detalleCompras[5].append(celularDestinatario)

    detalleCompras[6].append(random.randint(1, 1000))

    print("Selecciona el tipo de repartidor")
    print("1) Repartidor Básico")
    print("2) Repartidor Premium")
    print("3) Repartidor VIP")

    opcion = int(input("Ingrese la opción: "))
    
    if opcion == 1:
        detalleCompras[7].append(1.1)
    elif opcion == 2:
        detalleCompras[7].append(2.2)
    elif opcion == 3:
        detalleCompras[7].append(3.3)

    print("Pedido Registrado con Éxito")

def mostrarPedidos(c):
    print("Datos de cliente")
    print("\t\t Nombre cliente: ",detalleCompras[0][c])
    print("\t\t Apellido cliente: ",detalleCompras[1][c])
    print("\t\t Telefono cliente: ",detalleCompras[2][c])

    print("Datos del destinatario")
    print("\t\t Nombre destinatario: ",detalleCompras[3][c])
    print("\t\t Lugar destinatario: ",detalleCompras[4][c])
    print("\t\t Celular destinatario: ",detalleCompras[5][c])

    print("Datos del pedido")
    print("\t\t Codigo del pedido: ",detalleCompras[6][c])
    print("\t\t Coto del pedido: ",detalleCompras[7][c])


def mostrarPedidosTabla(c):
    tabla=PrettyTable()
    tabla.field_names=["Pedido","Detalle"]
    tabla.align="l"
    tabla.add_row(["Nombre cliente",detalleCompras[0][c]])
    tabla.add_row(["Apellido cliente",detalleCompras[1][c]])
    tabla.add_row(["Telefono cliente",detalleCompras[2][c]])
    tabla.add_row(["Nombre destinatario",detalleCompras[3][c]])
    tabla.add_row(["Lugar destinatario",detalleCompras[4][c]])
    tabla.add_row(["Celular destinatario",detalleCompras[5][c]])
    tabla.add_row(["Codigo del pedido",detalleCompras[6][c]])
    tabla.add_row(["Costo del pedido",detalleCompras[7][c]])

    
    print(tabla)



def eliminarPedidos():
    print("Ingrese el codigo para eliminar el pedido")
    codigo=int(input("codigo: "))
    if codigo in detalleCompras[6]:
        codigoFound=detalleCompras[6].index(codigo)
        for f in range(len(detalleCompras)):
            detalleCompras[f].pop(codigoFound)
        print("Pedido eliminado con exito")
    else:
        print("El codigo no existe")



def main():
    opcion = menu()
    while opcion != 5:
        if opcion == 1:
            registrarPedidos()
        elif opcion == 2:
            if len(detalleCompras[0])==0:
                print("No hay pedidos registrados")
            else:
                for c in range(len(detalleCompras[0])):
                    mostrarPedidos(c)
                    mostrarPedidosTabla(c)
        elif opcion == 3:
            print("Actualizar pedido")
        elif opcion == 4:
            if len(detalleCompras[0])==0:
                print("No hay pedidos registrados")
            else:
              eliminarPedidos()

        opcion = menu()

    print("Muchas Gracias")
main()