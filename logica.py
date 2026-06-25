import os
import random
import json
from datetime import datetime
import copy

PlazosCuotas = ["3 Cuotas", "6 Cuotas", "8 Cuotas", "10 Cuotas"]
PlazosCuotNUM = [3, 6, 8, 10]
PorcentajeCuotas = ["10%", "20%", "30%", "40%"]
PagosCuotas = [1.1, 1.2, 1.3, 1.40]

RUTA_ACTUAL = os.path.dirname(__file__)
RUTA_USUARIOS = os.path.join(RUTA_ACTUAL, "usuarios.json")
RUTA_CUPONES = os.path.join(RUTA_ACTUAL, "cupones.txt")
RUTA_PRODUCTOS = os.path.join(RUTA_ACTUAL, "productos.json")

def randomNumber():
    '''
    Genera un numero aleatorio
    Entrada: N/A
    Salida: Numero aleatorio
    '''
    return str(random.randint(10000000000, 99999999999))


def calcularCarritoTotal(carrito):
    '''
    Funcion que calcula el precio total del carrito
    Entrada: Carrito (diccionario) - Items en el carrito (usa particularmente "precio_final")
    Salida: CarritoTotal (float)
    '''
    carritoTotal = 0
    for producto in carrito:
        carritoTotal += producto["precio_final"]
    return carritoTotal


def mailExiste(usuarios, mail):
    '''
    Funcion para verificar si un correo esta ya registrado en el sistema
    Entrada: usuarios (lista) - lista de diccionarios de usuarios, mail (str) mail que se buscara
    Salida: True/False dependiendo de si encuentra coincidencias o no en el sistema
    '''
    for usu in usuarios:
        if usu["email"] == mail:
            return True
    return False


def verificarCredenciales(usuarios, mail, contrasenia):
    '''
    Funcion para comprobar si el correo y contrasenia coinciden con el de algun usuario en el sistema
    Entrada: usuarios (lista) - lista de diccionarios de usuarios, mail (str) - correo a verificar, contrasenia (str) - contrasenia a verificar
    Salida: usu (diccionario) - diccionario perteneciente al usuario, None si no se encuentra usuario en el sistema
    '''
    for usu in usuarios:
        if usu["email"] == mail and usu["password"] == contrasenia:
            return usu
    return None


def filtrarPorNombre(productos, nombre):
    '''
    Funcion para filtrar la lista de productos con un nombre dado
    Entrada: productos (lista) - Lista de diccionarios de productos, nombre (str) - cadena de texto con el nombre del item a buscar
    Salida: lista de productos cuyo nombre incluya el texto buscado
    '''
    return list(filter(lambda prod: nombre in prod["nombre"].lower(), productos))


def filtrarPorCategoria(productos, categoria):
    '''
    Funcion para filtrar la lista de productos con una categoria dada
    Entrada: productos (lista) - Lista de diccionarios de productos, categoria (str) - cadena de texto con la categoria de productos a buscar
    Salida: lista de productos cuya categoria sea la buscada
    '''
    return list(filter(lambda prod: categoria in prod["categoria"].lower(), productos))


def filtrarPorPrecio(productos, precio, tipoPrecio):
    '''
        Funcion para filtrar la lista de productos en relacion a un precio y tipo de filtro dado
        Entrada: productos (lista) - Lista de diccionarios de productos, precio (float) - valor con el cual filtraremos, tipoPrecio (int) - Indicador de que operacion haremos (1 para igual, 2 para mayor a, 3 para menor a)
        Salida: lista de productos cuyo precio cumpla con las condiciones dadas
        '''
    if tipoPrecio == 1:
        return list(filter(lambda prod: prod["precio"] == precio, productos))
    if tipoPrecio == 2:
        return list(filter(lambda prod: prod["precio"] >= precio, productos))
    if tipoPrecio == 3:
        return list(filter(lambda prod: prod["precio"] <= precio, productos))
    return []


def calcularPrecioConDescuento(precio, descuento):
    '''
    Funcion para calcular el precio de un producto segun un descuento dado
    Entradas: precio (float) - Valor que representa el precio, descuento (float) - porcentaje de descuento a aplicar (0 a 100)
    Salida: precio final calculado con el descuento
    '''
    return precio - (precio * (descuento / 100))


def calcularTotalItem(precio, descuento, cantidad):
    '''
    Funcion para calcular el valor total de una compra de un item
    Entradas: precio (float) - Valor representativo del costo del item, descuento (float) porcentaje del descuento a aplicar, cantidad (int) - cantidad de productos a comprar
    Salida: Precio final (Precio - descuento ) * cantidad
    '''
    return round((precio - (precio * (descuento / 100))) * cantidad, 2)


def generarNuevoId(productos):
    '''
    Funcion para crear una Id nueva, que seria 1 mayor a la id mas grande existente
    Entrada: productos (lista) - Lista de diccionarios de productos en el sistema
    Salida: un String que representa una Id que no exista ya en la lista
    '''
    nuevoId = 0
    for prod in productos:
        if int(prod["id"]) > nuevoId:
            nuevoId = int(prod["id"])
    return str(nuevoId + 1)


def buscarCuponPorCodigo(cupones, codigo):
    '''
    Funcion para buscar un cupon esecifico segun su codigo
    Entradas: cupones (set) - conjunto de cupones (codigo, descuento), codigo (str) - codigo del cupon a buscar
    Salida: Tupla del cupon si se encontro o None sino
    '''
    for cupon in cupones:
        if cupon[0].lower() == codigo.lower():
            return cupon
    return None


def aplicarDescuentoAlCarrito(carrito, descuento):
    '''
    Funcion para aplicar un descuento a todos los productos del carrito
    Entrada: carrito (lista) - lista de diccionarios de los items en el carrito, descuento (float) - porcentaje del descuento a aplicar
    Salida: carrito (lista) - lista de diccionarios de los items en el carrito, con su precio modificado
    '''
    for producto in carrito:
        producto["descuento_cupon"] = descuento
        producto["precio_final"] = round(producto["precio_final"] * (1 - descuento / 100), 2)
    return carrito


def calcularCuota(deuda, indicePlazo):
    '''
    Calcula el valor de cada cuota a pagar segun la deuda y el plazo elegido
    Entradas: deuda (float) - Valor total de la deuda, indicePlazo (int) - Posicion del plazo elegid en la lista de opciones
    Salida: Valor redondeado de cada cuota mensual
    '''
    return (deuda * PagosCuotas[indicePlazo]) // PlazosCuotNUM[indicePlazo]


def crearDiccionarioUsuario(nombre, mail, contrasenia):
    '''
    Crea un diccionario segun los datos de usuario de entrada
    Entrada: nombre (str) - Nombre de usuario, mail (str) - Correo electronico, contrasenia (str) - Contrasenia de la cuenta
    Salida: Diccionario de usuario armado con los datos, y otros campos necesarios
    '''
    return {
        "nombre": nombre,
        "email": mail,
        "password": contrasenia,
        "tarjetas": [],
        "es_admin": False,
        "cuenta": {"ordenes": [], "deuda": 0},
        "historial": []
    }


def crearDiccionarioProducto(nuevoId, nombre, precio, stock, categoria):
    '''
    Crea un diccionario de producto segun los datos dados
    Entradas: nuevoId (str) - Id del producto, nombre(str) - nombre del producto, precio (float) - precio del producto, stock (int) - cantidad disponible, categoria (str) - Categoria del producto
    Salida: Diccionario armado con los datos de producto y campo de descuento
    '''
    return {
        "id": nuevoId,
        "nombre": nombre,
        "precio": precio,
        "stock": stock,
        "descuento": 0,
        "categoria": categoria
    }


def guardarCupones(cupones):
    '''
    Guarda el conjunto de cupones actual en un archivo de texto plano, formateando cada uno como 'codigo;descuento'.
    Entrada: cupones (list) - Lista de tuplas de cupones (codigo, descuento).
    Salida: N/A - Escribe directamente en el archivo RUTA_CUPONES.
    '''
    try:
        with open(RUTA_CUPONES, "w") as archivo:
            for cupon in cupones:
                archivo.write(f"{cupon[0]};{cupon[1]}\n")
    except Exception as e:
        print(f"Error al guardar en el archivo de cupones: {e}")


def cargarCupones(cupones_base):
    '''
    Lee los cupones guardados desde el archivo de texto. Si el archivo no existe, crea uno nuevo con los cupones base.
    Entrada: cupones_base (list) - Cupones hard-codeados que se usarán si no existe el archivo.
    Salida: cupones (set) - Los cupones cargados desde el archivo o los cupones hard-codeados si falta no hay archivo.
    '''
    cupones = set()
    if os.path.exists(RUTA_CUPONES):
        try:
            with open(RUTA_CUPONES, "r") as archivo:
                for linea in archivo:
                    codigo, descuento = linea.strip().split(";")
                    cupones.add((codigo, int(descuento)))
            return cupones
        except Exception as e:
            print(f"Error al cargar el archivo de cupones: {e}")
            return cupones_base
    else:
        # Primera ejecución: crea el archivo con los cupones base
        guardarCupones(cupones_base)
        return cupones_base


def obtenerAlertaStock(stock):
    '''
    Funcion encargada de devolver una advertencia segun stock restante
    Entrada: stock (int) - Cantidad actual de unidades del producto.
    Salida: str - Cadena de texto con la advertencia correspondiente, o un string vacío si el stock es normal.
    '''
    if 0 < stock < 3:
        return "- El stock del producto esta bajo"
    elif stock == 0:
        return "- No hay mas stock"
    return ""


def crearOrden(prod_sel, cantidad):
    '''
    Genera un diccionario de orden de compra calculando los precios finales y descuentos para un producto y cantidad específicos.
    Entradas: prod_sel (dict) - Diccionario del producto seleccionado, cantidad (int) - Unidades que se desean comprar.
    Salida: orden (dict) - Estructura de la orden con los datos copiados del producto y los totales de precio actualizados.
    '''
    precio_descuento = calcularPrecioConDescuento(prod_sel["precio"], prod_sel["descuento"])
    precio_final = calcularTotalItem(prod_sel["precio"], prod_sel["descuento"], cantidad)
    orden = {}
    orden.update(prod_sel)
    orden.update({"stock": cantidad})
    orden.update({"precio_descuento": precio_descuento})
    orden.update({"precio_final": precio_final})
    orden.update({"descuento_cupon": 0})
    return orden


def agregarOActualizarCarrito(carrito, orden):
    '''
    Agrega una orden al carrito de compras. Si el producto ya existía en el carrito, acumula la cantidad y actualiza el precio total.
    Entradas: carrito (lista) - Lista de diccionarios con los items actuales, orden (dict) - Nueva orden que se quiere ingresar.
    Salida: N/A - Modifica directamente la lista 'carrito' por referencia.
    '''
    for item in carrito:
        if item["id"] == orden["id"]:
            item["stock"] += orden["stock"]
            item["precio_final"] += orden["precio_final"]
            return
    carrito.append(orden)


def restaurarStockCarrito(carrito, productos):
    '''
    Devuelve al catálogo general las unidades de los productos que estaban retenidas en el carrito de compras (útil al vaciar o cancelar).
    Entradas: carrito (lista) - Productos que están en el carrito, productos (list) - Catálogo general de productos de la tienda.
    Salida: N/A - Modifica directamente el stock de los productos en la lista general.
    '''
    for item in carrito:
        for prod in productos:
            if item["id"] == prod["id"]:
                prod["stock"] += item["stock"]


def cancelarDeuda(user):
    '''
    Reinicia a cero el estado financiero de la cuenta de un socio, vaciando sus órdenes pendientes de pago
    Entrada: user (diccionario) - Diccionario del usuario a modificar
    Salida: N/A, modifica el valor del diccionario directamente
    '''
    user["cuenta"]["ordenes"] = []
    user["cuenta"]["deuda"] = 0

def cargarUsuarios(lista_hardcodeada):
    '''
    Carga la lista de usuarios desde un archivo JSON. Si no existe, crea el archivo
    usando la lista de usuarios hardcodeada.
    Entrada: lista_hardcodeada (lista) - Lista de usuarios iniciales.
    Salida: list - Lista de usuarios cargada desde el archivo o la lista inicial.
    '''
    if os.path.exists(RUTA_USUARIOS):
        try:
            with open(RUTA_USUARIOS, "r") as f:
                return json.load(f)
        except Exception as e:
            print(f"Error al cargar usuarios: {e}")
            return lista_hardcodeada
    else:
        guardarUsuarios(lista_hardcodeada)
        return lista_hardcodeada

def guardarUsuarios(lista_usuarios):
    """Guarda el estado actual de todos los usuarios en el JSON."""
    try:
        with open(RUTA_USUARIOS, "w") as f:
            json.dump(lista_usuarios, f, indent=4)
            return True
    except Exception as e:
        print(f"Error al guardar en el archivo de usuarios: {e}")
        return False
    

def crearFactura(carrito, usuarioLogueado, medioPago):
    '''
    Funcion encargada de crear el archivo de factura una vez se complete la compra (Luego de confirmar en la etapa de tarjeta)
    Entrada: Datos del carrito (Productos, cantidad y precio final), datos del usuario (nombre, mail y deuda)
    Salida: Un archivo .txt
    '''

    idCompra = randomNumber()
    reciboNom = f"Factura{idCompra}.txt"
    RUTA_FACTURA = os.path.join(RUTA_ACTUAL, reciboNom)

    while os.path.exists(RUTA_FACTURA):
        idCompra = randomNumber()
        reciboNom = f"Factura{idCompra}.txt"
        RUTA_FACTURA = os.path.join(RUTA_ACTUAL, reciboNom)

    fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    total_bruto = 0
    total_final = 0
    total_con_descuento_prod = 0

    try:
        with open(RUTA_FACTURA, "w") as file:
            file.write("=======================================================================\n")
            file.write("E-Commerce(-)E-Commerce(-)E-Commerce(-)E-Commerce(-)E-Commerce(-)E-Commerce(-)\n")
            file.write("=======================================================================\n")

            file.write("\nFACTURA DE COMPRA\n")
            file.write(f"Nro Factura: {idCompra}\n")
            file.write(f"Fecha: {fecha}\n")
            file.write(f"Medio de Pago: {medioPago}\n")

            file.write("\nDATOS DEL CLIENTE\n")
            file.write(f"Nombre: {usuarioLogueado['nombre']}\n")
            file.write(f"Email: {usuarioLogueado['email']}\n")

            file.write("\nPRODUCTOS COMPRADOS\n")
            file.write("-----------------------------------------------------------------------\n")
            i = 1
            for producto in carrito:
                subtotal_producto = producto['precio'] * producto['stock']
                total_bruto += subtotal_producto
                total_final += producto['precio_final']

                descuentoProd = producto['descuento'] / 100
                precio_con_d1 = subtotal_producto * (1 - descuentoProd)
                total_con_descuento_prod += precio_con_d1

                descuentoCupon = producto['descuento_cupon'] / 100
                porcenaje_descuento = round(((1 - (1 - descuentoProd) * (1 - descuentoCupon)) * 100), 2)

                file.write(
                    f"{i}. {producto['nombre']} "
                    f"| Cantidad: {producto['stock']} "
                    f"| Precio Unitario: ${producto['precio']:.2f} "
                    f"| Descuento: {porcenaje_descuento}% "
                    f"| Total: ${producto['precio_final']:.2f}\n"
                )
                i += 1
            file.write("-----------------------------------------------------------------------\n")

            ahorro_productos = total_bruto - total_con_descuento_prod
            ahorro_cupon = total_con_descuento_prod - total_final

            file.write(f"{'SUBTOTAL:':<22} ${total_bruto:>8.2f}\n")
            file.write(f"{'DESCUENTOS PRODUCTOS:':<22}-${ahorro_productos:>8.2f}\n")
            file.write(f"{'DESCUENTOS CUPON:':<22}-${ahorro_cupon:>8.2f}\n")
            file.write(f"{'TOTAL A PAGAR:':<22} ${total_final:>8.2f}\n")

            file.write("\nMUCHAS GRACIAS POR SU COMPRA!\n")

            file.write("===================================================================================\n")
            file.write("E-Commerce(-)E-Commerce(-)E-Commerce(-)E-Commerce(-)E-Commerce(-)E-Commerce(-)\n")
            file.write("===================================================================================\n")

            print("Tu factura fue creada exitosamente!")
    except Exception as e:
        print("Hubo un error en el creado de la factura:", e)
    else:
        factura_historial = {
            "id_factura": idCompra,
            "fecha": fecha,
            "medio_pago": medioPago,
            "total": total_final,
            "productos": copy.deepcopy(carrito)
        }
        usuarioLogueado["historial"].append(factura_historial)


def obtenerProductoMasComprado(usuarioLogueado):
    """
    Analiza el historial del usuario y devuelve el nombre del producto 
    del cual ha comprado la mayor cantidad de unidades en total.
    Si no hay historial o compras registradas, devuelve None.
    """
    historial = usuarioLogueado["historial"]
    if len(historial) == 0:
        return None

    conteo_productos = {}

    for registro in historial:
        for item in registro["productos"]:
            nombre = item["nombre"]
            cantidad = item["stock"]
            if nombre in conteo_productos:
                conteo_productos[nombre] += cantidad
            else:
                conteo_productos[nombre] = cantidad

    producto_estrella = None
    maxima_cantidad = -1  # Arranca en un número bajo para que cualquier producto lo supere

    for producto in conteo_productos:
        if conteo_productos[producto] > maxima_cantidad:
            maxima_cantidad = conteo_productos[producto]
            producto_estrella = producto

    return producto_estrella

def cargarProductos(lista_hardcodeada):
    '''
    Carga el diccionario de productos desde un archivo JSON, si no existe, crea el archivo
    Entrada: lista_hardcodeada (lista) - Lista de diccionarios de productos que se usa en caso de que no haya un archivo JSON
    Salida: list - Lista de diccionarios con la informacion de productos cargados del archivo JSON
    '''
    if os.path.exists(RUTA_PRODUCTOS):
        try:
            with open(RUTA_PRODUCTOS, "r") as f:
                return json.load(f)
        except Exception as e:
            print(f"Error al cargar productos: {e}")
            return lista_hardcodeada
    else:
        guardarProductos(lista_hardcodeada)
        return lista_hardcodeada
    
def guardarProductos(productos):
    '''
    Guarda el estado actual del diccionario de productos a un archivo JSON
    Entrada: productos (lista) - Lista de diccionarios de productos
    Salida: True si la escritura fue exitosa, False si hubo un error con esta
    '''
    try:
        with open(RUTA_PRODUCTOS, "w") as f:
            json.dump(productos, f, indent=4)
        return True
    except Exception as e:
        print(f"Error al guardar productos: {e}")
        return False
