import funciones

#Variables útiles
relleno = "|-|-|-|-|-|-|"
lineaPunt = "- - - - - - - - - - - - - - - - - - - - -"
regre="Regresando..."

#Ecommerce
##Listas y Listas Paralelas
productos=      ["Manzana", "Banana","Pera", "Melon"]
productosPrecio=[2, 1, 3, 4]
productosStock= [32, 25, 20, 15]
productosId=    [1, 2, 3, 4]
opcionesMenu=["Comprar", "Ver productos", "Salir"]
carrito=[]
carritoTotal=0


while True:
    funciones.mostrarLogo()
    opcion= funciones.MostrarMenu(opcionesMenu)
    if opcion == 1: # COMPRAR
        while True:
            res = funciones.Comprar(carritoTotal, carrito, productos, productosPrecio, productosStock)

            if res == "confirmar":
                exito = funciones.ConfirmarCompra(carrito, carritoTotal)
                if exito: 
                    carrito = []
                    carritoTotal = 0