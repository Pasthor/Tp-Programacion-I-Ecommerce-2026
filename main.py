

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
funciones.mostrar("Bienvenid@ a nuestro Ecommerce")
funciones.loginSignUp()

while Run==True:
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

    ## TARJETA ECOMMERCE
NumTarjetasEcommerce=[123456, 789011, 181818, 121212, 223344]
PINTarjetasEcommerce=[123,      789,    181,    121,    223,]
NomTarjetasEcommerce=[   "JUAN",    "PEDRO",    "ANA",     "LEO",    "MARIA"]
CuentasEcommerce=    [   [ [],0 ] , [ [],0 ] , [ [],0 ] , [ [],0 ] , [ [],0 ]   ]##Lista de listas para los  datos de clientes
                                                                            ## En CuentasEcommerce, cada lista pertenece a un cliente
                                                                            ## donde el primer item es una lista de todas sus compras realizadas
                                                                            ## y el segundo item es el total de sus compras para pagarlas
                                                                            ## mediante el financiamiento por cuotas




while Run==True:
    opcion= funciones.MostrarMenu(opcionesMenu)
    if opcion == 1: # COMPRAR
        confirmando=False
        comprando=True
        while confirmando==False: ##Bucle te mantiene dentro de la funcion comprar a menos que se confirme el carrito o Se presione la tecla para salir
            resultado=funciones.Comprar(carritoTotal, carrito, productos, productosPrecio, productosStock, comprando)
            if resultado == "P":
                confirmando=True
            elif resultado == "SALIR":
                break
            elif resultado is not None:##Si el usuario ingresa sus productos correctamente, se sumaran a su carrito siempre y cuando el producto exista (Not none)
                carritoTotal = carritoTotal+resultado
            else:
                print("ERROR!")
        if confirmando==True: ##Cuando se confirma el carrito...
            Pago=funciones.ConfirmarCompra(carrito, carritoTotal)
            comprando=False
            CompraRealizada=0
            if Pago == "Efectivo":
                CompraRealizada=funciones.PagarEfectivo(carrito, carritoTotal)
                if CompraRealizada=="COMPRA NUEVA":
                    carrito=[]
                    carritoTotal=0
                  
            if Pago == "Tarjeta":## Si el pago es con tarjetaecommerce, la compra se añade a la lista de compras del socio Ecommerce
                CompraRealizada, idx = funciones.PagarTarjeta(carrito, carritoTotal, NomTarjetasEcommerce, PINTarjetasEcommerce, NumTarjetasEcommerce)
                if CompraRealizada=="COMPRANUEVA":
                    CuentasEcommerce[idx][0].append(carrito[:])
                    CuentasEcommerce[idx][1]+=carritoTotal
                    carrito=[]
                    carritoTotal=0
                    continue 

            if str(Pago).startswith("BorrarUno"): ##Si el return empieza con BorrarUno
                partir=Pago.split(":") ##El return "BorrarUno:{indice a elminar}" se parte en dos mitades
                indice=int(partir[1]) ##Se toma la segunda mitad para solo tener el indice

                eliminar=carrito[indice]              ##Se extrae el fstring de la orden a eliminar 
                precio=eliminar.split("$")[-1].strip()## Para seguidamente extraer solo el precio de la orden 
                restar=int(precio)

                ##Devolver el stock al prodcuto
                ProdEliminar=eliminar.split("|")[0].strip()
                for i in range (len(productos)):
                    if ProdEliminar == productos[i]:
                        idxtemp=i
                
                StockDevolver=eliminar.split("#")[-1].strip()
                StockDevolver=int(StockDevolver.split("|")[0].strip())
                productosStock[idxtemp]=productosStock[idxtemp]+StockDevolver




                carritoTotal=carritoTotal-restar 
                print(f"Eliminando: {carrito[indice]}")##Se quita la orden de la lista carrito y se resta el costo de la orden al total del carrito $
                carrito.pop(indice)

                
                
                continue

            if Pago == "LIMPIAR":
                carrito=[]
                carritoTotal=0
                continue
            

           
    if opcion == 2: ##Ver productos  
        pass  


    if opcion == 3:
        
        idx=0
        nombre, NumTarjeta, Pin=funciones.SolicitarDatos()
        validacion, idx=funciones.validarTarjetaEcommerce(nombre, NumTarjeta, Pin, NomTarjetasEcommerce, PINTarjetasEcommerce, NumTarjetasEcommerce)
        if validacion == 3:
            continuar=funciones.MostarCuentaCliente(idx, CuentasEcommerce, nombre)
            if continuar=="CANCELAR DEUDA":
                PagoDeudas=funciones.CancelarCuentaCliente(idx, CuentasEcommerce, nombre)
                if PagoDeudas=="True":
                    pass


        else: 
             print("ERROR al ingresar datos")
             print (regre)
             input("")
                            


    if opcion == 4: ##SALIR
        break
   
    

           