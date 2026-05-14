msjSeleccione = "Seleccione una opción: "
msjNoExiste = "Opción no válida. Por favor, intente de nuevo."
PlazosCuotas=["3 Cuotas", "6 Cuotas", "8 Cuotas", "10 Cuotas"]
PlazosCuotNUM=[  3       ,  6        , 8        ,      10   ]
PorcentajeCuotas=[ "10%"   ,  "20%" ,   "30%"  ,     "40%"]
PagosCuotas=[     1.1     ,    1.2  ,    1.3    ,   1.40]

# Utilidades
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

def calcularCarritoTotal(carrito):
    carritoTotal = 0
    for producto in carrito:
        carritoTotal += producto["precio_final"]
    return carritoTotal

# Login/Signup
def loginSignUp(usuarios):
    '''
    Flujo que permite al usuario iniciar sesión o crear una nueva cuenta.\n
    Entrada: `usuarios` (list) - lista donde se buscan o agregan usuarios.\n
    Salida: `dict` - el diccionario del usuario logeado después de iniciar sesión o crear una cuenta.
    '''
    opcion = mostrarPrompt("LOGIN",["Iniciar Sesión", "Crear Usuario"])
    if opcion == 1:
        usuarioLogeado = iniciarSesion(usuarios)
        return usuarioLogeado
    elif opcion == 2:
        usuarioLogeado = crearUsuario(usuarios)
        return usuarioLogeado
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
        return loginSignUp()

def crearUsuario(usuarios): 
    '''
    Crea un nuevo usuario solicitando nombre, email y contraseña.\n
    Entrada: `usuarios` (list) - lista donde se almacenan los usuarios.\n
    Salida: `dict` - el diccionario del nuevo usuario creado.
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
        "es_admin": False,
        "cuenta": {"ordenes": [], "deuda": 0, "Historial": []}
    }
    usuarios.append(nuevo_usuario)
    print(f"Bienvenid@ {nombre}, tu cuenta fue creada exitosamente.")
    return nuevo_usuario

def iniciarSesion(usuarios):
    '''
    Verifica las credenciales ingresadas e inicia sesión.\n
    Entrada: `usuarios` (list) - lista de diccionarios con claves `email`, `password` y `es_admin`.\n
    Salida: `dict` - el diccionario del usuario logeado
    '''
    mail = input("Ingrese su correo electrónico: ")
    contrasenia = input("Ingrese su contraseña: ")

    for usu in usuarios:
        if usu["email"] == mail and usu["password"] == contrasenia:
            print(f"Bienvenid@ de nuevo {usu['nombre']}!")
            return usu

    print("Tu mail o contraseña son incorrectos.")
    return iniciarSesion(usuarios)

# Menu Principal
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

# Ver/Buscar Productos
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
        encontrados = list(filter(lambda prod: nom in prod["nombre"].lower(), productos))
    elif tipo == 2:
        cat = input("Ingrese la categoria del producto: ").lower()
        encontrados = list(filter(lambda prod: cat in prod["categoria"].lower(), productos))
    elif tipo == 3:
        tipoPrecio = mostrarPrompt("Seleccione forma de buscar por precio:", ["Igual","Mayor o Igual","Menor o Igual"])
        precio = float(input("Ingrese el precio del producto: "))
        if tipoPrecio == 1:
            encontrados = list(filter(lambda prod: prod["precio"] == precio, productos))
        if tipoPrecio == 2:
            encontrados = list(filter(lambda prod: prod["precio"] >= precio, productos))
        if tipoPrecio == 3:
            encontrados = list(filter(lambda prod: prod["precio"] <= precio, productos))

    return encontrados

# Compra

def MenuComprar(carrito, productos, usuarioLogeado, cupones):
    '''
    Flujo que gestiona la interacción para agregar productos al carrito y procesar la compra.\n
    Entrada: `carritoTotal` (int), `carrito` (list), `productos` (list), `cupones` (list).\n
    Salida: `carritoTotal` modificado después de agregar productos o procesar la compra.
    '''
    while True:
        print("-"*30)
        op = mostrarPrompt("Menu de Compra", ["Ver Carrito", "Agregar Productos a Carrito", "Quitar Productos de Carrito", "Confirmar Compra", "Salir"])
        print("-"*30)
        if op == 1:
            verCarrito(carrito)
        elif op == 2:
            agregarCarrito(carrito, productos)
        elif op == 3:
            borrarCarrito(carrito, productos)
        elif op == 4:
            confirmarCompra(carrito, usuarioLogeado, cupones)
        elif op == 5:
            return


def verCarrito(carrito):
    '''
    Muestra el contenido del carrito y ofrece opciones para confirmar o modificar la compra.\n
    Entrada: `carrito` (list), `carritoTotal` (int).\n
    Salida: N/A - muestra el carrito y el total, no modifica los datos.
    '''
    print("|-|-|-|-|-|-|-- Carrito --|-|-|-|-|-|-|-|")
    
    for prod in carrito:
        if prod["descuento"] > 0:
            promo = f"({prod['descuento']}% OFF)"
        else:
            promo = ""
        print(f"{prod['nombre']} | Precio: ${prod['precio_descuento']} {promo} | Cantidad: {prod['stock']} | Total: ${prod['precio_final']}")
    print(f"\nEl total de su compra es de: $ {calcularCarritoTotal(carrito)}")
    print("--------------------------------")


def agregarCarrito(carrito, productos):
    '''
    Interfaz que muestra los productos disponibles y permite agregarlos al carrito.\n
    Entrada: `carritoTotal` (int), `carrito` (list), `productos` (list), `cupones` (list).\n
    Salida: `carritoTotal` modificado.
    '''
    while True:
        # Interfaz de carrito
        print("=" * 80)
        print("Tu carrito es: $", calcularCarritoTotal(carrito))
        print("=" * 80)
        print(f"{'':^4} | {'PRODUCTO':<27} | {'PRECIO':<19} | {'STOCK':^10}")
        print("-" * 80)
        for i in range(len(productos)):
            p = productos[i]
            print(f"[{i + 1:^3}] {p['nombre']:<28} | Precio:  ${p['precio']:<8}  | Stock: {p['stock']:>8}")
        print("[ 0 ] SALIR")

        # Anadir al carrito
        print("----------------AÑADIR AL CARRITO DE COMPRAS----------------")
        compra = input("Ingrese el numero del producto que desea comprar: ")
        if compra == "0":
            return
        ## Si el input no es 0(salir) se continuan añadiendo productos
        else:
            if compra.isdigit() and int(compra) > 0:
                compra = int(compra)
                if compra > 0 and compra <= len(productos):
                    prod_sel = productos[compra-1]
                    print("-------------------------------------------------------------------")
                    print(f"\nComprando Item: {prod_sel['nombre']} | ${prod_sel['precio']}")
                    cantidad = (input("UNIDADES A COMPRAR: "))
                    if cantidad.isdigit():
                        cantidad = int(cantidad)
                        if cantidad <= prod_sel['stock']:
                            total = round((prod_sel["precio"] - (prod_sel["precio"] * (prod_sel["descuento"] / 100)))*cantidad, 2)
                            agregar = input(f"Seguro que quiere añadir {cantidad} {prod_sel['nombre']} | Por un total de ${total} (S/N): ")
                            if agregar.lower() == "s":
                                # Modificamos los valores directamente en el diccionario
                                prod_sel['stock'] -= cantidad
                                # Crear diccionario de orden
                                orden = {}
                                orden.update(prod_sel)
                                orden.update({"stock": cantidad})
                                orden.update({"precio_descuento": (prod_sel["precio"] - (prod_sel["precio"] * (prod_sel["descuento"] / 100)))})
                                orden.update({"precio_final": (prod_sel["precio"] - (prod_sel["precio"] * (prod_sel["descuento"] / 100)))*cantidad})
                                orden.update({"msj": f"{prod_sel['nombre']:25}  #{cantidad:<8}  ${orden['precio_final']:>10.2f}"})
                                # Modificar orden existente o agregar a carrito
                                existe = False
                                for item in carrito:
                                    if item["id"] == orden["id"]:
                                        item["stock"] += orden["stock"]
                                        item["precio_final"] += orden["precio_final"]
                                        existe = True
                                if not existe:
                                    carrito.append(orden)
                            else:
                                print("Cancelado!")
                        elif cantidad > prod_sel['stock']:
                            print(f"Stock insuficiente!")
                        else:
                            print("Caracter invalido!")
                    else:
                        print("ingreses caracter valido!")
                else:
                    print("Producto invalido!")
            else:
                print("ingrese caracter valido!")

def borrarCarrito(carrito, productos):
    '''
    Borra un producto del carrito o limpia el carrito entero según la elección del usuario.\n
    Entrada: `carrito` (list), `carritoTotal` (int), `productos` (list).\n
    Salida: `carritoTotal` modificado después de eliminar productos.
    '''
    op = mostrarPrompt("¿Quitar solo 1 item o limpiar carrito entero?", ["Quitar Item","Limpiar carrito"])
    if op == 1: ##BORRAR UN ELEMENTO
        verCarrito(carrito)
        prompt = [item["nombre"] for item in carrito]
        elimIndice = (mostrarPrompt("---------Eliminando un item----------", prompt) - 1)

        for prod in productos:
            if carrito[elimIndice]["id"] == prod["id"]:
                prod["stock"] += carrito[elimIndice]["stock"]

        carrito.pop(elimIndice)
    elif op == 2: ##LIMPIA TOTAL DEL CARRITO
        verCarrito(carrito)
        print("Confirmar limpia del carrito de compras?")
        print("----------------------------------------")
        opcion = input("S/N: ")
        if opcion.lower() == "s":
            for item in carrito:
                for prod in productos:
                    if item["id"] == prod["id"]:
                        prod["stock"] += item["stock"]
            carrito.clear()
            print("Carrito Limpio ✓")
        if opcion == "N" or opcion == "n":
            print("¡¡Operacion Cancelada!!")

def confirmarCompra(carrito, usuarioLogeado, cupones):
    '''
    Confirma la compra del carrito y procesa el pago.\n
    Entrada: `carrito` (list), `carritoTotal` (int).\n
    Salida: `carritoTotal` modificado después de procesar la compra.
    '''
    print("Confirmar Carrito de compras?")
    print("--------------------------------")
    opcion = input("S/N: ")

    if opcion.lower() == "s":
        print("")
        print("- - - - - - - - - - - - - - - - - - - - - ")
        print("$$ Inciando Checkout $$")
        hayCupon = input("¿Tiene un cupón de descuento? (S/N): ")
        if hayCupon.lower() == "s":
            carrito = aplicarCupon(carrito, cupones)

        op= mostrarPrompt("Seleccione metodo de pago...", ["Tarjeta", "Cuenta Socio Ecommerce"])
        if op == 1:
            PagarTarjeta(carrito)
        elif op == 2:
            PagarSocio(carrito, usuarioLogeado)

        if len(carrito) == 0:
            envio = elegirEnvio()
            mostrarMensajeFinal(envio)
        else: 
            print("Compra no realizada :( ")
    else:
        print("¡¡Compra Cancelada!!")

def PagarTarjeta(carrito):
    '''
    Procesa un pago con tarjeta solicitando al usuario las credenciales y validando la tarjeta.\n
    Entrada: `carrito` (list), `carritoTotal` (int).\n
    Salida: `carritoTotal` modificado después de procesar el pago con tarjeta.
    '''
    print(f"\n==================================================================")
    print("----------Pago con Tarjeta----------")
    print(f"\n   Pago en total: ${calcularCarritoTotal(carrito)}")
    op = input("¿Desea proceder con el pago? (S/N): ")
    if op.lower() != "s":
        print("Cancelando pago...")
        return
    
    num = input(f"Ingrese numero de tarjeta: ")
    nom = input(f"Ingrese nombre en la tarjeta: ")
    vencA = input(f"Ingrese año de vencimiento: ")
    vencM = input(f"Ingrese mes de vencimiento: ")
    cod = input(f"Ingrese codigo de seguridad: ")

    print(f"Numero de tarjeta: {num} | Nombre: {nom} | Vencimiento: {vencM}/{vencA} | Codigo de seguridad: {cod}")
    confirmar = input(f"Confirma que desea pagar ${calcularCarritoTotal(carrito)} con la tarjeta ingresada? (S/N): ")
    if confirmar.lower() != "s":
        print("Cancelando pago...")
        return
    print(f"--------PAGO REALIZADO--------")
    ##Reinicializacon del carrito
    carrito.clear()

def PagarSocio(carrito, usuarioLogeado):
    '''
    Intenta procesar un pago usando las credenciales registradas de tarjeta ecommerce.\n
    Entrada: `carrito` (list), `carritoTotal` (int), `NomTarjetasEcommerce` (list), `PINTarjetasEcommerce` (list), `NumTarjetasEcommerce` (list).\n
    Salida: `carritoTotal` modificado después de procesar el pago con tarjeta
    '''
    print(f"\n==================================================================")
    print(f"Iniciando Pago con Tarjeta Ecommerce....")
    print(f"\nPagando el carrito actual de: {usuarioLogeado['nombre']} ")
    print(f"PRESIONA 0 PARA CANCELAR")
    print(f"\n   Pago en total: {calcularCarritoTotal(carrito)}")
    while True:
        print("----------------------------------------")
        print (f"\ningrese su contraseña para continuar")
        print(f"Ingrese 0 para cancelar el checkout")
        continuar = input("contraseña: ")
        if continuar == "0":
            return
        else:
            if continuar == usuarioLogeado["password"]:
                print(f"\nContraseña validada!")
                input("Su compra se esta realizando.... ")
                usuarioLogeado["cuenta"]["ordenes"].append(carrito)
                usuarioLogeado["cuenta"]["deuda"] += calcularCarritoTotal(carrito)
                carrito.clear()
                input("Compra realizada!!")
                print("-----------------------------------------------------------------------")
                print(f"Su deuda actual es de: {usuarioLogeado['cuenta']['deuda']}")
                print("Puede dirigirse a la opcion 'Ver mi cuenta' para cancelar sus deudas")
                print("-----------------------------------------------------------------------")
                return
            else: 
                print("Error al ingresar contraseña")
                print("(verifique mayusculas y espacios)") 

def elegirEnvio():
    '''
    Muestra opciones de envio y devuelve la seleccion del usuario.\n
    Entrada: N/A\n
    Salida: `int` - opcion elegida (1, 2 o 3).
    '''
    opcion = mostrarPrompt("METODO DE ENVIO", ["Envío estándar (5 a 7 días)","Envío express (1 a 2 días)","Retiro en el local"])
    return opcion

def mostrarMensajeFinal(tipoEnvio):
    '''
    Muestra el resumen final de la compra según el tipo de envio.\n
    Entrada: `tipoEnvio` (int) - opción de envío elegida por el usuario (1, 2 o 3).\n
    Salida: N/A
    '''
    print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    if tipoEnvio == 1:
        print("Seleccionaste envío estándar. Tu pedido llegará dentro de 5 a 7 días hábiles.")
        print(f"El código de seguimiento de tu pedido es: {randomNumber()}")
    elif tipoEnvio == 2:
        print("Seleccionaste envío express. Tu pedido llegará dentro de 1 a 2 días hábiles.")
        print(f"El código de seguimiento de tu pedido es: {randomNumber()}")
    elif tipoEnvio == 3:
        print("A partir de mañana vas a poder retirar tu pedido en nuestro local.")
        print("Nuestro horario de atención es de lunes a viernes de 9 a 18 horas. Te esperamos!")
    print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")

# Socio
def MenuMiCuenta(usuarioLogeado):
    '''
    Accede al menú de la cuenta del cliente verificando credenciales.\n
    Entrada: `NomTarjetasEcommerce` (list), `PINTarjetasEcommerce` (list), `NumTarjetasEcommerce` (list), `CuentasEcommerce` (list).\n
    Salida: N/A - muestra la cuenta y permite cancelar deudas si corresponde.
    '''
    cancelar = MostarCuentaCliente(usuarioLogeado)
    if cancelar == True:
        CancelarCuentaCliente(usuarioLogeado)
    else: 
        print("ERROR al ingresar datos")
        print ("Volver a intentar")
        input("")

def CancelarCuentaCliente(usuarioLogeado):
    '''
    Funcion para que el cliente pueda cancelar su cuenta de compras realizadas en comodas cuotas.\n
    Entrada: `idx` (int) - indice de la cuenta del cliente en `CuentasEcommerce`, `CuentasEcommerce` (list) - lista de cuentas con compras y totales, `nombre` (str) - nombre del cliente.\n
    Salida: N/A - muestra opciones de pago en cuotas y modifica la cuenta del cliente reiniciando su deuda y ordenes después de cancelar.
    '''
    print("===============CANCELAR DEUDA===============")
    print(f"SOCIO: {usuarioLogeado['nombre']}")
    print(f"\nDeuda a cancelar:   ${usuarioLogeado['cuenta']['deuda']:>8}")
    print("-"*50)
    print(f"")
    for i in range (len(PlazosCuotas)):
        print(f"[{i+1}] {PlazosCuotas[i]:<20}    Comision: {PorcentajeCuotas[i]:>5}")
    pagando=True
    while pagando==True:
        OpcionPago=input(f"\nOPCION: ") 
        if OpcionPago.isdigit():
            OpcionPago=int(OpcionPago)-1
            if 0<=OpcionPago and OpcionPago<=len(PlazosCuotas):
                print("===========CALCULO DE CUOTAS===========")
                print(f"\nUsted pagara su deuda de: ${usuarioLogeado['cuenta']['deuda']}")
                Cuotas=(usuarioLogeado['cuenta']['deuda']*PagosCuotas[OpcionPago]) // PlazosCuotNUM[OpcionPago]
                ##Cuotas calcula:   la deuda del cliente *El interes que selecciono segun sus plazos (1.1, 1.2...)  // La cantidad de pagos que hara (meses por lo cuales pagara)
                        ##Cuotas= Pago que el cliente debera efectuar cada mes 
                print(f"\nPagara ${PlazosCuotas[OpcionPago]}     Cada una de: ${Cuotas} ")
                print(f"Pagando unicamente un {PorcentajeCuotas[OpcionPago]} de comision!!!")

                print(f"\nRegresando....")
                usuarioLogeado["cuenta"]["deuda"]=0  ##Reinicializando monto y objetos adeudados
                usuarioLogeado["cuenta"]["Historial"].append(usuarioLogeado["cuenta"]["ordenes"])
                usuarioLogeado["cuenta"]["ordenes"]=[]
                return
            else:
                print("ingrese opcion valida")

def MostarCuentaCliente(usuarioLogeado):
    '''
    Funcion para mostrar la cuenta del cliente a consultar con previo ingreso de credenciales, muestra los tickets de compras anteriores con sus respectivos items y el total de su cuenta a pagar.\n
    Entrada: `idx` (int) - indice de la cuenta en `CuentasEcommerce`, `CuentasEcommerce` (list) - lista con compras previas y totales, `nombre` (str) - nombre del cliente.\n
    Salida: `bool` - True si el cliente desea cancelar su cuenta, False en caso contrario.
    '''

    for i in range(len(usuarioLogeado["cuenta"]["ordenes"])): ##Ingresa a la lista del cliente donde se almacenan sus compras previas
        print(f"\n--- TICKET NRO {i+1} ---")  
        print(f"Socio Ecommerce: {usuarioLogeado['nombre']}")     ##Imprime las compras previas por separado             
        compra=usuarioLogeado["cuenta"]["ordenes"][i]
        for item in compra:
            print((f"•{item['msj']}"))
    
    print(f"\n  •TOTAL DE CUENTA ECOMMERCE: ${usuarioLogeado['cuenta']['deuda']}")
    opcion = mostrarPrompt("¿Qué desea hacer?", ["Cancelar cuenta", "Salir"])
    if opcion == 1:
        return True
    else:
        return False

def revisarStock(productos):
    print("\n--- REPORTE DE STOCK ---")
    print("ID - Producto - Stock - Estado\n")
    for prod in productos:
        stock_actual = prod["stock"]
        alerta = ""
        if 0 < stock_actual < 3:
            alerta = "- El stock del producto esta bajo"
        elif stock_actual == 0:
            alerta = "- No hay mas stock"
        else:
            alerta = ""

        print(prod['id'], prod['nombre'],stock_actual,alerta)

    input("\nPresione ENTER para volver al menú de admin...")

# Admin
def menuAdmin(productos, cupones):
    '''
    Activar el menu de Administrador (Se accede ingresando a la tienda con una cuenta con rol de admin).\n
    Entrada: `productos` (list) - lista de diccionarios con información de productos.\n
    Salida: N/A - funcionalidad del menu de administrador.
    '''
    while True:
        op = mostrarPrompt("Bienvenido, Administrador", ["Buscar productos","Modificar producto","Agregar producto","Revisar Stock","Gestionar Cupones","Salir"])
        
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
            revisarStock(productos)
        elif op == 5:
            menuCupones(cupones)
        elif op == 6:
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


def crearCupon(cupones):
    '''
    Crea un nuevo cupón de descuento y lo agrega al conjunto de cupones disponibles.\n
    Entrada: `cupones` (set) - conjunto donde se almacenan los códigos de cupones.\n
    Salida: N/A - agrega un nuevo código de cupón al conjunto `cupones`.
    '''
    nuevo_cupon = {}
    codigo = input("Ingrese el código del nuevo cupón: ")
    descuento = int(input("Ingrese el porcentaje de descuento: "))
    
    nuevo_cupon = {"codigo": codigo, "descuento": descuento}
    cupones.append(nuevo_cupon)
    print(f"Cupón '{codigo}' creado exitosamente.")

def eliminarCupon(cupones):
    '''
    Elimina un cupón de descuento existente del conjunto de cupones disponibles.\n
    Entrada: `cupones` (set) - conjunto donde se almacenan los códigos de cupones.\n
    Salida: N/A - elimina un código de cupón del conjunto `cupones`.
    '''
    codigo = input("Ingrese el código del cupón a eliminar: ")
    for cupon in cupones:
        if cupon["codigo"] == codigo:
            cupones.remove(cupon)
            print(f"Cupón '{codigo}' eliminado exitosamente.")
            return
    print("El código de cupón no existe. Por favor, ingrese un código válido.")

def mostrarCupones(cupones):
    '''
    Muestra en pantalla la lista de cupones de descuento disponibles.\n
    Entrada: `cupones` (set) - conjunto donde se almacenan los códigos de cupones.\n
    Salida: N/A - muestra en pantalla los códigos de cupones disponibles.
    '''
    print("--- CUPONES DE DESCUENTO DISPONIBLES ---")
    for cupon in cupones:
        print(f"Código: {cupon['codigo']} | Descuento: {cupon['descuento']}%")

def aplicarCupon(carrito, cupones):
    '''
    Permite al usuario ingresar un código de cupón para aplicar un descuento a su carrito de compras.\n
    Entrada: `carrito` (list) - lista de diccionarios con información de los productos en el carrito, `cupones` (set) - conjunto donde se almacenan los códigos de cupones.\n
    Salida: `carrito` modificado con los descuentos aplicados según el código de cupón ingresado.
    '''
    codigo = input("Ingrese el código del cupón a aplicar: ")
    for cupon in cupones:
        if cupon["codigo"] == codigo:
            descuento = cupon["descuento"]
            for producto in carrito:
                producto["precio_final"] = round(producto["precio_final"] * (1 - descuento / 100), 2)
            print(f"Cupón '{codigo}' aplicado exitosamente. Se ha aplicado un descuento del {descuento}% a su carrito.")
            print("Su precio total con el descuento aplicado es de: $", calcularCarritoTotal(carrito))
            return carrito
    print("El código de cupón no es válido. Por favor, ingrese un código válido.")

def menuCupones(cupones):
    '''
    Muestra el menú de gestión de cupones para el administrador, permitiendo crear, eliminar o mostrar cupones disponibles.\n
    Entrada: `cupones` (set) - conjunto donde se almacenan los códigos de cupones.\n
    Salida: N/A - funcionalidad del menú de gestión de cupones.
    '''
    while True:
        op = mostrarPrompt("Gestión de Cupones", ["Crear Cupón", "Eliminar Cupón", "Mostrar Cupones Disponibles", "Salir"])
        if op == 1:
            crearCupon(cupones)
        elif op == 2:
            eliminarCupon(cupones)
        elif op == 3:
            mostrarCupones(cupones)
        elif op == 4:
            print("Saliendo del menú de cupones...")
            break

def ingresarCupon(carrito, cupones):
    '''
    Permite al usuario ingresar un código de cupón para aplicar un descuento a su carrito de compras.\n
    Entrada: `carrito` (list) - lista de diccionarios con información de los productos en el carrito, `cupones` (set) - conjunto donde se almacenan los códigos de cupones.\n
    Salida: `carrito` modificado con los descuentos aplicados según el código de cupón ingresado.
    '''
    codigo = input("Ingrese el código del cupón a aplicar: ")
    for cupon in cupones:
        if cupon["codigo"] == codigo:
            descuento = cupon["descuento"]
            for producto in carrito:
                producto["precio_final"] = round(producto["precio_final"] * (1 - descuento / 100), 2)
            print(f"Cupón '{codigo}' aplicado exitosamente. Se ha aplicado un descuento del {descuento}% a su carrito.")
            return
    print("El código de cupón no es válido. Por favor, ingrese un código válido.")