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

def randomNumber():
    return str(random.randint(10000000000, 99999999999))


def calcularCarritoTotal(carrito):
    carritoTotal = 0
    for producto in carrito:
        carritoTotal += producto["precio_final"]
    return carritoTotal


def mailExiste(usuarios, mail):
    for usu in usuarios:
        if usu["email"] == mail:
            return True
    return False


def verificarCredenciales(usuarios, mail, contrasenia):
    for usu in usuarios:
        if usu["email"] == mail and usu["password"] == contrasenia:
            return usu
    return None


def filtrarPorNombre(productos, nombre):
    return list(filter(lambda prod: nombre in prod["nombre"].lower(), productos))


def filtrarPorCategoria(productos, categoria):
    return list(filter(lambda prod: categoria in prod["categoria"].lower(), productos))


def filtrarPorPrecio(productos, precio, tipoPrecio):
    if tipoPrecio == 1:
        return list(filter(lambda prod: prod["precio"] == precio, productos))
    if tipoPrecio == 2:
        return list(filter(lambda prod: prod["precio"] >= precio, productos))
    if tipoPrecio == 3:
        return list(filter(lambda prod: prod["precio"] <= precio, productos))
    return []


def calcularPrecioConDescuento(precio, descuento):
    return precio - (precio * (descuento / 100))


def calcularTotalItem(precio, descuento, cantidad):
    return round((precio - (precio * (descuento / 100))) * cantidad, 2)


def generarNuevoId(productos):
    nuevoId = 0
    for prod in productos:
        if int(prod["id"]) > nuevoId:
            nuevoId = int(prod["id"])
    return str(nuevoId + 1)


def buscarCuponPorCodigo(cupones, codigo):
    for cupon in cupones:
        if cupon[0] == codigo:
            return cupon
    return None


def aplicarDescuentoAlCarrito(carrito, descuento):
    for producto in carrito:
        producto["descuento_cupon"] = descuento
        producto["precio_final"] = round(producto["precio_final"] * (1 - descuento / 100), 2)
    return carrito


def calcularCuota(deuda, indicePlazo):
    return (deuda * PagosCuotas[indicePlazo]) // PlazosCuotNUM[indicePlazo]


def crearDiccionarioUsuario(nombre, mail, contrasenia):
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
    return {
        "id": nuevoId,
        "nombre": nombre,
        "precio": precio,
        "stock": stock,
        "descuento": 0,
        "categoria": categoria
    }


def guardarCupones(cupones):
    try:
        with open(RUTA_CUPONES, "w") as archivo:
            for cupon in cupones:
                archivo.write(f"{cupon[0]};{cupon[1]}\n")
    except Exception as e:
        print(f"Error al guardar en el archivo de cupones: {e}")


def cargarCupones(cupones_base):
    cupones = []
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
    if 0 < stock < 3:
        return "- El stock del producto esta bajo"
    elif stock == 0:
        return "- No hay mas stock"
    return ""


def crearOrden(prod_sel, cantidad):
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
    for item in carrito:
        if item["id"] == orden["id"]:
            item["stock"] += orden["stock"]
            item["precio_final"] += orden["precio_final"]
            return
    carrito.append(orden)


def restaurarStockCarrito(carrito, productos):
    for item in carrito:
        for prod in productos:
            if item["id"] == prod["id"]:
                prod["stock"] += item["stock"]


def cancelarDeuda(user):
    user["cuenta"]["ordenes"] = []
    user["cuenta"]["deuda"] = 0

def cargarUsuarios(lista_hardcodeada):
    if os.path.exists(RUTA_USUARIOS):
        try:
            with open(RUTA_USUARIOS, "r") as f:
                return json.load(f)
        except Exception as e:
            print(f"Error al cargar el archivo de usuarios: {e}")
            return lista_hardcodeada
    else:
        # Primera ejecución: creamos el archivo
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