

class Producto:
    def __init__(self, codigo,  nombre, stock, costo, precio):

        self.codigo = codigo
        self.nombre = nombre
        if stock < 0:
            raise ValueError("El stock no puede ser negativo")
        self.stock = stock
        if costo < 0:
            raise ValueError("El costo no puede ser negativo")
        self.costo = costo
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self.precio = precio



Productos = {
    1: Producto( "0001","Manzana", 50, 20.0, 40.0),
    2: Producto("0002" ,"Banana", 30, 15.0, 30.0),
    3: Producto("0003" , "Naranja", 40, 18.0, 36.0)
}