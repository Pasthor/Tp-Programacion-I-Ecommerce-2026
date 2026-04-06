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

# Main - proceso
funciones.mostrarLogo()
funciones.mostrar("Bienvenid@ a nuestro Ecommerce")
funciones.loginSignUp()
# Mostrar productos disponibles
funciones.verProductos(productos, productosPrecio)
# Proceso de compra, ya finaliza el carrito.
tipoEnvio = funciones.elegirEnvio()
# Finaliza compra y debe mostrar los detalles de compra con seguimiento de envío.
funciones.mostrarMensajeFinal(tipoEnvio)