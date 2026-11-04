import random
from validaciones import validar_pedir_eleccion,pedir_eleccion

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
                        numero = int(input("Que numero es del 1 al 10 ?: "))
                        
                        if numero == facil:
                            print("Ganaste")
                            break
                        else:
                            print(f"Ese no es, te quedan {intentos-1} intentos")
                            intentos -=1

                        if intentos < 1 :   
                            print("Ya no tienes mas intentos")
                

                if eleccion == "medio":
                    medio = random.randint(1,50)
                    intentos = 4
                    while intentos > 0 :
                        numero = int(input("Que numero es del 1 al 50 ?: "))

                        if numero == medio:
                            print("Ganaste")
                            break
                        else:
                            print(f"Ese no es, te quedan {intentos-1} intentos")
                            intentos-=1

                        if intentos < 1 :
                            print("Perdiste")
                

                if eleccion == "dificil":
                    dificil = random.randint(1,100)
                    intentos = 2    
                    while intentos > 0 :
                        numero = int(input("Que numero es del 1 al 100?: "))
            
                        if numero == dificil:
                            print("Ganaste")
                            break
                        else:
                            print(f"Ese no es, te quedan {intentos-1} intentos")
                            intentos -=1

                        if intentos < 1 :
                            print("Perdiste")
                

                print("Deseas volver a jugar?: ""\n","Deseas sair?: ")
                eleccion_2 = str(input("Que deseas hacer: "))

                if eleccion_2 == "salir":
                    print("Gracias por jugar")
                    break
        
mostrar_menu()            


