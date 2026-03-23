#Ecommerce
##Listas y Listas Paralelas
Productos=      ["Manzana", "Banana","Pera", "Melon"]
ProductosPrecio=[2, 1, 3, 4]
ProductosStock= [32, 25, 20, 15]
ProductosID=    [1, 2, 3, 4]

OpcionesMenu=["Comprar", "Ver Productos", "Salir"]
def Comprar():
    carrito=0
    print("------------------------------------------------------------------------")
    print("=======================================================================")
    print("E-Commerce⦿E-Commerce⦿E-Commerce⦿E-Commerce⦿E-Commerce⦿E-Commerce⦿")
    print("===========================COMPRA===========================================")
    print("Tu carrito es: $", carrito)
    for i in range (len(Productos)):
        print("[",i+1,"]", Productos[i], "Precio: $", ProductosPrecio[i], "Stock:", ProductosStock[i])
        compra=int(input("Ingrese el numero del producto que desea comprar: "))
        compra= compra-1
        cantidad=int(input("Ingrese la cantidad que desea comprar: "))
        if cantidad<=ProductosStock[compra]:
            total=ProductosPrecio[compra]*cantidad
            print("Total a pagar: $", total)
            ProductosStock[compra]-=cantidad
            carrito=carrito+total
            return Comprar()
        else:
            print("No hay suficiente stock para esa cantidad.")
        
def MostrarMenu():
    print("------------------------------------------------------------------------")
    print("=======================================================================")
    print("E-Commerce⦿E-Commerce⦿E-Commerce⦿E-Commerce⦿E-Commerce⦿E-Commerce⦿")
    print("=======================================================================")
    print("Bienvenido a la tienda virtual 🏪 ADMIN")
    for i in range (len(OpcionesMenu)):
        print("[",i+1,"]", OpcionesMenu[i])
    opcion=int(input("Opcion: "))
    opcion-=1
    if opcion == 1:
        Comprar()
    else:
        ("ingrese opcion valida")
    

    
MostrarMenu()

