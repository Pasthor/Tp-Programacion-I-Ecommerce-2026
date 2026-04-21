

Run=True


import funciones

#Ecommerce
Run=True
#Productos
productos = [
    {
        "id": 1,
        "nombre": "Manzana",
        "categoria": "Rojo",
        "precio": 2,
        "stock": 32,
        "descuento": 10
    },
    {
        "id": 2,
        "nombre": "Banana",
        "categoria": "Amarillo",
        "precio": 1,
        "stock": 25,
        "descuento": 0
    },
{
        "id": 3,
        "nombre": "Pera",
        "categoria": "Verde",
        "precio": 3,
        "stock": 20,
        "descuento": 20
    }
]
#Usuarios
# En main.py
usuarios = [
    {
        "nombre": "user1",
        "email": "user1@gmail.com",
        "password": "password",
        "rol": "admin"
    },
    {
        "nombre": "user2",
        "email": "user2@gmail.com",
        "password": "password",
        "rol": "user"
    }
]
#Otros
esAdmin= False
carrito=[]
carritoTotal=0
opcionMenu=0
confirmandoCompra=False
MostrarMenu=0
    ## TARJETA ECOMMERCE
NumTarjetasEcommerce=[123456, 789011, 181818, 121212, 223344]
PINTarjetasEcommerce=[123,      789,    181,    121,    223,]
NomTarjetasEcommerce=[   "JUAN",    "PEDRO",    "ANA",     "LEO",    "MARIA"]
CuentasEcommerce=    [   [ [],0 ] , [ [],0 ] , [ [],0 ] , [ [],0 ] , [ [],0 ]   ]
compra_done=False


# Main - proceso

funciones.mostrarLogo()
print("Bienvenid@ a nuestro Ecommerce")
esAdmin = funciones.loginSignUp(usuarios)
tipoEnvio= "N/A"



while Run==True:

    # Pantalla principal
    opcion = funciones.MostrarMenu(esAdmin)
    if opcion == 1: # COMPRAR
        carritoTotal = funciones.LogicaCompra(carritoTotal, carrito, productos, NomTarjetasEcommerce, PINTarjetasEcommerce, NumTarjetasEcommerce, CuentasEcommerce)

    if opcion == 2: # Ver productos  
        funciones.verProductos(productos)
    if opcion == 3: # Ver MiCuentaEcommerce
        funciones.MenuMiCuenta(productos, NomTarjetasEcommerce, PINTarjetasEcommerce, NumTarjetasEcommerce, CuentasEcommerce)
        funciones.VolverMenuPrincipal()
    if opcion == 4: #Buscar
        resultados = funciones.buscarProducto(productos)
        if len(resultados)>0:
            funciones.verProductos(resultados)
        else:
            print("No se encontraron productos")
            input("\nPresione ENTER para volver al menu...")
    if esAdmin:
        if opcion == 5:
            funciones.modoAdmin(productos)
            #funciones.aplicarDescuento(productos, productosPrecio, productosId, productosDescuento)
            funciones.VolverMenuPrincipal()
        elif opcion == 6:
            break
    else:
        if opcion == 5: # SALIR
            print("bye bye")
            break