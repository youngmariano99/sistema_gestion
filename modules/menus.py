
def mostrar_menu_principal():
    menu ="""
    Eliga una opción:
    Opción 1: Registrar venta
    Opción 2: Mostrar stock
    Opción 3: Actualizar Stock
    Opción 4: Agregar producto
    Opción 5: Quitar producto
    Opción 6: Salir
    """
    print(menu)
    opcion_elegida = int(input("Opción elegida: "))
    return opcion_elegida