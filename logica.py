import random
import os
import json 

PlazosCuotas = ["3 Cuotas", "6 Cuotas", "8 Cuotas", "10 Cuotas"]
PlazosCuotNUM = [3, 6, 8, 10]
PorcentajeCuotas = ["10%", "20%", "30%", "40%"]
PagosCuotas = [1.1, 1.2, 1.3, 1.40]

RUTA_ACTUAL = os.path.dirname(__file__)
RUTA_JSON = os.path.join(RUTA_ACTUAL, "usuarios.json")

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
        if cupon["codigo"] == codigo:
            return cupon
    return None


def aplicarDescuentoAlCarrito(carrito, descuento):
    for producto in carrito:
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
        "cuenta": {"ordenes": [], "deuda": 0, "Historial": []}
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


def crearDiccionarioCupon(codigo, descuento):  ##NO SE USA
    return {"codigo": codigo, "descuento": descuento}


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
    orden.update({"msj": f"{prod_sel['nombre']:25}  #{cantidad:<8}  ${precio_final:>10.2f}"})
    return orden


def agregarOActualizarCarrito(carrito, orden):
    for item in carrito:
        if item["id"] == orden["id"]:
            item["stock"] += orden["stock"]
            item["precio_final"] += orden["precio_final"]
            return
    carrito.append(orden)


def restaurarStockItem(productos, item):
    for prod in productos:
        if item["id"] == prod["id"]:
            prod["stock"] += item["stock"]


def restaurarStockCarrito(carrito, productos):
    for item in carrito:
        for prod in productos:
            if item["id"] == prod["id"]:
                prod["stock"] += item["stock"]


def cancelarDeuda(user):
    Registro={"Compras": (user["cuenta"]["ordenes"]), 
                   "Deuda":    (user["cuenta"]["deuda"]),
                   "MediosPago": (user["tarjetas"])}
                      
    user["cuenta"]["ordenes"] = []
    user["cuenta"]["deuda"] = 0
    return Registro

def InicializarDB(lista_hardcodeada):
    if os.path.exists(RUTA_JSON):
        try:
            with open(RUTA_JSON, "r") as f:
                return json.load(f)
        except Exception as e:
            print(f"Error al cargar la base de datos: {e}")
            return None
    else:
        # Primera ejecución: guardamos la lista base para crear el archivo
        try:
            with open(RUTA_JSON, "w") as f:
                json.dump(lista_hardcodeada, f, indent=4)
                return lista_hardcodeada
        except Exception as e:
            print(f"Error al guardar en la base de datos: {e}")
            return None


def actualizarDB(lista_usuarios):
    """Guarda el estado actual de todos los usuarios en el JSON."""
    try:
        with open(RUTA_JSON, "w") as f:
            json.dump(lista_usuarios, f, indent=4)
            return True
    except Exception as e:
        print(f"Error al guardar en la base de datos: {e}")
        return False