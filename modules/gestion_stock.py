from db import Producto,Productos

def mostrar_productos():
    print("Lista de productos")
    for id, producto in Productos.items():
        print (f"ID: {id}|Codigo: {producto.codigo} | Nombre: {producto.nombre} | Costo: ${producto.costo} | Precio: ${producto.precio} | Stock: {producto.stock}")


def agregar_productos_inventario():

    codigo = str(max(Productos.keys()) + 1).zfill(4)
    nombre = (input("Seleccione el nombre del producto: "))
    if any(producto.nombre == nombre for producto in Productos.values()):
        print(f"El producto '{nombre}' ya existe en el inventario.")
        return  # Termina la función si el producto ya existe

    stock = int(input("Seleccione el stock del producto: "))
    costo = float(input("Seleccione el costo del producto: "))
    precio = float(input("Seleccione el precio del producto: "))
    nuevo_id = max(Productos.keys()) + 1
    nuevo_producto = Producto(codigo ,nombre, stock, costo, precio)
    print(f"|Codigo: {nuevo_producto.codigo} | Nombre: {nuevo_producto.nombre} | Costo: ${nuevo_producto.costo} | Precio: ${nuevo_producto.precio} | Stock: {nuevo_producto.stock}")
    confirmacion = input("¿Confirmar? Si/No: ")
    if confirmacion == "Si":
        Productos[nuevo_id] = nuevo_producto
    else:
        return

def quitar_productos_inventario():
    producto_quitado = Productos.pop(int(input("Escriba el codigo del producto a eliminar: ")))
    print(f"El producto ha sido quitado correctamente... {producto_quitado.nombre} es el producto eliminado")


def actualizar_stock(id, nuevo_stock, eleccion):
    if eleccion == "agregar":
        Productos[id].stock += nuevo_stock
        print(f"El nuevo stock del producto {Productos[id].nombre} es de: {Productos[id].stock}")
    elif eleccion == "quitar" and nuevo_stock <  Productos[id].stock:
        Productos[id].stock -= nuevo_stock
        print(f"El nuevo stock del producto {Productos[id].nombre} es de: {Productos[id].stock}")
    else:
        print(f"El stock no puede ser negativo, stock atual {Productos[id].stock}")