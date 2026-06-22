import copy
import logica

msjSeleccione = "Seleccione una opción: "
msjNoExiste = "Opción no válida. Por favor, intente de nuevo."

def mostrarLogo():
    print("  ______  _____ ____  __  __ __  __ ______ _____   _____ ______ ")
    print(" |  ____|/ ____/ __ \\|  \\/  |  \\/  |  ____|  __ \\ / ____|  ____|")
    print(" | |__  | |   | |  | | \\  / | \\  / | |__  | |__) | |    | |__   ")
    print(" |  __| | |   | |  | | |\\/| | |\\/| |  __| |  _  /| |    |  __|  ")
    print(" | |____| |___| |__| | |  | | |  | | |____| | \\ \\| |____| |____ ")
    print(" |______|\\_____\\____/|_|  |_|_|  |_|______|_|  \\_\\\\_____|______|")


def mostrarPrompt(titulo, opciones):
    print(titulo)
    for i in range(len(opciones)):
        print(f"[{i+1}] {opciones[i]}")

    while True:
        try:
            opcion = int(input(msjSeleccione))
            if 1 <= opcion <= len(opciones):
                return opcion
            else:
                print(msjNoExiste)
        except ValueError:
            print(msjNoExiste)


# Login/Signup
def loginSignUp(usuarios):
    opcion = mostrarPrompt("LOGIN", ["Iniciar Sesión", "Crear Usuario"])
    if opcion == 1:
        return iniciarSesion(usuarios)
    elif opcion == 2:
        return crearUsuario(usuarios)


def crearUsuario(usuarios):
    nombre = input("Ingrese su nombre: ")
    mail = input("Ingrese su mail electrónico: ")
    contrasenia = input("Ingrese su contraseña: ")

    if logica.mailExiste(usuarios, mail):
        print("Ya existe un usuario con ese mail.")
        return crearUsuario(usuarios)

    nuevo_usuario = logica.crearDiccionarioUsuario(nombre, mail, contrasenia)
    usuarios.append(nuevo_usuario)
    print(f"Bienvenid@ {nombre}, tu cuenta fue creada exitosamente.")
    return nuevo_usuario


def iniciarSesion(usuarios):
    mail = input("Ingrese su correo electrónico: ")
    contrasenia = input("Ingrese su contraseña: ")

    usu = logica.verificarCredenciales(usuarios, mail, contrasenia)
    if usu is not None:
        print(f"Bienvenid@ de nuevo {usu['nombre']}!")
        return usu

    print("Tu mail o contraseña son incorrectos.")
    return iniciarSesion(usuarios)


# Menu Principal
def MostrarMenu(esAdmin=False):
    mostrarLogo()
    print("------------------------------------------------------------------------")
    print("=======================================================================")
    print("E-Commerce⦿E-Commerce⦿E-Commerce⦿E-Commerce⦿E-Commerce⦿E-Commerce⦿")
    print("=======================================================================")

    opciones = ["Comprar", "Ver productos", "Buscar Productos", "Ver MiCuentaEcommerce", "Administrar Tarjetas", "Salir"]

    if esAdmin:
        opciones.insert(5, "Modo Admin")

    return mostrarPrompt("Bienvenido a la tienda virtual 🏪", opciones)


# Ver/Buscar Productos
def verProductos(productos):
    print("--- Catálogo de Productos ---")
    for prod in productos:
        precio_final = logica.calcularPrecioConDescuento(prod["precio"], prod["descuento"])
        if prod["descuento"] > 0:
            promo = f"({prod['descuento']}% OFF)"
        else:
            promo = ""
        print(f"ID: {prod['id']} | Nombre: {prod['nombre']} | Precio: ${precio_final} {promo} | Stock: {prod['stock']} | Categoría: {prod['categoria']}")


def buscarProducto(productos):
    tipo = mostrarPrompt("BUSCAR POR...", ["Nombre", "Categoria", "Precio"])
    encontrados = []

    if tipo == 1:
        nom = input("Ingrese el nombre del producto: ").lower()
        encontrados = logica.filtrarPorNombre(productos, nom)
    elif tipo == 2:
        cat = input("Ingrese la categoria del producto: ").lower()
        encontrados = logica.filtrarPorCategoria(productos, cat)
    elif tipo == 3:
        tipoPrecio = mostrarPrompt("Seleccione forma de buscar por precio:", ["Igual", "Mayor o Igual", "Menor o Igual"])
        try: 
            precio = float(input("Ingrese el precio del producto: "))
            encontrados = logica.filtrarPorPrecio(productos, precio, tipoPrecio)
        except:
            print("Ingrese un número válido")

    if len(encontrados) > 0:
        verProductos(encontrados)
        input("\nPresione ENTER para volver al menu...")
    else:
        print("No se encontraron productos")
        input("\nPresione ENTER para volver al menu...")


# Compra
def MenuComprar(carrito, productos, usuarioLogueado, cupones):
    while True:
        print("-" * 30)
        op = mostrarPrompt("Menu de Compra", ["Ver Carrito", "Agregar Productos a Carrito", "Quitar Productos de Carrito", "Confirmar Compra", "Salir"])
        print("-" * 30)
        if op == 1:
            verCarrito(carrito)
        elif op == 2:
            agregarCarrito(carrito, productos)
        elif op == 3:
            borrarCarrito(carrito, productos)
        elif op == 4:
            confirmarCompra(carrito, usuarioLogueado, cupones)
        elif op == 5:
            return


def verCarrito(carrito):
    print("|-|-|-|-|-|-|-- Carrito --|-|-|-|-|-|-|-|")

    for prod in carrito:
        if prod["descuento"] > 0:
            promo = f"({prod['descuento']}% OFF)"
        else:
            promo = ""
            print(f"{prod['nombre']:<15} | Precio: ${prod['precio_descuento']:<6} {promo:<9} | Cantidad: {prod['stock']:^6} | Total: ${prod['precio_final']:>10.2f}")
    print(f"\nEl total de su compra es de: $ {logica.calcularCarritoTotal(carrito)}")
    print("--------------------------------")


def agregarCarrito(carrito, productos):
    while True:
        print("=" * 80)
        print("Tu carrito es: $", logica.calcularCarritoTotal(carrito))
        print("=" * 80)
        print(f"{'':^4} | {'PRODUCTO':<27} | {'PRECIO':<19} | {'STOCK':^10}")
        print("-" * 80)
        for i in range(len(productos)):
            p = productos[i]
            print(f"[{i + 1:^3}] {p['nombre']:<28} | Precio:  ${p['precio']:<8}  | Stock: {p['stock']:>8}")
        print("[ 0 ] SALIR")

        print("----------------AÑADIR AL CARRITO DE COMPRAS----------------")
        compra = input("Ingrese el numero del producto que desea comprar: ")
        if compra == "0":
            return
        else:
            try:
                compra = int(compra)
            except ValueError:
                print("ingrese una respuesta válida!")
                continue
            if compra > 0 and compra <= len(productos):
                prod_sel = productos[compra - 1]
                print("-------------------------------------------------------------------")
                print(f"\nComprando Item: {prod_sel['nombre']} | ${prod_sel['precio']}")
                cantidad = input("UNIDADES A COMPRAR: ")
                try:
                    cantidad = int(cantidad)
                except ValueError:
                    print("ingrese una respuesta válida!")
                    continue
                if cantidad <= prod_sel['stock']:
                    total = logica.calcularTotalItem(prod_sel["precio"], prod_sel["descuento"], cantidad)
                    agregar = input(f"Seguro que quiere añadir {cantidad} {prod_sel['nombre']} | Por un total de ${total} (S/N): ")
                    if agregar.lower() == "s":
                        prod_sel['stock'] -= cantidad
                        orden = logica.crearOrden(prod_sel, cantidad)
                        logica.agregarOActualizarCarrito(carrito, orden)
                    else:
                        print("Cancelado!")
                elif cantidad > prod_sel['stock']:
                    print(f"Stock insuficiente!")
                else:
                    print("ingrese una respuesta válida!")
            else:
                print("ingrese una respuesta válida!")


def borrarCarrito(carrito, productos):
    op = mostrarPrompt("¿Quitar solo 1 item o limpiar carrito entero?", ["Quitar Item", "Limpiar carrito"])
    if op == 1:
        verCarrito(carrito)
        prompt = [item["nombre"] for item in carrito]
        elimIndice = (mostrarPrompt("---------Eliminando un item----------", prompt) - 1)

        logica.restaurarStockItem(productos, carrito[elimIndice])
        carrito.pop(elimIndice)
    elif op == 2:
        verCarrito(carrito)
        print("Confirmar limpia del carrito de compras?")
        print("----------------------------------------")
        opcion = input("S/N: ")
        if opcion.lower() == "s":
            logica.restaurarStockCarrito(carrito, productos)
            carrito.clear()
            print("Carrito Limpio ✓")
        if opcion == "N" or opcion == "n":
            print("¡¡Operacion Cancelada!!")


def confirmarCompra(carrito, usuarioLogueado, cupones):
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

        op = mostrarPrompt("Seleccione metodo de pago...", ["Tarjeta", "Cuenta Socio Ecommerce"])
        if op == 1:
            PagarTarjeta(carrito, usuarioLogueado)
        elif op == 2:
            PagarSocio(carrito, usuarioLogueado)

        if len(carrito) == 0:
            envio = elegirEnvio()
            mostrarMensajeFinal(envio)
        else:
            print("Compra no realizada :( ")
    else:
        print("¡¡Compra Cancelada!!")


def PagarTarjeta(carrito, usuarioLogueado):
    print(f"\n==================================================================")
    print("----------Pago con Tarjeta----------")
    print(f"\n   Pago en total: ${logica.calcularCarritoTotal(carrito)}")

    op = input("¿Desea proceder con el pago? (S/N): ")
    if op.lower() != "s":
        print("Cancelando pago...")
        return

    tarjetas = usuarioLogueado["tarjetas"]
    usar_guardada = False
    if len(tarjetas) > 0:
        op_guardada = input("¿Desea usar una tarjeta guardada? (S/N): ")
        if op_guardada.lower() == "s":
            usar_guardada = True

            opciones = []
            for tarjeta in tarjetas:
                opciones.append(f"{tarjeta[0]} - {tarjeta[1]}")

            seleccion = mostrarPrompt("Seleccione una tarjeta", opciones)
            tarjeta = tarjetas[seleccion - 1]

            nom = tarjeta[0]
            num = tarjeta[1]
            vencM = tarjeta[2]
            vencA = tarjeta[3]

            cod = input("Ingrese codigo de seguridad: ")

    if not usar_guardada:
        num = input("Ingrese numero de tarjeta: ")
        vencA = input("Ingrese año de vencimiento: ")
        vencM = input("Ingrese mes de vencimiento: ")
        cod = input("Ingrese codigo de seguridad: ")

        guardar = input("¿Desea guardar esta tarjeta? (S/N): ")
        if guardar.lower() == "s":
            nom = input("Ingrese nombre en la tarjeta: ")
            tarjeta = (nom, num, vencM, vencA)
            usuarioLogueado["tarjetas"].append(tarjeta)
            print("Tarjeta guardada correctamente")

    print(f"Numero de tarjeta: {num} | Vencimiento: {vencM}/{vencA}")
    confirmar = input(f"Confirma que desea pagar ${logica.calcularCarritoTotal(carrito)} con la tarjeta ingresada? (S/N): ")

    if confirmar.lower() != "s":
        print("Cancelando pago...")
        return

    print("--------PAGO REALIZADO--------")
    carrito.clear() 


def PagarSocio(carrito, usuarioLogueado):
    print(f"\n==================================================================")
    print(f"Iniciando Pago con Tarjeta Ecommerce....")
    print(f"\nPagando el carrito actual de: {usuarioLogueado['nombre']} ")
    print(f"PRESIONA 0 PARA CANCELAR")
    print(f"\n   Pago en total: {logica.calcularCarritoTotal(carrito)}")
    while True:
        print("----------------------------------------")
        print(f"\ningrese su contraseña para continuar")
        print(f"Ingrese 0 para cancelar el checkout")
        continuar = input("contraseña: ")
        if continuar == "0":
            return
        else:
            if continuar == usuarioLogueado["password"]:
                print(f"\nContraseña validada!")
                input("Su compra se esta realizando.... ")
                Clon = copy.deepcopy(carrito)
                usuarioLogueado["cuenta"]["ordenes"].append(Clon)
                usuarioLogueado["cuenta"]["deuda"] += round(logica.calcularCarritoTotal(carrito))
                carrito.clear()
                input("Compra realizada!!")
                print("-----------------------------------------------------------------------")
                print(f"Su deuda actual es de: {usuarioLogueado['cuenta']['deuda']}")
                print("Puede dirigirse a la opcion 'Ver mi cuenta' para cancelar sus deudas")
                print("-----------------------------------------------------------------------")
                return
            else:
                print("Error al ingresar contraseña")
                print("(verifique mayusculas y espacios)")


def elegirEnvio():
    opcion = mostrarPrompt("METODO DE ENVIO", ["Envío estándar (5 a 7 días)", "Envío express (1 a 2 días)", "Retiro en el local"])
    return opcion


def mostrarMensajeFinal(tipoEnvio):
    print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    if tipoEnvio == 1:
        print("Seleccionaste envío estándar. Tu pedido llegará dentro de 5 a 7 días hábiles.")
        print(f"El código de seguimiento de tu pedido es: {logica.randomNumber()}")
    elif tipoEnvio == 2:
        print("Seleccionaste envío express. Tu pedido llegará dentro de 1 a 2 días hábiles.")
        print(f"El código de seguimiento de tu pedido es: {logica.randomNumber()}")
    elif tipoEnvio == 3:
        print("A partir de mañana vas a poder retirar tu pedido en nuestro local.")
        print("Nuestro horario de atención es de lunes a viernes de 9 a 18 horas. Te esperamos!")
    print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")


# Socio




def MenuMiCuenta(usuarioLogueado, usuarios):
    cancelar = MostarCuentaCliente(usuarioLogueado)
    if cancelar == True:
        CancelarCuentaCliente(usuarioLogueado, usuarios)
    else:
        print("Regresando al Menu principal...")
        input("Enter para continuar")


def CancelarCuentaCliente(usuarioLogueado, usuarios):
    print("===============CANCELAR DEUDA===============")
    print(f"SOCIO: {usuarioLogueado['nombre']}")
    print(f"\nDeuda a cancelar:   ${usuarioLogueado['cuenta']['deuda']:>8}")
    print("-" * 50)
    print(f"")
    for i in range(len(logica.PlazosCuotas)):
        print(f"[{i+1}] {logica.PlazosCuotas[i]:<20}    Comision: {logica.PorcentajeCuotas[i]:>5}")
    pagando = True
    while pagando == True:
        OpcionPago = input(f"\nOPCION: ")
        try:
            OpcionPago = int(OpcionPago) - 1
        except:
            print("ingrese opcion valida")
            continue

        if 0 <= OpcionPago and OpcionPago <= len(logica.PlazosCuotas):
            print("===========CALCULO DE CUOTAS===========")
            print(f"\nUsted pagara su deuda de: ${usuarioLogueado['cuenta']['deuda']}")
            Cuotas = logica.calcularCuota(usuarioLogueado['cuenta']['deuda'], OpcionPago)
            print(f"\nPagara {logica.PlazosCuotas[OpcionPago]}     Cada una de: ${Cuotas} ")
            print(f"Pagando unicamente un {logica.PorcentajeCuotas[OpcionPago]} de comision!!!")

            print(f"\nRegresando....")
            
            NuevaComprarealizada=logica.cancelarDeuda(usuarioLogueado)
            usuarioLogueado["cuenta"]["Historial"].append(NuevaComprarealizada)
            return
        else:
            print("ingrese opcion valida")


def MostarCuentaCliente(usuarioLogueado):
    for i in range(len(usuarioLogueado["cuenta"]["ordenes"])):
        print(f"\n--- TICKET NRO {i+1} ---")
        print(f"Socio Ecommerce: {usuarioLogueado['nombre']}")
        compra = usuarioLogueado["cuenta"]["ordenes"][i]
        for item in compra:
            print((f"•{item['msj']}"))

    print(f"\n  •TOTAL DE CUENTA ECOMMERCE: ${usuarioLogueado['cuenta']['deuda']}")
    opcion = mostrarPrompt("¿Qué desea hacer?", ["Cancelar cuenta", "Salir"])
    if opcion == 1:
        if (usuarioLogueado['cuenta']['deuda']) > 0:
            return True
        else:
            print(f"\nActualmente no tiene deudas por pagar")
            return False
    else:
        return False


def revisarStock(productos):
    print("\n--- REPORTE DE STOCK ---")
    print("ID - Producto - Stock - Estado\n")
    for prod in productos:
        stock_actual = prod["stock"]
        alerta = logica.obtenerAlertaStock(stock_actual)
        print(prod['id'], prod['nombre'], stock_actual, alerta)

    input("\nPresione ENTER para volver al menú de admin...")


def menuTarjetas(usuarioLogueado):
    while True:
        op = mostrarPrompt("ADMINISTRAR TARJETAS", ["Ver tarjetas", "Borrar tarjeta", "Salir"])

        if op == 1:
            if len(usuarioLogueado["tarjetas"]) == 0:
                print("No hay tarjetas guardadas")
            else:
                for i in range(len(usuarioLogueado["tarjetas"])):
                    tarjeta = usuarioLogueado["tarjetas"][i]
                    print(f"[{i+1}] Nombre: {tarjeta[0]} | Numero: {tarjeta[1]} | Vence: {tarjeta[2]}/{tarjeta[3]}")

            input("ENTER para continuar...")
        elif op == 2:
            borrarTarjeta(usuarioLogueado)
        elif op == 3:
            return


def borrarTarjeta(usuarioLogueado):
    tarjetas = usuarioLogueado["tarjetas"]
    if len(tarjetas) == 0:
        print("No hay tarjetas guardadas")
        return

    opciones = []
    for tarjeta in tarjetas:
        opciones.append(f"{tarjeta[0]} - {tarjeta[1]}")

    op = mostrarPrompt("Seleccione tarjeta a borrar", opciones)
    tarjeta_borrada = tarjetas.pop(op - 1)
    print(f"Tarjeta {tarjeta_borrada[0]} eliminada correctamente")


# Admin
def menuAdmin(productos, cupones):
    while True:
        op = mostrarPrompt("Bienvenido, Administrador", ["Buscar productos", "Modificar producto", "Agregar producto", "Revisar Stock", "Gestionar Cupones", "Salir"])

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
    print(f"Producto seleccionado: {producto['nombre']} - Precio ${producto['precio']} - Stock {producto['stock']} - Descuento {producto['descuento']}% - Categoria {producto['categoria']}")

    tipo = ["Precio", "Stock", "Descuento", "Categoria", "Nombre"]
    op = mostrarPrompt("¿Que modificar?", tipo)
    tipoElegido = tipo[op-1]

    nuevoValor = input(f"Nuevo {tipoElegido}: ")

    if tipoElegido in ["Precio"]:
        try:
            nuevoValor = float(nuevoValor)
        except:
            print("Ingrese un número válido")
            return
    elif tipoElegido in ["Stock", "Descuento"]:
        try:
            nuevoValor = int(nuevoValor)
        except:
            print("Ingrese un número válido")
            return

    producto[tipoElegido.lower()] = nuevoValor
    print(f"{tipoElegido} modificado correctamente. Nuevo valor: {nuevoValor}")


def agregarProducto(productos):
    nombre = input("Nombre del producto: ")
    categoria = input("Categoría: ")

    try: 
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))
    except:
        print("Ingrese un número válido")
        return

    nuevoId = logica.generarNuevoId(productos)
    producto_nuevo = logica.crearDiccionarioProducto(nuevoId, nombre, precio, stock, categoria)
    productos.append(producto_nuevo)
    print(f"Producto '{nombre}' agregado correctamente.")


def crearCupon(cupones):
    codigo = input("Ingrese el código del nuevo cupón: ")
    try: 
        descuento = int(input("Ingrese el porcentaje de descuento: "))
    except:
        print("Ingrese un número válido")
        return
    nuevo_cupon = logica.crearDiccionarioCupon(codigo, descuento)
    cupones.add(nuevo_cupon)
    logica.guardarCupones(cupones)
    print(f"Cupón '{codigo}' creado exitosamente.")


def eliminarCupon(cupones):
    codigo = input("Ingrese el código del cupón a eliminar: ")
    for cupon in cupones:
        if cupon[0] == codigo:
            cupones.remove(cupon)
            logica.guardarCupones(cupones)
            print(f"Cupón '{codigo}' eliminado exitosamente.")
            return
    print("El código de cupón no existe. Por favor, ingrese un código válido.")


def mostrarCupones(cupones):
    print("--- CUPONES DE DESCUENTO DISPONIBLES ---")
    for cupon in cupones:
        print(f"Código: {cupon[0]} | Descuento: {cupon[1]}%")


def aplicarCupon(carrito, cupones):
    codigo = input("Ingrese el código del cupón a aplicar: ")
    cupon = logica.buscarCuponPorCodigo(cupones, codigo)
    if cupon is not None:
        descuento = cupon[1]
        logica.aplicarDescuentoAlCarrito(carrito, descuento)
        print(f"Cupón '{codigo}' aplicado exitosamente. Se ha aplicado un descuento del {descuento}% a su carrito.")
        print("Su precio total con el descuento aplicado es de: $", logica.calcularCarritoTotal(carrito))
        return carrito
    print("El código de cupón no es válido. Por favor, ingrese un código válido.")
    return carrito


def menuCupones(cupones):
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
    codigo = input("Ingrese el código del cupón a aplicar: ")
    cupon = logica.buscarCuponPorCodigo(cupones, codigo)
    if cupon is not None:
        descuento = cupon[1]
        logica.aplicarDescuentoAlCarrito(carrito, descuento)
        print(f"Cupón '{codigo}' aplicado exitosamente. Se ha aplicado un descuento del {descuento}% a su carrito.")
        return
    print("El código de cupón no es válido. Por favor, ingrese un código válido.")
