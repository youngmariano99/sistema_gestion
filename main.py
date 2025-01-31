import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))

from gestion_stock import agregar_productos_inventario, mostrar_productos, quitar_productos_inventario, actualizar_stock
from gestion_ventas import registrar_venta
from menus import mostrar_menu_principal
from db import Productos

while True:
    #Esta función nos muestra el menú principal y nos retorna un numero entero según la opción elegida por el cliente 

    opcion_elegida = mostrar_menu_principal()

    if opcion_elegida == 1:
        # Esta función nos permite registrar una nueva venta 
        registrar_venta()

    if opcion_elegida == 2:
        #Esta función nos permite mostrar todos los productos 
        mostrar_productos()

    if opcion_elegida == 3:
        for id, producto in Productos.items():
            print (f"ID: {id}|Codigo: {producto.codigo} | Nombre: {producto.nombre} | Costo: ${producto.costo} | Precio: ${producto.precio} | Stock: {producto.stock}")
        id = int(input("Ingresar el ID del producto: "))
        confirmacion = input(f"El producto elegido es: {Productos[id].nombre}, desea continuar: si/no: ")
        if confirmacion == "si":
            if id in Productos:
                eleccion = input("que desea hacer: agregar/quitar: ")
                if eleccion == "agregar" or eleccion == "quitar":
                    print(f"El stock del producto {Productos[id].nombre} es {Productos[id].stock}")
                    nuevo_stock = int(input("Ingrese la cantidad de stock que desea agregar/quitar: "))
                    actualizar_stock(id, nuevo_stock, eleccion)
                else:
                    print("error: opción no disponible")
                    print("Ingrese una elección correcta agregar/quitar")
            else:
                print("El producto no existe")

    if opcion_elegida == 4:
     #Esta función nos permite agregar un nuevo producto al inventario
        agregar_productos_inventario()

    if opcion_elegida == 5:
        #Esta función nos permite quitar un nuevo producto al inventario
        quitar_productos_inventario()

    if opcion_elegida == 6:
        break


