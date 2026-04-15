import os

carrito = []
listado = True
nombre = input("¿Cuál es tu nombre?: ")
print("¡Hola " + nombre + " estas dentro del carrito virtual!")
print("\n--FUNCIONES--")
print("\n1. Añadir producto")
print("2. Eliminar producto")
print("3. Generar archivo .txt en el escritorio")
print("4. Salir del carrito virtual")
while listado == True:
    try:
        opcion = int(input("\n¿Qué quieres hacer?: "))
    except ValueError:
        print("\nDigitaste mal la opción que quieres realizar")
        continue
    if opcion == 1:
        print("\n¿Qué producto deseas añadir? (Cuando termines escribe -fin- para ver como quedó tu lista): ")
        añadiendo = True
        while añadiendo == True:
            añadir = input().lower()
            carrito.append(añadir)
            if añadir.lower() == "fin":
                carrito.remove("fin")
                print("así quedó tu lista" + str(carrito))
                break
                añadiendo = False
    elif opcion == 2:
        eliminar = input("\n¿Qué producto deseas eliminar?: ").lower()
        carrito.remove(eliminar)
        print("así quedó tu lista" + str(carrito))
    elif opcion == 3:
        ruta = os.path.join(os.path.expanduser("~"), "Desktop", "mi_lista.txt")
        try:
            with open(ruta, "w") as archivo:
                archivo.write("---LISTA DE COMPRAS---\n")
                archivo.write("¡"+ nombre + " esta es tu lista de compras para esta semana!\n")
                for item in carrito:
                    archivo.write(f"{item.capitalize()}\n")
            print(f"Archivo guardado con éxito como 'mi lista.txt'")
        except Exception as e:
                print(f"Error al guardar el archivo")
    elif opcion == 4:
        print("Saliste del carrito virtual")
        listado = False

