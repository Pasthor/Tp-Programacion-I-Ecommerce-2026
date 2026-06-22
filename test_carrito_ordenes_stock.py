import pytest
from logica import calcularCarritoTotal,crearOrden,agregarOActualizarCarrito,restaurarStockItem,restaurarStockCarrito,cancelarDeuda

def test_calcularCarritoTotal():
    carrito = [
        {
            "precio_final": 1500
        },
        {
            "precio_final": 2500
        }
    ]

    assert calcularCarritoTotal(carrito) == 4000

def test_crearOrden():
    producto = {
        "id": "1",
        "nombre": "Remera",
        "precio": 1000,
        "stock": 10,
        "descuento": 10,
        "categoria": "ropa"
    }

    orden = crearOrden(producto, 2)

    assert orden["nombre"] == "Remera"
    assert orden["stock"] == 2
    assert orden["precio_final"] == 1800

def test_agregarOActualizarCarrito_agrega():
    carrito = []
    orden = {
        "id": "1",
        "nombre": "Remera",
        "stock": 2,
        "precio_final": 1800
    }

    agregarOActualizarCarrito(carrito, orden)

    assert len(carrito) == 1
    assert carrito[0]["nombre"] == "Remera"

def test_agregarOActualizarCarrito_actualiza():
    carrito = [
        {
            "id": "1",
            "nombre": "Remera",
            "stock": 2,
            "precio_final": 1800
        }
    ]
    orden = {
        "id": "1",
        "nombre": "Remera",
        "stock": 1,
        "precio_final": 900
    }

    agregarOActualizarCarrito(carrito, orden)

    assert carrito[0]["stock"] == 3
    assert carrito[0]["precio_final"] == 2700

def test_restaurarStockItem():
    productos = [
        {
            "id": "1",
            "nombre": "Remera",
            "stock": 5
        },
        {
            "id": "2",
            "nombre": "Pantalon",
            "stock": 3
        }
    ]
    item = {
        "id": "1",
        "nombre": "Remera",
        "stock": 2
    }

    restaurarStockItem(productos, item)

    assert productos[0]["stock"] == 7

def test_restaurarStockCarrito():
    productos = [
        {
            "id": "1",
            "nombre": "Remera",
            "stock": 5
        },
        {
            "id": "2",
            "nombre": "Pantalon",
            "stock": 3
        }
    ]
    carrito = [
        {
            "id": "1",
            "nombre": "Remera",
            "stock": 2
        },
        {
            "id": "2",
            "nombre": "Pantalon",
            "stock": 1
        }
    ]

    restaurarStockCarrito(carrito, productos)

    assert productos[0]["stock"] == 7
    assert productos[1]["stock"] == 4

def test_cancelarDeuda():
    ordenes = [
        [
            {
                "id": "1",
                "nombre": "Remera",
                "stock": 2,
                "precio_final": 1800
            }
        ]
    ]
    usuario = {
        "tarjetas": [],
        "cuenta": {
            "ordenes": ordenes,
            "deuda": 1800,
            "Historial": []
        }
    }

    cancelarDeuda(usuario)

    assert usuario["cuenta"]["ordenes"] == []
    assert usuario["cuenta"]["deuda"] == 0
