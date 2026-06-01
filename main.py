import interfaz

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
    usuarios = [
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
            "cuenta": {"ordenes": [], "deuda": 0, "Historial": []}
        }
    ]

    # Otros
    usuarioLogeado = None
    carrito = []
    cupones = []

    # Main - proceso
    interfaz.mostrarLogo()
    print("Bienvenid@ a nuestro Ecommerce")
    usuarioLogeado = interfaz.loginSignUp(usuarios)

    while True:
        # Pantalla principal
        opcion = interfaz.MostrarMenu(usuarioLogeado["es_admin"])
        if opcion == 1: # COMPRAR
            interfaz.MenuComprar(carrito, productos, usuarioLogeado, cupones)
        elif opcion == 2: # Ver productos
            interfaz.verProductos(productos)
            input("\nPresione ENTER para volver al menu...")
        elif opcion == 3: # Buscar
            resultados = interfaz.buscarProducto(productos)
            if len(resultados) > 0:
                interfaz.verProductos(resultados)
                input("\nPresione ENTER para volver al menu...")
            else:
                print("No se encontraron productos")
                input("\nPresione ENTER para volver al menu...")
        elif opcion == 4: # Ver MiCuentaEcommerce
            interfaz.MenuMiCuenta(usuarioLogeado)
        elif opcion == 5: # Manejar tarjetas guardadas
            interfaz.menuTarjetas(usuarioLogeado)
        elif usuarioLogeado["es_admin"]:
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