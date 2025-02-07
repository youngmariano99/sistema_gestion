
from datetime import datetime
from db import Producto, Productos
# Variable global para llevar el contador diario de ventas
contador_diario = 0

def registrar_venta():
    # Inicialización de variables
    entrada_productos_comprado = " "
    productos_a_comprar = []
    codigo_cantidad = []
    codigo_producto_comprado = 0
    cantidad_producto_comprado = 0
    total_a_pagar = 0
    lista_compras  = []

    # Mostrar la lista de productos disponibles
    print("LISTA DE PRODUCTOS")
    print("------------------")
    for id, producto in Productos.items():
        print (f"ID: {id} | Nombre: {producto.nombre} | Costo: ${producto.costo} | Precio: ${producto.precio} | Stock: {producto.stock}")
    print("------------------")

    # Solicitar al usuario que ingrese los productos a comprar y sus cantidades
    entrada_productos_comprado = input("Ingrese el codigo del producto y su cantidad separado con coma y por cada producto y cantidad separelo con guón ej: 1-2,2-20,3-50: ")

    # Dividir la entrada en una lista de productos
    productos_a_comprar = entrada_productos_comprado.split(",")

    # Procesar cada producto ingresado
    for producto in productos_a_comprar:
        codigo_cantidad = producto.split("-")
        codigo_producto_comprado = int(codigo_cantidad[0])
        cantidad_producto_comprado = int(codigo_cantidad[1])


        if cantidad_producto_comprado <=  Productos[codigo_producto_comprado].stock:
            # Dividir el código y la cantidad del producto
            lista_compras.append((Productos[codigo_producto_comprado].nombre, cantidad_producto_comprado))
            Productos[codigo_producto_comprado].stock -= cantidad_producto_comprado
            total_a_pagar += Productos[codigo_producto_comprado].precio * cantidad_producto_comprado
        else:
            # Informar al usuario sobre la falta de stock
            print(f"Lo sentimos, stock insuficiente del producto {Productos[codigo_producto_comprado].nombre}")

    # Generar un ID de venta único
    id_venta = generar_id_venta()
    fecha = datetime.now().strftime("%d de %B de %Y")

    # Mostrar los detalles de la compra
    print("------------------------------------------")
    print(f"ID COMPRA: {id_venta} FECHA: {fecha}")
    print("------------------------------------------")
    print(f"Productos comprados {lista_compras}")
    print("------------------------------------------")
    print(f"Total a pagar {total_a_pagar}")



def generar_id_venta():
    global contador_diario
    # Generar un ID de venta basado en la fecha y un contador diario
    fecha = datetime.now().strftime("%Y%m%d")  # Formato YYYYMMDD
    contador_diario += 1
    return f"{fecha}-{contador_diario:03}"  # Ejemplo: 20241223-001