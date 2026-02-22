carrito = {}
def agregar_producto():
    nombre = input("ingrese el nombre del producto: ").capitalize()    
    try:
        precio = float(input("ingrese el precio del producto: "))
        if precio <= 0:
            print("el precio debe ser mayor que cero.")
            return
        carrito[nombre] = precio
        print(f"producto '{nombre}' agregado correctamente.")
    except ValueError:
        print("debe ingresar un valor numerico valido para el precio.")
def eliminar_producto():
    nombre = input("ingrese el nombre del producto a eliminar: ").capitalize()
    if nombre in carrito:
        del carrito[nombre]
        print(f"producto '{nombre}' eliminado correctamente.")
    else:
        print("el producto no se encuentra en el carrito.")
def mostrar_carrito():
    if not carrito:
        print("el carrito esta vacío.")
        return
    print("\n productos en el carrito:")
    total = 0
    for producto, precio in carrito.items():
        print(f"- {producto}: ${precio:.2f}")
        total += precio    
    print(f"\n total a pagar: ${total:.2f}")
def menu():
    while True:
        print("\n carrito de compras ")
        print("1. agregar producto")
        print("2. eliminar producto")
        print("3. mostrar carrito")
        print("4. salir")
        opcion = input("seleccione una opcion: ")
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            eliminar_producto()
        elif opcion == "3":
            mostrar_carrito()
        elif opcion == "4":
            print("gracias por usar el carrito de compras.")
            break
        else:
            print("opcion invalida, intente nuevamente.")
menu()