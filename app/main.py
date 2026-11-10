import random

from validaciones import (
        pedir_eleccion,
        pedir_numero_dificil,
        pedir_numero_facil,
        pedir_numero_medio,
        pedir_reintento,
        validar_pedir_eleccion,
        validar_pedir_numero,
)


def mostrar_menu():
        print("¡¡¡¡¡¡Bienvenido a Adivina el numero!!!!!")
        while True:
                
                print("Dificultades","\n","Facil ","\n","Medio""\n","Dificil")
                eleccion = pedir_eleccion()
                if not validar_pedir_eleccion(eleccion):
                    print("Esa dificultad no existe, vuelve a elegir")
                    continue

                if eleccion == "facil":
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
                

                if eleccion == "medio":
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
                

                if eleccion == "dificil":
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
                

                eleccion_2 =pedir_reintento()
                while eleccion_2 not in ["jugar", "salir"]:
                    print("Esa opcion no existe, vuelve a elegir")
                    eleccion_2 = pedir_reintento()
                if eleccion_2 == "jugar":
                    continue
                if eleccion_2 == "salir":
                        print("Gracias por jugar, hasta la proxima")
                        return
mostrar_menu()    





