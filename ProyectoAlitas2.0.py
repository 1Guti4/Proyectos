#ProyectoAlitas 2.0
#precios:

precios = {"alitas_p": float(1800), "kilos_p": float(13500), "paquetes_p": float(27000)}

print("""------------ M E N Ú -----------------

        1. Calcular número de alitas
        2. Calcular número de kilos
        3. Calcular número de paquetes
        4. Salir
--------------------------------------\n""")

    
def conversion_alitas():
    alitas = float(input("\nIntroduce el número de alitas: "))
    alitas_k= 2*alitas/15
    alitas_p= alitas/15
    p_a= alitas*precios["alitas_p"]
    print(f"{alitas} alitas son {alitas_k} kilos\n")
    print(f"{alitas} alitas son {alitas_p} paquetes\n")
    print(f"En precio {alitas} alitas son {p_a} pesos")
    
def conversion_kilos():
    kilos = float(input("\nIntroduce el número de kilos: "))
    kilos_a= 15*kilos/2
    kilos_p= kilos/2
    p_k= kilos*precios["kilos_p"]
    print(f"{kilos} kilos son {kilos_a} alitas\n")
    print(f"{kilos} kilos son {kilos_p} paquetes\n")
    print(f"En precio {kilos} kilos son {p_k} pesos")
    
def conversion_paquetes():
    paquetes = float(input("\nIntroduce el número de paquetes: "))
    paquetes_a= 15*paquetes
    paquetes_k= 2*paquetes
    p_p= paquetes*precios["paquetes_p"]
    print(f"{paquetes} paquetes son {paquetes_a} alitas\n")
    print(f"{paquetes} paquetes son {paquetes_k} kilos\n")
    print(f"En precio {paquetes} paquetes son {p_p} pesos")

inicio = True

while inicio==True:
    try:
        opcion = int(input("\n¿Qué deseas hacer?(Digita: |1|2|3|4|): "))
    except ValueError:
        print("\nNo digitaste una opción válida del menú, ¡vuelve a intentarlo!\n")
        continue
    if opcion == 1:
        conversion_alitas()
    elif opcion == 2:
        conversion_kilos()
    elif opcion == 3:
        conversion_paquetes()
    elif opcion == 4:
        print("Saliste correctamente")
        inicio = False
    else:
        print("\nNo digitaste una opción válida del menú, ¡vuelve a intentarlo!\n")
