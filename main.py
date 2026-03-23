#Ecommerce
##Listas y Listas Paralelas
Productos=      ["Manzana"]
ProductosPrecio=[2]
ProductosStock= [32]
ProductosID=    [1]

OpcionesMenu=["Comprar", "Ver Productos", "Salir"]
def MostrarMenu():
    print("------------------------------------------------------------------------")
    print("=======================================================================")
    print("E-Commerce⦿E-Commerce⦿E-Commerce⦿E-Commerce⦿E-Commerce⦿E-Commerce⦿")
    print("=======================================================================")
    print("Bienvenido a la tienda virtual 🏪 ADMIN")
    for i in range (len(OpcionesMenu)):
        print("[",i,"]", OpcionesMenu[i])

    
MostrarMenu()

