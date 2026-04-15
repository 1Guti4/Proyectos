nombre = input("Ingresa tu nombre: ")
saldo = 50000
encendercajero = True

while encendercajero == True:
    print("\n Bienvenido " + nombre)
    print("\n--- Cajero Automatico ---")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Salir")
    eleccion = input("¿Que quieres hacer?: " )

    if eleccion == "1":
        print("\nTu saldo es de " + str(saldo))
    elif eleccion == "2":
        retiro = int(input("Ingresa el valor a retirar: "))
        if retiro <= saldo:
         print("\nHas retirado " + str(retiro) + " de manera exitosa")
         saldo = saldo - retiro
        else:
            print("\nSaldo insuficiente")
    elif eleccion == "3":
        deposito = int(input("Ingresa el valor a depositar: "))
        print("\nHas depositado " + str(deposito) + " de manera exitosa")
        saldo = saldo + deposito
    elif eleccion == "4":
        print("\nHas salido del sistema ¡gracias " + nombre + " por preferirnos!")
        encendercajero = False
    else:
        print("\nOpción Inválida")
        
