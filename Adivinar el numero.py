import random

numero = random.randint(0,100)
inicio = True
nombre = input ("Hola, ¿Cuál es tu nombre?: ")
print(" Muy bien " + str(nombre) + " adivina el número entero del 0 al 100")
intentos = 0

while inicio == True:
    try:
        numeroelegido = int(input("\nDigita un número entero: "))
    except ValueError:
        print("\nNo digitaste un número entero, ¡vuelve a intentarlo!")
        continue
    if numeroelegido > numero:
        print("\n¡Más abajo!")
        intentos += 1
    elif numeroelegido < numero:
        print("\n¡Más arriba!")
        intentos += 1
    elif numeroelegido == numero:
        print("¡Muy bien " + nombre + ", acertaste! el número entero era: " + str(numero) + " y lo adivinaste en " + str(intentos)+ " intentos")
        inicio = False
