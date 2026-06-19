import pytest
from logica import mailExiste,verificarCredenciales,crearDiccionarioUsuario,randomNumber,calcularCarritoTotal,crearOrden,agregarOActualizarCarrito,restaurarStockItem,restaurarStockCarrito,cancelarDeuda

def test_mailExiste_existe():
    usuarios = [
        {

            "email": "user1@gmail.com",
        },
        {
            "email": "user2@gmail.com",
        }
    ]

    assert mailExiste(usuarios, "user1@gmail.com") == True

def test_mailExiste_noexiste():
    usuarios = [
        {
            "email": "user1@gmail.com"
        },
        {
            "email": "user2@gmail.com"
        }
    ]

    assert mailExiste(usuarios, "user3@gmail.com") == False

def test_verificarCredenciales_correcto():
    usuarios = [
        {
            "email": "user1@gmail.com",
            "password": "password"
        },
        {
            "email": "user2@gmail.com",
            "password": "password"
        }
    ]

    assert verificarCredenciales(usuarios, "user1@gmail.com", "password") == usuarios[0]

def test_verificarCredenciales_mailinexistente():
    usuarios = [
        {
            "email": "user1@gmail.com",
            "password": "password"
        },
        {
            "email": "user2@gmail.com",
            "password": "password"
        }
    ]

    assert verificarCredenciales(usuarios, "user3@gmail.com", "password") == None

def test_verificarCredenciales_passincorrecto():
    usuarios = [
        {
            "email": "user1@gmail.com",
            "password": "password"
        },
        {
            "email": "user2@gmail.com",
            "password": "password"
        }
    ]

    assert verificarCredenciales(usuarios, "user1@gmail.com", "wrongpass") == None

def test_crearDiccionarioUsuario():
    diccionarioTest = crearDiccionarioUsuario("test","test@gmail.com","pass")
    assert diccionarioTest["nombre"] == "test"
    assert diccionarioTest["email"] == "test@gmail.com"
    assert diccionarioTest["password"] == "pass"
    assert diccionarioTest["es_admin"] == False
    assert diccionarioTest["tarjetas"] == []
    assert diccionarioTest["cuenta"] == {"ordenes": [], "deuda": 0, "Historial": []}

def test_randomNumber():
    num = randomNumber()
    otronum = randomNumber()
    assert len(num) == 11
    assert num.isdigit()
    assert num != otronum

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
    cuenta = {
        "ordenes": ordenes,
        "deuda": 1800,
        "Historial": []
    }

    cancelarDeuda(cuenta)

    assert cuenta["ordenes"] == []
    assert cuenta["deuda"] == 0
