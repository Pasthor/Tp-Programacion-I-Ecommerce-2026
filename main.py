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

    
MostrarMenu()
if opcionMenu == 1:
    Comprar(carritoTotal, carrito)

    if ConfirmandoCompra==True:
        ConfirmarCompra(carrito, carritoTotal)

