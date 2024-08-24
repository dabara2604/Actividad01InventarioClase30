inventario = [{"nombre":"McFlury", "precio":2.50, "stok":10}]

def menu_principal():
    """
    Muestra el menú menu principal
    """
    while True:
        print("Menú Principal")
        print("1. agregar producto")
        print("2. Mostrar Inventario")
        print("3. Vender Producto")
        print("4. Salir")

        opcion = input("Señeccion un opción: ")

        if opcion =="1":
            agregar_producto()
        elif opcion == "2":
            mostrar_invertario()
        elif opcion == "3":
            vender_producto()
        elif opcion == "4":
            break
        else:
            print("Opción no válidad. Por favor intente otra vez")

def agregar_producto():
    """
    Agregar un nuevo producto al inventario
    """

    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Infrese el precio del procudto: "))
    cantidad = int(input("Infrese la cantidad del preducto: "))

    producto = {"nombre": monbre, "precio": precio, "stock": cantidad}

    inventario.append(producto)

    print(f"Producto {nombre} agregado al inventario")

def mostrar_invertario():
    """
    Muestra todas los productos del inventario
    """

    if len(inventario) == 0:
        print("El inventario está vacio")
    else:
        print("Presentando Inventario")

        for producto in inventario:
            print(f"Nombre:¨{producto['nombre']}, Precio: {producto['precio']:.2f}, Cantidad: {producto['Stock']}")

def vender_producto():
    """
    Vender un producto; actualiza el inventario y muestra el otro de la vemta
    """
    nombre = input("Ingrese el monbre del producto que desea vender: ")

    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower()():
            cantidad = int(input(f"¿Cuantas unidades de {nombre} desea vender?: "))
            if cantidad <= producto["stock"]:
                producto["stock"] -= cantidad
                total (f"Venta realizada. Total: ${total:.2f}")

            if producto["stock"] == 0:
                print(f"El producto {nombre} se ha agotado. ")

            ruturn
        else:
            print("No hay suficiente Stock en INventario")
            return
        
    print("producto no encotrado en el invetario")


#menu_principal