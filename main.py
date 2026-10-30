import random


dificultades = [
    {"nombre": "facil", "intentos": 6},
    {"nombre": "medio", "intentos": 4},
    {"nombre": "dificil", "intentos": 2}
]

def mostrar_menu():
    print("¡¡¡¡¡¡Bienvenido a Adivina el numero!!!!!")
    print("Dificultades","\n","Facil: ","\n","Medio:""\n","Dificil:")
    eleccion = str(input("Elegi la dificultad: "))


    while True:
            
            if eleccion == "facil":
                facil = random.randint(1,10)
                while dificultades[0]["intentos"] > 0 :
                        numero = int(input("Que numero es del 1 al 10 ?: "))

                        if numero == facil:
                            print("Ganaste")
                        else:
                            print(f"Ese no es, te quedan {dificultades[0]["intentos"]-1} intentos")
                            dificultades[0]["intentos"] -=1

                        if dificultades[0]["intentos"] < 1 :
                            print("Perdiste")
                

            if eleccion == "medio":
                medio = random.randint(1,50)
                while dificultades[1]["intentos"] > 0 :
                    numero = int(input("Que numero es del 1 al 50 ?: "))

                    if numero == medio:
                        print("Ganaste")
                    else:
                        print(f"Ese no es, te quedan {dificultades[1]["intentos"]-1} intentos")
                        dificultades[1]["intentos"] -=1

                    if dificultades[1]["intentos"] < 1 :
                        print("Perdiste")
                

            if eleccion == "dificil":
                dificil = random.randint(1,100)    
                while dificultades[2]["intentos"] > 0 :
                    numero = int(input("Que numero es del 1 al 100?: "))
            
                    if numero == dificil:
                        print("Ganaste")
                    else:
                        print(f"Ese no es, te quedan {dificultades[2]["intentos"]-1} intentos")
                        dificultades[2]["intentos"] -=1

                    if dificultades[2]["intentos"] < 1 :
                        print("Perdiste")
                

            print("Deseas volver a jugar?: ""\n","Deseas sair?: ")
            eleccion_2 = str(input("Que deseas hacer: "))

            if eleccion_2 == "salir":
                return "Gracias por jugar"
            else:
                mostrar_menu()


print(mostrar_menu())
