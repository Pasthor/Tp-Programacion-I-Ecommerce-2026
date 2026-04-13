import funciones

#Ecommerce
Run=True
#Productos
productos=         ["Manzana", "Banana","Pera", "Melon"]
productosCategoria=["Rojo","Amarillo","Verde","Amarillo"]
productosPrecio=   [2, 1, 3, 4]
productosStock=    [32, 25, 20, 15]
productosId=       [1, 2, 3, 4]
productosDescuento=[10, 0, 20, 0]
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
usuarios = [["user1", "user@gmail.com", "password", "admin"], ["user2", "user@gmail.com", "password", "user"], ["user3", "user@gmail.com", "password", "user"]]


# Main - proceso

while Run==True:
    funciones.mostrarLogo()
    existeUser = funciones.loginSignUp()
    if existeUser == True:
        funciones.iniciarSesion(usuarios)
    else:
        funciones.crearUsuario(usuarios)
    opcion = funciones.MostrarMenu(esAdmin)
    if opcion == 1: # COMPRAR
        compraEfectiva, tipoEnvio = funciones.MenuComprar(carritoTotal, carrito, productos, productosPrecio, productosStock, confirmandoCompra, NomTarjetasEcommerce, PINTarjetasEcommerce, NumTarjetasEcommerce, CuentasEcommerce)
        funciones.mostrarMensajeFinal(compraEfectiva, tipoEnvio)
        funciones.VolverMenuPrincipal()
    if opcion == 2: # Ver productos  
        funciones.verProductos(productos, productosCategoria, productosPrecio)
        funciones.VolverMenuPrincipal()
    if opcion == 3: # Ver MiCuentaEcommerce
        funciones.MenuMiCuenta(productos, productosStock, NomTarjetasEcommerce, PINTarjetasEcommerce, NumTarjetasEcommerce, CuentasEcommerce)
        #funciones.aplicarDescuento(productos, productosPrecio, productosId, productosDescuento)
        funciones.VolverMenuPrincipal()
    if esAdmin:
        if opcion == 4:
            funciones.modoAdmin(productos, productosStock)
            funciones.VolverMenuPrincipal()
        elif opcion == 5:
            break
    else:
        if opcion == 4: # SALIR
            break