import funciones

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
            "cuenta": {"ordenes": [], "deuda": 0, "Historial": []}
        },
        {
            "nombre": "user2",
            "email": "user2@gmail.com",
            "password": "password",
            "es_admin": False,
            "cuenta": {"ordenes": [], "deuda": 0, "Historial": []}
        }
    ]
    # Otros
    usuarioLogeado = None
    carrito = []
    carritoTotal = 0
    #Tarjeta Ecommerce
    NumTarjetasEcommerce = [123456, 789011, 181818, 121212, 223344]
    PINTarjetasEcommerce = [123,      789,    181,    121,    223,]
    NomTarjetasEcommerce = [   "JUAN",    "PEDRO",    "ANA",     "LEO",    "MARIA"]
    CuentasEcommerce =     [   [ [],0 ] , [ [],0 ] , [ [],0 ] , [ [],0 ] , [ [],0 ]   ]

    # Main - proceso
    funciones.mostrarLogo()
    print("Bienvenid@ a nuestro Ecommerce")
    usuarioLogeado = funciones.loginSignUp(usuarios)
    print(f"USUARIO: {usuarioLogeado} ")

    while True:
        # Pantalla principal
        opcion = funciones.MostrarMenu(usuarioLogeado["es_admin"])
        if opcion == 1: # COMPRAR
            carritoTotal = funciones.MenuComprar(carritoTotal, carrito, productos, usuarioLogeado)
        elif opcion == 2: # Ver productos  
            funciones.verProductos(productos)
        elif opcion == 3: #Buscar
            resultados = funciones.buscarProducto(productos)
            if len(resultados)>0:
                funciones.verProductos(resultados)
            else:
                print("No se encontraron productos")
                input("\nPresione ENTER para volver al menu...")
        elif opcion == 4: # Ver MiCuentaEcommerce
            print("Arreglando")
            funciones.MenuMiCuenta(usuarioLogeado)
        elif usuarioLogeado["es_admin"]:
            if opcion == 5: # Menu Admin
                funciones.menuAdmin(productos)
            elif opcion == 6: # SALIR
                print("bye bye")
                break
        else:
            if opcion == 5: # SALIR
                print("bye bye")
                break

# Ejecutar programa
Main()