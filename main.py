##UNIDADES A COMPRAR NO TIENE CONTROL DE ENTRADA1

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
opcionesMenu=["Comprar", "Ver productos", "Salir"]
carrito=[]
carritoTotal=0

    ## TARJETA ECOMMERCE
NumTarjetasEcommerce=[123456, 789011, 181818, 121212, 223344]
PINTarjetasEcommerce=[123,      789,    181,    121,    223,]
NomTarjetasEcommerce=["Juan",  "Pedro",  "Ana",  "Leo", "Maaria"]




while Run==True:
    opcion= funciones.MostrarMenu(opcionesMenu)
    if opcion == 1: # COMPRAR
        confirmando=False
        comprando=True
        while confirmando==False:
            resultado=funciones.Comprar(carritoTotal, carrito, productos, productosPrecio, productosStock, comprando)
            if resultado == "P":
                confirmando=True
            elif resultado == "SALIR":
                break
            elif resultado is not None:
                carritoTotal = carritoTotal+resultado
            else:
                print("ERROR!")
        if confirmando==True:
            Pago=funciones.ConfirmarCompra(carrito, carritoTotal)
            comprando=False
            CompraRealizada=0
            if Pago == "Efectivo":
                CompraRealizada=funciones.PagarEfectivo(carrito, carritoTotal)
                if CompraRealizada=="COMPRA NUEVA":
                    carrito=[]
                    carritoTotal=0
                        
            if Pago == "Tarjeta":
                CompraRealizada=funciones.PagarTarjeta(carrito, carritoTotal, NomTarjetasEcommerce, NumTarjetasEcommerce, PINTarjetasEcommerce)
                if CompraRealizada=="COMPRA NUEVA":
                    carrito=[]
                    carritoTotal=0
                    continue
    if opcion == 3:
        break
    

           