def mostrarLogo():
    print("  ______  _____ ____  __  __ __  __ ______ _____   _____ ______ ")
    print(" |  ____|/ ____/ __ \\|  \\/  |  \\/  |  ____|  __ \\ / ____|  ____|")
    print(" | |__  | |   | |  | | \\  / | \\  / | |__  | |__) | |    | |__   ")
    print(" |  __| | |   | |  | | |\\/| | |\\/| |  __| |  _  /| |    |  __|  ")
    print(" | |____| |___| |__| | |  | | |  | | |____| | \\ \\| |____| |____ ")
    print(" |______|\\_____\\____/|_|  |_|_|  |_|______|_|  \\_\\\\_____|______|")

def validar Tarjeta Ecommerce

def PagarTarjeta(carrito, carritoTotal):
    print(f"\n==================================================================")
    print(f"Iniciando Pago con Tarjeta Ecommerce....")
    print(f"\n   Pago en total: {carritoTotal}")
    nombre=input(f"\nNombre: ")
    NumTarjeta=input(f"Ingrese su numero de tarjeta Ecommerce: ")
    Pin=input(f"Ingrese su PIN secreto: ")





def PagarEfectivo(carrito, carritoTotal):
    print(f"\n==================================================================")
    print("Calculando Pago y vuelto con Efectivo--------------------")
    print("ENTER para cancelar")
    print(f"\n   Pago en total: {carritoTotal}")
    pago=input(f"\n Con cuanto esta pagando: $")
    print("")
    if pago.isdigit():
    ##Control de entrada teclado, el programa solo continua si se ingresa un numero
        pago=int(pago)
        if pago>=carritoTotal:
            vuelto=pago-carritoTotal
            print(f"{'Pagando:':<10} $ {carritoTotal:>8}")
            print(f"{'Con:':<10} $ {pago:>8}")
            ##Especificadores de formato, para alinear listas en columnas
            print("-"*27)
            print(f"{'Vuelto:':<10} $ {vuelto:>8}")
            print(f"\nPAGO REALIZADO---------------------")
            ##Reinicializacon de los carritos
            carrito=[]
            carritoTotal=0
            print("Regresando....")
            input("")
            return "COMPRA NUEVA"
        else: 
            print(f"\n   ingrese monto valido ¡!")
            print("===================================")
            return PagarEfectivo(carrito, carritoTotal)
    else:
        print ("Ingrese monto valido ¡! ")
        return 

def ConfirmarCompra(carrito, carritoTotal):
    print("")
    ##Interfaz del carrito de compras/Confirma Compra
    print("|-|-|-|-|-|-|--Comprar carrito--|-|-|-|-|-|-|-|")
    for i in range (len(carrito)):
        print("Ob#",i, carrito[i])
    print(f"\nEl total de su compra es de: $ {carritoTotal}")
    print("")
    print("--------------------------------")
    print("Confirmar Carrito de compras?")
    print("--------------------------------")
    opcion=input("S/N: ")

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
            return "Efectivo"

        if op == 2:
            return "Tarjeta"
        else: 
            print("NO VALIDO")
            return
    if opcion == "N" or opcion == "n":
        print("¡¡Compra Cancelada!!")
        print("Regresando...")
        input()
        return

def Comprar(carritoTotal, carrito, productos, productosPrecio, productosStock, comprando):
    #Interfaz de compra
    while comprando == True:
        confirmando=0
        print("------------------------------------------------------------------------")
        print("==========================================================================")
        print("E-Commerce⦿E-Commerce⦿E-Commerce⦿E-Commerce⦿E-Commerce⦿E-Commerce⦿")
        print("===========================COMPRA===========================================")
        print("Tu carrito es: $", carritoTotal)
        print("="*80)
        print(f"{'ID':^4} | {'PRODUCTO':<27} | {'PRECIO':<19} | {'STOCK':^10}")
        print("-" * 80)
        for i in range (len(productos)):
            print(f"[{i+1:^3}] {productos[i]:<28} | Precio:  ${productosPrecio[i]:<8}  | Stock: {productosStock[i]:>8}")
        print("[ 0 ] SALIR")
        print("[ P ] Confirmar Carrito")
        #Añadir al carrito 
        print("----------------AÑADIR AL CARRITO DE COMPRAS----------------")
        compra=(input("Ingrese el numero del producto que desea comprar: "))
        if compra == "p" or compra == "P":
            if carritoTotal>0:
                return "P"
            else: 
                print("Su carrito esta vacio ¡! ¡!")
                print("---------------------------------")
                return
        if compra == "0":
            return "SALIR"
        else:
            if compra.isdigit() and int(compra)>0:
                compra=int(compra)
                if compra >0 and compra<((len(productos))+1):
                    index=compra-1
                    print("-------------------------------------------------------------------")
                    print(f"\nComprando Item: {productos[index]} | ${productosPrecio[index]}")
                    cantidad=(input("UNIDADES A COMPRAR: "))
                    if cantidad.isdigit():
                        cantidad=int(cantidad)
                        if int(cantidad)<productosStock[index]:
                            total=productosPrecio[index]*int(cantidad)
                            total=int(total)
                            AñadirProducto=input(f"Seguro que quiere añadir {cantidad} {productos[index]} | Por un total de ${total} (S/N): ") 
                            if AñadirProducto == "S" or AñadirProducto=="s":
                                carritoTotal=carritoTotal+total
                                productosStock[index]=productosStock[index]-int(cantidad)
                                orden=f"{productos[index]:<28} | #{cantidad:<5} | ${total:<8}"
                                carrito.append(orden)
                                total=int(total)
                                return int(total)
                                comprando=False
                            else: 
                                print("Ingrese opcion valida por favor!")
                                print("Regresando...")
                                input("")
                                return
                            
                        if int(cantidad)>productosStock[index]:
                            print(f"\nSTOCK INSUFICIENTE ¡!")
                            return
                        else:
                            print("Caracter invalido¡!")
                            print("Regresando...")
                            input("")
                            return
                    else:
                        print("ingreses caracter valido ¡!")
                        print("Regresando...")
                        return
                else:
                    print ("Producto invalido!")
                    print("Regresando...")
                    input("")
                    return
                            
            else:
                ("ingrese caracter valido ¡!: ")
                return
            

def MostrarMenu(opcionesMenu):
    mostrarLogo()
    print("------------------------------------------------------------------------")
    print("=======================================================================")
    print("E-Commerce⦿E-Commerce⦿E-Commerce⦿E-Commerce⦿E-Commerce⦿E-Commerce⦿")
    print("=======================================================================")
    print("Bienvenido a la tienda virtual 🏪 ADMIN")

    for i in range (len(opcionesMenu)):
        print("[",i+1,"]", opcionesMenu[i])
    opcion=(input("Opcion: "))
    if opcion.isdigit():
        opcion=int(opcion)
        if opcion>0:
            return opcion
            
    else:
        print("ingrese opcion valida")
        return MostrarMenu(opcionesMenu)
