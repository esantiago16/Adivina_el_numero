def pedir_eleccion():
    eleccion = input("Elegi la dificultad: ").lower().strip()
    return eleccion

dificultades = ["facil", "medio", "dificil"]

def validar_pedir_eleccion(eleccion):
    return eleccion in dificultades
               

