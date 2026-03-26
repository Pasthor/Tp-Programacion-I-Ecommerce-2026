import funciones

#Ecommerce
##Listas y Listas Paralelas
productos=      ["Manzana", "Banana","Pera", "Melon"]
productosPrecio=[2, 1, 3, 4]
productosStock= [32, 25, 20, 15]
productosId=    [1, 2, 3, 4]
opcionesMenu=["Comprar", "Ver productos", "Salir"]
carrito=[]
carritoTotal=0
opcionMenu=0
confirmandoCompra=False
MostrarMenu=0

if opcionMenu == 1:
    Comprar(carritoTotal, carrito)

    if confirmandoCompra==True:
        ConfirmarCompra(carrito, carritoTotal)


