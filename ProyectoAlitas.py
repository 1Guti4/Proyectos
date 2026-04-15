p_alitas = 1800 
p_kilos = 13500
p_paquete = 27000
paquete = 1

print("---MENÚ DE OPCIONES---\n")
print("1. Para calcular la cantidad de paquetes de acuerdo al número de kilos")
print("2. Para calcular la cantidad de kilos de acuerdo al número de paquetes")
print("3. Para calcular la cantidad de alitas de acuerdo al número de kilos")
print("4. Para calcular la cantidad de kilos de acuerdo al número de alitas")
print("5. Para calcular la cantidad de paquetes de acuerdo al número de alitas")
print("6. Para calcular la cantidad de alitas de acuerdo al número de paquetes")
print("7. Salir")

iniciar = True

while iniciar == True:
    try:
        opcion = int(input("\nDigita el número de opción del cálculo que deseas realizar: "))
    except ValueError:
        print("\nNo digitaste un valor númerico, ¡vuelve a intentarlo!")
        continue
    if opcion == 1:
        c_kilos = float(input("\nDigita la cantidad de kilos: "))
        n_paquetes = c_kilos/2
        print(str(c_kilos) + " kilos son " + str(n_paquetes) + " paquetes")
        print("\n¿Quieres saber la equivalencia en pesos de esta conversión? Escribe('si' o 'no'): ")
        eleccion = str(input()).lower()
        if eleccion == "si":
            precio_p = p_paquete * n_paquetes
            print(str(c_kilos) + " kilos equivalen a " + str(precio_p) + " pesos en paquetes\n")
        else:
            continue
    elif opcion == 2:
        c_paquetes = float(input("\nDigita la cantidad de paquetes: "))
        n_kilos = 2 * c_paquetes
        print(str(c_paquetes) + " paquetes son " + str(n_kilos) + " kilos\n")
        print("\n¿Quieres saber la equivalencia en pesos de esta conversión? Escribe('si' o 'no'): ")
        eleccion = str(input()).lower()
        if eleccion == "si":
            precio_k = p_kilos * n_kilos
            print(str(c_paquetes) + " paquetes equivalen a " + str(precio_k) + " pesos en kilos\n")
        else:
            continue
    elif opcion == 3:
        c_kilos= float(input("\nDigita la cantidad de kilos: "))
        n_alitas= 15 * c_kilos/2
        print(str(c_kilos) + " kilos son " + str(n_alitas) + " alitas")
        print("\n¿Quieres saber la equivalencia en pesos de esta conversión? Escribe('si' o 'no'): ")
        eleccion = str(input()).lower()
        if eleccion == "si":
            precio_a = p_alitas * n_alitas
            print(str(c_kilos) + " kilos equivalen a " + str(precio_a) + " pesos en alitas\n")
        else:
            continue
    elif opcion == 4:
        c_alitas = float(input("\nDigita la cantidad de alitas: "))
        n_kilos = 2* c_alitas/15
        print(str(c_alitas) + " alitas son " + str(n_kilos)+ " kilos")
        print("\n¿Quieres saber la equivalencia en pesos de esta conversión? Escribe('si' o 'no'): ")
        eleccion = str(input()).lower()
        if eleccion == "si":
            precio_k = p_kilos * n_kilos
            print(str(c_alitas) + " alitas equivalen a " + str(precio_k) + " pesos en kilos\n")
        else:
            continue
    elif opcion == 5:
        c_alitas= float(input("\nDigita la cantidad de alitas: "))
        n_paquetes = c_alitas/15
        print(str(c_alitas) + " alitas son " + str(n_paquetes) + " paquetes")
        print("\n¿Quieres saber la equivalencia en pesos de esta conversión? Escribe('si' o 'no'): ")
        eleccion = str(input()).lower()
        if eleccion == "si":
            precio_p = p_paquete * n_paquetes
            print(str(c_alitas) + " alitas equivalen a " + str(precio_p) + " pesos en paquetes\n")
        else:
            continue
    elif opcion == 6:
        c_paquetes = float(input("\nDigita la cantidad de paquetes: "))
        n_alitas = 15 * c_paquetes
        print(str(c_paquetes) + " paquetes son " + str(n_alitas) + " alitas")
        print("\n¿Quieres saber la equivalencia en pesos de esta conversión? Escribe('si' o 'no'): ")
        eleccion = str(input()).lower()
        if eleccion == "si":
            precio_a = p_alitas * n_alitas
            print(str(c_paquetes) + " paquetes equivalen a " + str(precio_a) + " pesos en alitas\n")
        else:
            continue
    elif opcion == 7:
        print("\nSaliste del sistema correctamente")
        iniciar = False
    elif opcion != [1,7]:
        print("Oigan a este, ¿no estas viendo que son solo 7 opciones? ¿de donde me saco la " + str(opcion)+ "?")
