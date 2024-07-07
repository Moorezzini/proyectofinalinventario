# main.py

import funciones

productos = [
    {"nombre": "Vape Sabor Menta", "cantidad": 10, "precio": 10.0},
    {"nombre": "Vape Sabor Fresa", "cantidad": 10, "precio": 10.0},
    {"nombre": "Vape Sabor Mango", "cantidad": 10, "precio": 10.0},
    {"nombre": "Vape Sabor Uva", "cantidad": 10, "precio": 10.0},
    {"nombre": "Vape Sabor Sandia", "cantidad": 10, "precio": 10.0},
    {"nombre": "Vape Sabor Piña", "cantidad": 10, "precio": 10.0},
    {"nombre": "Vape Sabor Limón", "cantidad": 10, "precio": 10.0},
    {"nombre": "Vape Sabor Coco", "cantidad": 10, "precio": 10.0},
    {"nombre": "Vape Sabor Naranja", "cantidad": 10, "precio": 10.0},
    {"nombre": "Vape Sabor Plátano", "cantidad": 10, "precio": 10.0}
]

num_productos = len(productos)

while True:
    print("\nSistema de Inventarios")
    print("1. Ingresar producto")
    print("2. Editar producto")
    print("3. Eliminar producto")
    print("4. Listar productos")
    print("5. Comprar productos")
    print("6. Control de inventario")
    print("7. Salir")
    opcion = int(input("Seleccionar una opción: "))

    if opcion == 1:
        funciones.ingresar_producto(productos, num_productos)
        num_productos += 1
    elif opcion == 2:
        funciones.editar_producto(productos, num_productos)
    elif opcion == 3:
        funciones.eliminar_producto(productos, num_productos)
        num_productos -= 1
    elif opcion == 4:
        funciones.listar_productos(productos, num_productos)
    elif opcion == 5:
        funciones.comprar_productos(productos, num_productos)
    elif opcion == 6:
        funciones.control_de_inventario(productos, num_productos)
    elif opcion == 7:
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida.")