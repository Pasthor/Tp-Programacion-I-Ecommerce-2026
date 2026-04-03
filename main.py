

Run=True


import funciones

#Variables útiles
relleno = "|-|-|-|-|-|-|"

lineaPunt = "- - - - - - - - - - - - - - - - - - - - -"
regre="Regresando..."
confirmando= False
comprando = False
#Ecommerces
##Listas y Listas Paralelas
productos=      ["TV Samsung Led", "Ninja Blender","Helader con Freezer Philips", "Microondas Electrolux"]
productosPrecio=[300,                     400,              350,                         120]
productosStock= [40,                      32,               23,                          160]
productosId=    [1,                        2,                3,                          4]
opcionesMenu=["Comprar", "Ver productos", "Ver MiCuentaEcommerce" "Salir"]
carrito=[]
carritoTotal=0

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
           
    if opcion == 2: ##Ver productos  
        pass  


    if opcion == 3:
        idx=0

        nombre, NumTarjeta, Pin=funciones.SolicitarDatos()

        validacion, idx=funciones.validarTarjetaEcommerce(nombre, NumTarjeta, Pin, NomTarjetasEcommerce, PINTarjetasEcommerce, NumTarjetasEcommerce)
        if validacion == 3:
            funciones.MostarCuentaCliente(idx, CuentasEcommerce)
            input("Regresando")
        else: 
             print("ERROR al ingresar datos")
                            


    if opcion == 4: ##SALIR
        break
   
    

           