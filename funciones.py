msjSeleccione = "Seleccione una opción: "
msjNoExiste = "Opción no válida. Por favor, intente de nuevo."
PlazosCuotas=["3 Cuotas", "6 Cuotas", "8 Cuotas", "10 Cuotas"]
PlazosCuotNUM=[  3       ,  6        , 8        ,      10   ]
PorcentajeCuotas=[ "10%"   ,  "20%" ,   "30%"  ,     "40%"]
PagosCuotas=[     1.1     ,    1.2  ,    1.3    ,   1.40]

def mostrarLogo():
    '''
    Funcion de utilidad que imprime en pantalla el logo del ecommerce \n
    Entrada: N/A \n
    Salida: N/A
    '''
    print("  ______  _____ ____  __  __ __  __ ______ _____   _____ ______ ")
    print(" |  ____|/ ____/ __ \\|  \\/  |  \\/  |  ____|  __ \\ / ____|  ____|")
    print(" | |__  | |   | |  | | \\  / | \\  / | |__  | |__) | |    | |__   ")
    print(" |  __| | |   | |  | | |\\/| | |\\/| |  __| |  _  /| |    |  __|  ")
    print(" | |____| |___| |__| | |  | | |  | | |____| | \\ \\| |____| |____ ")
    print(" |______|\\_____\\____/|_|  |_|_|  |_|______|_|  \\_\\\\_____|______|")

def mostrarPrompt(titulo, opciones):
    '''
    Funcion de utilidad para mostrar un prompt multiple choice en pantalla y devolver opcion elegida.\n
    Entrada: `titulo` (str), `opciones` (list) - lista de opciones.\n
    Salida: `int` - numero de opcion elegida.
    '''
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

def randomNumber():
    '''
    Funcion de utilidad que devuelve un codigo de seguimiento aleatorio.\n
    Entrada: N/A\n
    Salida: `str` - string aleatorio entre "10000000000" y "99999999999".
    '''
    import random
    return str(random.randint(10000000000, 99999999999))

def crearUsuario(usuarios): 
    '''
    Crea un nuevo usuario solicitando nombre, email y contraseña.\n
    Entrada: `usuarios` (list) - lista donde se almacenan los usuarios.\n
    Salida: N/A - agrega el nuevo usuario a la lista `usuarios`.
    '''
    nombre = input("Ingrese su nombre: ")
    mail = input("Ingrese su mail electrónico: ")
    contrasenia = input("Ingrese su contraseña: ")

    # Ver si ya hay un usuario con este mail
    for usu in usuarios:
        if mail == usu["email"]:
            print("Ya existe un usuario con ese mail.")
            return crearUsuario(usuarios)

    nuevo_usuario = {
        "nombre": nombre,
        "email": mail,
        "password": contrasenia,
        "rol": "user"
    }
    usuarios.append(nuevo_usuario)
    print(f"Bienvenid@ {nombre}, tu cuenta fue creada exitosamente.")

def iniciarSesion(usuarios):
    '''
    Verifica las credenciales ingresadas e inicia sesión.\n
    Entrada: `usuarios` (list) - lista de diccionarios con claves `email`, `password` y `rol`.\n
    Salida: `bool` - `True` si el rol del usuario es `admin`, `False` en caso contrario.
    '''
    mail = input("Ingrese su correo electrónico: ")
    contrasenia = input("Ingrese su contraseña: ")

    for usu in usuarios:
        if usu["email"] == mail and usu["password"] == contrasenia:
            print(f"Bienvenid@ de nuevo {usu['nombre']}!")

            # Si es admin devuelve verdadero
            return usu["rol"] == "admin"

    print("Tu mail o contraseña son incorrectos.")
    return iniciarSesion(usuarios)

def loginSignUp(usuarios):
    '''
    Flujo que permite al usuario iniciar sesión o crear una nueva cuenta.\n
    Entrada: `usuarios` (list) - lista donde se buscan o agregan usuarios.\n
    Salida: `bool` - `True` si se inició sesión y el usuario es admin, `False` en los demás casos.
    '''
    opcion = mostrarPrompt("LOGIN",["Iniciar Sesión", "Crear Usuario"])
    if opcion == 1:
        es_admin = iniciarSesion(usuarios)
        return es_admin
    elif opcion == 2:
        crearUsuario(usuarios)
        return False
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
        return loginSignUp()

def MostrarMenu(esAdmin=False):
    '''
    Muestra el menú principal del ecommerce y devuelve la opción elegida.\n
    Entrada: `esAdmin` (bool) - si es True se añade la opción de modo admin.\n
    Salida: `int` - entero con la opción seleccionada por el usuario.
    '''
    mostrarLogo()
    print("------------------------------------------------------------------------")
    print("=======================================================================")
    print("E-Commerce⦿E-Commerce⦿E-Commerce⦿E-Commerce⦿E-Commerce⦿E-Commerce⦿")
    print("=======================================================================")

    opciones = ["Comprar", "Ver productos","Buscar Productos", "Ver MiCuentaEcommerce", "Salir"]

    if esAdmin:
        opciones.insert(4, "Modo Admin")  # queda como opción 4

    return mostrarPrompt("Bienvenido a la tienda virtual 🏪", opciones)

def verProductos(productos):
    '''
    Muestra la lista de productos en pantalla con su precio, stock y descuento aplicado (si corresponde).\n
    Entrada: `productos` (list) - lista de diccionarios con claves `id`, `nombre`, `precio`, `stock`, `descuento`.\n
    Salida: N/A
    '''
    print("--- Catálogo de Productos ---")
    for prod in productos:
        #Ver precio con descuento
        precio_final = prod["precio"]
        if prod["descuento"] > 0:
            precio_final -= (prod["precio"] * (prod["descuento"] / 100))
            promo = f"({prod['descuento']}% OFF)"
        else:
            promo = ""

        print(f"ID: {prod['id']} | Nombre: {prod['nombre']} | Precio: ${precio_final} {promo} | Stock: {prod['stock']} | Categoría: {prod['categoria']}")

def buscarProducto(productos):
    '''
    Devuelve una lista de productos filtrados segun lo que pide el usuario, la cual es enviada a verProductos.\n
    Entrada: `productos` (list) - lista de diccionarios con información de productos.\n
    Salida: `list` - lista filtrada de productos.
    '''
    tipo = mostrarPrompt("BUSCAR POR...",["Nombre","Categoria","Precio"])
    encontrados = []

    if tipo == 1:
        nom = input("Ingrese el nombre del producto: ").lower()
        for prod in productos:
            if nom in prod["nombre"].lower():
                encontrados.append(prod)
    elif tipo == 2:
        cat = input("Ingrese la categoria del producto: ").lower()
        for prod in productos:
            if cat in prod["categoria"].lower():
                encontrados.append(prod)
    elif tipo == 3:
        tipoPrecio = mostrarPrompt("Seleccione forma de buscar por precio:", ["Igual","Mayor o Igual","Menor o Igual"])
        precio = float(input("Ingrese el precio del producto: "))
        for prod in productos:
            if tipoPrecio == 1:
                if prod["precio"] == precio:
                    encontrados.append(prod)
            if tipoPrecio == 2:
                if prod["precio"] >= precio:
                    encontrados.append(prod)
            if tipoPrecio == 3:
                if prod["precio"] <= precio:
                    encontrados.append(prod)
    
    return encontrados

def CancelarCuentaCliente(idx, CuentasEcommerce, nombre):
    '''
    Funcion para que el cliente pueda cancelar su cuenta de compras realizadas en comodas cuotas.\n
    Entrada: `idx` (int) - indice de la cuenta del cliente en `CuentasEcommerce`, `CuentasEcommerce` (list) - lista de cuentas con compras y totales, `nombre` (str) - nombre del cliente.\n
    Salida: `str` - "True" si se procesa la opción de pago seleccionada.
    '''
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
    '''
    Funcion para mostrar la cuenta del cliente a consultar con previo ingreso de credenciales, muestra los tickets de compras anteriores con sus respectivos items y el total de su cuenta a pagar.\n
    Entrada: `idx` (int) - indice de la cuenta en `CuentasEcommerce`, `CuentasEcommerce` (list) - lista con compras previas y totales, `nombre` (str) - nombre del cliente.\n
    Salida: `str` - "CANCELAR DEUDA" si se elige cancelar, "Cancelado" en otro caso.
    '''

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
    '''
    Funcion para solicitar datos: `nombre`, `NumTarjeta`, `Pin`. Valida que se ingresen en el formato correcto.\n
    Entrada: N/A\n
    Salida: `tuple` - `(nombre, NumTarjeta, Pin)` si es valido; o `("ERROR", None, None)` / `("CANCELADO", None, None)` si falla o se cancela.
    '''
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
    '''
    Funcion para validar los datos ingresados por la funcion `SolicitarDatos`.\n
    Entrada: `nombre` (str), `NumTarjeta` (int), `Pin` (int), `NomTarjetasEcommerce` (list), `PINTarjetasEcommerce` (list), `NumTarjetasEcommerce` (list).\n
    Salida: `tuple` - `(validacion, idx)` donde `validacion` es 3 si es correcto o un mensaje de error, e `idx` es el indice asociado o `None`.
    '''
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
    '''
    Intenta procesar un pago usando las credenciales registradas de tarjeta ecommerce.\n
    Entrada: `carrito` (list), `carritoTotal` (int), `NomTarjetasEcommerce` (list), `PINTarjetasEcommerce` (list), `NumTarjetasEcommerce` (list).\n
    Salida: `tuple` - `(estado, idx)` donde `estado` es una cadena como "COMPRANUEVA" o "CANCELADO", e `idx` es el índice del socio validado en las listas de tarjetas (o `None`).
    '''
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
    '''
    Procesa un pago en efectivo solicitando al usuario el monto y calculando el vuelto.\n
    Entrada: `carrito` (list), `carritoTotal` (int).\n
    Salida: `str` - resultado: por ejemplo "COMPRA NUEVA" si se completó, "Abort" si se canceló.
    '''
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
    '''
    Muestra el contenido del carrito y ofrece opciones para confirmar o modificar la compra.\n
    Entrada: `carrito` (list), `carritoTotal` (int).\n
    Salida: `str`/`None` - puede devolver "Efectivo"/"Tarjeta"/"BorrarUno:{indice}"/"LIMPIAR" o `None` si se canceló.
    '''
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

def MenuComprar(carritoTotal, carrito, productos, NomTarjetasEcommerce, PINTarjetasEcommerce, NumTarjetasEcommerce, CuentasEcommerce):
    '''
    Flujo que gestiona la interacción para agregar productos al carrito y procesar la compra.\n
    Entrada: `carritoTotal` (int), `carrito` (list), `productos` (list), `NomTarjetasEcommerce` (list), `PINTarjetasEcommerce` (list), `NumTarjetasEcommerce` (list), `CuentasEcommerce` (list).\n
    Salida: `tuple` - puede retornar `(carritoTotal, 'BACK')` si se sale, o `(carritoTotal, True/False)` indicando si la compra fue realizada.
    '''
    confirmando=False
    comprando=True
    while confirmando==False: ##Bucle te mantiene dentro de la funcion comprar a menos que se confirme el carrito o Se presione la tecla para salir
        resultado=Comprar(carritoTotal, carrito, productos, comprando)
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
            CompraRealizada, idx = PagarTarjeta(carrito, carritoTotal, NomTarjetasEcommerce, PINTarjetasEcommerce, NumTarjetasEcommerce)
            if CompraRealizada=="COMPRANUEVA":
                CuentasEcommerce[idx][0].append(carrito[:])
                CuentasEcommerce[idx][1]+=carritoTotal
                carrito=[]
                carritoTotal=0
                return carritoTotal, True
            
            else: 
                return carritoTotal, False

        if str(Pago).startswith("BorrarUno"): ##Si el return empieza con BorrarUno
            eliminandoItem, carritoTotal=BorrarItemCarrito(Pago, carrito,productos, carritoTotal)
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
    
def LogicaCompra(carritoTotal, carrito, productos, NomTarjetasEcommerce, PINTarjetasEcommerce, NumTarjetasEcommerce, CuentasEcommerce):
    '''
    Orquesta el proceso completo de compra: invoca `MenuComprar`, solicita envío y muestra el resumen final si la compra fue efectiva.\n
    Entrada: `carritoTotal` (int), `carrito` (list), `productos` (list), `NomTarjetasEcommerce` (list), `PINTarjetasEcommerce` (list), `NumTarjetasEcommerce` (list), `CuentasEcommerce` (list).\n
    Salida: `int` - `carritoTotal` (actualizado) al finalizar el flujo.
    '''
    confirmandoCompra = False
    tipoEnvio = "N/A"

    carritoTotal, compraEfectiva = MenuComprar(carritoTotal, carrito, productos, confirmandoCompra, NomTarjetasEcommerce, PINTarjetasEcommerce, NumTarjetasEcommerce, CuentasEcommerce)
    if compraEfectiva==True:
        if tipoEnvio== "N/A":
            tipoEnvio=elegirEnvio()
        mostrarMensajeFinal(compraEfectiva,tipoEnvio)
    else:
        input(f"\nRegresando...")
    return carritoTotal     

def BorrarItemCarrito(Pago, carrito, productos, carritoTotal):
    '''
    Elimina un item del carrito a partir de una cadena `Pago` con formato "BorrarUno:{indice}".\n
    Entrada: `Pago` (str), `carrito` (list), `productos` (list), `carritoTotal` (int).\n
    Salida: `tuple` - ("CompraEliminada", `carritoTotal_actualizado`).
    '''

    partir=Pago.split(":") ##El return "BorrarUno:{indice a elminar}" se parte en dos mitades
    indice=int(partir[1]) ##Se toma la segunda mitad para solo tener el indice
    eliminar=carrito[indice]              ##Se extrae el fstring de la orden a eliminar 
    precio=eliminar.split("$")[-1].strip()## Para seguidamente extraer solo el precio de la orden 
    restar=int(precio)

    ##Devolver el stock al prodcuto
    ProdEliminar = eliminar.split("|")[0].strip()
    for i in range(len(productos)):
        if ProdEliminar == productos[i]["nombre"]:
            StockDevolver = eliminar.split("#")[-1].split("|")[0].strip()
            productos[i]["stock"] += int(StockDevolver)
            break
    carritoTotal=carritoTotal-restar 
    print(f"Eliminando: {carrito[indice]}")##Se quita la orden de la lista carrito y se resta el costo de la orden al total del carrito $
    carrito.pop(indice)
    input("ENTER...")
    return "CompraEliminada", carritoTotal

def Comprar(carritoTotal, carrito, productos, comprando):
    '''
    Interfaz que muestra los productos disponibles y permite agregarlos al carrito.\n
    Entrada: `carritoTotal` (int), `carrito` (list), `productos` (list), `comprando` (bool).\n
    Salida: `int`/`str`/`None` - puede devolver el total añadido, "P", "SALIR" o `None`.
    '''
    # Interfaz de compra
    while comprando == True:
        confirmando = 0
        print("------------------------------------------------------------------------")
        print("==========================================================================")
        print("E-Commerce⦿E-Commerce⦿E-Commerce⦿E-Commerce⦿E-Commerce⦿E-Commerce⦿")
        print("===========================COMPRA===========================================")
        print("Tu carrito es: $", carritoTotal)
        print("=" * 80)
        print(f"{'ID':^4} | {'PRODUCTO':<27} | {'PRECIO':<19} | {'STOCK':^10}")
        print("-" * 80)
        for i in range(len(productos)):
            p = productos[i]
            print(f"[{i + 1:^3}] {p['nombre']:<28} | Precio:  ${p['precio']:<8}  | Stock: {p['stock']:>8}")
        print("[ 0 ] SALIR")
        print("[ P ] Ver Carrito")
        #Anadir al carrito
        print("----------------AÑADIR AL CARRITO DE COMPRAS----------------")
        compra = (input("Ingrese el numero del producto que desea comprar: "))
        if compra == "p" or compra == "P":
            if carritoTotal > 0:
                return "P"
            else:
                print("Su carrito esta vacio ¡! ¡!")
                print("---------------------------------")
                return
        if compra == "0" or compra == 0:
            return "SALIR"
        ## SI el input no es 0(salir) o p(comprar) se continuan añadiendo productos
        else:
            if compra.isdigit() and int(compra) > 0:
                compra = int(compra)
                if compra > 0 and compra < (len(productos) + 1):
                    index = compra - 1
                    prod_sel = productos[index]
                    print("-------------------------------------------------------------------")
                    print(f"\nComprando Item: {prod_sel['nombre']} | ${prod_sel['precio']}")
                    cantidad = (input("UNIDADES A COMPRAR: "))
                    if cantidad.isdigit():
                        cantidad = int(cantidad)
                        if cantidad <= prod_sel['stock']:
                            total = prod_sel['precio'] * cantidad
                            total = int(total)
                            AñadirProducto = input(
                                f"Seguro que quiere añadir {cantidad} {prod_sel['nombre']} | Por un total de ${total} (S/N): ")
                            if AñadirProducto == "S" or AñadirProducto == "s":
                                carritoTotal = carritoTotal + total
                                # Modificamos el stock directamente en el diccionario
                                prod_sel['stock'] = prod_sel['stock'] - cantidad
                                orden = f"{prod_sel['nombre']:<28} | #{cantidad:<5} | ${total:<8}"
                                carrito.append(orden)
                                return int(total)
                            else:
                                print("Ingrese opcion valida por favor!")
                                print("Regresando...")
                                return
                        if cantidad > prod_sel['stock']:
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
                    print("Producto invalido!")
                    print("Regresando...")
                    return
            else:
                print("ingrese caracter valido ¡!: ")
                return

def elegirEnvio():
    '''
    Muestra opciones de envio y devuelve la seleccion del usuario.\n
    Entrada: N/A\n
    Salida: `int` - opcion elegida (1, 2 o 3).
    '''
    opcion = mostrarPrompt("METODO DE ENVIO", ["Envío estándar (5 a 7 días)","Envío express (1 a 2 días)","Retiro en el local"])

    if opcion == 1:
        print("Seleccionaste envío estándar.")
    elif opcion == 2:
        print("Seleccionaste envío express.")
    elif opcion == 3:
        print("Retiro en el local.")

    return opcion

def mostrarMensajeFinal(compraEfectiva, tipoEnvio):
    '''
    Muestra el resumen final de la compra según el tipo de envio.\n
    Entrada: `compraEfectiva` (bool), `tipoEnvio` (int).
    Salida: N/A
    '''
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

def MenuMiCuenta(productos, NomTarjetasEcommerce, PINTarjetasEcommerce, NumTarjetasEcommerce, CuentasEcommerce):
    '''
    Accede al menú de la cuenta del cliente verificando credenciales.\n
    Entrada: `productos` (list), `NomTarjetasEcommerce` (list), `PINTarjetasEcommerce` (list), `NumTarjetasEcommerce` (list), `CuentasEcommerce` (list).\n
    Salida: N/A - muestra la cuenta y permite cancelar deudas si corresponde.
    '''
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

def modoAdmin(productos):
    '''
    Activar el menu de Administrador (Se accede ingresando a la tienda con una cuenta con rol de admin).\n
    Entrada: `productos` (list) - lista de diccionarios con información de productos.\n
    Salida: N/A - funcionalidad del menu de administrador.
    '''
    while True:
        op = mostrarPrompt("Bienvenido, Administrador", ["Buscar productos","Modificar producto","Agregar producto","Salir"])
        
        if op == 1:
            buscarProducto(productos)
        elif op == 2:
            verProductos(productos)
            prodID = input("Ingrese el ID del producto a modificar: ")
            for prod in productos:
                if prodID == prod["id"]:
                    modificarProducto(prod)
        elif op == 3:
            agregarProducto(productos)
        elif op == 4:
            print("Saliendo del menu de admin...")
            break

def modificarProducto(producto):
    '''
    Modificar un producto existente, permitiendo cambiar precio, stock, descuento, categoria o nombre.\n
    Entrada: `producto` (dict) - diccionario con claves `id`, `nombre`, `precio`, `stock`, `descuento`, `categoria`.\n
    Salida: N/A - modifica el diccionario `producto`.
    '''
    print(f"Producto seleccionado: {producto['nombre']} - Precio ${producto['precio']} - Stock {producto['stock']} - Descuento {producto['descuento']}% - Categoria {producto['categoria']}")
    
    tipo = ["Precio", "Stock", "Descuento", "Categoria", "Nombre"]
    op = mostrarPrompt("¿Que modificar?", tipo)
    i = int(input(f"Nuevo {tipo[op-1]}: "))
    
    if tipo[op-1] in ["Precio", "Stock", "Descuento"]:
        i = int(i)

    producto[tipo[op-1].lower()] = i
    print(f"{tipo[op-1]} modificado correctamente. Nuevo valor: {i}")

def agregarProducto(productos):
    '''
    Agrega un nuevo producto a la lista, incluyendo precio, categoria y stock.\n
    Entrada: `productos` (list) - lista de diccionarios con información de productos.\n
    Salida: N/A - agrega un nuevo diccionario a la lista `productos` con un ID único generado automáticamente.
    '''
    nombre = input("Nombre del producto: ")
    categoria = input("Categoría: ")
    precio = int(input("Precio: "))
    stock = int(input("Stock: "))

    nuevoId = 0
    for prod in productos:
        if int(prod["id"]) > nuevoId:
            nuevoId = int(prod["id"])
    nuevoId = str(nuevoId + 1)

    producto_nuevo = {
        "id": nuevoId,
        "nombre": nombre,
        "precio": precio,
        "stock": stock,
        "descuento": 0,
        "categoria": categoria
    }
    productos.append(producto_nuevo)
    print(f"Producto '{nombre}' agregado correctamente.")
