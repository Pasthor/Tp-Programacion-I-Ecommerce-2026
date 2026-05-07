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

    # Main - proceso
    funciones.mostrarLogo()
    print("Bienvenid@ a nuestro Ecommerce")
    usuarioLogeado = funciones.loginSignUp(usuarios)

    while True:
        # Pantalla principal
        opcion = funciones.MostrarMenu(usuarioLogeado["es_admin"])
        if opcion == 1: # COMPRAR
            funciones.MenuComprar(carrito, productos, usuarioLogeado)
        elif opcion == 2: # Ver productos  
            funciones.verProductos(productos)
            input("\nPresione ENTER para volver al menu...")
        elif opcion == 3: #Buscar
            resultados = funciones.buscarProducto(productos)
            if len(resultados)>0:
                funciones.verProductos(resultados)
                input("\nPresione ENTER para volver al menu...")
            else:
                print("No se encontraron productos")
                input("\nPresione ENTER para volver al menu...")
        elif opcion == 4: # Ver MiCuentaEcommerce
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