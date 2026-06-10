import pytest
from logica import calcularPrecioConDescuento,calcularTotalItem,buscarCuponPorCodigo,crearDiccionarioCupon,aplicarDescuentoAlCarrito,calcularCuota


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

##((precio - (precio * (descuento / 100))) * cantidad, 2)
@pytest.mark.parametrize(
    "precio, descuento, cantidad, resultado_esperado",
    [
        (100, 10, 4, 360.0),     # Total normal
        (100, 0, 1, 100),        # Precio sin Dsc
        (150.50, 10, 2, 270.90), # Precios con centavos (Prueba la precisión del round)
        (500, 100, 3, 0.0),      # Producto con 100% de descuento (Debe dar gratis, no negativo)
        (200, 10, 0, 0.0)        # Cantidad en cero (Llevando 0 unidades el total debe ser 0)
    ]
)
def test_calcular_total_item(precio, descuento, cantidad, resultado_esperado):
    assert calcularTotalItem(precio, descuento, cantidad) == resultado_esperado