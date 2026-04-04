PlazosCuotas=["3 Cuotas", "6 Cuotas", "8 Cuotas", "10 Cuotas"]
PlazosCuotNUM=[  3       ,  6        , 8        ,      10   ]
PorcentajeCuotas=[ "10%"   ,  "20%" ,   "30%"  ,     "40%"]
PagosCuotas=[     1.1     ,    1.2  ,    1.3    ,   1.40]

def mostrarLogo():
    print(f"\n \n")
    print("  ______  _____ ____  __  __ __  __ ______ _____   _____ ______ ")
    print(" |  ____|/ ____/ __ \\|  \\/  |  \\/  |  ____|  __ \\ / ____|  ____|")
    print(" | |__  | |   | |  | | \\  / | \\  / | |__  | |__) | |    | |__   ")
    print(" |  __| | |   | |  | | |\\/| | |\\/| |  __| |  _  /| |    |  __|  ")
    print(" | |____| |___| |__| | |  | | |  | | |____| | \\ \\| |____| |____ ")
    print(" |______|\\_____\\____/|_|  |_|_|  |_|______|_|  \\_\\\\_____|______|")

def GenerarRecibo(nombre, carrito, total):
    pass


def CancelarCuentaCliente(idx, CuentasEcommerce, nombre):

    print("===============CANCELAR DEUDA===============")
    print(f"SOCIO: {nombre}")
    print(f"\nDeuda a cancelar:   ${CuentasEcommerce[idx][1]:>8}")
    print("-"*50)
    print(f"")
    for i in range (len(PlazosCuotas)):
        print(f"[{i+1}] {PlazosCuotas[i]:<20}    Comision: {PorcentajeCuotas[i]:>5}")
    while True:
        OpcionPago=input(f"\nOPCION: ") 
        if OpcionPago.isdigit():
            OpcionPago=int(OpcionPago)-1
            if 0<=OpcionPago and OpcionPago<len(PlazosCuotas):
                print("===========CALCULO DE CUOTAS===========")
                print(f"\nUsted pagara su deuda de: {CuentasEcommerce[idx][1]}")
                Cuotas=(CuentasEcommerce[idx][1]*PagosCuotas[OpcionPago]) // PlazosCuotNUM[OpcionPago]
                print(f"\nPagara ${PlazosCuotas[OpcionPago]}     Cada una de: ${Cuotas} ")
                print(f"Pagando unicamente un {PorcentajeCuotas[OpcionPago]} de comision!!!")

                print(f"\nRegresando....")
                input("")
                return "True"

            else:
                print("ingrese opcion valida")
                continue

def MostarCuentaCliente(idx, CuentasEcommerce, nombre):

    for i in range(len(CuentasEcommerce[idx][0])): ##Ingresa a la lista del cliente donde se almacenan sus compras previas
        print(f"\n--- TICKET NRO {i+1} ---")  
        print(f"Socio Ecommerce: {nombre}")     ##Imprime las compras previas por separado             
        for producto in CuentasEcommerce[idx][0][i]: ##Imprime cada item dentro de las listas de compras previas 
            print(f"  • {producto}") 
    print(f"\n  •TOTAL DE CUENTA ECOMMERCE: ${CuentasEcommerce[idx][1]}")
    print(f"\n[1] CANCELAR CUENTA")
    print(f"[2] SALIR")
    opcion=input("Ingrese opcion: ")
    if opcion == "1":
        return "CANCELAR DEUDA"
    if opcion == "2":
        return "Cancelado"
    else: 
        print("Opcion no valida")
        print("Regresando...")
        input("")
        return "Cancelado"
    

def SolicitarDatos():
    print(f"\n{'='*20}Solicitando Datos{'='*20}")
    Datos=0
    nombre=input(f"\nNombre: ").upper()
    if nombre.isdigit():
        if nombre == "0": ##CANCELAR
            print("Cancelando...")
            input("")
            return"CANCELADO", None, None
        else:
            pass
    else:
        Datos=Datos+1

    NumTarjeta=input(f"Ingrese su numero de tarjeta Ecommerce: ")
    if NumTarjeta.isdigit():
        NumTarjeta=int(NumTarjeta)
        if NumTarjeta == 0: ##CANCELAR
            print("Cancelando...")
            input("")
            return"CANCELADO", None, None
        else:
            Datos=Datos+1
            
    else: 
        print("SINTAX ERROR")
        return "ERROR", None, None
    
    Pin=input(f"Ingrese su PIN secreto: ")
    if Pin.isdigit():
        Pin=int(Pin)
        if Pin == 0: ##CANCELAR
            print("Cancelando...")
            input("")
            return"CANCELADO", None, None
        else:
            print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
            Datos=Datos+1
    else: 
        print("SINTAX ERROR")
        return "ERROR", None, None
    if Datos==3:
        return nombre, NumTarjeta, Pin
    else:
        return "ERROR", None, None


def validarTarjetaEcommerce(nombre, NumTarjeta, Pin, NomTarjetasEcommerce, PINTarjetasEcommerce, NumTarjetasEcommerce):
    validacion=999
    if nombre in NomTarjetasEcommerce:
        idx=NomTarjetasEcommerce.index(nombre)
        
        if NumTarjeta==NumTarjetasEcommerce[idx]:
            
            if Pin==PINTarjetasEcommerce[idx]:
                validacion=3
                return validacion, idx
            
            else:
                validacion="ERROR PIN"
                return validacion, None


        else:
            validacion="ERROR NUM"
            return validacion, None


    else:
        validacion="ERROR NOM"
        return validacion, None


def PagarTarjeta(carrito, carritoTotal, NomTarjetasEcommerce, PINTarjetasEcommerce, NumTarjetasEcommerce):
    
    print(f"\n==================================================================")
    print(f"Iniciando Pago con Tarjeta Ecommerce....")
    print(f"PRESIONA 0 PARA CANCELAR")
    print(f"\n   Pago en total: {carritoTotal}")
    while True:
        
        nombre, NumTarjeta, Pin=SolicitarDatos()
        validado, idx =validarTarjetaEcommerce(nombre, NumTarjeta, Pin, NomTarjetasEcommerce, PINTarjetasEcommerce, NumTarjetasEcommerce)

        if validado == 3:
            print(f"\nPago Validado! ✓")
            return "COMPRANUEVA", idx
            
        else:
            print(f"\n{validado}")
            print("No se pudo procesar el pago")
            print(f"\n====================================")
            print("[1] Intenar de nuevo")
            print("[2] Salir")
            opcion=input("Opcion: ")
            if opcion.isdigit():
                opcion=int(opcion)
                if opcion==1:
                    continue
                if opcion==2:
                    return "CANCELADO", None
                else:
                    print("INVALIDO ¡!")
                    return "CANCELADO", None

            else: 
                print("INVALIDO !¡")
                return "CANCELADO", None






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
    print(f"[1] Confirmar Carrito")
    print(f"[2] Quitar Item del carrito")
    print(f"[3] Limpiar todo el Carrito")
    op=input("OPCION: ")
    if op == "1": ##CONFIRMAR COMPRA
        print("Confirmar Carrito de compras?")
        print("--------------------------------")
        opcion=input("S/N: ")

        if opcion == "S" or opcion == "s":
            print("")
            print("- - - - - - - - - - - - - - - - - - - - - ")
            print("$$ Inciando Compra $$")
            print("Seleccione metodo de pago...")
            print("[1] Efectivo")
            print("[2] Cuenta Socio Ecommerce")
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
    if op == "2": ##BORRAR UN ELEMENTO
        print("----------------------------------------")
        print("Eliminando un Ob#-----------------------")
        eliminar=input(f"\nIngrese el numer de Ob# a eliminar: Ob#")
        if eliminar.isdigit():
            eliminar=int(eliminar)
            if eliminar>=0 and eliminar<len(carrito):
                return f"BorrarUno:{eliminar}"

            else:
                print("Ingrese Ob# dentro del rango")
                return
        else: 
            print("Ingrese caracter valido ¡!")
            return
        
    if op == "3": ##LIMPIA TOTAL DEL CARRITO
        print("Confirmar limpia del carrito de compras?")
        print("----------------------------------------")
        opcion=input("S/N: ")

        if opcion == "S" or opcion == "s":
            print(f"\nCarrito Limpio ✓")
            print("Regresando...")
            input()
            return "LIMPIAR"
        
        if opcion == "N" or opcion == "n":
            print("¡¡Operacion Cancelada!!")
            print("Regresando...")
            input()
            return
        else:
            print("Ingrese opcion valida ¡!")
            return
    else:
        print("Ingrese opcion valida !¡")
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
        print("[ P ] Ver Carrito")
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
        ## SI el input no es 0(salir) o p(comprar) se continuan añadiendo productos
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
                        if int(cantidad)<=productosStock[index]:
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
