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

# Login/Signup
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
        "rol": "user",
        "cuenta" : {
                "ordenes": [], "deuda": 0, "Historial": []}
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

# Compra

def MenuComprar(carritoTotal, carrito, productos):
    '''
    Flujo que gestiona la interacción para agregar productos al carrito y procesar la compra.\n
    Entrada: `carritoTotal` (int), `carrito` (list), `productos` (list).\n
    Salida: `carritoTotal` modificado después de agregar productos o procesar la compra.
    '''
    while True:
        print("-"*30)
        op = mostrarPrompt("Menu de Compra", ["Ver Carrito", "Agregar Productos a Carrito", "Quitar Productos de Carrito", "Confirmar Compra", "Salir"])
        print("-"*30)
        if op == 1:
            verCarrito(carrito, carritoTotal)
        elif op == 2:
            carritoTotal = agregarCarrito(carrito, carritoTotal, productos)
        elif op == 3:
            carritoTotal = borrarCarrito(carrito, carritoTotal)
        elif op == 4:
            carritoTotal = confirmarCompra(carrito, carritoTotal)
        elif op == 5:
            return carritoTotal


def verCarrito(carrito, carritoTotal):
    '''
    Muestra el contenido del carrito y ofrece opciones para confirmar o modificar la compra.\n
    Entrada: `carrito` (list), `carritoTotal` (int).\n
    Salida: N/A - muestra el carrito y el total, no modifica los datos.
    '''
    ##Interfaz del carrito de compras/Confirma Compra
    print("|-|-|-|-|-|-|-- Carrito --|-|-|-|-|-|-|-|")
    
    for prod in carrito:
        if prod["descuento"] > 0:
            promo = f"({prod['descuento']}% OFF)"
        else:
            promo = ""
        print(f"{prod['nombre']} | Precio: ${prod['precio_descuento']} {promo} | Cantidad: {prod['stock']} | Total: ${prod['precio_final']}")
    print(f"\nEl total de su compra es de: $ {carritoTotal}")
    print("--------------------------------")

def agregarCarrito(carrito, carritoTotal, productos):
    '''
    Interfaz que muestra los productos disponibles y permite agregarlos al carrito.\n
    Entrada: `carritoTotal` (int), `carrito` (list), `productos` (list).\n
    Salida: `carritoTotal` modificado.
    '''
    while True:
        # Interfaz de carrito
        print("=" * 80)
        print("Tu carrito es: $", carritoTotal)
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
            return carritoTotal
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
                                carritoTotal += total
                                # Crear diccionario de orden
                                orden = {}
                                orden.update(prod_sel)
                                orden.update({"stock": cantidad})
                                orden.update({"precio_descuento": (prod_sel["precio"] - (prod_sel["precio"] * (prod_sel["descuento"] / 100)))})
                                orden.update({"precio_final": (prod_sel["precio"] - (prod_sel["precio"] * (prod_sel["descuento"] / 100)))*cantidad})
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

def borrarCarrito(carrito, carritoTotal):
    '''
    Borra un producto del carrito o limpia el carrito entero según la elección del usuario.\n
    Entrada: `carrito` (list), `carritoTotal` (int).\n
    Salida: `carritoTotal` modificado después de eliminar productos.
    '''
    op = mostrarPrompt("¿Quitar solo 1 item o limpiar carrito entero?", ["Quitar Item","Limpiar carrito"])
    if op == 1: ##BORRAR UN ELEMENTO
        verCarrito(carrito, carritoTotal)
        prompt = [item["nombre"] for item in carrito]
        elimIndice = (mostrarPrompt("---------Eliminando un item----------", prompt) - 1)
        carritoTotal -= carrito[elimIndice]["precio_final"]
        carrito.pop(elimIndice)
    elif op == 2: ##LIMPIA TOTAL DEL CARRITO
        print("Confirmar limpia del carrito de compras?")
        print("----------------------------------------")
        opcion = input("S/N: ")
        if opcion.lower() == "s":
            carrito.clear()
            carritoTotal = 0
            print("Carrito Limpio ✓")
        if opcion == "N" or opcion == "n":
            print("¡¡Operacion Cancelada!!")
    return carritoTotal

def confirmarCompra(carrito, carritoTotal):
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
        op = mostrarPrompt("Seleccione metodo de pago...", ["Tarjeta", "Cuenta Socio Ecommerce"])
        if op == 1:
            carritoTotal = PagarTarjeta(carrito, carritoTotal)
        elif op == 2:
            carritoTotal = PagarSocio(carrito, carritoTotal)
    else:
        print("¡¡Compra Cancelada!!")
    return carritoTotal

def PagarTarjeta(carrito, carritoTotal):
    '''
    Procesa un pago con tarjeta solicitando al usuario las credenciales y validando la tarjeta.\n
    Entrada: `carrito` (list), `carritoTotal` (int).\n
    Salida: `carritoTotal` modificado después de procesar el pago con tarjeta.
    '''
    print(f"\n==================================================================")
    print("----------Pago con Tarjeta----------")
    print(f"\n   Pago en total: ${carritoTotal}")
    op = input("¿Desea proceder con el pago? (S/N): ")
    if op.lower() != "s":
        print("Cancelando pago...")
        return carritoTotal
    num = input(f"Ingrese numero de tarjeta: ")
    nom = input(f"Ingrese nombre en la tarjeta: ")
    vencA = input(f"Ingrese año de vencimiento: ")
    vencM = input(f"Ingrese mes de vencimiento: ")
    cod = input(f"Ingrese codigo de seguridad: ")
    print(f"Numero de tarjeta: {num} | Nombre: {nom} | Vencimiento: {vencM}/{vencA} | Codigo de seguridad: {cod}")
    confirmar = input(f"Confirma que desea pagar ${carritoTotal} con la tarjeta ingresada? (S/N): ")
    if confirmar.lower() != "s":
        print("Cancelando pago...")
        return carritoTotal
    print(f"--------PAGO REALIZADO--------")
    ##Reinicializacon de los carritos
    carrito.clear()
    carritoTotal = 0
    return carritoTotal

def PagarSocio(carritoTotal, NomTarjetasEcommerce, PINTarjetasEcommerce, NumTarjetasEcommerce):
    '''
    Intenta procesar un pago usando las credenciales registradas de tarjeta ecommerce.\n
    Entrada: `carrito` (list), `carritoTotal` (int), `NomTarjetasEcommerce` (list), `PINTarjetasEcommerce` (list), `NumTarjetasEcommerce` (list).\n
    Salida: `carritoTotal` modificado después de procesar el pago con tarjeta, o `None` si se canceló o hubo un error.
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

# Socio
def MenuMiCuenta(NomTarjetasEcommerce, PINTarjetasEcommerce, NumTarjetasEcommerce, CuentasEcommerce):
    '''
    Accede al menú de la cuenta del cliente verificando credenciales.\n
    Entrada: `NomTarjetasEcommerce` (list), `PINTarjetasEcommerce` (list), `NumTarjetasEcommerce` (list), `CuentasEcommerce` (list).\n
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

# Admin
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