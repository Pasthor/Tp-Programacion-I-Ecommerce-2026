

Run=True


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



# Main - proceso
funciones.mostrarLogo()
print("Bienvenid@ a nuestro Ecommerce")
funciones.loginSignUp()
tipoEnvio= "N/A"


while Run==True:
    opcion = funciones.MostrarMenu(esAdmin)
    if opcion == 1: # COMPRAR
        carritoTotal = funciones.LogicaCompra(carritoTotal, carrito, productos, productosPrecio, productosStock, NomTarjetasEcommerce, PINTarjetasEcommerce, NumTarjetasEcommerce, CuentasEcommerce)             
    if opcion == 2: # Ver productos  
        funciones.verProductos(productos, productosCategoria, productosPrecio)
        funciones.VolverMenuPrincipal()
    if opcion == 3: # Ver MiCuentaEcommerce
        funciones.FlujoVerMiCuenta(NomTarjetasEcommerce, PINTarjetasEcommerce, NumTarjetasEcommerce, CuentasEcommerce)
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
            print("bye bye")
            break



