

class Producto:
    def __init__(self, codigo,  nombre, stock, costo, precio):
        """
        Constructor de la clase Producto.

        Parámetros:
        codigo (str): Código del producto.
        nombre (str): Nombre del producto.
        stock (int): Cantidad de stock del producto. No puede ser negativo.
        costo (float): Costo del producto. No puede ser negativo.
        precio (float): Precio de venta del producto. No puede ser negativo.
        """
        self.codigo = codigo
        self.nombre = nombre

        # Validar que el stock no sea negativo
        if stock < 0:
            raise ValueError("El stock no puede ser negativo")
        self.stock = stock

        # Validar que el costo no sea negativo
        if costo < 0:
            raise ValueError("El costo no puede ser negativo")
        self.costo = costo

        # Validar que el precio no sea negativo
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self.precio = precio


# Diccionario de productos con sus respectivos objetos Producto
Productos = {
    1: Producto( "0001","Manzana", 50, 20.0, 40.0),
    2: Producto("0002" ,"Banana", 30, 15.0, 30.0),
    3: Producto("0003" , "Naranja", 40, 18.0, 36.0)
}