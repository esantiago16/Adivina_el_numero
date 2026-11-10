from juego import nivel_dificil, nivel_facil, nivel_medio
from validaciones import pedir_eleccion, pedir_reintento, validar_pedir_eleccion


def mostrar_menu():
        print("¡¡¡¡¡¡Bienvenido a Adivina el numero!!!!!")
        
        while True:
                
                print("Dificultades","\n","Facil ","\n","Medio""\n","Dificil")
                eleccion = pedir_eleccion()
                if not validar_pedir_eleccion(eleccion):
                    print("Esa dificultad no existe, vuelve a elegir")
                    continue

                if eleccion == "facil":
                    nivel_facil()

                if eleccion == "medio":
                    nivel_medio()
                
                if eleccion == "dificil":
                    nivel_dificil()
                
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





