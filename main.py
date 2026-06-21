import interfaz
import os
import json
RUTA_ACTUAL = os.path.dirname(__file__)
RUTA_JSON = os.path.join(RUTA_ACTUAL, "usuarios.json")

def InicializarDB(lista_hardcodeada):
    
    if os.path.exists(RUTA_JSON):
        with open(RUTA_JSON, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        with open(RUTA_JSON, "w", encoding="utf-8") as f:
            json.dump(lista_hardcodeada, f, indent=4, ensure_ascii=False)
        return lista_hardcodeada


# Programa principal del Ecommerce
def Main():
    '''
    Funcion principal del programa
    '''
    ## Variables
    # Productos
    productos = [
        {
            "id": "1",
            "nombre": "Manzana",
            "categoria": "Rojo",
            "precio": 2,
            "stock": 32,
            "descuento": 10
        },
        {
            "id": "2",
            "nombre": "Banana",
            "categoria": "Amarillo",
            "precio": 1,
            "stock": 25,
            "descuento": 0
        },
        {
            "id": "3",
            "nombre": "Pera",
            "categoria": "Verde",
            "precio": 3,
            "stock": 20,
            "descuento": 20
        }
    ]
    # Usuarios
    usuariosHARDCODE = [
        {
            "nombre": "user1",
            "email": "user1@gmail.com",
            "password": "password",
            "es_admin": True,
            "tarjetas": [],
            "cuenta": {"ordenes": [], "deuda": 0, "Historial": []}
        },
        {
            "nombre": "user2",
            "email": "user2@gmail.com",
            "password": "password",
            "es_admin": False,
            "tarjetas": [],
            "cuenta": {"ordenes": [], 
                       "deuda": 0, 
                       "Historial": []}
        }
    ]

    usuarios=InicializarDB(usuariosHARDCODE)
    # Otros
    usuarioLogueado = None
    carrito = []
    cupones = []

    # Main - proceso
    interfaz.mostrarLogo()
    print("Bienvenid@ a nuestro Ecommerce")
    usuarioLogueado = interfaz.loginSignUp(usuarios)

    while True:
        # Pantalla principal
        opcion = interfaz.MostrarMenu(usuarioLogueado["es_admin"])
        if opcion == 1: # COMPRAR
            interfaz.MenuComprar(carrito, productos, usuarioLogueado, cupones)
        elif opcion == 2: # Ver productos
            interfaz.verProductos(productos)
            input("\nPresione ENTER para volver al menu...")
        elif opcion == 3: # Buscar
            interfaz.buscarProducto(productos)
        elif opcion == 4: # Ver MiCuentaEcommerce
            interfaz.MenuMiCuenta(usuarioLogueado, usuarios)
        elif opcion == 5: # Manejar tarjetas guardadas
            interfaz.menuTarjetas(usuarioLogueado)
        elif usuarioLogueado["es_admin"]:
            if opcion == 6: # Menu Admin
                interfaz.menuAdmin(productos, cupones)
            elif opcion == 7: # SALIR
                print("bye bye")
                break
        elif opcion == 6: # SALIR
            print("bye bye")
            break

# Ejecutar programa
Main()