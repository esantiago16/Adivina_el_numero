def pedir_eleccion():
    eleccion = input("Elegi la dificultad: ").lower().strip()
    return eleccion

dificultades = ["facil", "medio", "dificil"]

def validar_pedir_eleccion(eleccion):
    return eleccion in dificultades
               
def pedir_numero_facil():
    numero = int(input("Dame un numero del 1 al 10: "))
    return numero

def pedir_numero_medio():
    numero = int(input("Dame un numero del 1 al 50: "))
    return numero

def pedir_numero_dificil():
    numero = int(input("Dame un numero del 1 al 100: "))
    return numero

def validar_pedir_numero(numero, limite_inferior, limite_superior):
    return limite_inferior <= numero <= limite_superior

def pedir_reintento():
    reintento = input("Quieres volver a jugar o salir?: ").lower().strip()
    return reintento

