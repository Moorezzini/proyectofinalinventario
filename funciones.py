# funciones.py

def ingresar_producto(productos, num_productos):
    if num_productos >= 100:
        print("No se pueden agregar más productos.")
        return

    nombre = input("Ingresar nombre del producto: ")
    cantidad = int(input("Ingresar cantidad del producto: "))
    precio = float(input("Ingresar precio del producto: "))

    productos.append({"nombre": nombre, "cantidad": cantidad, "precio": precio})
    num_productos += 1

def editar_producto(productos, num_productos):
    nombre = input("Ingresar nombre del producto a editar: ")

    for producto in productos:
        if producto["nombre"] == nombre:
            cantidad = int(input("Ingresar nueva cantidad del producto: "))
            precio = float(input("Ingresar nuevo precio del producto: "))
            producto["cantidad"] = cantidad
            producto["precio"] = precio
            return

    print("Producto no encontrado.")

def eliminar_producto(productos, num_productos):
    nombre = input("Ingresar nombre del producto a eliminar: ")

    for i, producto in enumerate(productos):
        if producto["nombre"] == nombre:
            del productos[i]
            num_productos -= 1
            print("Producto eliminado.")
            return

    print("Producto no encontrado.")

def listar_productos(productos, num_productos):
    if num_productos == 0:
        print("No hay productos para listar.")
        return

    print("Listado de productos:")
    for producto in productos:
        print(f"Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio: {producto['precio']}")

def comprar_productos(productos, num_productos):
    total_productos_comprados = 0
    total_precio = 0.0

    while True:
        nombre = input("Ingresar nombre del producto a comprar (o 'fin' para terminar): ")

        if nombre == "fin":
            break

        for producto in productos:
            if producto["nombre"] == nombre:
                cantidad = int(input("Ingresar cantidad a comprar: "))
                if producto["cantidad"] < cantidad:
                    print("No hay suficiente stock del producto.")
                    break

                producto["cantidad"] -=cantidad
                total_productos_comprados += cantidad
                total_precio += producto["precio"] * cantidad
                break

        if total_productos_comprados > 6:
            total_precio *= 0.8

        es_estudiante_udla = input("¿Eres estudiante de la UDLA? (sí/no): ")
        if es_estudiante_udla.lower() == "sí" or es_estudiante_udla.lower() == "si":
            total_precio *= 0.9

    print(f"Total de productos comprados: {total_productos_comprados}")
    print(f"Precio total: ${total_precio:.2f}")

def control_de_inventario(productos, num_productos):
    password = int(input("Digite la contraseña: "))

    if password == 1234:
        while True:
            print("Control de Inventario")
            print("1. Chequeo de inventario")
            print("2. Agregar productos mensuales")
            print("3. Salir")
            opcion = int(input("Seleccionar una opción: "))

            if opcion == 1:
                chequeo_de_inventario(productos, num_productos)
            elif opcion == 2:
                agregar_productos_mensuales(productos, num_productos)
            elif opcion == 3:
                print("Saliendo del control de inventario...")
                break
            else:
                print("Opción no válida.")
    else:
        print("Contraseña incorrecta.")

def chequeo_de_inventario(productos, num_productos):
    total_vapes = 0
    print("Chequeo de inventario:")
    for producto in productos:
        print(f"Nombre: {producto['nombre']}, Cantidad restante: {producto['cantidad']}")
        total_vapes += producto["cantidad"]
    print(f"Número total de vapes restantes: {total_vapes}")

def agregar_productos_mensuales(productos, num_productos):
    for producto in productos:
        producto["cantidad"] += 10
    print("El producto mensual se ha agregado.")