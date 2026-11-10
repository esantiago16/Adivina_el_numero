import random

from validaciones import (
    pedir_numero_dificil,
    pedir_numero_facil,
    pedir_numero_medio,
    validar_pedir_numero,
)


def nivel_facil():
    facil = random.randint(1,10)
    intentos = 6    
    while intentos > 0 :
        numero = pedir_numero_facil()
        if not validar_pedir_numero(numero, 1, 10):
            print("Numero fuera de rango, vuelve a intentarlo")
            continue

        if numero == facil:
            print("Ganaste")
            break
        else:
            print(f"Ese no es, te quedan {intentos-1} intentos")
            intentos -=1

        if intentos < 1 :   
            print("Perdiste,ya no tienes mas intentos")

def nivel_medio():
    medio = random.randint(1,50)
    intentos = 4
    while intentos > 0 :
        numero = pedir_numero_medio()
        if not validar_pedir_numero(numero, 1, 50):
            print("Numero fuera de rango, vuelve a intentarlo")
            continue

        if numero == medio:
            print("Ganaste")
            break
        else:
            print(f"Ese no es, te quedan {intentos-1} intentos")
            intentos-=1

        if intentos < 1 :
            print("Perdiste,ya no tienes mas intentos")

def nivel_dificil():
    dificil = random.randint(1,100)
    intentos = 2    
    while intentos > 0 :
        numero = pedir_numero_dificil()
        if not validar_pedir_numero(numero, 1, 100):
            print("Numero fuera de rango, vuelve a intentarlo")
            continue

        if numero == dificil:
            print("Ganaste")
            break
        else:
            print(f"Ese no es, te quedan {intentos-1} intentos")
            intentos -=1

        if intentos < 1 :
            print("Perdiste,ya no tienes mas intentos")