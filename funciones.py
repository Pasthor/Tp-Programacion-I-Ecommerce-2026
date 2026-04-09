msjSeleccione = "Seleccione una opción: "
msjNoExiste = "Opción no válida. Por favor, intente de nuevo."
PlazosCuotas=["3 Cuotas", "6 Cuotas", "8 Cuotas", "10 Cuotas"]
PlazosCuotNUM=[  3       ,  6        , 8        ,      10   ]
PorcentajeCuotas=[ "10%"   ,  "20%" ,   "30%"  ,     "40%"]
PagosCuotas=[     1.1     ,    1.2  ,    1.3    ,   1.40]
usuarios = [["user1", "user@gmail.com",  "password"], ["user2", "user@gmail.com",  "password"], ["user3", "user@gmail.com",  "password"]]

def mostrarLogo():
    print("  ______  _____ ____  __  __ __  __ ______ _____   _____ ______ ")
    print(" |  ____|/ ____/ __ \\|  \\/  |  \\/  |  ____|  __ \\ / ____|  ____|")
    print(" | |__  | |   | |  | | \\  / | \\  / | |__  | |__) | |    | |__   ")
    print(" |  __| | |   | |  | | |\\/| | |\\/| |  __| |  _  /| |    |  __|  ")
    print(" | |____| |___| |__| | |  | | |  | | |____| | \\ \\| |____| |____ ")
    print(" |______|\\_____\\____/|_|  |_|_|  |_|______|_|  \\_\\\\_____|______|")

def mostrarPrompt(titulo, opciones):
    """
    Funcion de utilidad para mostrar un prompt multiple choice en pantalla y devolver opcion elegida \n
    Entrada: titulo de prompt, lista de opciones \n
    Salida: numero de opcion elegida
    """

    print(titulo)
    for i in range(len(opciones)):
        print(f"[{i+1}] {opciones[i]}")
    opcion = int(input(msjSeleccione))
    while opcion <= 0 or opcion > len(opciones):
        print(msjNoExiste)
        opcion = int(input(msjSeleccione))
    return opcion

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
            return "LIMPIAR"
        
        if opcion == "N" or opcion == "n":
            print("¡¡Operacion Cancelada!!")
            print("Regresando...")
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
                                return
                            
                        if int(cantidad)>productosStock[index]:
                            print(f"\nSTOCK INSUFICIENTE ¡!")
                            return
                        else:
                            print("Caracter invalido¡!")
                            print("Regresando...")
                            return
                    else:
                        print("ingreses caracter valido ¡!")
                        print("Regresando...")
                        return
                else:
                    print ("Producto invalido!")
                    print("Regresando...")
                    return
                            
            else:
                print("ingrese caracter valido ¡!: ")
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

def verificarCorreo (nomFuncion):
    correo = input("Ingrese su correo electrónico: ")
    if "@" not in correo or "." not in correo:
        print("Correo electrónico inválido. Por favor, intente de nuevo.")
        return nomFuncion()
    return correo

def verificarContrasenia (nomFuncion):
    contrasenia = input("Ingrese su contraseña (mínimo 6 caracteres): ")
    if len(contrasenia) < 6:
        print("La contraseña debe tener al menos 6 caracteres. Por favor, intente de nuevo.")
        return nomFuncion()
    return contrasenia

def crearUsuario():
    nombre = input("Ingrese su nombre: ")
    correo = verificarCorreo(crearUsuario)
    contrasenia = verificarContrasenia(crearUsuario)
    yaExiste=False
    for i in range(len(usuarios)):
        if correo == usuarios[i][1]:   
            print("Ya existe un usuario con ese correo. Por favor, intente de nuevo.")
            yaExiste=True
            return crearUsuario()
    if (yaExiste == False):
        usuarios.append([nombre, correo, contrasenia])
        print(f"Bienvenid@ {nombre}! Tu cuenta se creó exitosamente.")

def iniciarSesion():
    nombre = input("Ingrese su nombre: ")
    correo = verificarCorreo(iniciarSesion)
    contrasenia = verificarContrasenia(iniciarSesion)
    usuarios.append([nombre, correo, contrasenia])
    print(f"Bienvenid@ de nuevo {nombre}!")

def mostrar(msj):
    print(msj)

# Función para el proceso de login o creación de usuario
def loginSignUp():
    print("1. Iniciar Sesión")
    print("2. Crear Usuario")
    opcion = input(msjSeleccione)
    if opcion == "1":
        iniciarSesion()
    elif opcion == "2":
        crearUsuario()
    else:
        while opcion not in ["1", "2"]:
            print(msjNoExiste)
            opcion = input(msjSeleccione)

# Función para elegir método de envío
def elegirEnvio():
    print("Seleccione el método de envío:")
    print("1. Envío estándar de 5 a 7 días hábiles")
    print("2. Envío express de 1 a 2 días hábiles")
    print("3. Retiro en el local")
    opcion = input(msjSeleccione)
    if opcion == "1":
        print("Seleccionaste envío estándar.")
    elif opcion == "2":
        print("Seleccionaste envío express.")
    elif opcion == "3":
        print("Seleccionaste retiro en el local.")
    else:
        while opcion not in ["1", "2", "3"]:
            print(msjNoExiste)
            opcion = input(msjSeleccione)
    return int(opcion)

# Generador de código de seguimiento random
def randomNumber():
    import random
    return str(random.randint(10000000000, 99999999999))

# Resumen compra
def mostrarMensajeFinal(compraEfectiva, tipoEnvio):
    if(compraEfectiva):
        if tipoEnvio == 1:
            mostrar("Seleccionaste envío estándar. Tu pedido llegará dentro de 5 a 7 días hábiles.")
            mostrar(f"El código de seguimiento de tu pedido es: {randomNumber()}")
        elif tipoEnvio == 2:
            mostrar("Seleccionaste envío express. Tu pedido llegará dentro de 1 a 2 días hábiles.")
            mostrar(f"El código de seguimiento de tu pedido es: {randomNumber()}")
        elif tipoEnvio == 3:
            mostrar("A partir de mañana vas a poder retirar tu pedido en nuestro local.")
            mostrar("Nuestro horario de atención es de lunes a viernes de 9 a 18 horas. Te esperamos!")
    else:
        mostrar("Gracias por visitar nuestro Ecommerce. Esperamos que vuelvas!")

# Mostrar productos disponibles
def verProductos(productos, productosCategoria, productosPrecio):
    opcion = mostrarPrompt("VER PRODUCTOS",["Ver todos los productos","Usar Buscador"])
    if opcion == 1:
        print("Productos disponibles:")
        for i in range(len(productos)):
            print(f"{i + 1}. {productos[i]} - Precio: ${productosPrecio[i]}")
    if opcion == 2:
        buscarProducto(productos, productosCategoria, productosPrecio)

def buscarProducto(productos, productosCategoria, productosPrecio):
    """
    Imprime todos los productos que coinciden con el nombre, la categoria o el precio definido por el usuario \n
    Entrada: listas paralelas de productos, productosCategoria y productosPrecio \n
    Salida: N/A, hace un print en pantalla
    """

    tipo = mostrarPrompt("BUSCAR POR...",["Nombre","Categoria","Precio"])
    prodNums = []

    if tipo == 1:
        nom = input("Ingrese el nombre del producto: ").lower()
        for i in range(len(productos)):
            if nom in productos[i].lower():
                prodNums.append(i)
    elif tipo == 2:
        cat = input("Ingrese la categoria del producto: ").lower()
        for i in range(len(productos)):
            if cat in productosCategoria[i].lower():
                prodNums.append(i)
    elif tipo == 3:
        tipoPrecio = mostrarPrompt("Seleccione forma de buscar por precio:", ["Igual","Mayor o Igual","Menor o Igual"])
        precio = float(input("Ingrese el precio del producto: "))
        for i in range(len(productosPrecio)):
            if tipoPrecio == 1:
                if precio == productosPrecio[i]:
                    prodNums.append(i)
            if tipoPrecio == 2:
                if precio <= productosPrecio[i]:
                    prodNums.append(i)
            if tipoPrecio == 3:
                if precio >= productosPrecio[i]:
                    prodNums.append(i)
    
    print("Productos disponibles:")
    for i in range(len(prodNums)):
        print(f"{i + 1}. {productos[prodNums[i]]} - Precio: ${productosPrecio[prodNums[i]]}")

def aplicarDescuento(productos, productosPrecio, productosId, productosDescuento):
    """
    Aplicar un descuento porcentual a un producto definido por el usuario \n
    Entrada: listas paralelas de productosId, productosPrecio, productosId y productosDescuento \n
    Salida: N/A, modifica la lista de productosDescuento
    """

    prod = int(input("Ingrese la id del producto a modificar: "))
    for i in range(len(productosId)):
        if productosId[i] == prod:
            print(f"producto seleccionado: {productos[i]} - Precio ${productosPrecio[i]} - Descuento actual {productosDescuento[i]}%")
            desc = int(input("Ingrese descuento: "))
            productosDescuento[i] = desc
    print (productosDescuento)

def modoAdmin(productos, productosStock):
    """
    Activar el menu de Administrador (Se accede a tal poniando ADMIN de usuario, n tarjeta y pin no importan
    Entrada: listas paralelas de productosId y  productosStock
    Salida: N/A, es la funcionalidad del menu nada mas
    """
    esAdministrador = True
    while esAdministrador:
        print("\nBienvenido, Administrador")
        print("[1] Ver productos")
        print("[2] Modificar Stock")
        print("[5] Salir")

        op = input("Opción: ")

        if op == "1":
            print("\nProductos disponibles:")
            for i in range(len(productos)):
                print(f"{i + 1}. {productos[i]} - Stock: {productosStock[i]}")
            input("\nPresione ENTER para volver al menu admin...")
        elif op == "2":
            for i in range(len(productos)):
                print(f"{i + 1}. {productos[i]} - Stock: {productosStock[i]}")
            prod = input("Ingrese el número del producto a modificar: ")
            if prod.isdigit():
                numProd = int(prod) - 1
                if 0 <= numProd < len(productos):
                    nuevo_stock = input(f"Ingrese nuevo stock para {productos[numProd]}: ")
                    if nuevo_stock.isdigit():
                        productosStock[numProd] = int(nuevo_stock)
                        print(f"Stock actualizado: {productos[numProd]} - {productosStock[numProd]}")
                    else:
                        print("Debe ingresar un número válido")
                else:
                    print("Producto inválido")
            else:
                print("Ingrese un número válido")


        elif op == '5':
            print("Saliendo del menu de admin...")
            esAdministrador = False

        else:
            print("Opción inválida")

def MenuComprar(carritoTotal, carrito, productos, productosPrecio, productosStock, confirmandoCompra, NomTarjetasEcommerce, PINTarjetasEcommerce, NumTarjetasEcommerce, CuentasEcommerce):
    CompraEfectiva = False
    confirmando=False
    comprando=True
    while confirmando==False: ##Bucle te mantiene dentro de la funcion comprar a menos que se confirme el carrito o Se presione la tecla para salir
        resultado = Comprar(carritoTotal, carrito, productos, productosPrecio, productosStock, comprando)
        if resultado == "P":
            confirmando=True
        elif resultado == "SALIR":
            break
        elif resultado is not None:##Si el usuario ingresa sus productos correctamente, se sumaran a su carrito siempre y cuando el producto exista (Not none)
            carritoTotal = carritoTotal+resultado
        else:
            print("ERROR!")
    if confirmando==True: ##Cuando se confirma el carrito...
        Pago= ConfirmarCompra(carrito, carritoTotal)
        comprando=False
        CompraRealizada=0
        if Pago == "Efectivo":
            CompraRealizada= PagarEfectivo(carrito, carritoTotal)
            if CompraRealizada=="COMPRA NUEVA":
                carrito=[]
                carritoTotal=0
                CompraEfectiva = True
                tipoEnvio = elegirEnvio()
                
        if Pago == "Tarjeta":## Si el pago es con tarjetaecommerce, la compra se añade a la lista de compras del socio Ecommerce
            CompraRealizada, idx = PagarTarjeta(carrito, carritoTotal, NomTarjetasEcommerce, PINTarjetasEcommerce, NumTarjetasEcommerce)
            if CompraRealizada=="COMPRANUEVA":
                CuentasEcommerce[idx][0].append(carrito[:])
                CuentasEcommerce[idx][1]+=carritoTotal
                carrito=[]
                carritoTotal=0
                CompraEfectiva = True
                tipoEnvio = elegirEnvio()
                VolverMenuPrincipal() 

        if str(Pago).startswith("BorrarUno"): ##Si el return empieza con BorrarUno
            partir=Pago.split(":") ##El return "BorrarUno:{indice a elminar}" se parte en dos mitades
            indice=int(partir[1]) ##Se toma la segunda mitad para solo tener el indice

            eliminar=carrito[indice]              ##Se extrae el fstring de la orden a eliminar 
            precio=eliminar.split("$")[-1].strip()## Para seguidamente extraer solo el precio de la orden 
            restar=int(precio)

            ##Devolver el stock al prodcuto
            ProdEliminar=eliminar.split("|")[0].strip()
            for i in range (len(productos)):
                if ProdEliminar == productos[i]:
                    idxtemp=i
            
            StockDevolver=eliminar.split("#")[-1].strip()
            StockDevolver=int(StockDevolver.split("|")[0].strip())
            productosStock[idxtemp]=productosStock[idxtemp]+StockDevolver
            carritoTotal=carritoTotal-restar 
            print(f"Eliminando: {carrito[indice]}")##Se quita la orden de la lista carrito y se resta el costo de la orden al total del carrito $
            carrito.pop(indice)
            VolverMenuPrincipal()

        if Pago == "LIMPIAR":
            carrito=[]
            carritoTotal=0
            VolverMenuPrincipal()
    return CompraEfectiva, tipoEnvio

def MenuMiCuenta(productos, productosStock, NomTarjetasEcommerce, PINTarjetasEcommerce, NumTarjetasEcommerce, CuentasEcommerce):
        idx=0
        nombre, NumTarjeta, Pin= SolicitarDatos()

        if nombre == "ADMIN": ##Si el nombre es admin, se saltea el resto, y va directo al menu
            modoAdmin(productos, productosStock)

        else:
            validacion, idx=validarTarjetaEcommerce(nombre, NumTarjeta, Pin, NomTarjetasEcommerce, PINTarjetasEcommerce, NumTarjetasEcommerce)
            if validacion == 3:
                continuar=MostarCuentaCliente(idx, CuentasEcommerce, nombre)
                if continuar=="CANCELAR DEUDA":
                    PagoDeudas=CancelarCuentaCliente(idx, CuentasEcommerce, nombre)
                    if PagoDeudas=="True":
                        pass


                else: 
                    print("ERROR al ingresar datos")
                    print ("Volver a intentar")
                    input("")

def VolverMenuPrincipal():
    print("\nPresione ENTER para volver al menu principal...")
    input("")