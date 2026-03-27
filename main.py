##UNIDADES A COMPRAR NO TIENE CONTROL DE ENTRADA1

Run=True


import funciones

#Variables útiles
relleno = "|-|-|-|-|-|-|"

lineaPunt = "- - - - - - - - - - - - - - - - - - - - -"
regre="Regresando..."
confirmando= False
comprando = False
#Ecommerce
##Listas y Listas Paralelas
productos=      ["TV Samsung Led", "Ninja Blender","Helader con Freezer Philips", "Microondas Electrolux"]
productosPrecio=[300,                     400,              350,                         120]
productosStock= [40,                      32,               23,                          160]
productosId=    [1,                        2,                3,                          4]
opcionesMenu=["Comprar", "Ver productos", "Salir"]
carrito=[]
carritoTotal=0




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
                print("Caracter invalido")
        if confirmando==True:
            CompraRealizada=funciones.ConfirmarCompra(carrito, carritoTotal)
            comprando=False
            if CompraRealizada=="COMPRA NUEVA":
                continue

    

           