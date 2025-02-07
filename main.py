import sys
import os

# Agregar el directorio 'modules' al PATH del sistema
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))

# Importar funciones de otros módulos
from gestion_stock import agregar_productos_inventario, mostrar_productos, quitar_productos_inventario, actualizar_stock
from gestion_ventas import registrar_venta
from menus import mostrar_menu_principal
from db import Productos

# Bucle principal del programa
while True:

    # Mostrar el menú principal y obtener la opción elegida por el usuario
    opcion_elegida = mostrar_menu_principal()
    opcion_elegida = mostrar_menu_principal()

    if opcion_elegida == 1:
        # Registrar una nueva venta
        registrar_venta()

    elif opcion_elegida == 2:
        # Mostrar todos los productos 
        mostrar_productos()

    elif opcion_elegida == 3:
        # Listar productos con detalles
        for id, producto in Productos.items():
            print (f"ID: {id}|Codigo: {producto.codigo} | Nombre: {producto.nombre} | Costo: ${producto.costo} | Precio: ${producto.precio} | Stock: {producto.stock}")

        # Obtener ID del producto y confirmar selección
        id = int(input("Ingresar el ID del producto: "))
        confirmacion = input(f"El producto elegido es: {Productos[id].nombre}, desea continuar: si/no: ")

        if confirmacion == "si":
            if id in Productos:
                # Obtener la acción deseada (agregar/quitar) y la cantidad de stock a modificar
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

    elif opcion_elegida == 4:
        # Agregar un nuevo producto al inventario
        agregar_productos_inventario()

    elif opcion_elegida == 5:
        # Quitar un producto del inventario
        quitar_productos_inventario()

    elif opcion_elegida == 6:
        # Salir del bucle principal y terminar el programa
        break


