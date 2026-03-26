
##CONFIRMAR CARRO
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
            return
        if op == 2:
            print("Gracias")
            print("Regresando...")
            input()
            return
        else: 
            print("NO VALIDO")
            return
    if opcion == "N" or opcion == "n":
        print("¡¡Compra Cancelada!!")
        print("Regresando...")
        input()
        MostrarMenu()
    else:
        print("¡!")
        print("Marque opcion valida")
        return


##COMPRA
def Comprar(carritoTotal, carrito):
    #Interfaz de compra
    print("------------------------------------------------------------------------")
    print("=======================================================================")
    print("E-Commerce⦿E-Commerce⦿E-Commerce⦿E-Commerce⦿E-Commerce⦿E-Commerce⦿")
    print("===========================COMPRA===========================================")
    print("Tu carrito es: $", carritoTotal)
    for i in range (len(productos)):
        print("[",i+1,"]", productos[i], "| Precio: $", productosPrecio[i], "|  Stock:", productosStock[i])
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
            if cantidad<=productosStock[compra]:
                total=productosPrecio[compra]*cantidad
                total=int(total)
                print("Total a pagar: $", total)
                productosStock[compra]-=cantidad
                carritoTotal=int(carritoTotal)
                carritoTotal=carritoTotal+total
                Orden=(f"{productos[compra] }    |#{cantidad}    |${total}")

                carrito.append(Orden)
                return Comprar(carritoTotal, carrito)
            else:
                print("No hay suficiente stock para esa cantidad.")
        else:
            return MostrarMenu()
            
            
##MOSTRAR MENU
def MostrarMenu(productos, productosPrecio, productosStock, opcionesMenu, carrito, carritoTotal):
    print("------------------------------------------------------------------------")
    print("=======================================================================")
    print("E-Commerce⦿E-Commerce⦿E-Commerce⦿E-Commerce⦿E-Commerce⦿E-Commerce⦿")
    print("=======================================================================")
    print("Bienvenido a la tienda virtual 🏪 ADMIN")

    for i in range (len(opcionesMenu)):
        print("[",i+1,"]", opcionesMenu[i])
    opcion=int(input("Opcion: "))
   
    if opcion == 1:
        Comprar(carritoTotal, carrito)
    else:
        print("ingrese opcion valida")
        return