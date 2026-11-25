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
    
    #Given : El usuario envia una palabra con espacios y mayusculas
    monkeypatch.setattr(validaciones,"input",lambda devolver_si:" SI ",raising=False)

    #When : Se pide el nuevo intento
    resultado = pedir_reintento()

    #Then: La entrada llega sin espacios y en miniscula 
    assert resultado == "si"

def test_validar_pedir_reintento_lower(monkeypatch):
    
    #Given : El usuario envia una palabra la primera letra en mayuscula
    monkeypatch.setattr(validaciones,"input", lambda devolver_no: "No",raising=False)

    #When : Se pide el nuevo intento
    re_final = pedir_reintento()

    #Then: La entrada llega toda en miniscula 
    assert re_final == "no"