#Ecommerce
##Listas y Listas Paralelas
Productos=      ["Manzana", "Banana","Pera", "Melon"]
ProductosPrecio=[2, 1, 3, 4]
ProductosStock= [32, 25, 20, 15]
ProductosID=    [1, 2, 3, 4]
OpcionesMenu=["Comprar", "Ver Productos", "Salir"]
carrito=[]
carritoTotal=0
def ConfirmarCompra(carrito, carritoTotal):
    print("")
    print("|-|-|-|-|-|-|--Comprar carrito--|-|-|-|-|-|-|-|")
    for i in range (len(carrito)):
        print("Ob#",i, carrito[i])
    print(f"El total de su compra es de: $ {carritoTotal}")
    print("")
    print("Confirmar Carrito de compras?")
    opcion=input("S/N")
    if opcion == "S" or opcion == "s":
        print("")
        print("- - - - - - - - - - - - - - - - - - - - - ")
        print("$$ Inciando Compra $$")
        print("Seleccione metodo de pago...")
        print("[1] Efectivo")
        print("[2] Debito/Credito")
        print("- - - - - - - - - - - - - - - - - - - - - ")
        op=(int(input("-.-.-")))
        if op == 1:
            print("Gracias")
            print("Regresando...")
            input()
            MostrarMenu()
        if op == 2:
            print("Gracias")
            print("Regresando...")
            input()
            MostrarMenu()
        else: 
            print("NO VALIDO")
            return
    if opcion == "N" or opcion == "n":
        print("¡¡Compra Cancelada!!")
        print("Regresando...")
        input()
        MostrarMenu()

def Comprar(carritoTotal, carrito):
    ##Interfaz de compra
    print("------------------------------------------------------------------------")
    print("=======================================================================")
    print("E-Commerce⦿E-Commerce⦿E-Commerce⦿E-Commerce⦿E-Commerce⦿E-Commerce⦿")
    print("===========================COMPRA===========================================")
    print("Tu carrito es: $", carritoTotal)
    for i in range (len(Productos)):
        print("[",i+1,"]", Productos[i], "| Precio: $", ProductosPrecio[i], "|  Stock:", ProductosStock[i])
    print("[ 0 ] SALIR")
    print("[ P ] Confirmar Carrito")
    #Añadir al carrito 
    print("----------------AÑADIR AL CARRITO DE COMPRAS----------------")
    compra=(input("Ingrese el numero del producto que desea comprar: "))
    if compra=="p" or compra == "P":
        ConfirmarCompra(carrito, carritoTotal)
    else:
        compra=int(compra)
        if compra>0:
            compra= compra-1
            cantidad=int(input("Ingrese la cantidad que desea añadir: "))
            #Revisa que la cantidad a comprar sea menor al stock disponible siempre
            if cantidad<=ProductosStock[compra]:
                total=ProductosPrecio[compra]*cantidad
                total=int(total)
                print("Total a pagar: $", total)
                ProductosStock[compra]-=cantidad
                carritoTotal=int(carritoTotal)
                carritoTotal=carritoTotal+total
                Orden=(f"{Productos[compra] }    |#{cantidad}    |${total}")

                carrito.append(Orden)
                return Comprar(carritoTotal, carrito)
            else:
                print("No hay suficiente stock para esa cantidad.")
        else:
            return MostrarMenu()
            
def MostrarMenu():
    print("------------------------------------------------------------------------")
    print("=======================================================================")
    print("E-Commerce⦿E-Commerce⦿E-Commerce⦿E-Commerce⦿E-Commerce⦿E-Commerce⦿")
    print("=======================================================================")
    print("Bienvenido a la tienda virtual 🏪 ADMIN")
    for i in range (len(OpcionesMenu)):
        print("[",i+1,"]", OpcionesMenu[i])
    opcion=int(input("Opcion: "))
   
    if opcion == 1:
        Comprar(carritoTotal, carrito)
    else:
        print("ingrese opcion valida")
    

    
MostrarMenu()

