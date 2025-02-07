from db import Producto,Productos

def mostrar_productos():
    # Imprimir la lista de productos disponibles
    print("Lista de productos")
    for id, producto in Productos.items():
        print (f"ID: {id}|Codigo: {producto.codigo} | Nombre: {producto.nombre} | Costo: ${producto.costo} | Precio: ${producto.precio} | Stock: {producto.stock}")

def agregar_productos_inventario():
    # Generar un nuevo código para el producto
    codigo = str(max(Productos.keys()) + 1).zfill(4)

    # Solicitar el nombre del nuevo producto
    nombre = (input("Seleccione el nombre del producto: "))

    # Verificar si el producto ya existe en el inventario
    if any(producto.nombre == nombre for producto in Productos.values()):
        print(f"El producto '{nombre}' ya existe en el inventario.")
        return  # Termina la función si el producto ya existe

    # Solicitar los detalles del nuevo producto
    stock = int(input("Seleccione el stock del producto: "))
    costo = float(input("Seleccione el costo del producto: "))
    precio = float(input("Seleccione el precio del producto: "))

    # Crear un nuevo producto y añadirlo al inventario
    nuevo_id = max(Productos.keys()) + 1
    nuevo_producto = Producto(codigo ,nombre, stock, costo, precio)
    print(f"|Codigo: {nuevo_producto.codigo} | Nombre: {nuevo_producto.nombre} | Costo: ${nuevo_producto.costo} | Precio: ${nuevo_producto.precio} | Stock: {nuevo_producto.stock}")

    # Confirmar la adición del nuevo producto
    confirmacion = input("¿Confirmar? Si/No: ")
    if confirmacion == "Si":
        Productos[nuevo_id] = nuevo_producto
    else:
        return

def quitar_productos_inventario():
    # Solicitar el código del producto a eliminar
    producto_quitado = Productos.pop(int(input("Escriba el codigo del producto a eliminar: ")))
    print(f"El producto ha sido quitado correctamente... {producto_quitado.nombre} es el producto eliminado")


def actualizar_stock(id, nuevo_stock, eleccion):
    # Actualizar el stock del producto según la elección del usuario
    if eleccion == "agregar":
        Productos[id].stock += nuevo_stock
        print(f"El nuevo stock del producto {Productos[id].nombre} es de: {Productos[id].stock}")
    elif eleccion == "quitar" and nuevo_stock <  Productos[id].stock:
        Productos[id].stock -= nuevo_stock
        print(f"El nuevo stock del producto {Productos[id].nombre} es de: {Productos[id].stock}")
    else:
        print(f"El stock no puede ser negativo, stock atual {Productos[id].stock}")