
from datetime import datetime
from db import Producto, Productos
contador_diario = 0

def registrar_venta():
    entrada_productos_comprado = " "
    productos_a_comprar = []
    codigo_cantidad = []
    codigo_producto_comprado = 0
    cantidad_producto_comprado = 0
    total_a_pagar = 0
    lista_compras  = []

    print("LISTA DE PRODUCTOS")
    print("------------------")
    for id, producto in Productos.items():
        print (f"ID: {id} | Nombre: {producto.nombre} | Costo: ${producto.costo} | Precio: ${producto.precio} | Stock: {producto.stock}")
    print("------------------")

    entrada_productos_comprado = input("Ingrese el codigo del producto y su cantidad separado con coma y por cada producto y cantidad separelo con guón ej: 1-2,2-20,3-50: ")

    productos_a_comprar = entrada_productos_comprado.split(",")

    for producto in productos_a_comprar:
        codigo_cantidad = producto.split("-")
        codigo_producto_comprado = int(codigo_cantidad[0])
        cantidad_producto_comprado = int(codigo_cantidad[1])


        if cantidad_producto_comprado <=  Productos[codigo_producto_comprado].stock:
            lista_compras.append((Productos[codigo_producto_comprado].nombre, cantidad_producto_comprado))
            Productos[codigo_producto_comprado].stock -= cantidad_producto_comprado
            total_a_pagar += Productos[codigo_producto_comprado].precio * cantidad_producto_comprado
        else:
            print(f"Lo sentimos, stock insuficiente del producto {Productos[codigo_producto_comprado].nombre}")

    id_venta = generar_id_venta()
    fecha = datetime.now().strftime("%d de %B de %Y")
    print("------------------------------------------")
    print(f"ID COMPRA: {id_venta} FECHA: {fecha}")
    print("------------------------------------------")
    print(f"Productos comprados {lista_compras}")
    print("------------------------------------------")
    print(f"Total a pagar {total_a_pagar}")



def generar_id_venta():
    global contador_diario
    fecha = datetime.now().strftime("%Y%m%d")  # Formato YYYYMMDD
    contador_diario += 1
    return f"{fecha}-{contador_diario:03}"  # Ejemplo: 20241223-001