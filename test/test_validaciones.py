from app import validaciones
from app.validaciones import (validar_pedir_eleccion,validar_pedir_numero,pedir_reintento)


def test_validar_pedir_eleccion():
    assert validar_pedir_eleccion("facil")
    assert validar_pedir_eleccion("medio") 
    assert validar_pedir_eleccion("dificil")
    assert not validar_pedir_eleccion("imposible") 
    assert not validar_pedir_eleccion("")


def test_validar_pedir_numero_dentro_del_rango():
    assert validar_pedir_numero(5,1,10)

def test_validar_pedir_numero_limite_inferior():
    assert validar_pedir_numero(1,1,10)

def test_validar_pedir_numero_limite_superior():
    assert validar_pedir_numero(10,1,10)

def test_validar_pedir_numero_fuera_rango_inferior():
    assert not validar_pedir_numero(-1,1,10)

def test_validar_pedir_numero_fuera_rango_superior():
    assert not validar_pedir_numero(16,1,10)

def test_validar_pedir_reintento_strip(monkeypatch):
    
    def devolver_si(mensaje):
        return " SI "
    
    monkeypatch.setattr(validaciones,"input",devolver_si, raising=False)

    resultado = validaciones.pedir_reintento()

    assert resultado == "si"

def test_validar_pedir_reintento_lower(monkeypatch):

    def devolver_no(mensaje):
        return "No"

    monkeypatch.setattr(validaciones,"input",devolver_no,raising=False)

    re_final = pedir_reintento()

    assert re_final == "no"