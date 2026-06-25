import pytest
from logica import mailExiste,verificarCredenciales,crearDiccionarioUsuario,randomNumber

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
    assert diccionarioTest["cuenta"] == {"ordenes": [], "deuda": 0}
    assert diccionarioTest["historial"] == []

def test_randomNumber():
    num = randomNumber()
    otronum = randomNumber()
    assert len(num) == 11
    assert num.isdigit()
    assert num != otronum