import pytest
from logica import calcularPrecioConDescuento,calcularTotalItem,buscarCuponPorCodigo,crearDiccionarioCupon,aplicarDescuentoAlCarrito,calcularCuota

## Test calcular precio con descuento
@pytest.mark.parametrize(
    "precio, descuento, resultado_esperado",
    [
        (1000, 20, 800.0),   # Descuento normal
        (500, 0, 500.0),     # Sin descuento
        (350, 100, 0.0),     # Gratis
        (100, 15.5, 84.5),   # Decimales
        (0, 50, 0.0)         # Producto de precio 0
    ]
)
def test_calcular_precio_con_descuento(precio, descuento, resultado_esperado):
    assert calcularPrecioConDescuento(precio, descuento) == resultado_esperado


## Test Calcular total item
@pytest.mark.parametrize(
    "precio, descuento, cantidad, resultado_esperado",
    [
        (100, 10, 4, 360),       # Total normal con dsc
        (100, 0, 1, 100),        # Precio sin Dsc
        (150.50, 10, 2, 270.90), # Precios con centavos (Prueba la precisión del round)
        (500, 100, 3, 0.0),      # Producto con 100% de descuento (Debe dar gratis, no negativo)
        (200, 10, 0, 0.0)        # Cantidad en cero (Llevando 0 unidades el total debe ser 0)
    ]
)
def test_calcular_total_item(precio, descuento, cantidad, resultado_esperado):
    assert calcularTotalItem(precio, descuento, cantidad) == resultado_esperado


## Test Buscar cupon por codigo
CUPONES_DE_PRUEBA = {
    ("WIN20", 20),
    ("JLO10", 10),
    ("PROFE100", 100)
}

@pytest.mark.parametrize(
    "codigo_buscado, resultado_esperado",
    [

        ("WIN20", ("WIN20", 20)),
       
        ("jLO10", None),
        
        ("CUPONFALSO", None),
    ]
)
def test_buscar_cupon_por_codigo(codigo_buscado, resultado_esperado):
    resultado = buscarCuponPorCodigo(CUPONES_DE_PRUEBA, codigo_buscado)
    assert resultado == resultado_esperado



## Tests Aplicar dscto al carrito
def test_aplicar_descuento_carrito_con_un_producto():
    carrito_test = [
        {"nombre": "Teclado Mecánico", "precio_final": 1000.0}
    ]
    carrito_resultado = aplicarDescuentoAlCarrito(carrito_test, 10)
    assert carrito_resultado[0]["precio_final"] == 900.0


def test_aplicar_descuento_carrito_multiple_y_redondeo():
    carrito_test = [
        {"nombre": "Mouse Gamer", "precio_final": 500.0},
        {"nombre": "Monitor 24'", "precio_final": 150.50}
    ]
    
    carrito_resultado = aplicarDescuentoAlCarrito(carrito_test, 15.5)

    assert carrito_resultado[0]["precio_final"] == 422.5
    assert carrito_resultado[1]["precio_final"] == 127.17


def test_aplicar_descuento_cero_y_total():
    carrito_base = [
        {"nombre": "Auriculares", "precio_final": 200.0}
    ]
    
    carrito_sin_descuento = aplicarDescuentoAlCarrito((carrito_base), 0)
    assert carrito_sin_descuento[0]["precio_final"] == 200.0
    
    carrito_gratis = aplicarDescuentoAlCarrito((carrito_base), 100)
    assert carrito_gratis[0]["precio_final"] == 0.0


## TEST Calcular cuotas
PagosCuotas = [1.1, 1.2, 1.3, 1.40]
PlazosCuotNUM = [3, 6, 8, 10]
@pytest.mark.parametrize(
    "deuda, indice_plazo, resultado_esperado",
    [
     
        (5000, 1, 1000), 
        (1500, 3, 210),
        (1000, 0, 366.0)  # 1000*1.1 -> 1100 // 3 == 366.666(366.0 round)
    ]
)
def test_calcular_cuota(deuda, indice_plazo, resultado_esperado):
    resultado = calcularCuota(deuda, indice_plazo)
    assert resultado == resultado_esperado
