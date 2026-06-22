import pytest
import logica

def productosPrueba(): #Para no poner el diccionario en cada funcion de prueba
    return [
    {"id": "1", "nombre": "Zapallo","categoria": "Naranja", "precio": 10, "stock": 15, "descuento": 25},
    {"id": "3", "nombre": "Gato","categoria": "Negro", "precio": 120, "stock": 3, "descuento": 0},
    {"id": "5", "nombre": "Mandarina","categoria": "Naranja", "precio": 7, "stock": 23, "descuento": 15}
]

def test_filtrarPorNombre():
    resultado = logica.filtrarPorNombre(productosPrueba(),"gato")
    assert resultado[0]["id"] == "3"

def test_filtrarPorCategoria():
    resultado = logica.filtrarPorCategoria(productosPrueba(),"naranja")
    assert len(resultado) == 2

def test_filtrarPorPrecio_igual():
    resultado = logica.filtrarPorPrecio(productosPrueba(),120,1)
    assert len(resultado) == 1
    assert resultado[0]["id"] == "3"

def test_filtrarPrecio_mayorIgual():
    resultado = logica.filtrarPorPrecio(productosPrueba(),8,2)
    assert len(resultado) == 2

def test_filtrarPorPrecio_menorIgual():
    resultado = logica.filtrarPorPrecio(productosPrueba(),8,3)
    assert len(resultado) == 1

def test_generarNuevoId():
    idNueva = logica.generarNuevoId(productosPrueba())
    assert idNueva == "6"

def test_crearDiccionarioProducto():
    producto = logica.crearDiccionarioProducto("10","Pelota de Tennis",50,20,"Verde")
    assert producto["id"] == "10"
    assert producto["nombre"] == "Pelota de Tennis"
    assert producto["precio"] == 50
    assert producto["stock"] == 20
    assert producto["categoria"] == "Verde"

def test_alertaStock():
    alerta1 = logica.obtenerAlertaStock(1)
    alerta2 = logica.obtenerAlertaStock(0)
    alerta3 = logica.obtenerAlertaStock(100)
    assert alerta1 == "- El stock del producto esta bajo"
    assert alerta2 == "- No hay mas stock"
    assert alerta3 == ""

