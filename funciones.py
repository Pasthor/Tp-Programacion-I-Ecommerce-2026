msjSeleccione = "Seleccione una opción: "
msjNoExiste = "Opción no válida. Por favor, intente de nuevo."
PlazosCuotas=["3 Cuotas", "6 Cuotas", "8 Cuotas", "10 Cuotas"]
PlazosCuotNUM=[  3       ,  6        , 8        ,      10   ]
PorcentajeCuotas=[ "10%"   ,  "20%" ,   "30%"  ,     "40%"]
PagosCuotas=[     1.1     ,    1.2  ,    1.3    ,   1.40]

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
    
    opcion = input(msjSeleccione)
    while not opcion.isdigit():
        print(msjNoExiste)
        opcion = input(msjSeleccione)

    opcion = int(opcion)
    while opcion <= 0 or opcion > len(opciones):
        print(msjNoExiste)
        opcion = int(input(msjSeleccione))
        
    return opcion
"""
def verificarCorreo (nomFuncion): # Que cumpla con las condiciones de un correo electronico
    correo = input("Ingrese su correo electrónico: ")
    if "@" not in correo or "." not in correo:
        print("Correo electrónico inválido. Por favor, intente de nuevo.")
        return nomFuncion()
    return correo

def verificarContrasenia (nomFuncion): # Que cumpla con las condiciones de una contraseña
    contrasenia = input("Ingrese su contraseña (mínimo 6 caracteres): ")
    if len(contrasenia) < 6:
        print("La contraseña debe tener al menos 6 caracteres. Por favor, intente de nuevo.")
        return nomFuncion()
    return contrasenia
"""
# Generador de código de seguimiento random
def randomNumber():
    import random
    return str(random.randint(10000000000, 99999999999))

def crearUsuario(usuarios): 
    nombre = input("Ingrese su nombre: ")

    #correo = verificarCorreo(crearUsuario)
    #contrasenia = verificarContrasenia(crearUsuario)
    correo = input("Ingrese su correo electrónico: ")
    contrasenia = input("Ingrese su contraseña (mínimo 6 caracteres): ")

    for i in range(len(usuarios)):
        if correo == usuarios[i][1]:   
            print("Ya existe un usuario con ese correo. Por favor, intente de nuevo.")
            return crearUsuario(usuarios) # Si ya existe, debe volver a arrancar con el proceso de Sign Up
    #Si sale del for el usuario no existe
    usuarios.append([nombre, correo, contrasenia, "user"])
    print(f"Bienvenid@ {nombre}! Tu cuenta se creó exitosamente.")

def iniciarSesion(usuarios):
    #correo = verificarCorreo(iniciarSesion)
    correo = input("Ingrese su correo electrónico: ")

    contrasenia = input("Ingrese su contraseña: ")
    for i in range(len(usuarios)):
        if usuarios[i][1] == correo and usuarios[i][2] == contrasenia:
            print(f"Bienvenid@ de nuevo {usuarios[i][0]}!")
            inicioSesion = True
            if usuarios[i][3] == "admin":
                return True  # es admin
            else:
                return False # no es admin
    # Si sale del for el input fue invalido
    print("Correo o contraseña incorrectos. Por favor, intente de nuevo.")
    iniciarSesion(usuarios) # Si ingresa datos mal, debe volver a empezar con el proceso de Login

# Función para el proceso de login o creación de usuario
def loginSignUp():
    opcion = mostrarPrompt("LOGIN",["Iniciar Sesión", "Crear Usuario"])
    if opcion == 1:
        return True
    elif opcion == 2:
        return False
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
        return loginSignUp()

def MostrarMenu(esAdmin=False):
    mostrarLogo()
    print("------------------------------------------------------------------------")
    print("=======================================================================")
    print("E-Commerce⦿E-Commerce⦿E-Commerce⦿E-Commerce⦿E-Commerce⦿E-Commerce⦿")
    print("=======================================================================")

    opciones = ["Comprar", "Ver productos", "Ver MiCuentaEcommerce", "Salir"]

    if esAdmin:
        opciones.insert(3, "Modo Admin")  # queda como opción 4

    return mostrarPrompt("Bienvenido a la tienda virtual 🏪", opciones)

# Mostrar productos disponibles
def verProductos(productos, productosCategoria, productosPrecio, productosStock, productosId, productosDescuento):
    opcion = mostrarPrompt("VER PRODUCTOS",["Ver todos los productos","Usar Buscador"])
    if opcion == 1:
        print("Productos disponibles:")
        for i in range(len(productos)):
            if productosDescuento[i] > 0:
                print(f"ID{productosId[i]} - {productos[i]} - Precio: ${productosPrecio[i]-(productosPrecio[i]*(productosDescuento[i]/100))} ({productosDescuento[i]}% OFF) - Stock: {productosStock[i]} - Categoría: {productosCategoria[i]}")
            else:
                print(f"ID{productosId[i]} - {productos[i]} - Precio: ${productosPrecio[i]} - Stock: {productosStock[i]} - Categoría: {productosCategoria[i]}")
    if opcion == 2:
        buscarProducto(productos, productosCategoria, productosPrecio, productosStock, productosId, productosDescuento)

def buscarProducto(productos, productosCategoria, productosPrecio, productosStock, productosId, productosDescuento):
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
        if productosDescuento[prodNums[i]] > 0:
            print(f"ID{productosId[prodNums[i]]} - {productos[prodNums[i]]} - Precio: ${productosPrecio[prodNums[i]]-(productosPrecio[prodNums[i]]*(productosDescuento[prodNums[i]]/100))} ({productosDescuento[prodNums[i]]}% OFF) - Stock: {productosStock[prodNums[i]]} - Categoría: {productosCategoria[prodNums[i]]}")
        else:
            print(f"ID{productosId[prodNums[i]]} - {productos[prodNums[i]]} - Precio: ${productosPrecio[prodNums[i]]} - Stock: {productosStock[prodNums[i]]} - Categoría: {productosCategoria[prodNums[i]]}")

def CancelarCuentaCliente(idx, CuentasEcommerce, nombre):
    """"
    Funcion para que el cliente pueda cancelar su cuenta de compras realizadas en comodas cuotas 

    Entradas: idx(previamente se hace una validacion de datos con la cual extraemos el indice de la cuenta del cliente en caso exista)
              CuentasEcommerce(Lista de listas donde se encuentran las compras del cliente y el total de sus compras)
              nombre(Nombre del cliente)
    """""
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
    """"
    Funcion para mostrar la cuenta del cliente a consultar con previo ingreso de credenciales, muestra los tickets de compras anteriores con sus respectivos
    items y el total de su cuenta a pagar
    
    Entradas: idx(previamente se hace una validacion de datos con la cual extraemos el indice de la cuenta del cliente en caso exista)
              CuentasEcommerce(Lista de listas donde se encuentran las compras del cliente y el total de sus compras)
              nombre(Nombre del cliente)  
    """""

    for i in range(len(CuentasEcommerce[idx][0])): ##Ingresa a la lista del cliente donde se almacenan sus compras previas
        print(f"\n--- TICKET NRO {i+1} ---")  
        print(f"Socio Ecommerce: {nombre}")     ##Imprime las compras previas por separado             
        for producto in CuentasEcommerce[idx][0][i]: ##Imprime cada item dentro de las listas de compras previas 
            print(f"  • {producto}")
    
    print(f"\n  •TOTAL DE CUENTA ECOMMERCE: ${CuentasEcommerce[idx][1]}")
    opcion = mostrarPrompt("¿Qué desea hacer?", ["Cancelar cuenta", "Salir"])
    if opcion == 1:
        return "CANCELAR DEUDA"
    else:
        return "Cancelado"

def SolicitarDatos():
    """"
    Funcion para solicitar datos: Nombre, NumTarjeta, PIN unicamente valida que se ingresen los datos en el formato correcto
    Entradas: -
    Salidas: Nombr, NumTarjeta, Pin o Error si se ingresan mal
    
    """""
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
    """"
    Funcion para validar los datos ingresados por la funcion SolicitarDatos()
    Entradas: nombre, NumTarjeta, Pin (Datos ingresados en la funcion SolicitarDatos
                NomTarjetasEcommerce, PINTarjetasEcommerce, NumTarjetasEcommerce 
                (Listas de datos con credenciales de clientes)
    Salidas:  Validacion (Confirma si los datos ingresados fueron coincidentes con un cliente actual de nuestrs 
                         datos)
              idx: indice del cliente 
    """""
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

def PagarTarjeta(carritoTotal, NomTarjetasEcommerce, PINTarjetasEcommerce, NumTarjetasEcommerce):
    """""
    Funcion para pagar una compra con el metodo de pago Tarjeta Ecommerce (añadir a la cuenta Ecommerce
    del cliente el monto y los productos comprados)
    - Primero se le solicita al usuario sus datos
    - Los datos se validan
    - Si la validacion fue correcta la compra se realiza

    Entradas: carritoTotal, NomTarjetasEcommerce, PINTarjetasEcommerce, NumTarjetasEcommerce
    Salidas: CompraNueva (confirma si la compra fue realizada o no)
             idx (el indice del cliente que realizo la compra para luego añadir la compra a su cuenta)
    """""
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
            opcion = mostrarPrompt("No se pudo procesar el pago", ["Intentar de nuevo", "Salir"])
            if opcion == 1:
                continue
            else:
                return "CANCELADO", None

def PagarEfectivo(carrito, carritoTotal):
    """""
    Funcion para pagar con el metodo de pago "Efectivo"
    Se despliega interfaz de la cuenta a pagar 
    A continuacion se ingresa el monto con el que se esta pagando
    Por ultimo se calcula el vuelto
    
    Entradas: carrito, carritoTotal
    Salidas:  CompraNueva (confirma si la compra se realizo)
              o error en caso de fallo
    """""
    print(f"\n==================================================================")
    print("Calculando Pago y vuelto con Efectivo--------------------")
    print("000 Para Cancelar")
    print(f"\n   Pago en total: {carritoTotal}")
    pago=input(f"\n Con cuanto esta pagando: $")
    print("")
    if pago.isdigit():
    ##Control de entrada teclado, el programa solo continua si se ingresa un numero
        pago=int(pago)
        if pago == "000":
            return "Abort" 
        else:
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
        return PagarEfectivo(carrito, carritoTotal)

def ConfirmarCompra(carrito, carritoTotal):
    """""
    Muestra la interfaz de confirmar carrito de compras, enlista los productos añadidos al carrito, su cantidad
    y precio total de cada uno, permite seleccionar metodo de pago y eliminar un producto del carrito o limpiar
    todo el carrito

    Entradas:carrito, carritoTotal
    Salidas:
    
    """""
    print("")
    ##Interfaz del carrito de compras/Confirma Compra
    print("|-|-|-|-|-|-|--Comprar carrito--|-|-|-|-|-|-|-|")
    for i in range (len(carrito)):
        print("Ob#",i, carrito[i])
    print(f"\nEl total de su compra es de: $ {carritoTotal}")
    print("")
    print("--------------------------------")
    op = mostrarPrompt("Opciones del carrito", ["Confirmar Carrito","Quitar Item","Limpiar carrito"])

    if op == 1 : ##CONFIRMAR COMPRA
        print("Confirmar Carrito de compras?")
        print("--------------------------------")
        while True:
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
            else:
                print("ERROR¡!")
                continue
    elif op == 2: ##BORRAR UN ELEMENTO
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
    elif op == 3: ##LIMPIA TOTAL DEL CARRITO
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
        print("ERROR")

def MenuComprar(carritoTotal, carrito, productos, productosPrecio, productosStock, confirmandoCompra, NomTarjetasEcommerce, PINTarjetasEcommerce, NumTarjetasEcommerce, CuentasEcommerce):
    confirmando=False
    comprando=True
    while confirmando==False: ##Bucle te mantiene dentro de la funcion comprar a menos que se confirme el carrito o Se presione la tecla para salir
        resultado=Comprar(carritoTotal, carrito, productos, productosPrecio, productosStock, comprando)
        if resultado == "P":
            confirmando=True
            break
        elif resultado == "SALIR":
            return carritoTotal, "BACK"
            
        elif resultado is not None:##Si el usuario ingresa sus productos correctamente, se sumaran a su carrito siempre y cuando el producto exista (Not none)
            carritoTotal = carritoTotal+resultado
        else:
            print("ERROR!")
    if confirmando==True: ##Cuando se confirma el carrito...
        Pago=ConfirmarCompra(carrito, carritoTotal)
        comprando=False
        CompraRealizada=0

        if Pago == "Efectivo":
            CompraRealizada=PagarEfectivo(carrito, carritoTotal)
            if CompraRealizada=="COMPRA NUEVA":
                carrito=[]
                carritoTotal=0
                return carritoTotal, True
            else: 
                return carritoTotal, False
                  
        if Pago == "Tarjeta":## Si el pago es con tarjetaecommerce, la compra se añade a la lista de compras del socio Ecommerce
            CompraRealizada, idx = PagarTarjeta(carritoTotal, NomTarjetasEcommerce, PINTarjetasEcommerce, NumTarjetasEcommerce)
            if CompraRealizada=="COMPRANUEVA":
                CuentasEcommerce[idx][0].append(carrito[:])
                CuentasEcommerce[idx][1]+=carritoTotal
                carrito=[]
                carritoTotal=0
                return carritoTotal, True
            
            else: 
                return carritoTotal, False

        if str(Pago).startswith("BorrarUno"): ##Si el return empieza con BorrarUno
            eliminandoItem, carritoTotal=BorrarItemCarrito(Pago, carrito, productosStock,productos, carritoTotal)
            if eliminandoItem == "CompraEliminada":
                return carritoTotal, False


        if Pago == "LIMPIAR":
            carrito=[]
            carritoTotal=0
            input("ENTER...")
            return carritoTotal, False
        else:
            return carritoTotal, True
    else:
        return carritoTotal, True
    
def LogicaCompra(carritoTotal, carrito, productos, productosPrecio, productosStock, NomTarjetasEcommerce, PINTarjetasEcommerce, NumTarjetasEcommerce, CuentasEcommerce):
    
    confirmandoCompra = "" 
    tipoEnvio = "N/A"

    carritoTotal, compraEfectiva = MenuComprar(carritoTotal, carrito, productos, productosPrecio, productosStock, confirmandoCompra, NomTarjetasEcommerce, PINTarjetasEcommerce, NumTarjetasEcommerce, CuentasEcommerce)
    if compraEfectiva==True:
        if tipoEnvio== "N/A" or not tipoEnvio:
            tipoEnvio=elegirEnvio()
        mostrarMensajeFinal(compraEfectiva,tipoEnvio)
    else:
        input(f"\nRegresando...")
    return carritoTotal     


def BorrarItemCarrito(Pago, carrito, productosStock,productos, carritoTotal):

    partir=Pago.split(":") ##El return "BorrarUno:{indice a elminar}" se parte en dos mitades
    indice=int(partir[1]) ##Se toma la segunda mitad para solo tener el indice
    eliminar=carrito[indice]              ##Se extrae el fstring de la orden a eliminar 
    precio=eliminar.split("$")[-1].strip()## Para seguidamente extraer solo el precio de la orden 
    restar=int(precio)

    ##Devolver el stock al prodcuto
    ProdEliminar=eliminar.split("|")[0].strip()
    for i in range (len(productos)):
        if ProdEliminar == productos[i]: ##Busca index del producto a devolver comparando el nombre de la orden con todos los prod en productos(lista)
            idxtemp=i
        
    StockDevolver=eliminar.split("#")[-1].strip()
    StockDevolver=int(StockDevolver.split("|")[0].strip())
    productosStock[idxtemp]=productosStock[idxtemp]+StockDevolver

    carritoTotal=carritoTotal-restar 
    print(f"Eliminando: {carrito[indice]}")##Se quita la orden de la lista carrito y se resta el costo de la orden al total del carrito $
    carrito.pop(indice)
    input("ENTER...")
    return "CompraEliminada", carritoTotal

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
        if compra == "0" or compra == 0:
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

# Función para elegir método de envío
def elegirEnvio():
    opcion = mostrarPrompt("METODO DE ENVIO", ["Envío estándar (5 a 7 días)","Envío express (1 a 2 días)","Retiro en el local"])

    if opcion == 1:
        print("Seleccionaste envío estándar.")
    elif opcion == 2:
        print("Seleccionaste envío express.")
    elif opcion == 3:
        print("Retiro en el local.")

    return opcion

# Resumen compra
def mostrarMensajeFinal(compraEfectiva, tipoEnvio):
    if compraEfectiva == True:
        print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
        if tipoEnvio == 1:
            print("Seleccionaste envío estándar. Tu pedido llegará dentro de 5 a 7 días hábiles.")
            print(f"El código de seguimiento de tu pedido es: {randomNumber()}")
        elif tipoEnvio == 2:
            print("Seleccionaste envío express. Tu pedido llegará dentro de 1 a 2 días hábiles.")
            print(f"El código de seguimiento de tu pedido es: {randomNumber()}")
        elif tipoEnvio == 3:
            print("A partir de mañana vas a poder retirar tu pedido en nuestro local.")
            print("Nuestro horario de atención es de lunes a viernes de 9 a 18 horas. Te esperamos!")
    else:
        print("Gracias por visitar nuestro Ecommerce. Esperamos que vuelvas!")

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
    Activar el menu de Administrador (Se accede ingresando a la tienda con una cuenta con rol de admin)
    Entrada: listas paralelas de productosId y  productosStock
    Salida: N/A, es la funcionalidad del menu nada mas
    """
    while True:
        op = mostrarPrompt("Bienvenido, Administrador", ["Ver productos","Modificar stock","Salir"])
        
        if op == 1:
            print("\nProductos disponibles:")
            for i in range(len(productos)):
                print(f"{i + 1}. {productos[i]} - Stock: {productosStock[i]}")
            input("\nPresione ENTER para volver al menu admin...")
        elif op == 2:
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
        elif op == 3:
            print("Saliendo del menu de admin...")
            break


def MenuMiCuenta(NomTarjetasEcommerce, PINTarjetasEcommerce, NumTarjetasEcommerce, CuentasEcommerce):
        """""
        Funcion para mostrar 
        """""
        
        idx=0
        nombre, NumTarjeta, Pin= SolicitarDatos()

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

def modoAdmin(productos, productosCategoria, productosPrecio, productosStock, productosId, productosDescuento):
    """
    Activa el menu de Administrador (Se accede ingresando a la tienda con una cuenta con rol de admin)
    Entrada: listas paralelas de productos, productosCategoria, productosPrecio, productosStock, productosId y productosDescuento.
    Salida: N/A, es la funcionalidad del menu nada mas
    """
    while True:
        op = mostrarPrompt("Bienvenido, Administrador", ["Ver productos","Modificar stock","Modificar precio","Agregar producto","Salir"])
        
        if op == 1:
            verProductos(productos, productosCategoria, productosPrecio, productosStock, productosId, productosDescuento)
        elif op == 2:
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
        elif op == 3:
            for i in range(len(productos)):
                print(f"{i + 1}. {productos[i]} - Precio: ${productosPrecio[i]}")
            prod = input("Ingrese producto: ")
            if prod.isdigit():
                numProd = int(prod) - 1
                if 0 <= numProd < len(productos):
                    nuevo_precio = input("Nuevo precio: ")
                    if nuevo_precio.isdigit():
                        productosPrecio[numProd] = int(nuevo_precio)
                        print("Precio actualizado.")
        elif op == 4:
            agregarProducto(productos, productosCategoria, productosPrecio, productosStock, productosId,productosDescuento)
        elif op == 5:
                print("Saliendo del menu de admin...")
                break

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

def agregarProducto(productos, productosCategoria, productosPrecio, productosStock, productosId, productosDescuento):
    """
    Agrega un nuevo producto a la lista, inclutendo precio, categoria y stock
    Entrada: listas paralelas de productos, productosCategoria, productosPrecio, productosStock, productosId y productosDescuento.
    Salida: N/A, modifica las listas agregando un nuevo producto.
    """
    nombre = input("Nombre del producto: ")
    categoria = input("Categoría: ")
    precio = input("Precio: ")
    stock = input("Stock: ")
    if precio.isdigit() and stock.isdigit():
        nuevoId = max(productosId) + 1
        productos.append(nombre)
        productosCategoria.append(categoria)
        productosPrecio.append(int(precio))
        productosStock.append(int(stock))
        productosId.append(nuevoId)
        productosDescuento.append(0)
        print(f"Producto '{nombre}' agregado correctamente.")
    else:
        print("Precio y stock deben ser números.")

def VolverMenuPrincipal():
    print("\nPresione ENTER para volver al menu principal...")
    input("")
