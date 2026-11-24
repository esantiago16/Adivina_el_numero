from app.validaciones import (validar_pedir_eleccion,validar_pedir_numero,pedir_reintento)

def test_validar_pedir_eleccion():
    assert validar_pedir_eleccion("facil") == True
    assert validar_pedir_eleccion("medio") == True
    assert validar_pedir_eleccion("dificil") == True
    assert validar_pedir_eleccion("imposible") == False
    assert validar_pedir_eleccion("") == False